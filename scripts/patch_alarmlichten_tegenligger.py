import re
p='autolichten.html'
h=open(p,encoding='utf-8').read()
def rep(old,new,cnt=1):
    global h
    assert h.count(old)==cnt,(h.count(old),old[:80])
    h=h.replace(old,new)

# ---- svg2 vervangen ----
svg2=open('svg2.txt',encoding='utf-8').read()
h,n=re.subn(r'<svg id="scene2".*?</svg>',lambda m:svg2,h,count=1,flags=re.S); assert n==1

# ---- symbool ----
rep('    <symbol id="i-sun"','''    <symbol id="i-hazard" viewBox="0 0 52 36" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M26 4 46 32H6Z"/><path d="M26 13 36 27H16Z"/></symbol>
    <symbol id="i-sun"''')

# ---- CSS ----
rep('.scene.s-stand .m-stand,.scene.s-stand .g-stand{opacity:1}','.scene.s-stand .m-stand,.scene.s-stand .g-stand{opacity:var(--vis,1)}')
rep('.scene.s-dim .m-dim,.scene.s-dim .g-dim{opacity:1}','.scene.s-dim .m-dim,.scene.s-dim .g-dim{opacity:var(--vis,1)}')
rep('.scene.s-groot .m-groot,.scene.s-groot .g-groot{opacity:1}','.scene.s-groot .m-groot,.scene.s-groot .g-groot{opacity:var(--vis,1)}')
rep('.scene.s-mistf .m-mistf,.scene.s-mistf .g-mistf{opacity:1}','.scene.s-mistf .m-mistf,.scene.s-mistf .g-mistf{opacity:var(--vis,1)}')
rep('position:absolute;top:10px;right:10px;display:flex;align-items:center;gap:6px;','display:flex;align-items:center;gap:6px;')
extra='''
.alerts{position:absolute;top:10px;right:10px;display:flex;flex-direction:column;align-items:flex-end;gap:6px;pointer-events:none}
.warn2{background:#ffe08a;color:#1a1200}
.light.hazard{--c:var(--alert);grid-column:1/-1;grid-template-columns:auto 1fr auto;grid-template-areas:"ico name sw" "ico hint sw";column-gap:14px;align-items:center}
.light.hazard[aria-pressed="true"] .ico{animation:blink 1s steps(1,end) infinite}
.oncl{margin-top:16px}
.oncl .h{margin-bottom:8px}
.chip svg.lamp{width:38px;height:26px}
@keyframes blink{0%,49.9%{opacity:1}50%,100%{opacity:0}}
.scene .hz{opacity:0}
.scene.s-hazard .hz{animation:blink 1s steps(1,end) infinite}
.scene.s-hazard .ind-hz{color:var(--alert);filter:drop-shadow(0 0 4px var(--alert));animation:blink 1s steps(1,end) infinite}
.scene .oc,.scene .dz,.scene .flare,.scene .glare{opacity:0;transition:opacity .35s}
.scene.s-onc.s-od .m-od,.scene.s-onc.s-od .g-od,.scene.s-onc.s-og .m-og,.scene.s-onc.s-og .g-og{opacity:1}
.scene.s-onc.s-od .oc-lit,.scene.s-onc.s-og .oc-lit,.scene.s-onc.s-od .oc-dim,.scene.s-onc.s-og .oc-groot{opacity:1}
.scene.s-dazzled .dz,.scene.s-dazzled .flare{opacity:1}
.scene.s-dazzled{--vis:.35}
.scene.s-fog.s-dim:not(.s-mistf) .glare{opacity:.35}
.scene.s-fog.s-dim.s-mistf .glare{opacity:.1}
.scene.s-fog.s-groot .glare{opacity:.65}
.scene.s-day .glare{opacity:0!important}
'''
rep('\n@media (min-width:900px){',extra+'\n@media (min-width:900px){')
rep('  *{transition:none!important;animation:none!important}\n}','  *{transition:none!important;animation:none!important}\n  .scene.s-hazard .hz{opacity:.9!important}\n}')

