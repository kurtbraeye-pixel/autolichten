import math
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
def ygrad(id_,color,y1,y2,stops):
    out='<linearGradient id="%s" gradientUnits="userSpaceOnUse" x1="0" y1="%s" x2="0" y2="%s">'%(id_,f(y1),f(y2))
    for off,o in stops: out+='<stop offset="%s" stop-color="%s" stop-opacity="%s"/>'%(off,color,o)
    return out+'</linearGradient>'

DIM=[(-5,3.9),(-5,9),(-3.6,15),(-1.9,23),(-0.6,29),(1.6,32),(3.6,27),(5.2,17),(6,9),(6,3.9)]
GROOT=[(-7,3.9),(-6.5,9),(-4.2,16),(-3.2,40),(-2.6,80),(-1.7,104),(0,109),(1.7,104),(2.6,80),(3.2,40),(4.2,16),(6.5,9),(7,3.9)]
MIST=[(-11,3.9),(-11,10),(-6,18),(0,22),(6,18),(11,10),(11,3.9)]
STAND=[(-4,3.9),(-3,5.5),(-1.2,7.2),(1.2,7.2),(3,5.5),(4,3.9)]
OD=[(-4.8,70),(-2.2,70),(-1.0,40),(-6.6,40)]
OG=[(-4.6,70),(-2.4,70),(-0.3,10),(-7.5,10)]

S=130*P(70); cx=XS(-3.5,70); cy=Y(70)
lx1,lx2=XS(-3.5-.65,70),XS(-3.5+.65,70); ly=Y(70)-.75*S

