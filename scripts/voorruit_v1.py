import re, math
p='autolichten.html'
h=open(p,encoding='utf-8').read()

def Y(Z): return 130+270*(4/Z)**0.62
def P(Z): return (Y(Z)-130)/270
def XS(X,Z): return 320+X*130*P(Z)
def f(v): return ('%.1f'%v)
def poly(pts): return 'M'+'L'.join('%s %s'%(f(XS(x,z)),f(Y(z))) for x,z in pts)+'Z'
def grad(id_, color, stops, y_end_d):
    yend=Y(y_end_d)
    out='<linearGradient id="%s" gradientUnits="userSpaceOnUse" x1="0" y1="400" x2="0" y2="%s">'%(id_,f(yend))
    for d,o in stops:
        y=Y(max(d,4)); off=(400-y)/(400-yend)
        out+='<stop offset="%.3f" stop-color="%s" stop-opacity="%s"/>'%(max(0,min(1,off)),color,o)
    return out+'</linearGradient>'

# ---------- beams ----------
DIM=[(-7,3.9),(-7,9),(-4.2,15),(-1.9,23),(-0.6,29),(1.6,32),(4.2,27),(6.5,17),(8,9),(8,3.9)]
GROOT=[(-7,3.9),(-6.5,9),(-4.2,16),(-3.2,40),(-2.6,80),(-1.7,104),(0,109),(1.7,104),(2.6,80),(3.2,40),(4.2,16),(6.5,9),(7,3.9)]
MIST=[(-9,3.9),(-9,9),(-5,16),(0,20),(5,16),(9,9),(9,3.9)]
STAND=[(-4,3.9),(-3,5.5),(-1.2,7.2),(1.2,7.2),(3,5.5),(4,3.9)]

defs=''
defs+='<filter id="soft3" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="5"/></filter>'
defs+='<filter id="soft4" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="3.5"/></filter>'
defs+='<linearGradient id="skyN" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#070b20"/><stop offset="1" stop-color="#1a2a55"/></linearGradient>'
defs+='<linearGradient id="skyD" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#5f93dc"/><stop offset="1" stop-color="#c4dbf4"/></linearGradient>'
defs+=grad('mgDim2','#000',[(0,1),(21,.85),(33,0)],33)
defs+=grad('mgGroot2','#000',[(0,1),(40,.9),(79,.6),(101,0)],101)
defs+=grad('mgMist2','#000',[(0,1),(15.7,.8),(22.5,0)],22.5)
defs+=grad('mgStand2','#000',[(0,1),(7.5,0)],7.5)
defs+=grad('ggDim2','#fff0cc',[(0,.55),(21,.3),(33,0)],33)
defs+=grad('ggGroot2','#e4eeff',[(0,.6),(40,.38),(79,.15),(101,0)],101)
defs+=grad('ggMist2','#ffe29a',[(0,.6),(22.5,0)],22.5)
defs+=grad('ggStand2','#fff0cc',[(0,.5),(7.5,0)],7.5)
defs+=grad('fogGrad2','#b8c4d6',[(4,0),(10,.15),(20,.45),(35,.85),(50,1)],50)
defs+='<linearGradient id="fogCutW2" gradientUnits="userSpaceOnUse" x1="0" y1="%s" x2="0" y2="%s"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset="1" stop-color="#fff" stop-opacity="1"/></linearGradient>'%(f(Y(40)),f(Y(51.5)))
defs+='<linearGradient id="fogCutB2" gradientUnits="userSpaceOnUse" x1="0" y1="%s" x2="0" y2="%s"><stop offset="0" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity="1"/></linearGradient>'%(f(Y(40)),f(Y(51.5)))
defs+='<radialGradient id="rgWarm2"><stop offset="0" stop-color="#fff1c4" stop-opacity=".95"/><stop offset="1" stop-color="#fff1c4" stop-opacity="0"/></radialGradient>'
defs+='<mask id="night2" maskUnits="userSpaceOnUse" x="0" y="0" width="640" height="400"><rect width="640" height="400" fill="#fff"/><g filter="url(#soft3)">'
defs+='<path class="m m-stand" d="%s" fill="url(#mgStand2)"/>'%poly(STAND)
defs+='<path class="m m-mistf" d="%s" fill="url(#mgMist2)"/>'%poly(MIST)
defs+='<path class="m m-dim" d="%s" fill="url(#mgDim2)"/>'%poly(DIM)
defs+='<path class="m m-groot" d="%s" fill="url(#mgGroot2)"/>'%poly(GROOT)
defs+='</g><rect class="fogcut" width="640" height="400" fill="url(#fogCutW2)"/></mask>'
defs+='<mask id="glowMask2" maskUnits="userSpaceOnUse" x="0" y="0" width="640" height="400"><rect width="640" height="400" fill="#fff"/><rect class="fogcut" width="640" height="400" fill="url(#fogCutB2)"/></mask>'

