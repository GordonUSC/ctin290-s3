#!/usr/bin/env python3
"""Sheet 2: key terms with definitions, each pointing at a video that actually reinforces it.
Tier 1 definitions are verbatim from the course glossary (the single source, 55 terms).
Tier 2 unpacks terms the session teaches inside other definitions."""
import html as H
from _kit import KIT, NAV

V = {
 "arcane": ("fXmAurh012s", "Arcane, Official Trailer"),
 "awaken": ("zF5Ddo9JdpY", "Awaken, LoL Cinematic"),
 "coco":   ("xlnPHQ3TLX8", "Coco, Official US Trailer"),
 "encanto":("aUts14xyjHg", "Disney's Encanto, Official Trailer"),
}

# term, definition, video key, what to look at, extra
CANON = [
 ("Color Script",
  "A sequence of images or notations showing the intended color palette and mood progression "
  "across a scene or film.", "arcane",
  "Piltover gold against undercity neon. The palette argues class before any dialogue does.",
  "Ralph Eggleston brought the color script to Pixar in 1992 as art director on Toy Story, "
  "working in pastel on black paper because it was fast and cheap. You can read the emotional "
  "arc of a film off its colour alone, sound off, no dialogue."),
 ("Palette",
  "The selected range of colors in a shot, scene, or project; establishes mood and visual unity.",
  "arcane", "Saturation doing emotional work, scene to scene.",
  "A palette is a rule you set and then keep. The emotional payload arrives at the moment you "
  "break it, which is the constraint on today's build."),
 ("Warm / Cool",
  "Color temperature: warm colors (red, orange, yellow) feel intimate and energetic; cool "
  "colors (blue, green) feel distant and calm.", "arcane",
  "Temperature as allegiance. Which side of the city are you being asked to stand on.", ""),
 ("Lighting",
  "The quality, direction, and color of illumination. Hard vs. soft light; high-key vs. "
  "low-key; motivated vs. stylized.", "awaken",
  "Emotional information sitting in the lighting and in how materials answer it, wet metal, "
  "dust, cloth, rather than in the cutting.",
  "CHANGED ON THIS SHEET. The glossary points this term at the Blue Lock trailer, which is a "
  "Session 6 text and is not played today. Awaken is in today's session and is the stronger "
  "lighting example. Flagged for your call."),
]

UNPACKED = [
 ("Saturation",
  "How much pure hue a colour carries, from flat grey at one end to full intensity at the "
  "other. Independent of how light or dark it is.", "coco",
  "The living world is muted; the Land of the Dead is saturated to the edge of comfort. Same "
  "film, two settings of one dial."),
 ("Value",
  "How light or dark a colour is, independent of its hue. The dimension that survives when "
  "you turn the picture greyscale.", "arcane",
  "Turn Zaun greyscale in your head. The class argument still reads, because it was built in "
  "value as well as in hue."),
 ("High-key / Low-key",
  "High-key lighting is bright and evenly lit with few shadows. Low-key is dominated by "
  "shadow with small, deliberate pools of light.", "awaken",
  "Where the frame goes low-key, count what you are no longer being shown."),
 ("Motivated / Stylized light",
  "Motivated light comes from a source you can point to inside the world. Stylized light "
  "exists because the shot needs it, and no lamp in the fiction explains it.", "awaken",
  "Find one light you can trace to a source and one you cannot. Ask what the second one is for."),
 ("Hard / Soft light",
  "Hard light comes from a small source and gives sharp-edged shadows. Soft light comes from "
  "a large or diffused source and gives gradual ones.", "awaken",
  "Watch the shadow edges on faces and on wet metal. The edge is the tell, not the brightness."),
 ("Cultural vs. universal colour",
  "Some colour associations are learned inside a culture rather than shared by everyone. "
  "Treating a learned association as universal is the most common failure in a mood board.",
  "encanto",
  "Name one colour choice that is cultural rather than universal, and say how you know. You "
  "will be asked this about Coco in the second half."),
]

FORWARD = [
 ("Tone", "The emotional or stylistic mood of a work; created through every visual and sonic "
  "choice.", "Session 8", "Today is the colour half of it."),
 ("Constraint", "A hard limit on the palette, resolution, color depth, or geometry available "
  "to you. Constraint is not the opposite of expression, it is often the engine of it.",
  "Session 2", "Where Winds Meet sits here, which is why it is optional today."),
 ("Blue Lock (visual)", "Visual technique of isolating a key object or character through "
  "color, lighting, or position to direct viewer attention.", "Session 6",
  "This is where the Blue Lock trailer actually belongs."),
]

def card(term, defn, vkey, look, extra, n):
    vid, vname = V[vkey]
    url = "https://www.youtube.com/watch?v=" + vid
    ex = ""
    if extra:
        cls = "flag" if extra.startswith("CHANGED") else "more"
        ex = f'<p class="{cls}">{H.escape(extra)}</p>'
    return f'''<article class="term">
  <div class="n">{n:02d}</div>
  <div class="body">
    <h2>{H.escape(term)}</h2>
    <p class="def">{H.escape(defn)}</p>
    {ex}
    <div class="rein">
      <span class="lbl">Reinforced by</span>
      <p class="vid"><a href="{url}" target="_blank" rel="noopener">{H.escape(vname)}</a></p>
      <p class="look">{H.escape(look)}</p>
      <p class="url"><a href="{url}" target="_blank" rel="noopener">{url}</a></p>
    </div>
  </div>
</article>'''