# ---- svg1: defs ----
rep('<!-- mist: zicht stopt op ± 50 m -->','''<linearGradient id="mgOd" gradientUnits="userSpaceOnUse" x1="0" y1="213" x2="0" y2="348"><stop offset="0" stop-color="#000" stop-opacity="1"/><stop offset=".6" stop-color="#000" stop-opacity=".8"/><stop offset="1" stop-color="#000" stop-opacity="0"/></linearGradient>
            <linearGradient id="mgOg" gradientUnits="userSpaceOnUse" x1="0" y1="213" x2="0" y2="565"><stop offset="0" stop-color="#000" stop-opacity="1"/><stop offset=".5" stop-color="#000" stop-opacity=".85"/><stop offset="1" stop-color="#000" stop-opacity="0"/></linearGradient>
            <linearGradient id="ggOd" gradientUnits="userSpaceOnUse" x1="0" y1="213" x2="0" y2="348"><stop offset="0" stop-color="#fff0cc" stop-opacity=".55"/><stop offset="1" stop-color="#fff0cc" stop-opacity="0"/></linearGradient>
            <linearGradient id="ggOg" gradientUnits="userSpaceOnUse" x1="0" y1="213" x2="0" y2="565"><stop offset="0" stop-color="#e4eeff" stop-opacity=".6"/><stop offset=".5" stop-color="#e4eeff" stop-opacity=".35"/><stop offset="1" stop-color="#e4eeff" stop-opacity="0"/></linearGradient>
            <radialGradient id="rgGlare"><stop offset="0" stop-color="#dfe8f5" stop-opacity=".85"/><stop offset="1" stop-color="#dfe8f5" stop-opacity="0"/></radialGradient>
            <radialGradient id="rgFlare"><stop offset="0" stop-color="#fff" stop-opacity=".95"/><stop offset=".45" stop-color="#fff" stop-opacity=".55"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></radialGradient>
            <radialGradient id="rgAmber"><stop offset="0" stop-color="#ffb224" stop-opacity=".9"/><stop offset="1" stop-color="#ffb224" stop-opacity="0"/></radialGradient>
            <!-- mist: zicht stopt op ± 50 m -->''')
# mask: bundels tegenligger
rep('<rect class="fogcut" width="360" height="640" fill="url(#fogCutW)"/>','''<g filter="url(#soft)"><path class="m m-od" d="M115 213L82 300Q130 348 178 300L145 213Z" fill="url(#mgOd)"/><path class="m m-og" d="M115 213L50 430Q150 600 260 430L145 213Z" fill="url(#mgOg)"/></g>
              <rect class="fogcut" width="360" height="640" fill="url(#fogCutW)"/>''')
# bundels mistlicht voor en dimlicht aanpassen
rep('M212 508L100 490Q130 428 230 420Q330 428 360 490L248 508Z','M212 508L40 494Q70 428 230 418Q340 428 360 494L248 508Z',2)
rep('M214 504L112 474Q130 424 208 396Q236 366 268 374Q322 392 340 462L246 504Z','M214 504L150 478Q150 424 208 396Q236 366 268 374Q312 392 318 462L246 504Z',2)
rep('<stop offset="0" stop-color="#ffe29a" stop-opacity=".6"/><stop offset="1" stop-color="#ffe29a" stop-opacity="0"/>','<stop offset="0" stop-color="#ffe29a" stop-opacity=".85"/><stop offset="1" stop-color="#ffe29a" stop-opacity="0"/>')
# tegenligger: lichten + bundels
h,n=re.subn(r'<!-- tegenligger: eigen lichten -->.*?(?=<circle class="dazzle")',lambda m:'''<ellipse class="glare" cx="230" cy="450" rx="135" ry="105" fill="url(#rgGlare)"/>
          <!-- tegenligger: eigen lichten -->
          <g style="mix-blend-mode:screen"><g filter="url(#soft2)">
            <path class="g g-od" d="M115 213L82 300Q130 348 178 300L145 213Z" fill="url(#ggOd)"/>
            <path class="g g-og" d="M115 213L50 430Q150 600 260 430L145 213Z" fill="url(#ggOg)"/>
          </g></g>
          <g class="onc-only">
            <g class="oc oc-dim"><circle cx="115" cy="212" r="16" fill="url(#rgWarm)"/><circle cx="145" cy="212" r="16" fill="url(#rgWarm)"/></g>
            <g class="oc oc-groot"><circle cx="115" cy="212" r="32" fill="url(#rgCool)"/><circle cx="145" cy="212" r="32" fill="url(#rgCool)"/></g>
            <g class="oc oc-lit"><circle cx="115" cy="212" r="3.6" fill="#fffbea"/><circle cx="145" cy="212" r="3.6" fill="#fffbea"/></g>
          </g>
          ''',h,count=1,flags=re.S); assert n==1
# auto: alarmlichten + flare
rep('''<circle class="halo halo-fogr" cx="-4" cy="98" r="14" fill="url(#rgRed)"/>
          </g>
          </g>''','''<circle class="halo halo-fogr" cx="-4" cy="98" r="14" fill="url(#rgRed)"/>
            <g class="hz">
              <circle cx="-21" cy="9" r="22" fill="url(#rgAmber)"/><circle cx="21" cy="9" r="22" fill="url(#rgAmber)"/><circle cx="-21" cy="91" r="22" fill="url(#rgAmber)"/><circle cx="21" cy="91" r="22" fill="url(#rgAmber)"/>
              <rect x="-25" y="7" width="7" height="4" rx="1.5" fill="#ffb224"/><rect x="18" y="7" width="7" height="4" rx="1.5" fill="#ffb224"/><rect x="-25" y="89" width="7" height="4" rx="1.5" fill="#ffb224"/><rect x="18" y="89" width="7" height="4" rx="1.5" fill="#ffb224"/>
            </g>
            <circle class="flare" cx="0" cy="25" r="75" fill="url(#rgFlare)"/>
          </g>
          </g>''')

