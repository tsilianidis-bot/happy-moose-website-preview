# Happy Moose — video hero update

- [x] Preserve yesterday’s cinematic moose intro and existing website design, navigation, and sections. The cinematic pre-open remains the first visible experience. The original `Jx` intro component is byte-for-byte unchanged.
- [x] Replace the landing page’s still hero graphic with the supplied `happy_moose_commercial_v6_final.mp4`, playing muted, inline, and looping after the intro completes or is skipped. Keep readable text and working calls to action. The compact “Get loose. At the Moose.” lockup leaves more space for the video.
- [x] Keep a still fallback only for loading, playback errors, or reduced-motion preference; provide an accessible pause/play control. On mobile, show the full 16:9 commercial above the text rather than cropping or covering its content.
- [x] Save the cinematic loading screen and full landing page together, including all media, in a single reusable save file.

## Verification evidence

JavaScript syntax checks passed. The existing intro stays mounted with video paused at time 0 in intro-review mode. After Skip intro and the existing 580 ms exit, playback starts from the beginning. Native muted, inline, and loop properties are enabled; playback advances and wraps from the end to the beginning without error. Pause/play works. A 390-pixel mobile frame shows a 390 × 219.375-pixel video region with `object-fit: contain`, the copy below it, and no horizontal overflow.

## Existing project facts

Recovered the Oct. 20 preview from `tsilianidis-bot/happy-moose-website-preview`, original commit `65e7edd`. This repository contains the deployed React build and original media rather than original TypeScript sources. A readable, scoped hero component and repeatable patch are retained for maintenance. No Manus website resource was attached to this task. The restaurant’s production domain is unchanged.