defs=''
defs+='<filter id="soft3" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="5"/></filter>'
defs+='<filter id="soft4" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="3.5"/></filter>'
defs+='<linearGradient id="skyN" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#070b20"/><stop offset="1" stop-color="#1a2a55"/></linearGradient>'
defs+='<linearGradient id="skyD" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#5f93dc"/><stop offset="1" stop-color="#c4dbf4"/></linearGradient>'
defs+=grad('mgDim2','#000',[(0,1),(21,.85),(33,0)],33)
defs+=grad('mgGroot2','#000',[(0,1),(40,.9),(79,.6),(101,0)],101)
defs+=grad('mgMist2','#000',[(0,1),(15.7,.85),(22.5,0)],22.5)
defs+=grad('mgStand2','#000',[(0,1),(7.5,0)],7.5)
defs+=grad('ggDim2','#fff0cc',[(0,.55),(21,.3),(33,0)],33)
defs+=grad('ggGroot2','#e4eeff',[(0,.6),(40,.38),(79,.15),(101,0)],101)
defs+=grad('ggMist2','#ffe29a',[(0,.85),(15.7,.55),(22.5,0)],22.5)
defs+=grad('ggStand2','#fff0cc',[(0,.5),(7.5,0)],7.5)
defs+=ygrad('mgOd2','#000',Y(70),Y(40),[(0,1),(1,0)])
defs+=ygrad('mgOg2','#000',Y(70),Y(10),[(0,1),(1,0)])
defs+=ygrad('ggOd2','#fff0cc',Y(70),Y(40),[(0,.6),(1,0)])
defs+=ygrad('ggOg2','#e4eeff',Y(70),Y(10),[(0,.6),(1,0)])
defs+=grad('fogGrad2','#b8c4d6',[(4,0),(10,.15),(20,.45),(35,.85),(50,1)],50)
defs+='<linearGradient id="fogCutW2" gradientUnits="userSpaceOnUse" x1="0" y1="%s" x2="0" y2="%s"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset="1" stop-color="#fff" stop-opacity="1"/></linearGradient>'%(f(Y(40)),f(Y(51.5)))
defs+='<linearGradient id="fogCutB2" gradientUnits="userSpaceOnUse" x1="0" y1="%s" x2="0" y2="%s"><stop offset="0" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity="1"/></linearGradient>'%(f(Y(40)),f(Y(51.5)))
defs+='<radialGradient id="rgWarm2"><stop offset="0" stop-color="#fff1c4" stop-opacity=".95"/><stop offset="1" stop-color="#fff1c4" stop-opacity="0"/></radialGradient>'
defs+='<radialGradient id="rgCool2"><stop offset="0" stop-color="#dbe8ff" stop-opacity=".95"/><stop offset="1" stop-color="#dbe8ff" stop-opacity="0"/></radialGradient>'
defs+='<radialGradient id="rgGlare2"><stop offset="0" stop-color="#dfe8f5" stop-opacity=".85"/><stop offset="1" stop-color="#dfe8f5" stop-opacity="0"/></radialGradient>'
defs+='<radialGradient id="rgAmber2"><stop offset="0" stop-color="#ffb224" stop-opacity=".9"/><stop offset="1" stop-color="#ffb224" stop-opacity="0"/></radialGradient>'
defs+='<radialGradient id="rgBloom2"><stop offset="0" stop-color="#fff" stop-opacity=".95"/><stop offset=".4" stop-color="#fff" stop-opacity=".6"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></radialGradient>'
defs+='<radialGradient id="rgVeil2" gradientUnits="userSpaceOnUse" cx="%s" cy="%s" r="340"><stop offset="0" stop-color="#fff" stop-opacity=".55"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></radialGradient>'%(f(cx),f(ly))
defs+='<mask id="night2" maskUnits="userSpaceOnUse" x="0" y="0" width="640" height="400"><rect width="640" height="400" fill="#fff"/><g filter="url(#soft3)">'
defs+='<path class="m m-stand" d="%s" fill="url(#mgStand2)"/>'%poly(STAND)
defs+='<path class="m m-mistf" d="%s" fill="url(#mgMist2)"/>'%poly(MIST)
defs+='<path class="m m-dim" d="%s" fill="url(#mgDim2)"/>'%poly(DIM)
defs+='<path class="m m-groot" d="%s" fill="url(#mgGroot2)"/>'%poly(GROOT)
defs+='<path class="m m-od" d="%s" fill="url(#mgOd2)"/>'%poly(OD)
defs+='<path class="m m-og" d="%s" fill="url(#mgOg2)"/>'%poly(OG)
defs+='</g><rect class="fogcut" width="640" height="400" fill="url(#fogCutW2)"/></mask>'
defs+='<mask id="glowMask2" maskUnits="userSpaceOnUse" x="0" y="0" width="640" height="400"><rect width="640" height="400" fill="#fff"/><rect class="fogcut" width="640" height="400" fill="url(#fogCutB2)"/></mask>'

world='<g class="world">'
world+='<rect width="640" height="400" fill="url(#skyN)"/>'
world+='<rect y="130" width="640" height="270" fill="#17331f"/>'
world+='<path d="M%s 400L%s 400L320 130Z" fill="#2c3346"/>'%(f(XS(-5.5,4)),f(XS(2.4,4)))
def band(X,w,Za,Zb,fill):
    a,b=XS(X-w/2,Za),XS(X+w/2,Za); c,d=XS(X+w/2,Zb),XS(X-w/2,Zb)
    return '<path d="M%s %sL%s %sL%s %sL%s %sZ" fill="%s"/>'%(f(a),f(Y(Za)),f(b),f(Y(Za)),f(c),f(Y(Zb)),f(d),f(Y(Zb)),fill)
world+=band(1.95,.14,3.9,2000,'#e8ecf5')+band(-5.35,.14,3.9,2000,'#e8ecf5')
def obj(Z,X,inner):
    s=130*P(Z)
    return '<g transform="translate(%s %s) scale(%.3f)">%s</g>'%(f(XS(X,Z)),f(Y(Z)),s,inner)
