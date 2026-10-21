# Happy Moose — cinematic intro + video landing page

This saved package retains the October 20 Happy Moose website and cinematic moose pre-open. The supplied version 6 commercial replaces the still landing-page hero. It preloads during the intro and starts from the beginning after the intro completes or is skipped, playing inline, muted, and looping. The original user-uploaded MP4 remains untouched; the web copy uses the same H.264 video frames with its audio stream removed and fast-start metadata added.

The headline is now a compact “Get loose. At the Moose.” lockup so the moving commercial remains the primary landing-page graphic. Existing site sections, navigation, ordering links, and intro animation are preserved. On mobile, the full 16:9 video sits above the copy rather than cropping the commercial’s text and faces into a portrait background. A pause/play control and reduced-motion fallback are included.

## Open the saved website

Unzip the single save file and serve this folder with a static server. For example, run `python3 -m http.server 3000` here, then open `http://localhost:3000/`. Use an HTTP server instead of double-clicking `index.html`, because browsers restrict module scripts on `file://` URLs.

## Saved together

`index.html`, the original React bundle and styling, all original moose-intro media, the background video and poster, and the new hero styles are included in this one package. No separate loading-screen file is needed.

## Maintenance

This repository was recovered as the original deployed build; original TypeScript source was not available in this task. The readable hero component is in `src/hero-video-component.js`, with scoped styles in `assets/hero-video.css`. After changing the component, run `python3 src/apply-video-hero.py` to update its block inside the existing build. No other site components are regenerated.

The restaurant’s production domain is not changed by this package.
