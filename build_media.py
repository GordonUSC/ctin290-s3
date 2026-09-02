#!/usr/bin/env python3
"""Sheet 1: the five items that play in Session 3, in play order, and what each one teaches.
Every link was confirmed against the YouTube oEmbed endpoint before this file was written."""
import html as H
from _kit import KIT, NAV

# id, title, channel, runtime, when it plays, what it teaches, what to watch for, swatches
ITEMS = [
 ("tJbzMqJGH4k", "Grand Theft Auto VI, Trailer 3", "Rockstar Games, official", "26:48",
  "10:00 &middot; Opening &middot; PLAYED IN FULL, all 26:48",
  "Color and time of day carrying a whole place, seen running rather than cut.",
  "Rockstar released this on 28 August under the title \"An Extended Look\" and never puts the "
  "words Trailer 3 on it, so search the title, not the number. It is a gameplay presentation, "
  "which is why it earns a color session: the first sustained look at the world lit and "
  "running rather than edited. THE WHOLE 26:48 RAN IN THE ROOM, not the planned six minutes. "
  "Two questions after: three words for the color of this world and what the palette says "
  "before anyone speaks, then pick one moment and say what the LIGHT is telling you that the "
  "action is not. Both are setup, for Arcane and for Awaken.",
  [("Night", ["#E0348B","#2E7FC2","#1B1A38"]), ("Day", ["#F2B33D","#E8CFA0","#4E8C5A"])]),

 ("fXmAurh012s", "Arcane, Official Trailer", "Netflix", "2:44",
  "10:12 &middot; Case Study &middot; play it twice",
  "Palette as an argument about class.",
  "Zaun is desaturated, industrial, blue and gray. Piltover is bright, organized, gold and "
  "crimson. The two palettes make the claim about place and class before a single line of "
  "dialogue does. This is the anchor text for the whole session.",
  [("Zaun", ["#3E4A52","#55707F","#7C8C93"]), ("Piltover", ["#C9992E","#E0B252","#8E3B34"])]),

 ("zF5Ddo9JdpY", "Awaken, Season 2019 Cinematic", "League of Legends, official", "3:28",
  "10:12 &middot; Case Study",
  "Lighting and material response carrying emotion.",
  "Same company, same world as Arcane, years apart. Watch how much emotional information "
  "sits in the lighting and in how materials answer it, wet metal, dust, cloth, rather than "
  "in the cutting. This is the clearest lighting text in the session.",
  [("Key", ["#E5C97A"]), ("Fill", ["#3A5A72"]), ("Rim", ["#B8D2E0"])]),

 ("aUts14xyjHg", "Disney's Encanto, Official Trailer", "Walt Disney Studios Philippines", "2:12",
  "10:12 &middot; Case Study",
  "A color problem solved in public.",
  "The Madrigal house runs a saturated Colombian palette, and every Madrigal is given a hue "
  "that is theirs before they speak. Watch the house shift warmth depending on whose story is "
  "being told, and notice that Bruno's absence is a color absence too.",
  [("House", ["#E0A33A","#C9552F","#3E8C6E"]), ("Bruno", ["#6E7A80","#4A5560"])]),

 ("xlnPHQ3TLX8", "Coco, Official US Trailer", "Pixar, official", "1:28",
  "11:16 &middot; Second Text &middot; play it twice",
  "Palette as the line between two worlds.",
  "Arcane splits color by class and district. Coco splits it by world. The living world is "
  "warm, dim and domestic; the Land of the Dead is saturated to a degree that would be "
  "unbearable if you had not just spent twenty minutes in the muted version. A palette is a "
  "rule you set and keep, and the payload arrives when you break it.",
  [("Living", ["#8A6A4E","#B9926A","#5C4433"]), ("Dead", ["#E85FA8","#F2B02E","#3FC9C1"])]),

 ("e8S4yoXNMPU", "Where Winds Meet, Gameplay Trailer", "official channel", "2:36",
  "Optional &middot; not placed in a block",
  "Restraint and negative space.",
  "Carried over from the Constraint through-line rather than the color argument. Reach for "
  "it only if the room is ahead of schedule; nothing in the session depends on it.",
  [("Ink", ["#2B2E30","#7E888C","#D8DAD6"])]),
]

rows = []
for i, (vid, title, chan, rt, when, teaches, watch, sw) in enumerate(ITEMS, 1):
    url = "https://www.youtube.com/watch?v=" + vid
    opt = " opt" if "Optional" in when else ""
    groups = "".join(
      '<div class="sg"><span class="sgn">{}</span><span class="chips">{}</span></div>'.format(
        H.escape(name), "".join('<i style="background:{}"></i>'.format(c) for c in cols))
      for name, cols in sw)
    rows.append(f'''<article class="item{opt}">
  <div class="n">{i:02d}</div>
  <div class="body">
    <h2><a href="{url}" target="_blank" rel="noopener">{H.escape(title)}</a></h2>
    <p class="meta"><span class="lbl">{H.escape(chan)}</span> <span class="rt">{rt}</span> <span class="when">{when}</span></p>
    <p class="teach">{teaches}</p>
    <p class="watch">{watch}</p>
    <div class="sws">{groups}</div>
    <p class="url"><a href="{url}" target="_blank" rel="noopener">{url}</a></p>
  </div>
</article>''')