person='<rect x="-.2" y="-.8" width=".4" height=".8" fill="#2a3040"/><rect x="-.28" y="-1.45" width=".56" height=".7" rx=".08" fill="#ffd21f"/><rect x="-.28" y="-1.2" width=".56" height=".07" fill="#fff"/><circle cy="-1.62" r=".15" fill="#d9a77e"/>'
cone='<rect x="-.2" y="-.04" width=".4" height=".04" fill="#242a3a"/><path d="M-.17 -.04L-.05 -.7H.05L.17 -.04Z" fill="#ff6a1a"/><path d="M-.12 -.28L-.09 -.42H.09L.12 -.28Z" fill="#fff3e0"/>'
deer='<ellipse cy="-.95" rx=".65" ry=".3" fill="#8b5e3c"/><g fill="#8b5e3c"><rect x="-.55" y="-.8" width=".08" height=".8"/><rect x="-.35" y="-.8" width=".08" height=".8"/><rect x=".3" y="-.8" width=".08" height=".8"/><rect x=".5" y="-.8" width=".08" height=".8"/><path d="M-.55 -1.1L-.78 -1.45L-.9 -1.38L-.62 -.95Z"/><circle cx="-.85" cy="-1.5" r=".16"/></g><path d="M-.85 -1.65l-.1 -.3M-.85 -1.65l.12 -.28M-.95 -1.9l-.12 -.1" stroke="#d9c6a3" stroke-width=".05" stroke-linecap="round" fill="none"/><circle cx="-.93" cy="-1.52" r=".04" fill="#e9ff7a"/>'
world+=obj(15,2.7,person)+obj(25,0.2,cone)+obj(63,0.6,deer)
world+='<g class="onc-only"><g transform="translate(%s %s) scale(%.3f)"><rect x="-.95" y="-.35" width=".25" height=".35" fill="#0a0c14"/><rect x=".7" y="-.35" width=".25" height=".35" fill="#0a0c14"/><rect x="-.9" y="-1.5" width="1.8" height="1.2" rx=".25" fill="#8a6a4e"/><rect x="-.7" y="-1.45" width="1.4" height=".5" rx=".12" fill="#141c30"/></g></g>'%(f(cx),f(cy),S)
world+='</g>'

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
            s=130*P(z)
            out+='<g transform="translate(%s %s) scale(%.3f)"><rect x="-.07" y="-.95" width=".14" height=".95" fill="#f5f6fa"/><rect x="-.07" y="-.95" width=".14" height=".16" fill="#e23a3a"/></g>'%(f(XS(X,z)),f(Y(z)),s)
    for k in range(0,12):
        for X,off in ((-9.5,3),(7.5,9)):
            z=12*k+off-j
            if z<25 or z>140: continue
            s=130*P(z)
            out+='<g transform="translate(%s %s) scale(%.3f)"><rect x="-.2" y="-1.6" width=".4" height="1.6" fill="#2a2018"/><ellipse cy="-4.2" rx="2" ry="2.8" fill="#173d25"/></g>'%(f(XS(X,z)),f(Y(z)),s)
    return out+'</g>'
phases=''.join(phase(j) for j in range(12))

pts=['0 130']
for i in range(0,41):
    x=i*16; hgt=7+5*math.sin(i*1.7)+4*math.sin(i*0.63+1)
    pts.append('%d %.1f'%(x,130-hgt))
pts.append('640 130')
horizon='<path class="horizon" d="M%sZ" fill="#14301f"/>'%'L'.join(pts)

rul=''
for d in (20,40,60,80,100):
    y=Y(d); x=XS(2.3,d)
    rul+='<path d="M%s %sh14" stroke="#9fb0d9" stroke-opacity=".55"/><text x="%s" y="%s">%d m</text>'%(f(x),f(y),f(x+17),f(y+3.5),d)

