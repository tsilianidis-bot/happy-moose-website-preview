"""Patch the recovered October 20 preview while preserving its original intro/site."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
bundle = ROOT / 'assets/index-V4OGY_0U.js'
text = bundle.read_text()
marker = '/* HAPPY_MOOSE_VIDEO_HERO_START */'
end_marker = '/* HAPPY_MOOSE_VIDEO_HERO_END */'
component = (ROOT / 'src/hero-video-component.js').read_text()
if marker in text:
    start = text.index(marker)
    end = text.index(end_marker, start) + len(end_marker)
    text = text[:start] + marker + '\n' + component + end_marker + text[end:]
else:
    anchor = 'function $x(){'
    assert text.count(anchor) == 1
    text = text.replace(anchor, marker + '\n' + component + end_marker + '\n' + anchor, 1)
    old = 'g.jsx("div",{"data-loc":"client/src/pages/Home.tsx:229",className:"hero-image",style:{backgroundImage:`url(${ue.basketballArena})`}})'
    assert text.count(old) == 1
    text = text.replace(old, 'g.jsx(HappyMooseHeroVideo,{introActive:i})', 1)
    old_heading = 'children:["The Best ",g.jsx("em",{"data-loc":"client/src/pages/Home.tsx:235",children:"Wings,"}),g.jsx("br",{"data-loc":"client/src/pages/Home.tsx:235"}),"Burgers, ",g.jsx("span",{"data-loc":"client/src/pages/Home.tsx:236",children:"Beer"}),g.jsx("br",{"data-loc":"client/src/pages/Home.tsx:236"}),"and Big Game Venue."]'
    assert text.count(old_heading) == 1
    text = text.replace(old_heading, 'children:["Get loose.",g.jsx("br",{}),"At the ",g.jsx("em",{children:"Moose."})]', 1)
    text = text.replace('" Lake County\'s Go-To Spot for the Big Game"]}),g.jsxs("h1"', '" Mentor\'s neighborhood sports bar"]}),g.jsxs("h1"', 1)
    text = text.replace('The home-field advantage for cold drafts, scratch-made favorites, and every can\'t-miss play.', 'Great wings. Cold drafts. Every big game. Bring your crew to Happy Moose in Mentor.', 1)
bundle.write_text(text)

entry = ROOT / 'index.html'
html = entry.read_text()
css = '    <link rel="stylesheet" href="./assets/hero-video.css">'
if css not in html:
    html = html.replace('  </head>', css + '\n  </head>', 1)
entry.write_text(html)
print('Applied the video hero update; original intro and other sections retained.')
