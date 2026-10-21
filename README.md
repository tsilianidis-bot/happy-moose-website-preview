# Happy Moose — cinematic intro + ambient video website

This saved package retains the October 20 Happy Moose website and cinematic moose pre-open. The full commercial has been replaced with a short, silent ambient loop made only from the supplied version 6 footage. The edit uses the strongest bar-hospitality, draft-tap, burger-detail, and close-up-toast imagery, gently retimed and color matched. Advertising lower-thirds are removed by checked crops or clean timing; crowd/eating distractions, event and price callouts, and the closing logo card are excluded. Soft dissolves include the last-to-first join, so there is no fade to black or obvious commercial restart.

The background preloads during the intro, then starts after the intro completes or is skipped. The compact “Get loose. At the Moose.” headline, original site sections, navigation, ordering links, and moose intro are preserved. Mobile now uses a full-bleed atmospheric background under a readable gradient rather than presenting the ad as a separate video player. Pause/play, tab-visibility pausing, and reduced-motion fallback remain available.

## Open the saved website

Unzip the single save file and serve this folder with a static server. For example, run `python3 -m http.server 3000` here, then open `http://localhost:3000/`. Use an HTTP server instead of double-clicking `index.html`, because browsers restrict module scripts on `file://` URLs.

## Saved together

`index.html`, the original React bundle and styling, all original cinematic loading-screen assets, the edited ambient loop and matching poster, and the hero styling are included in one complete ZIP. No separate loading-screen file is required. The original uploaded commercial remains untouched and is not included as an unnecessary second large video in the website save.

## Maintenance

This repository was recovered as the original deployed build; original TypeScript source was unavailable in this task. The readable hero component is in `src/hero-video-component.js`, with scoped styles in `assets/hero-video.css`. After changing the component, run `python3 src/apply-video-hero.py` to update its block inside the existing build.

The reproducible video-edit script is `src/render-ambient-loop.py`; give it a path to the original `happy_moose_commercial_v6_final.mp4`. `src/ambient-loop-edit.json` records selected source ranges, crop rectangles, playback speeds, transitions, and final output metadata. No original footage is overwritten or generated.

The restaurant’s production domain is unchanged by this saved preview revision.