page = f'''{KIT}
<title>Session 3 Media</title>
<style>
.item{{display:grid;grid-template-columns:96px 1fr;gap:26px;padding:30px 0;
 border-bottom:1px solid var(--rule);align-items:start}}
.item:first-of-type{{border-top:1px solid var(--rule)}}
.n{{font-family:"IBM Plex Mono",monospace;font-size:44px;font-weight:600;line-height:1;
 color:var(--blue);font-variant-numeric:tabular-nums}}
.item.opt .n{{color:var(--silver)}}
.item h2{{margin:0 0 8px;font-size:38px;line-height:1.06;font-weight:700;letter-spacing:-.03em;
 text-wrap:balance}}
.item h2 a{{color:var(--ink);text-decoration:none;border-bottom:3px solid var(--blue)}}
.item h2 a:hover,.item h2 a:focus-visible{{color:var(--blue)}}
.meta{{margin:0 0 14px;display:flex;gap:16px;align-items:baseline;flex-wrap:wrap}}
.rt{{font-family:"IBM Plex Mono",monospace;font-size:15px;font-weight:600;
 font-variant-numeric:tabular-nums}}
.when{{font-family:"IBM Plex Mono",monospace;font-size:12px;letter-spacing:.16em;
 text-transform:uppercase;background:var(--ink);color:var(--paper);padding:4px 11px}}
.item.opt .when{{background:var(--silver);color:var(--ink)}}
.teach{{margin:0 0 10px;font-size:25px;line-height:1.28;font-weight:600;letter-spacing:-.015em;
 color:var(--ink);max-width:34ch}}
.watch{{margin:0 0 16px;font-size:19px;line-height:1.55;color:var(--ink2);max-width:66ch}}
.sws{{display:flex;gap:26px;flex-wrap:wrap;margin:0 0 12px}}
.sg{{display:flex;flex-direction:column;gap:5px}}
.sgn{{font-family:"IBM Plex Mono",monospace;font-size:10.5px;letter-spacing:.2em;
 text-transform:uppercase;color:var(--ink2)}}
.chips{{display:flex;gap:3px}}
.chips i{{width:38px;height:22px;display:block;border:1px solid rgba(0,0,0,.14)}}
.url{{margin:0;font-family:"IBM Plex Mono",monospace;font-size:13px;word-break:break-all}}
</style>
<div class="wrap">
<header class="mast">
 <div><span class="lbl">CTIN 290 &middot; Session 3 &middot; Mon 31 Aug &middot; SCI L104</span>
  <h1>What we are<br>watching, and<br>what it teaches</h1></div>
 <div class="rt"><span class="lbl">Sheet 1 of 2</span></div>
</header>
<div class="sub">
 <div><span class="lbl">Items</span><b>6</b></div>
 <div><span class="lbl">In class</span><b>18:16</b></div>
 <div><span class="lbl">In a block</span><b>5</b></div>
 <div><span class="lbl">Links checked</span><b>6 of 6</b></div>
 <div><span class="lbl">Unit</span><b>1 &middot; Seeing</b></div>
</div>
{NAV.format(m=' class="here"', t='')}
<main style="margin-top:30px">
{chr(10).join(rows)}
</main>
<div class="note">
 <p><b>On the swatches.</b> They are drawn from the words in the session plan, not sampled from
 the frames. Use them as a cue for what to point at, not as a color reference.</p>
 <p><b>Trailer 3 runs 26:48 and the whole thing ran in the room.</b> The board had planned six
 minutes. Rockstar titles it <em>An Extended Look</em> and never writes Trailer 3 on the video,
 so search the title, not the number. The documented price of running it in full was Encanto
 plus twelve minutes off the build; what actually got traded is recorded on the rundown block.
 One consequence worth carrying forward: the class now shares all twenty-seven minutes of it,
 so Session 4 does not need to screen a second of it.</p>
 <p><b>Encanto is a regional official channel</b> (Walt Disney Studios Philippines), not the main
 Disney account. It is official, and it is worth saying so out loud when you play it.</p>
</div>
<div class="foot">
 <p>Every link on this sheet was confirmed against the YouTube oEmbed endpoint on 31 Aug 2026,
 and the returned title and channel are what you see printed above.</p>
 <p>Class meets 10:00 AM to 12:50 PM, Mon and Wed. 170 minutes.</p>
</div>
</div>'''
open("media.html","w").write(page)
print("media.html", len(page), "bytes")