n = 0; canon_html = []
for t, d, v, l, e in CANON:
    n += 1; canon_html.append(card(t, d, v, l, e, n))
unp_html = []
for t, d, v, l in UNPACKED:
    n += 1; unp_html.append(card(t, d, v, l, "", n))
fwd = "".join(
  f'<article class="fwd"><h3>{H.escape(t)}</h3><p class="def">{H.escape(d)}</p>'
  f'<p class="when2"><span class="lbl">{H.escape(s)}</span> {H.escape(note)}</p></article>'
  for t, d, s, note in FORWARD)

page = f'''{KIT}
<title>Session 3 Key Terms</title>
<style>
h2.sec{{margin:52px 0 0;font-size:15px;font-family:"IBM Plex Mono",monospace;letter-spacing:.22em;
 text-transform:uppercase;font-weight:600;border-bottom:3px solid var(--ink);padding-bottom:11px}}
h2.sec span{{float:right;letter-spacing:.06em;color:var(--ink2);font-weight:400;text-transform:none}}
.term{{display:grid;grid-template-columns:96px 1fr;gap:26px;padding:28px 0;
 border-bottom:1px solid var(--rule);align-items:start}}
.n{{font-family:"IBM Plex Mono",monospace;font-size:40px;font-weight:600;line-height:1;
 color:var(--green);font-variant-numeric:tabular-nums}}
.term h2{{margin:0 0 10px;font-size:40px;line-height:1.04;font-weight:700;letter-spacing:-.035em}}
.def{{margin:0 0 14px;font-size:23px;line-height:1.4;max-width:56ch}}
.more{{margin:0 0 14px;font-size:18px;line-height:1.55;color:var(--ink2);max-width:64ch;
 border-left:3px solid var(--rule);padding-left:16px}}
.flag{{margin:0 0 14px;font-size:17px;line-height:1.5;max-width:64ch;background:#FBF2E4;
 border-left:6px solid var(--orange);padding:13px 17px}}
.rein{{background:var(--fill);padding:16px 20px;max-width:70ch}}
.vid{{margin:6px 0 8px;font-size:22px;font-weight:600;letter-spacing:-.015em}}
.vid a{{color:var(--ink);text-decoration:none;border-bottom:3px solid var(--green)}}
.vid a:hover,.vid a:focus-visible{{color:var(--green)}}
.look{{margin:0 0 9px;font-size:18px;line-height:1.5;color:var(--ink2)}}
.url{{margin:0;font-family:"IBM Plex Mono",monospace;font-size:12.5px;word-break:break-all}}
.fwds{{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:0;
 border-top:1px solid var(--rule)}}
.fwd{{padding:22px 26px 22px 0;border-right:1px solid var(--rule)}}
.fwd:last-child{{border-right:0}}
.fwd h3{{margin:0 0 8px;font-size:25px;font-weight:700;letter-spacing:-.02em}}
.fwd .def{{font-size:17.5px;line-height:1.5;color:var(--ink2)}}
.when2{{margin:0;font-size:16px}}
</style>
<div class="wrap">
<header class="mast">
 <div><span class="lbl">CTIN 290 &middot; Session 3 &middot; Colour &amp; Lighting &middot; Unit 1, Seeing</span>
  <h1>The words for<br>what you are<br>looking at</h1></div>
 <div class="rt"><span class="lbl">Sheet 2 of 2</span></div>
</header>
<div class="sub">
 <div><span class="lbl">Terms</span><b>10</b></div>
 <div><span class="lbl">From the glossary</span><b>4</b></div>
 <div><span class="lbl">Unpacked today</span><b>6</b></div>
 <div><span class="lbl">Videos used</span><b>4</b></div>
 <div><span class="lbl">Links checked</span><b>all</b></div>
</div>
{NAV.format(m='', t=' class="here"')}
<main>
<h2 class="sec">In the course glossary <span>These are the four the syllabus already owns for Session 3</span></h2>
{chr(10).join(canon_html)}
<h2 class="sec">Taught today, not yet in the glossary <span>Unpacked from inside the definitions above</span></h2>
{chr(10).join(unp_html)}
<h2 class="sec">Next door <span>Named today, owned by another session</span></h2>
<div class="fwds">{fwd}</div>
</main>
<div class="note">
 <p><b>Every definition in the first block is verbatim from the course glossary</b>, the 55-term
 single source shared with the class. The second block is not in the glossary yet; those six are
 already taught inside the Lighting and Color Script definitions and in the synthesis exercise,
 so they are pulled out here where students can see them. Promote any of them and I will fold
 them into the glossary properly.</p>
 <p><b>No timestamps are given inside the videos.</b> The glossary marks all of these
 &ldquo;Throughout&rdquo; and I have not watched the footage frame by frame, so a precise minute
 mark would be invented. What is printed instead is what to look at.</p>
</div>
<div class="foot">
 <p>All four videos confirmed against the YouTube oEmbed endpoint on 31 Aug 2026.</p>
 <p>Exit ticket: one term you learned today and where you saw it. One thing you are still unsure of.</p>
</div>
</div>'''
open("terms.html","w").write(page)
print("terms.html", len(page), "bytes")