# ---- HTML ----
rep('''          <span>Verblind!</span>
        </div>''','''          <span>Hij is verblind!</span>
        </div>
        <div class="warn warn2" id="warn2" hidden>
          <svg class="i24" viewBox="0 0 24 24" aria-hidden="true"><use href="#i-eye"/></svg>
          <span>Jij bent verblind!</span>
        </div>
      </div>''')
rep('''        <div class="warn" id="warn" hidden>''','''        <div class="alerts">
        <div class="warn" id="warn" hidden>''')
rep('''          <button class="alloff" type="button" id="alloff">
            <svg viewBox="0 0 24 24" aria-hidden="true"><use href="#i-power"/></svg>
            <span>Alles uit</span>
          </button>''','''          <button class="alloff" type="button" id="alloff">
            <svg viewBox="0 0 24 24" aria-hidden="true"><use href="#i-power"/></svg>
            <span>Alles uit</span>
          </button>
          <button class="light hazard" type="button" data-light="hazard" aria-pressed="false">
            <svg class="ico" viewBox="0 0 52 36" aria-hidden="true"><use href="#i-hazard"/></svg>
            <span class="sw" aria-hidden="true"></span>
            <span class="name">Alarmlichten</span>
            <span class="hint">Autopech of gevaar</span>
          </button>''')
rep('''<span>Mist op de weg</span>
          </button>
        </div>''','''<span>Mist op de weg</span>
          </button>
        </div>
        <div class="oncl" id="oncl" hidden>
          <h3 class="h">Lichten van de tegenligger</h3>
          <div class="chips">
            <button class="chip" type="button" data-oncl="off" aria-pressed="false"><svg class="i24" viewBox="0 0 24 24" aria-hidden="true"><use href="#i-power"/></svg><span>Uit</span></button>
            <button class="chip" type="button" data-oncl="dim" aria-pressed="true"><svg class="lamp" viewBox="0 0 52 36" aria-hidden="true"><use href="#i-dim"/></svg><span>Dimlicht</span></button>
            <button class="chip" type="button" data-oncl="groot" aria-pressed="false"><svg class="lamp" viewBox="0 0 52 36" aria-hidden="true"><use href="#i-groot"/></svg><span>Grootlicht</span></button>
          </div>
        </div>''')

# ---- JS ----
rep("var warnEl = document.getElementById('warn');","var warnEl = document.getElementById('warn');\n  var warn2El = document.getElementById('warn2');")
rep("'day', 'parked'];","'day', 'parked', 'hazard'];")
rep('day: false, parked: false, moving: true };','day: false, parked: false, moving: true, hazard: false, oncl: \'dim\' };')
h=re.sub(r'parked: (true|false) \}',r'parked: \1, hazard: false }',h)
rep("    var text;\n    if (s.day) {","""    var dz = s.onc && s.oncl === 'groot' && !s.day;
    scenes.forEach(function (sc) {
      sc.classList.toggle('s-od', s.oncl === 'dim');
      sc.classList.toggle('s-og', s.oncl === 'groot');
      sc.classList.toggle('s-dazzled', dz);
    });
    document.getElementById('oncl').toggleAttribute('hidden', !s.onc);
    document.querySelectorAll('[data-oncl]').forEach(function (b) {
      b.setAttribute('aria-pressed', String(b.getAttribute('data-oncl') === s.oncl));
    });
    warn2El.hidden = !dz;

    var text;
    if (s.day) {""")
rep("    } else if (t.hasAttribute('data-view')) {","    } else if (t.hasAttribute('data-oncl')) {\n      s.oncl = t.getAttribute('data-oncl');\n    } else if (t.hasAttribute('data-view')) {")
rep("['stand', 'dim', 'groot', 'mistf', 'mista'].forEach(function (k) { s[k] = false; });","['stand', 'dim', 'groot', 'mistf', 'mista', 'hazard'].forEach(function (k) { s[k] = false; });")
rep("KEYS.forEach(function (k) { if (k !== 'parked') s[k] = p[k]; });","KEYS.forEach(function (k) { if (k !== 'parked') s[k] = p[k]; });\n      s.oncl = 'dim';")
open(p,'w',encoding='utf-8').write(h)
js=re.search(r'<script>(.*?)</script>',h,re.S).group(1)
open('check.js','w').write(js)
print('ok',len(h))
