"""Render a restrained, circular website loop from the supplied v6 commercial.

Run: python3 src/render-ambient-loop.py /path/to/happy_moose_commercial_v6_final.mp4
The original source is never overwritten. Only source footage is used.
"""
import json
import subprocess
import sys
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
source = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('/home/ubuntu/upload/happy_moose_commercial_v6_final.mp4')
assert source.is_file(), f'Missing supplied source: {source}'
output = ROOT / 'assets/media/happy-moose-ambient-v2.mp4'
poster = ROOT / 'assets/media/happy-moose-ambient-poster-v2.jpg'

# Timestamps and reframing checked against full-resolution source frames.
# The 896x504 frames exclude source pillarboxes and every promotional lower-third.
# The burger detail is selected only before its advertising caption appears.
shots = [
    dict(name='Warm bar hospitality', start=12.20, end=13.90, speed=0.48, crop=[896, 504, 300, 0]),
    dict(name='Draft taps', start=8.08, end=9.92, speed=0.56, crop=[896, 504, 168, 0]),
    dict(name='Clean burger detail', start=22.083333, end=22.708333, speed=0.25, crop=[1088, 612, 96, 96]),
    dict(name='Close-up toast', start=36.30, end=43.25, speed=0.72, crop=[896, 504, 192, 24]),
]
fps = 24
fade = Fraction(21, fps)  # 0.875 seconds, exactly 21 frames.
filters = ['[0:v]split=4[raw0][raw1][raw2][raw3]']
lengths = []
for index, shot in enumerate(shots):
    frame_count = round((shot['end'] - shot['start']) / shot['speed'] * fps)
    duration = Fraction(frame_count, fps)
    lengths.append(duration)
    crop = ':'.join(str(value) for value in shot['crop'])
    filters.append(
        f"[raw{index}]trim=start={shot['start']}:end={shot['end']},"
        f"setpts=(PTS-STARTPTS)/{shot['speed']},crop={crop},"
        'scale=1280:720:flags=lanczos,setsar=1,'
        f'fps={fps},tpad=stop_mode=clone:stop_duration=1,'
        f'trim=duration={float(duration):.9f},setpts=PTS-STARTPTS,'
        'eq=brightness=-0.032:contrast=1.025:saturation=0.84:gamma=0.985,'
        'colorbalance=rs=0.012:bs=-0.006:rm=0.012:bm=-0.012,'
        f'format=yuv420p,settb=1/{fps}[shot{index}]'
    )

filters.append('[shot0]split=2[head][wrapraw]')
filters.append(f'[wrapraw]trim=duration={float(fade):.9f},setpts=PTS-STARTPTS[wrap]')
current = 'head'
elapsed = lengths[0]
for index in range(1, len(shots)):
    label = f'blend{index}'
    offset = elapsed - fade
    filters.append(f'[{current}][shot{index}]xfade=transition=fade:duration={float(fade):.9f}:offset={float(offset):.9f}[{label}]')
    current = label
    elapsed += lengths[index] - fade
# Fade the last shot back into the first 21 frames. Start the delivered clip
# after that first interval, so its first frame follows its last without a jump.
filters.append(f'[{current}][wrap]xfade=transition=fade:duration={float(fade):.9f}:offset={float(elapsed-fade):.9f}[circle]')
loop_duration = elapsed - fade
filters.append(f'[circle]trim=start={float(fade):.9f}:duration={float(loop_duration):.9f},setpts=PTS-STARTPTS[v]')
filter_path = ROOT / 'src/ambient-loop-filter.txt'
filter_path.write_text(';\n'.join(filters) + '\n')
print('Rendering ambient loop: bar → taps → food detail → toast → bar.', flush=True)
print(f'Planned duration {float(loop_duration):.3f}s; original promotional graphics excluded.', flush=True)
subprocess.run([
    'ffmpeg', '-hide_banner', '-loglevel', 'warning', '-filter_complex_threads', '2',
    '-i', str(source), '-filter_complex_script', str(filter_path), '-map', '[v]', '-an',
    '-c:v', 'libx264', '-preset', 'medium', '-crf', '23', '-pix_fmt', 'yuv420p',
    '-g', '48', '-movflags', '+faststart', '-y', str(output)
], check=True)
subprocess.run([
    'ffmpeg', '-hide_banner', '-loglevel', 'error', '-ss', '0', '-i', str(output),
    '-frames:v', '1', '-q:v', '2', '-y', str(poster)
], check=True)
probe = json.loads(subprocess.check_output([
    'ffprobe', '-v', 'error', '-show_entries', 'format=duration,size:stream=codec_name,width,height,r_frame_rate',
    '-of', 'json', str(output)
]))
manifest = {
    'source_filename': source.name,
    'output': str(output.relative_to(ROOT)),
    'poster': str(poster.relative_to(ROOT)),
    'shots': shots,
    'transition': '21-frame soft cross-dissolves including last-to-first',
    'grade': 'Subtle warm bias, reduced saturation, restrained brightness',
    'audio': 'None; silent decorative background',
    'probe': probe,
}
(ROOT / 'src/ambient-loop-edit.json').write_text(json.dumps(manifest, indent=2) + '\n')
print(json.dumps(probe, indent=2), flush=True)
print('Ambient loop and matching first-frame poster saved.', flush=True)