# ---------- world ----------
world='<g class="world">'
world+='<rect width="640" height="400" fill="url(#skyN)"/>'
world+='<rect y="130" width="640" height="270" fill="#17331f"/>'
world+='<path d="M%s 400L%s 400L320 130Z" fill="#2c3346"/>'%(f(XS(-5.5,4)),f(XS(2.4,4)))
def band(X,w,Za,Zb,fill):
    a,b=XS(X-w/2,Za),XS(X+w/2,Za); c,d=XS(X+w/2,Zb),XS(X-w/2,Zb)
    return '<path d="M%s %sL%s %sL%s %sL%s %sZ" fill="%s"/>'%(f(a),f(Y(Za)),f(b),f(Y(Za)),f(c),f(Y(Zb)),f(d),f(Y(Zb)),fill)
world+=band(1.95,.14,3.9,2000,'#e8ecf5')+band(-5.35,.14,3.9,2000,'#e8ecf5')
def obj(Z,X,inner):
    S=130*P(Z)
    return '<g transform="translate(%s %s) scale(%s)">%s</g>'%(f(XS(X,Z)),f(Y(Z)),'%.3f'%S,inner)
person='<rect x="-.2" y="-.8" width=".4" height=".8" fill="#2a3040"/><rect x="-.28" y="-1.45" width=".56" height=".7" rx=".08" fill="#ffd21f"/><rect x="-.28" y="-1.2" width=".56" height=".07" fill="#fff"/><circle cy="-1.62" r=".15" fill="#d9a77e"/>'
cone='<rect x="-.2" y="-.04" width=".4" height=".04" fill="#242a3a"/><path d="M-.17 -.04L-.05 -.7H.05L.17 -.04Z" fill="#ff6a1a"/><path d="M-.12 -.28L-.09 -.42H.09L.12 -.28Z" fill="#fff3e0"/>'
deer='<ellipse cy="-.95" rx=".65" ry=".3" fill="#8b5e3c"/><g fill="#8b5e3c"><rect x="-.55" y="-.8" width=".08" height=".8"/><rect x="-.35" y="-.8" width=".08" height=".8"/><rect x=".3" y="-.8" width=".08" height=".8"/><rect x=".5" y="-.8" width=".08" height=".8"/><path d="M-.55 -1.1L-.78 -1.45L-.9 -1.38L-.62 -.95Z"/><circle cx="-.85" cy="-1.5" r=".16"/></g><path d="M-.85 -1.65l-.1 -.3M-.85 -1.65l.12 -.28M-.95 -1.9l-.12 -.1" stroke="#d9c6a3" stroke-width=".05" stroke-linecap="round" fill="none"/><circle cx="-.93" cy="-1.52" r=".04" fill="#e9ff7a"/>'
world+=obj(15,2.7,person)+obj(25,0.2,cone)+obj(63,0.6,deer)
# oncoming car (front view) Z=70, X=-3.5
S=130*P(70); cx=XS(-3.5,70); cy=Y(70)
car='<g class="onc-only"><g transform="translate(%s %s) scale(%.3f)" ><rect x="-.95" y="-.35" width=".25" height=".35" fill="#0a0c14"/><rect x=".7" y="-.35" width=".25" height=".35" fill="#0a0c14"/><rect x="-.9" y="-1.5" width="1.8" height="1.2" rx=".25" fill="#8a6a4e"/><rect x="-.7" y="-1.45" width="1.4" height=".5" rx=".12" fill="#141c30"/></g></g>'%(f(cx),f(cy),S)
world+=car
world+='</g>'

# ---------- phases (moving road details) ----------
def phase(j):
    out='<g class="ph" style="animation-delay:%.3fs">'%(j*0.05-0.6)
    for k in range(0,13):
        za=12*k+5-j; zb=za+3
        if zb<4 or za>150: continue
        za=max(za,3.9)
        out+=band(-1.75,.14,za,zb,'#f2f4fa')
    for k in range(0,13):
        z=12*k+6-j
        if z<5 or z>140: continue
        for X in (-5.9,2.9):
            S=130*P(z)
            out+='<g transform="translate(%s %s) scale(%.3f)"><rect x="-.07" y="-.95" width=".14" height=".95" fill="#f5f6fa"/><rect x="-.07" y="-.95" width=".14" height=".16" fill="#e23a3a"/></g>'%(f(XS(X,z)),f(Y(z)),S)
    for k in range(0,12):
        for X,off in ((-9.5,3),(7.5,9)):
            z=12*k+off-j
            if z<25 or z>140: continue
            S=130*P(z)
            out+='<g transform="translate(%s %s) scale(%.3f)"><rect x="-.2" y="-1.6" width=".4" height="1.6" fill="#2a2018"/><ellipse cy="-4.2" rx="2" ry="2.8" fill="#173d25"/></g>'%(f(XS(X,z)),f(Y(z)),S)
    return out+'</g>'
