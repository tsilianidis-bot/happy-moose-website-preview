/* Uses the existing build's React (N) and JSX runtime (g); no new framework. */
function HappyMooseHeroVideo({ introActive }) {
  const videoRef = N.useRef(null);
  const [paused, setPaused] = N.useState(
    () => window.matchMedia('(prefers-reduced-motion: reduce)').matches
  );
  const [playing, setPlaying] = N.useState(false);
  const [failed, setFailed] = N.useState(false);

  N.useEffect(() => {
    const mediaQuery = window.matchMedia('(prefers-reduced-motion: reduce)');
    const updatePreference = (event) => setPaused(event.matches);
    mediaQuery.addEventListener('change', updatePreference);
    return () => mediaQuery.removeEventListener('change', updatePreference);
  }, []);

  N.useEffect(() => {
    const video = videoRef.current;
    if (!video || failed) return;

    const syncPlayback = () => {
      if (introActive || paused || document.hidden) {
        video.pause();
        return;
      }
      video.muted = true;
      const playback = video.play();
      if (playback) playback.catch(() => setPaused(true));
    };

    syncPlayback();
    document.addEventListener('visibilitychange', syncPlayback);
    return () => {
      document.removeEventListener('visibilitychange', syncPlayback);
      video.pause();
    };
  }, [introActive, paused, failed]);

  return g.jsxs('div', {
    className: 'hero-media',
    children: [
      g.jsx('div', {
        className: 'hero-video-poster',
        'aria-hidden': 'true'
      }),
      g.jsx('video', {
        ref: videoRef,
        className: `hero-video${playing ? ' is-playing' : ''}`,
        src: './assets/media/happy-moose-ambient-v3.mp4',
        poster: './assets/media/happy-moose-ambient-poster-v3.jpg',
        muted: true,
        loop: true,
        playsInline: true,
        preload: 'auto',
        controls: false,
        disablePictureInPicture: true,
        'aria-hidden': 'true',
        tabIndex: -1,
        onPlaying: () => setPlaying(true),
        onError: () => { setFailed(true); setPlaying(false); setPaused(true); },
      }),
      !failed && g.jsx('button', {
        type: 'button',
        className: 'hero-video-control',
        'aria-label': paused ? 'Play background video' : 'Pause background video',
        onClick: () => setPaused((value) => !value),
        children: paused ? 'Play video' : 'Pause video'
      })
    ]
  });
}