frame='''<path d="M0 0H86L30 400H0Z" fill="#090d1b"/><path d="M640 0H554L610 400H640Z" fill="#090d1b"/>
<path d="M0 0H640V22Q320 46 0 22Z" fill="#090d1b"/>
<rect x="282" y="14" width="76" height="26" rx="7" fill="#0d1324" stroke="#202c4d"/><rect x="288" y="19" width="64" height="16" rx="4" fill="#121b36"/>
<path d="M0 374Q320 336 640 374V400H0Z" fill="#090d1b"/><path d="M0 374Q320 336 640 374" fill="none" stroke="#1d2744" stroke-width="2"/>'''
ind=''
for i,k in enumerate(['stand','dim','groot','mistf','mista']):
    ind+='<use class="ind ind-%s" href="#i-%s" x="%d" y="362" width="40" height="28"/>'%(k,k,185+i*50)
ind+='<use class="ind ind-hz" href="#i-hazard" x="450" y="362" width="40" height="28"/>'

glow='<g class="glowwrap" mask="url(#glowMask2)" style="mix-blend-mode:screen"><g filter="url(#soft4)">'
glow+='<path class="g g-stand" d="%s" fill="url(#ggStand2)"/>'%poly(STAND)
glow+='<path class="g g-mistf" d="%s" fill="url(#ggMist2)"/>'%poly(MIST)
glow+='<path class="g g-dim" d="%s" fill="url(#ggDim2)"/>'%poly(DIM)
glow+='<path class="g g-groot" d="%s" fill="url(#ggGroot2)"/>'%poly(GROOT)
glow+='<path class="g g-od" d="%s" fill="url(#ggOd2)"/>'%poly(OD)
glow+='<path class="g g-og" d="%s" fill="url(#ggOg2)"/>'%poly(OG)
glow+='</g></g>'

glare='<ellipse class="glare" cx="320" cy="310" rx="300" ry="120" fill="url(#rgGlare2)"/>'

def lights(r,fill,sf): return '<circle cx="%s" cy="%s" r="%s" fill="%s"/><circle cx="%s" cy="%s" r="%s" fill="%s"/>'%(f(lx1),f(ly),f(r),fill,f(lx2),f(ly),f(r),fill)
onc_l='<g class="onc-only">'
onc_l+='<g class="oc oc-dim">'+lights(S*1.6,'url(#rgWarm2)',0)+'</g>'
onc_l+='<g class="oc oc-groot">'+lights(S*4.5,'url(#rgCool2)',0)+'</g>'
onc_l+='<g class="oc oc-lit">'+lights(2.2,'#fffbea',0)+'</g></g>'
ring='<ellipse class="dazzle" cx="%s" cy="%s" rx="%s" ry="%s" fill="none" stroke="#ff5a5f" stroke-width="3" stroke-dasharray="8 6"/>'%(f(cx),f(cy-.8*S),f(S*2.4),f(S*2.0))
dz='<g class="dz"><circle cx="%s" cy="%s" r="75" fill="url(#rgBloom2)"/><rect width="640" height="400" fill="url(#rgVeil2)"/></g>'%(f(cx),f(ly))
hz='<g class="hz"><circle cx="30" cy="372" r="75" fill="url(#rgAmber2)"/><circle cx="610" cy="372" r="75" fill="url(#rgAmber2)"/></g>'

svg2='<svg id="scene2" class="scene drive" viewBox="0 0 640 400" role="img" aria-label="Zicht door de voorruit op een donkere weg met de lichtbundels" hidden>'
svg2+='<defs>'+defs+'</defs>'
svg2+=world
svg2+='<rect class="daysky" width="640" height="131" fill="url(#skyD)"/>'
svg2+=horizon
svg2+='<g>'+phases+'</g>'
svg2+='<rect class="fogveil" width="640" height="400" fill="url(#fogGrad2)"/>'
svg2+='<rect class="nightrect" width="640" height="400" fill="#04061a" fill-opacity=".93" mask="url(#night2)"/>'
svg2+=glow+glare+onc_l+ring+dz
svg2+='<g class="rl" aria-hidden="true" stroke-width="1" fill="none">'+rul+'</g>'
svg2+=hz+frame+ind
svg2+='</svg>'
open('svg2.txt','w').write(svg2)