phases=''.join(phase(j) for j in range(12))

# horizon trees
pts=['0 130']
for i in range(0,41):
    x=i*16; hgt=7+5*math.sin(i*1.7)+4*math.sin(i*0.63+1)
    pts.append('%d %.1f'%(x,130-hgt))
pts.append('640 130')
horizon='<path class="horizon" d="M%sZ" fill="#14301f"/>'%'L'.join(pts)

# rulers
rul=''
for d in (20,40,60,80,100):
    y=Y(d); x=XS(2.3,d)
    rul+='<path d="M%s %sh14" stroke="#9fb0d9" stroke-opacity=".55"/><text x="%s" y="%s">%d m</text>'%(f(x),f(y),f(x+17),f(y+3.5),d)

# frame + dashboard
frame='''<path d="M0 0H86L30 400H0Z" fill="#090d1b"/><path d="M640 0H554L610 400H640Z" fill="#090d1b"/>
<path d="M0 0H640V22Q320 46 0 22Z" fill="#090d1b"/>
<rect x="282" y="14" width="76" height="26" rx="7" fill="#0d1324" stroke="#202c4d"/><rect x="288" y="19" width="64" height="16" rx="4" fill="#121b36"/>
<path d="M0 374Q320 336 640 374V400H0Z" fill="#090d1b"/><path d="M0 374Q320 336 640 374" fill="none" stroke="#1d2744" stroke-width="2"/>'''
ind=''
for i,(k) in enumerate(['stand','dim','groot','mistf','mista']):
    ind+='<use class="ind ind-%s" href="#i-%s" x="%d" y="362" width="40" height="28"/>'%(k,k,200+i*50)

glow='<g class="glowwrap" mask="url(#glowMask2)" style="mix-blend-mode:screen"><g filter="url(#soft4)">'
glow+='<path class="g g-stand" d="%s" fill="url(#ggStand2)"/>'%poly(STAND)
glow+='<path class="g g-mistf" d="%s" fill="url(#ggMist2)"/>'%poly(MIST)
glow+='<path class="g g-dim" d="%s" fill="url(#ggDim2)"/>'%poly(DIM)
glow+='<path class="g g-groot" d="%s" fill="url(#ggGroot2)"/>'%poly(GROOT)
glow+='</g></g>'

# oncoming lights above overlay
lx1,lx2=XS(-3.5-.65,70),XS(-3.5+.65,70); ly=Y(70)-.75*S
onc_l='<g class="onc-only"><circle cx="%s" cy="%s" r="%s" fill="url(#rgWarm2)"/><circle cx="%s" cy="%s" r="%s" fill="url(#rgWarm2)"/><circle cx="%s" cy="%s" r="2.2" fill="#fffbea"/><circle cx="%s" cy="%s" r="2.2" fill="#fffbea"/></g>'%(f(lx1),f(ly),f(S*1.6),f(lx2),f(ly),f(S*1.6),f(lx1),f(ly),f(lx2),f(ly))
ring='<ellipse class="dazzle" cx="%s" cy="%s" rx="%s" ry="%s" fill="none" stroke="#ff5a5f" stroke-width="3" stroke-dasharray="8 6"/>'%(f(cx),f(cy-.8*S),f(S*2.4),f(S*2.0))

svg2='<svg id="scene2" class="scene drive" viewBox="0 0 640 400" role="img" aria-label="Zicht door de voorruit op een donkere weg met de lichtbundels" hidden>'
svg2+='<defs>'+defs+'</defs>'
svg2+=world
svg2+='<rect class="daysky" width="640" height="131" fill="url(#skyD)"/>'
svg2+=horizon
svg2+='<g>'+phases+'</g>'
svg2+='<rect class="fogveil" width="640" height="400" fill="url(#fogGrad2)"/>'
svg2+='<rect class="nightrect" width="640" height="400" fill="#04061a" fill-opacity=".93" mask="url(#night2)"/>'
svg2+=glow+onc_l+ring
svg2+='<g class="rl" aria-hidden="true" stroke-width="1" fill="none">'+rul+'</g>'
svg2+=frame+ind
svg2+='</svg>'
open('svg2.txt','w').write(svg2)

# ---------- patch html ----------
def rep(old,new,cnt=1):
    global h
    assert h.count(old)==cnt,(h.count(old),old[:70])
    h=h.replace(old,new)

# css: #scene -> .scene
m=re.search(r'<style>(.*?)</style>',h,re.S); css=m.group(1)
css=css.replace('#scene #world{','.scene .world{').replace('#scene.s-day #world{','.scene.s-day .world{').replace('#scene','.scene')
css=css.replace('display:flex;justify-content:center;\n}','display:flex;flex-direction:column;align-items:center;gap:8px;\n}')
assert 'flex-direction:column;align-items:center;gap:8px' in css
css=css.replace('height:clamp(300px,52svh,560px)','height:clamp(280px,46svh,560px)')
extra='''
.views{display:flex;gap:4px;padding:4px;background:var(--panel);border:1px solid var(--line);border-radius:99px}
.views button{display:inline-flex;align-items:center;gap:7px;padding:7px 14px;border:0;border-radius:99px;background:transparent;color:var(--muted);font-weight:600;font-size:15px;transition:background-color .2s,color .2s}
.views button svg{width:22px;height:22px}
.views button[aria-pressed="true"]{background:var(--text);color:var(--bg)}
svg.scene.drive{height:auto;width:min(100%,640px);aspect-ratio:8/5}
.scene .ind{color:#27304f;transition:color .25s,filter .25s}
.scene.s-stand .ind-stand,.scene.s-dim .ind-dim,.scene.s-mistf .ind-mistf{color:var(--green);filter:drop-shadow(0 0 4px var(--green))}
.scene.s-groot .ind-groot{color:var(--blue);filter:drop-shadow(0 0 4px var(--blue))}
.scene.s-mista .ind-mista{color:var(--amber);filter:drop-shadow(0 0 4px var(--amber))}
.scene .daysky{opacity:0;transition:opacity .8s}
.scene.s-day .daysky{opacity:1}
.scene.s-day .horizon{filter:brightness(1.7)}
.scene .ph{opacity:0;animation:ph .6s linear infinite;animation-play-state:paused}
.scene.s-moving .ph{animation-play-state:running}
@keyframes ph{0%{opacity:1}8.3%{opacity:1}8.4%{opacity:0}100%{opacity:0}}
'''
css=css.replace('\n@media (min-width:900px){',extra+'\n@media (min-width:900px){',1)
css=css.replace('svg.scene{height:clamp(460px,calc(100svh - 130px),800px)}','svg.scene{height:clamp(460px,calc(100svh - 130px),800px)}\n  svg.scene.drive{width:clamp(480px,50vw,640px)}')
h=h[:m.start(1)]+css+h[m.end(1):]

rep('<g id="world">','<g id="world" class="world">')
rep('    <symbol id="i-sun"','''    <symbol id="i-top" viewBox="0 0 24 24"><rect x="7" y="2.5" width="10" height="19" rx="3.5"/><path d="M9 8.5h6M9 16h6"/></symbol>
    <symbol id="i-wind" viewBox="0 0 24 24"><path d="M3 20 8.5 5h7L21 20Z"/><path d="M12 7.5V10M12 13v2.5"/></symbol>
    <symbol id="i-sun"''')
rep('<div class="stagebox">','''<div class="views" role="group" aria-label="Kijkrichting">
        <button type="button" data-view="top" aria-pressed="true"><svg class="i24" viewBox="0 0 24 24" aria-hidden="true"><use href="#i-top"/></svg><span>Van boven</span></button>
        <button type="button" data-view="drive" aria-pressed="false"><svg class="i24" viewBox="0 0 24 24" aria-hidden="true"><use href="#i-wind"/></svg><span>Voorruit</span></button>
      </div>
      <div class="stagebox">''')
rep('</svg>\n\n        <div class="readout"','</svg>\n'+svg2+'\n\n        <div class="readout"')

# js
rep("var scene = document.getElementById('scene');","var scene = document.getElementById('scene');\n  var scene2 = document.getElementById('scene2');\n  var scenes = [scene, scene2];\n  var view = 'top';")
rep("""    KEYS.forEach(function (k) { scene.classList.toggle('s-' + k, s[k]); });
    scene.classList.toggle('s-moving', s.moving);
    scene.classList.toggle('s-tail', s.stand || s.dim || s.groot);""","""    scenes.forEach(function (sc) {
      KEYS.forEach(function (k) { sc.classList.toggle('s-' + k, s[k]); });
      sc.classList.toggle('s-moving', s.moving);
      sc.classList.toggle('s-tail', s.stand || s.dim || s.groot);
    });
    scene.toggleAttribute('hidden', view !== 'top');
    scene2.toggleAttribute('hidden', view !== 'drive');
    document.querySelectorAll('[data-view]').forEach(function (b) {
      b.setAttribute('aria-pressed', String(b.getAttribute('data-view') === view));
    });""")
rep("    } else if (t.id === 'alloff') {","    } else if (t.hasAttribute('data-view')) {\n      view = t.getAttribute('data-view');\n    } else if (t.id === 'alloff') {")
open(p,'w',encoding='utf-8').write(h)
js=re.search(r'<script>(.*?)</script>',h,re.S).group(1)
open('check.js','w').write(js)
print(len(h))
