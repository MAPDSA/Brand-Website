import os
D=os.path.dirname(os.path.abspath(__file__))
IC={'eye':'<path d="M2 12s3.5-6.5 10-6.5S22 12 22 12s-3.5 6.5-10 6.5S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
'beep':'<path d="M11 5L6 9H3v6h3l5 4z"/><path d="M15.5 8.5a5 5 0 0 1 0 7M18.5 5.5a9 9 0 0 1 0 13"/>',
'chart':'<path d="M4 19V10M10 19V5M16 19v-7M22 19H2"/>',
'sleep':'<path d="M3 12c2.5 3 5.5 4.5 9 4.5s6.5-1.5 9-4.5"/><path d="M6 15.5l-1.5 2M10 16.5l-.5 2.5M14 16.5l.5 2.5M18 15.5l1.5 2"/>',
'clock':'<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 3"/>',
'away':'<path d="M3 3l18 18"/><path d="M10.6 5.6A9.7 9.7 0 0 1 12 5.5c6.5 0 10 6.5 10 6.5a17 17 0 0 1-3.2 4M6.6 6.6A17 17 0 0 0 2 12s3.5 6.5 10 6.5a9.6 9.6 0 0 0 5.4-1.6"/>',
'speed':'<path d="M3.5 17a9 9 0 1 1 17 0"/><path d="M12 13l4.5-4.5"/><circle cx="12" cy="13" r="1.2"/>',
'face':'<circle cx="12" cy="12" r="9"/><path d="M9 10h.01M15 10h.01M9 15h6"/>',
'belt':'<path d="M5 3l14 18M9 3h6M4 21h16"/>',
'truck':'<path d="M3 6h11v10H3zM14 9h4l3 3v4h-7"/><circle cx="7" cy="18" r="2"/><circle cx="17" cy="18" r="2"/>',
'users':'<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0"/><path d="M16 4.5a3.5 3.5 0 0 1 0 7M21.5 20a6.5 6.5 0 0 0-4-6"/>',
'heart':'<path d="M12 20s-7-4.5-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.5-7 10-7 10z"/>',
'lock':'<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/>',
'pin':'<path d="M12 21s-7-6.5-7-12a7 7 0 0 1 14 0c0 5.5-7 12-7 12z"/><circle cx="12" cy="9" r="2.5"/>',
'star':'<path d="M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1L3.2 9.5l6.1-.9z"/>',
'sos':'<circle cx="12" cy="12" r="9"/><path d="M12 7v6M12 16.5v.5"/>',
'plug':'<path d="M9 2v6M15 2v6M6 8h12v4a6 6 0 0 1-12 0zM12 18v4"/>',
'layers':'<path d="M12 3l9 5-9 5-9-5z"/><path d="M3 13l9 5 9-5"/>'}
def ic(n): return f'<div class="ic"><svg viewBox="0 0 24 24" aria-hidden="true">{IC[n]}</svg></div>'
def card(icon,t,p,blue=False,num=''):
  return f'<div class="card{" b" if blue else ""}">{ic(icon)}{f"<p class=num>{num}</p>" if num else ""}<h3>{t}</h3><p>{p}</p></div>'
NAV=[('Products','products.html',[('blinksmart.html','Blinksmart™','Driver drowsiness &amp; distraction (DMS + DFMS)'),('copilot-ai.html','CoPilot AI™','Modular ADAS platform and fleet dashboard'),('bike-adas.html','Bike ADAS','Rider safety for two-wheelers'),('products.html#buy','How you buy it','Hardware, APIs, subscriptions, data')]),
 ('Solutions','solutions.html',[('public-transport.html','Public transport &amp; school','Buses, state transport, school fleets'),('logistics.html','Logistics &amp; fleet','Trucks, cabs and staff transport'),('oem.html','OEM integration','Factory-fit DMS and ADAS'),('defense.html','Defense &amp; special vehicles','Convoys and mission vehicles')]),
 ('Technology','technology.html',[('technology.html#platform','Platform &amp; hardware','Edge NPU, cameras, connectivity'),('technology.html#ai','CoPilot AI™ vision &amp; ML','On-device computer vision'),('technology.html#compliance','Compliance &amp; standards','CMVR 2025 DDAWS')]),
 ('Company','about.html',[('about.html','About us','Our story and founder'),('about.html#team','Team &amp; advisors','Leadership and advisory board'),('customers.html','Customers','Clients and track record'),('research.html','Research &amp; innovation','Patents and R&amp;D'),('news.html','News &amp; media','Announcements'),('careers.html','Careers','Join the team')]),
 ('Contact','contact.html',[])]
def navhtml(fn):
  out=''
  for t,h,ch in NAV:
    on=fn==h or any(fn==c[0].split('#')[0] for c in ch)
    cls=' class="on"' if on else ''
    if ch:
      sub=''.join(f'<a href="{c[0]}"><b>{c[1]}</b><span>{c[2]}</span></a>' for c in ch)
      out+=f'<li class="dd"><a href="{h}"{cls}>{t}<svg viewBox="0 0 12 12" aria-hidden="true"><path d="M3 4.5l3 3 3-3"/></svg></a><div class="ddp">{sub}</div></li>'
    else: out+=f'<li><a href="{h}"{cls}>{t}</a></li>'
  return out
DEMO='https://youtu.be/9kMJqMemYnM'
def page(fn,title,desc,body):
  nav=navhtml(fn)
  html=f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="claude:viewport-fit-sides" content="cover">
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="assets/device-angled.webp">
<link rel="icon" href="assets/sapience-logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap">
<link rel="stylesheet" href="style.css">
</head>
<body>
<header class="nav"><div class="wrap">
<a href="./" aria-label="Sapience Automata home"><img src="assets/sapience-logo.png" alt="Sapience Automata™ Crafting Greatness" width="200" height="34"></a>
<nav aria-label="Main"><ul id="menu">{nav}</ul></nav>
<div class="btns"><a class="btn btn-p" href="contact.html">Request a demo</a><button class="menu" id="menuBtn" aria-controls="menu" aria-expanded="false">Menu</button></div>
</div></header>
<main>
{body}
</main>
<footer><div class="wrap">
<div class="col" style="max-width:340px"><img src="assets/sapience-logo.png" alt="Sapience Automata™"><p class="muted">Transforming road safety with AI. Makers of Blinksmart™ and CoPilot AI™.</p></div>
<div class="col"><b>Products</b><a href="blinksmart.html">Blinksmart™</a><a href="copilot-ai.html">CoPilot AI™</a><a href="bike-adas.html">Bike ADAS</a><a href="products.html#buy">How you buy it</a></div>
<div class="col"><b>Solutions</b><a href="public-transport.html">Public transport</a><a href="logistics.html">Logistics &amp; fleet</a><a href="oem.html">OEM integration</a><a href="defense.html">Defense</a></div>
<div class="col"><b>Company</b><a href="about.html">About us</a><a href="technology.html">Technology</a><a href="customers.html">Customers</a><a href="research.html">Research</a><a href="news.html">News</a><a href="careers.html">Careers</a><a href="https://www.sapienceautomata.com/privacy-policy" target="_blank" rel="noopener">Privacy policy</a></div>
<div class="col"><b>Get in touch</b><a href="mailto:info@sapienceautomata.com">info@sapienceautomata.com</a><a href="tel:+918100675937">+91 81006 75937</a><span class="muted">Indiranagar, Bengaluru</span>
<div class="btns" style="gap:16px;margin-top:6px"><a href="https://www.linkedin.com/company/sapienceautomata/" target="_blank" rel="noopener">LinkedIn</a><a href="https://www.instagram.com/sapience_automata/" target="_blank" rel="noopener">Instagram</a><a href="https://www.youtube.com/@SapienceAutomata" target="_blank" rel="noopener">YouTube</a></div></div>
</div><div class="wrap"><p class="copy">© 2026 Quivive Automata Private Limited (Sapience Automata™). Blinksmart™, CoPilot AI™ and Sapience Automata™ are trademarks of Quivive Automata Private Limited.</p></div></footer>
<script>(function(){{var b=document.getElementById('menuBtn'),m=document.getElementById('menu');if(b&&m)b.addEventListener('click',function(){{m.classList.toggle('open');b.setAttribute('aria-expanded',m.classList.contains('open'))}});var v=document.getElementById('heroVid'),sb=document.getElementById('sndBtn');if(v&&sb)sb.addEventListener('click',function(){{v.muted=!v.muted;if(!v.muted){{v.currentTime=0;v.play()}}sb.textContent=v.muted?'Sound on':'Sound off';sb.setAttribute('aria-pressed',String(!v.muted))}});}})();</script>
</body>
</html>'''
  open(os.path.join(D,fn),'w').write(html)
  if fn=='index.html':
    head=html.split('<head>')[1].split('</head>')[0].replace('<meta charset="utf-8">','').replace('<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">','')
    bodyh=html.split('<body>')[1].split('</body>')[0]
    open(os.path.join(D,'home-artifact.html'),'w').write(head.strip()+'\n'+bodyh)

STATS='''<section class="statwrap"><div class="wrap"><div class="statcard row">
<div><b>1000+</b><span>Blinksmart™ devices installed</span></div>
<div><b>2.9 Cr+</b><span>km with zero fatal accidents</span></div>
<div><b>10,000+</b><span>passengers travel safely every day</span></div>
<div><b>95%+</b><span>alert accuracy</span></div></div></div></section>'''
CTA=lambda h,p:f'''<section><div class="wrap"><div class="cta"><div><span class="eyebrow eb-w">Get in touch</span><h2>{h}</h2><p class="lead" style="color:#DCE6FF">{p}</p><div class="btns"><a class="btn btn-w" href="contact.html">Book a demo</a><a class="btn btn-g" href="{DEMO}" target="_blank" rel="noopener">Watch demo</a></div></div><dl class="cta-dl"><div><dt>Email</dt><dd>info@sapienceautomata.com</dd></div><div><dt>Phone</dt><dd>+91 81006 75937</dd></div><div><dt>Office</dt><dd>Indiranagar, Bengaluru</dd></div></dl></div></div></section>'''

# ---------------- SHARED BLOCKS ----------------
CL=[('redbus','redBus'),('ksrtc','KSRTC'),('kkrtc','KKRTC'),('cabswale','CabsWale'),('volvo-eicher','Volvo Eicher'),('dreamline','DreamLine Travels'),('humsafar','Humsafar Travels'),('kondody','Kondody Autocraft'),('itriangle','iTriangle'),('cognecto','Cognecto'),('masstrans','Masstrans'),('datakrew','DataKrew'),('damodar','Damodar'),('rajesh','Rajesh Transports'),('agustya','Agustya'),('ve-connected','VE Connected')]
LOGOS='<div class="clients">'+''.join(f'<div><img src="assets/clients/{f}.webp" alt="{n}" loading="lazy"></div>' for f,n in CL)+'</div>'
def head(eb,h,p='',center=False):
  return f'<div class="stack{" center" if center else ""}"><span class="eyebrow">{eb}</span><h2>{h}</h2>{f"<p class=lead>{p}</p>" if p else ""}</div>'
def tile(href,icon,t,p,blue=False):
  return f'<a class="card link{" b" if blue else ""}" href="{href}">{ic(icon)}<h3>{t}</h3><p>{p}</p><span class="more">Learn more →</span></a>'
OUTCOMES=f'''<div class="row">{card('sos','Accident &amp; collision prevention','Catch drowsiness, distraction and road hazards before they turn into a crash.')}{card('eye','Predictive safety','Patented AI that reads risk around the vehicle early, not after the fact.')}{card('users','Driver risk management','Scores, snapshots and coaching data for every driver.')}</div>
<div class="row">{card('pin','Real-time monitoring','Live alerts and location for every vehicle, on web and mobile.')}{card('chart','Safety analytics','Trends across routes, shifts and drivers, so you fix the cause.')}{card('plug','Vehicle diagnostics','OBD and CAN data alongside driver behaviour on one platform.')}</div>'''
FLOW='''<div class="flow">
<div class="fcol"><span class="flab">Inputs</span><b>Up to 4 AI cameras</b><b>GPS + OBD</b><b>CAN bus</b><b>4G / 5G · Wi-Fi · BT</b></div>
<div class="fdev"><span class="flab" style="color:#BFD0FF">One edge device</span><h3>CoPilot AI™ edge platform</h3><p>6–12 TOPS NPU. Computer vision and behaviour analytics run on the vehicle, in real time.</p></div>
<div class="fcol"><span class="flab">Systems</span><b>DDAWS · driver drowsiness</b><b>BSIS · blind spot</b><b>MOIS · moving off</b><b>LDWS · lane departure</b><b>FCW / AEBS-ready</b></div>
</div>'''
FAQ='''<section><div class="wrap stack" style="gap:24px;max-width:900px">
<span class="eyebrow">FAQs</span><h2>Questions, answered.</h2>
<div>
<details><summary>How is Blinksmart™ different from a traditional DMS or dashcam?</summary><p>A dashcam records the crash. Blinksmart™ watches the driver and alerts them the moment they turn drowsy or distracted, so they can correct course in time. The AI runs on the device, so alerts don’t wait on the cloud.</p></details>
<details><summary>Is CoPilot AI™ included with Blinksmart™?</summary><p>Yes. Blinksmart™ is part of the CoPilot AI™ ecosystem. Alerts, live location and driver scores reach the fleet owner on the CoPilot AI™ web and mobile apps.</p></details>
<details><summary>Which vehicles does it work in?</summary><p>Buses, trucks, cabs and special vehicles, as a retrofit or factory-fit with OEMs. CoPilot AI™ scales from one AI camera to four.</p></details>
<details><summary>Can it predict risk, or only react?</summary><p>Both. Blinksmart™ alerts on drowsiness and distraction in real time, and our patented AI is built for early prediction of risks surrounding the vehicle.</p></details>
<details><summary>Does it help with the new DDAWS rules?</summary><p>Blinksmart™ is a driver drowsiness and attention warning system built for the CMVR (Sixth Amendment) Rules, 2025. Talk to us about retrofitting your fleet.</p></details>
</div></div></section>'''

# ---------------- HOME ----------------
home=f'''
<section class="hero grid-bg"><div class="wrap">
<div class="txt"><span class="eyebrow">Edge AI · Driver monitoring · ADAS</span>
<h1>Edge AI that keeps every driver <span class="blue">alert.</span></h1>
<p class="lead">Sapience Automata™ builds the AI safety platform for every vehicle on the road: driver monitoring and ADAS that run on the vehicle, with alert accuracy above 95%.</p>
<div class="btns"><a class="btn btn-p" href="contact.html">Request a demo</a><a class="btn btn-s" href="products.html">Explore products →</a></div></div>
<div class="pic"><div class="vframe"><video id="heroVid" src="assets/feature.mp4" poster="assets/feature-poster.jpg" autoplay muted loop playsinline aria-label="Blinksmart feature film: the device spots a drowsy driver and beeps"></video><button class="snd" id="sndBtn" type="button" aria-pressed="false">Sound on</button></div></div>
</div></section>
{STATS}
<section class="creds"><div class="wrap"><div><b>Patent 575297</b><span>Granted, Government of India</span></div><div><b>10+ patents</b><span>Filed across the stack</span></div><div><b>CMVR 2025 ready</b><span>DDAWS for buses and trucks</span></div><div><b>TU Delft · NTU Singapore</b><span>Research advisory board</span></div></div></section>
<section><div class="wrap stack" style="gap:48px">
{head('Who it’s for','Built for everyone who <span class="blue">moves people and goods.</span>','',True)}
<div class="row">{tile('logistics.html','truck','Fleets &amp; operators','Live alerts, driver scores and fewer incidents across every route.')}{tile('public-transport.html','users','Drivers &amp; passengers','A co-pilot that never blinks, on every bus, cab and school run.',True)}{tile('oem.html','plug','OEMs &amp; partners','Factory-fit DMS and modular ADAS, with firmware and open APIs.')}</div>
</div></section>
<section class="soft"><div class="wrap stack" style="gap:48px">
<div class="split" style="align-items:flex-end">{head('What we do','One edge device. <span class="blue">Many safety systems.</span>')}<p class="lead">Computer vision, behaviour analytics and edge AI on a single in-vehicle platform. Add cameras and modules as your fleet grows, without changing the box.</p></div>
{FLOW}
</div></section>
<section><div class="wrap stack" style="gap:48px">
{head('Products','From one camera <span class="blue">to full ADAS.</span>')}
<div class="row">
<a class="card link pcard" href="blinksmart.html"><img src="assets/device-cutout.webp" alt="Blinksmart device" loading="lazy" width="900" height="737"><h3>Blinksmart™</h3><p>AI driver drowsiness &amp; distraction warning (DMS + DFMS). Beeps the instant a driver drifts.</p><span class="more">Learn more →</span></a>
<a class="card link pcard" href="copilot-ai.html"><img src="assets/dashboard.webp" alt="CoPilot AI dashboard" loading="lazy" width="1338" height="792"><h3>CoPilot AI™</h3><p>Super-modular ADAS on one edge device, with the fleet dashboard on web and mobile.</p><span class="more">Learn more →</span></a>
<a class="card link pcard" href="bike-adas.html"><div class="ph">{ic('speed')}</div><h3>Bike ADAS</h3><p>Rider safety for two-wheelers, built on the same edge AI. In development.</p><span class="more">Register interest →</span></a>
</div></div></section>
<section class="soft"><div class="wrap stack" style="gap:48px">
<div class="split" style="align-items:flex-end">{head('Outcomes','<span class="blue">2 lakh+</span> alerts generated. <br>Every one, a driver called back.')}<p class="lead">60K+ drowsiness, 80K+ distraction and 60K+ fatigue alerts so far, and 30% better driver performance within 3 months.</p></div>
{OUTCOMES}
</div></section>
<section class="tint"><div class="wrap split">
<div class="stack"><span class="eyebrow">Credibility</span><h2>Patented. <span class="blue">Regulation-ready.</span></h2><p class="lead">Patent No. 575297, granted by the Government of India, for early prediction of risks surrounding a vehicle, with 10+ more in process. Blinksmart™ is built for the DDAWS mandate in the CMVR (Sixth Amendment) Rules, 2025.</p><div class="btns"><a class="btn btn-p" href="research.html">Our research →</a><a class="btn btn-s" href="technology.html#compliance">Compliance</a></div></div>
<div class="tl" style="flex-direction:column"><div><b>1 Oct 2026</b><span>School buses: camera and monitoring fitment</span></div><div><b>1 Oct 2027</b><span>DDAWS on new bus and truck models</span></div><div><b>1 Jan 2028</b><span>DDAWS on existing models</span></div><p style="font-size:14px;color:var(--mute)">Source: G.S.R. 834(E), MoRTH, 11 Nov 2025.</p></div>
</div></section>
<section><div class="wrap stack" style="gap:40px">
<div class="split" style="align-items:flex-end">{head('Clients &amp; partners','50+ businesses keep their drivers <span class="blue">alert with us.</span>')}<p class="lead">Intercity bus operators, state transport, cab platforms, coach builders, telematics partners and OEMs across India.</p></div>
{LOGOS}
<figure class="quote"><blockquote>“Long night drives demand constant focus. The alert system really helps me stay attentive and safer on the road.”</blockquote><figcaption><span class="av">M</span><span><b>Mashood</b><br>Driver, Punchiry Travels</span></figcaption></figure>
</div></section>
{FAQ}
{CTA('Ready to build <span style="color:#fff;text-decoration:underline;text-decoration-thickness:4px;text-underline-offset:8px">safer vehicles?</span>','See Blinksmart™ and CoPilot AI™ live in your vehicle. Our team will walk you through a demo.')}
'''
page('index.html','Sapience Automata Website','Sapience Automata™ builds edge AI driver monitoring and ADAS: Blinksmart™, CoPilot AI™ and Bike ADAS, with alert accuracy above 95%.',home)

# ---------------- BLINKSMART ----------------
bs=f'''
<section class="hero"><div class="wrap">
<div class="txt"><span class="chip">APS 2.0 · AI driver drowsiness &amp; attention warning</span>
<h1>Blinksmart™. The co-pilot that <span class="blue">never blinks.</span></h1>
<p class="lead">A compact AI camera that reads the driver’s eyes and face, beeps the instant they turn drowsy or distracted, and logs every alert to CoPilot AI™.</p>
<div class="btns"><a class="btn btn-p" href="contact.html">Book a demo</a><a class="btn btn-s" href="{DEMO}" target="_blank" rel="noopener">▶ Watch demo</a></div></div>
<div class="pic"><img src="assets/pack.webp" alt="Blinksmart APS 2.0 retail pack" width="900" height="975" fetchpriority="high" style="max-width:460px;margin-inline:auto"></div>
</div></section>
{STATS}
<section><div class="wrap stack" style="gap:40px">
<div class="stack"><span class="eyebrow">Every angle</span><h2>Small device. <span class="blue">Big job.</span></h2></div>
<div class="gallery">
<figure><img src="assets/device-front.webp" alt="Blinksmart front: AI camera and illuminator" loading="lazy" width="1100" height="1100"><figcaption>Front: AI camera on the driver</figcaption></figure>
<figure><img src="assets/device-side.webp" alt="Blinksmart side view with speaker and mount" loading="lazy" width="1000" height="1000"><figcaption>Side: built-in speaker, adjustable mount</figcaption></figure>
<figure><img src="assets/device-back.webp" alt="Blinksmart back view" loading="lazy" width="1000" height="1000"><figcaption>Back: part of the CoPilot AI™ ecosystem</figcaption></figure>
</div></div></section>
<section class="soft"><div class="wrap stack" style="gap:48px">
<div class="stack center"><span class="eyebrow">Features</span><h2>Six ways it keeps drivers <span class="blue">safe.</span></h2></div>
<div class="row">{card('eye','AI camera','Reads the driver’s eyes and face in real time.')}{card('beep','Instant beep','Wakes the driver right in the cab.',True)}{card('sleep','Drowsiness','Eyes closing, head drop and yawning.')}</div>
<div class="row">{card('away','Distraction','Looking away, face not visible, overspeeding.')}{card('chart','Live dashboard','Every alert reaches the owner on CoPilot AI™.')}{card('pin','Live location','Track every vehicle, every trip.')}</div>
</div></section>
<section><div class="wrap split">
<div class="pic"><img src="assets/device-cable.webp" alt="Blinksmart APS 2.0 on its mount with cable" width="1100" height="1100" loading="lazy"></div>
<div class="stack"><span class="eyebrow">At a glance</span><h2>Blinksmart™ <span class="blue">APS 2.0</span></h2>
<table><tr><td>Product type</td><td>AI Driver Drowsiness &amp; Attention Warning System (DDAWS)</td></tr><tr><td>Detects</td><td>Eyes closing, head drop, yawning, looking away, face not visible, overspeeding</td></tr><tr><td>Alerts</td><td>Instant beep in the cab, plus live alert on CoPilot AI™</td></tr><tr><td>Alert accuracy</td><td>Above 95%</td></tr><tr><td>Mounting</td><td>Dashboard or A-pillar</td></tr><tr><td>Fleet software</td><td>CoPilot AI™ web dashboard and Android app</td></tr><tr><td>Made by</td><td>Sapience Automata™, Bengaluru</td></tr></table></div>
</div></section>
{CTA('Put Blinksmart™ in your fleet.','Tell us about your vehicles and routes. We’ll show you Blinksmart™ live.')}
'''
page('blinksmart.html','Blinksmart™ APS 2.0 | AI driver drowsiness warning','Blinksmart™ APS 2.0 reads the driver’s eyes and face and beeps the instant they turn drowsy or distracted. Alert accuracy above 95%.',bs)

# ---------------- COPILOT ----------------
cp=f'''
<section class="hero"><div class="wrap">
<div class="txt"><span class="chip">CoPilot AI™ · Your driving assistant</span>
<h1>Every alert, every vehicle. <span class="blue">One dashboard.</span></h1>
<p class="lead">CoPilot AI™ is the platform behind Blinksmart™. It brings live alerts, location, event snapshots and driver scores together on web and mobile.</p>
<div class="btns"><a class="btn btn-p" href="contact.html">Book a demo</a></div></div>
<div class="pic"><img src="assets/dashboard.webp" alt="CoPilot AI web dashboard and mobile app" width="1338" height="792" fetchpriority="high"></div>
</div></section>
<section class="soft"><div class="wrap stack" style="gap:48px">
<div class="stack center"><span class="eyebrow">Platform</span><h2>Built for fleet owners. <span class="blue">Loved by drivers.</span></h2></div>
<div class="row">{card('chart','Live alerts','Critical alerts from every vehicle the moment they happen.',True)}{card('pin','GPS &amp; OBD','Live location tracking and vehicle data.')}{card('star','Know your driver','Driver ratings and critical-event data for every trip.')}</div>
<div class="row">{card('lock','Prevent unauthorised access','Facial recognition knows who is driving.')}{card('sos','SOS','Help, one press away.')}{card('plug','APIs &amp; integrations','Plug CoPilot AI™ into your telematics and apps.')}</div>
</div></section>
<section><div class="wrap split">
<div class="stack"><span class="eyebrow">Modular ADAS</span><h2>From one camera <span class="blue">to four.</span></h2><p class="lead">CoPilot AI™ grows with your fleet: start with driver monitoring, then add road, blind-spot and rear cameras on the same platform.</p></div>
<ul class="list"><li><i>✓</i><div><b>DDAWS</b><span>Driver drowsiness &amp; attention warning, live today with Blinksmart™</span></div></li><li><i>+</i><div><b>BSIS</b><span>Blind spot information system</span></div></li><li><i>+</i><div><b>MOIS</b><span>Moving off information system</span></div></li><li><i>+</i><div><b>LDWS</b><span>Lane departure warning</span></div></li><li><i>+</i><div><b>AEBS-ready</b><span>Advanced emergency braking support</span></div></li></ul>
</div><div class="wrap" style="margin-top:44px"><div class="specs"><span>Edge hardware</span><b>Octa-core ARM @ 2.2 GHz</b><b>6–12 TOPS NPU</b><b>Up to 4 AI cameras</b><b>4G / 5G · Wi-Fi · BT</b><b>GPS + OBD</b><b>CAN bus · RADAR / LiDAR ready</b></div>
</div></section>
{CTA('See your fleet on CoPilot AI™.','Get a walkthrough of the dashboard with your own vehicles.')}
'''
page('copilot-ai.html','CoPilot AI™ | Fleet safety dashboard and ADAS platform','CoPilot AI™ brings live driver alerts, GPS, event snapshots and driver scores together on web and mobile, and scales from one camera to four.',cp)

# ---------------- ABOUT ----------------
ab=f'''
<section class="hero"><div class="wrap">
<div class="txt"><span class="eyebrow">About Sapience Automata™</span>
<h1>Intelligence for <span class="blue">safer roads.</span></h1>
<p class="lead">We build AI that understands risk before it becomes an accident. Our hardware, firmware and apps are designed and built in-house in Bengaluru, for every vehicle on the road.</p></div>
<div class="pic"><video class="logo-video" src="assets/logo-anim.mp4" poster="assets/logo-poster.jpg" autoplay muted playsinline aria-label="Sapience Automata logo animation"></video></div>
</div></section>
{STATS}
<section><div class="wrap split">
<div class="pic" style="background:var(--blue);border-radius:200px 32px 32px 32px;padding-top:40px;overflow:hidden"><img src="assets/founder.webp" alt="Dr. Satyajit Neogi, Founder and CEO" width="800" height="1023" loading="lazy" style="margin-inline:auto;max-width:440px"></div>
<div class="stack"><span class="eyebrow">Meet our founder</span><h2>Dr. Satyajit Neogi</h2><p style="font-weight:600;color:var(--mute)">Founder &amp; CEO</p><p class="lead">A decade spent making roads safer with computer vision and AI. He has led ADAS and self-driving innovation, and is the inventor behind Sapience Automata’s patented technology.</p><a class="btn btn-s" href="https://www.linkedin.com/in/satyajit-neogi-ph-d-aa1bb1b2/" target="_blank" rel="noopener" style="align-self:flex-start">LinkedIn →</a></div>
</div></section>
<section class="soft" id="team"><div class="wrap stack" style="gap:40px">
<div class="stack"><span class="eyebrow">Team &amp; advisors</span><h2>Built by people who <span class="blue">obsess over safety.</span></h2></div>
<div class="row">
<div class="card"><div class="person"><span class="av">UD</span><div><h3>Unmesh Dabhade</h3><p>Co-Founder &amp; CTO</p></div></div><p>Hardware and firmware architect leading product development and manufacturing.</p></div>
<div class="card"><div class="person"><span class="av">SU</span><div><h3>Srinivasan D Uppili</h3><p>Business Head</p></div></div><p>Former General Manager, 3M, with 25+ years in business leadership and road safety.</p></div></div>
<div class="row">
<div class="card"><div class="person"><span class="av">AC</span><div><h3>Dr. Anupam Chattopadhyay</h3><p>Tech Advisor</p></div></div><p>NTU Singapore. Hardware security, embedded systems and AI.</p></div>
<div class="card"><div class="person"><span class="av">JD</span><div><h3>Dr. Justin Dauwels</h3><p>Tech Advisor</p></div></div><p>TU Delft. AI researcher in autonomous systems.</p></div>
<div class="card"><div class="person"><span class="av">SN</span><div><h3>Stoffer Anko Norden</h3><p>Business Advisor</p></div></div><p>Ex Co-Founder and CEO, Booking.com.</p></div></div>
</div></section>
<section><div class="wrap split">
<div class="stack"><span class="eyebrow">Intellectual property</span><h2>A patent wall around <span class="blue">the full stack.</span></h2><p class="lead">Patent No. 575297 granted by the Government of India. A patent for our AI-based crash prevention ADAS is under examination, with 10+ more in process across hardware, firmware and design.</p></div>
<div class="pic" style="max-width:380px;margin-inline:auto"><img src="assets/patent.webp" alt="Patent certificate No. 575297" width="800" height="1132" loading="lazy" style="border-radius:8px;box-shadow:0 30px 60px rgba(11,30,91,.2)"></div>
</div></section>
{CTA('Let’s make roads safer, together.','Fleets, OEMs, distributors and partners: we’d love to talk.')}
'''
page('about.html','About Sapience Automata™ | AI for safer roads','Sapience Automata™ builds AI that understands road risk before it becomes an accident. Meet our founder, team, advisors and patented technology.',ab)

# ---------------- CONTACT ----------------
ct=f'''
<section class="hero"><div class="wrap">
<div class="txt"><span class="eyebrow">Contact</span><h1>Let’s keep your drivers <span class="blue">awake.</span></h1><p class="lead">Book a live demo, ask about pricing, or explore a partnership. We usually reply within one working day.</p></div>
<div class="pic"><img src="assets/device-cutout.webp" alt="Blinksmart device" width="900" height="737" style="max-width:420px;margin-inline:auto"></div>
</div></section>
<section style="padding-top:0"><div class="wrap row">
{card('star','Email us','<a href="mailto:info@sapienceautomata.com" style="color:var(--blue);font-weight:600">info@sapienceautomata.com</a>',)}
{card('sos','Call us','<a href="tel:+918100675937" style="color:var(--blue);font-weight:600">+91 81006 75937</a>')}
{card('pin','Visit us','No 1012/B, MES Builders’ Association, 1st Floor, 17th D Cross Road, Indiranagar, Bengaluru 560038')}
</div></section>
<section class="soft"><div class="wrap stack" style="gap:40px"><div class="stack center"><span class="eyebrow">How can we help?</span><h2>Pick the team <span class="blue">you need.</span></h2></div>
<div class="row"><div class="card b"><h3>Request a demo or brochure</h3><p>See Blinksmart™ and CoPilot AI™ live, or get the product brochure. Call Swarupa on +91 74786 08393.</p></div><div class="card"><h3>Talk to sales</h3><p>Pricing, fleet rollouts, distributors and subscriptions. info@sapienceautomata.com</p></div><div class="card"><h3>Talk to engineering</h3><p>OEM integration, APIs, specifications and compliance. +91 81006 75937</p></div></div></div></section>
<section><div class="wrap stack center" style="gap:24px">
<h2>Who should reach out?</h2>
<div class="logos"><span>Bus operators</span><span>Logistics fleets</span><span>Cab &amp; staff transport</span><span>School buses</span><span>OEMs &amp; Tier-1s</span><span>Distributors</span></div>
</div></section>
'''
page('contact.html','Contact Sapience Automata™ | Book a Blinksmart™ demo','Book a Blinksmart™ demo or talk to Sapience Automata™ about fleets, OEM programmes and partnerships.',ct)
# ---------------- PRODUCTS ----------------
def hero(eb,h1,lead,pic='',btns=True,cta='Request a demo'):
  b=f'<div class="btns"><a class="btn btn-p" href="contact.html">{cta}</a><a class="btn btn-s" href="{DEMO}" target="_blank" rel="noopener">▶ Watch demo</a></div>' if btns else ''
  p=f'<div class="pic">{pic}</div>' if pic else ''
  return f'<section class="hero{"" if pic else " solo"}"><div class="wrap"><div class="txt"><span class="eyebrow">{eb}</span><h1>{h1}</h1><p class="lead">{lead}</p>{b}</div>{p}</div></section>'
pr=f'''
{hero('Products','One platform. <span class="blue">Every vehicle.</span>','Driver monitoring, modular ADAS and rider safety, built on one edge AI platform and managed from CoPilot AI™.','<img src="assets/pack.webp" alt="Blinksmart APS 2.0 pack" width="900" height="975" fetchpriority="high" style="max-width:420px;margin-inline:auto">')}
<section><div class="wrap stack" style="gap:48px">
{head('What we make','Three products. <span class="blue">One stack.</span>')}
<div class="row">
<a class="card link pcard" href="blinksmart.html"><img src="assets/device-cutout.webp" alt="Blinksmart device" loading="lazy" width="900" height="737"><h3>Blinksmart™</h3><p>DMS + DFMS. Detects drowsiness, fatigue and distraction and beeps in the cab.</p><span class="more">Learn more →</span></a>
<a class="card link pcard" href="copilot-ai.html"><img src="assets/dashboard.webp" alt="CoPilot AI dashboard" loading="lazy" width="1338" height="792"><h3>CoPilot AI™</h3><p>Super-modular ADAS: DDAWS, BSIS, MOIS, LDWS and more, from one camera to four.</p><span class="more">Learn more →</span></a>
<a class="card link pcard" href="bike-adas.html"><div class="ph">{ic('speed')}</div><h3>Bike ADAS</h3><p>Rider safety for two-wheelers. In development.</p><span class="more">Register interest →</span></a>
</div></div></section>
<section class="soft" id="buy"><div class="wrap stack" style="gap:48px">
<div class="split" style="align-items:flex-end">{head('How you buy it','Take the whole stack, <span class="blue">or just the layer you need.</span>')}<p class="lead">Fleets buy a ready system. OEMs and partners can license the layers underneath.</p></div>
<div class="row">{card('plug','Hardware','The edge device and AI cameras, aftermarket or factory-fit.',num='01')}{card('layers','Firmware + APIs','Platform-agnostic firmware and open APIs for your own systems.',num='02')}{card('star','Subscriptions','CoPilot AI™ web and mobile apps, alerts and driver scores.',True,'03')}{card('chart','Data &amp; analytics','Safety analytics and driver-risk data across your fleet.',num='04')}</div>
<div class="row" style="gap:16px"><div class="card"><h3>Aftermarket vehicles</h3><p>Retrofit Blinksmart™ and CoPilot AI™ into the fleet you already run. Dashboard or A-pillar mount.</p><a class="more" href="logistics.html">For fleets →</a></div><div class="card"><h3>OEM programmes</h3><p>Factory-fit DMS and ADAS modules for new bus, truck and special-vehicle models.</p><a class="more" href="oem.html">For OEMs →</a></div></div>
</div></section>
{CTA('Not sure which fits?','Tell us about your vehicles. We’ll recommend the right setup and show it live.')}
'''
page('products.html','Products | Sapience Automata™','Blinksmart™, CoPilot AI™ and Bike ADAS: driver monitoring and modular ADAS on one edge AI platform, as hardware, APIs, subscriptions or data.',pr)

bk=f'''
{hero('Bike ADAS · In development','Rider safety, <span class="blue">for two wheels.</span>','We’re bringing the edge AI behind Blinksmart™ and CoPilot AI™ to two-wheelers. Bike ADAS is in development with early partners.','<div class="ph big">'+ic('speed')+'</div>',True,'Register interest')}
<section><div class="wrap stack" style="gap:48px">
{head('Why two-wheelers','The riders most at risk <span class="blue">have the least protection.</span>','Two-wheeler riders make up a large share of India’s road deaths. They get no airbags, no crumple zone and no second chance.')}
<div class="row">{card('eye','Same AI, smaller form','On-device computer vision adapted for the rider’s view of the road.')}{card('beep','Alerts the rider can feel','Warnings designed to reach a rider in traffic, wind and noise.')}{card('chart','Fleet-ready','Delivery and rental fleets see rider safety on CoPilot AI™.')}</div>
</div></section>
<section class="soft"><div class="wrap stack center" style="gap:20px;max-width:760px"><h2>Building a two-wheeler or running a rider fleet?</h2><p class="lead">We’re looking for OEM, delivery and rental partners for early pilots. Specifications will be shared with partners first.</p><a class="btn btn-p" href="contact.html">Talk to us</a></div></section>
'''
page('bike-adas.html','Bike ADAS | Sapience Automata™','Bike ADAS brings Sapience Automata’s edge AI to two-wheeler rider safety. In development with early partners.',bk)

# ---------------- SOLUTIONS ----------------
SEG=[('public-transport.html','users','Public transport &amp; school','Intercity and city buses, state transport and school fleets.'),('logistics.html','truck','Logistics &amp; fleet','Long-haul trucks, cabs and staff transport.'),('oem.html','plug','OEM integration','Factory-fit DMS and modular ADAS for new models.'),('defense.html','lock','Defense &amp; special vehicles','Convoys, mission and emergency vehicles.')]
so=f'''
{hero('Solutions','Does it fit <span class="blue">your fleet?</span>','Every road is different. Find how Sapience Automata™ works for the vehicles you run or build.')}
<section style="padding-top:0"><div class="wrap stack" style="gap:24px">
<div class="row">{''.join(tile(h,i,t,p,n==1) for n,(h,i,t,p) in enumerate(SEG[:2]))}</div>
<div class="row">{''.join(tile(h,i,t,p) for h,i,t,p in SEG[2:])}</div>
</div></section>
<section class="soft"><div class="wrap stack" style="gap:48px">{head('Outcomes','What every segment <span class="blue">gets.</span>')}{OUTCOMES}</div></section>
{CTA('Tell us about your fleet.','We’ll map the right setup to your vehicles and routes.')}
'''
page('solutions.html','Solutions | Sapience Automata™','Driver monitoring and ADAS for public transport, school buses, logistics fleets, OEMs and defense vehicles.',so)

def seg(fn,eb,h1,lead,pic,pains,how,prods,ctah,ctap,title,desc):
  rows=''.join(f'<li><i>{n+1}</i><div><b>{a}</b><span>{b}</span></div></li>' for n,(a,b) in enumerate(pains))
  body=f'''
{hero(eb,h1,lead,pic)}
{STATS}
<section><div class="wrap split">
<div class="stack"><span class="eyebrow">The challenge</span><h2>{how[0]}</h2><ul class="list">{rows}</ul></div>
<div class="stack"><span class="eyebrow">How we help</span><div class="row" style="gap:16px">{how[1]}</div></div>
</div></section>
<section class="soft"><div class="wrap stack" style="gap:48px">{head('Outcomes','Proof, <span class="blue">not promises.</span>')}{OUTCOMES}</div></section>
<section><div class="wrap stack" style="gap:40px">{head('Products for this segment',prods[0])}<div class="row">{prods[1]}</div></div></section>
{CTA(ctah,ctap)}
'''
  page(fn,title,desc,body)
PB=tile('blinksmart.html','eye','Blinksmart™','Driver drowsiness and distraction warning, with an instant beep in the cab.')
PC=tile('copilot-ai.html','chart','CoPilot AI™','Modular ADAS and the fleet dashboard, on web and mobile.',True)
seg('public-transport.html','Solutions · Public transport &amp; school','Every passenger <span class="blue">deserves an alert driver.</span>','Night routes, long shifts and full buses. Blinksmart™ keeps the driver awake and gives operators live visibility of every vehicle.','<img src="assets/device-angled.webp" alt="Blinksmart device" width="1100" height="1100" style="max-width:440px;margin-inline:auto">',
 [('Night and intercity routes','Microsleep peaks in the small hours, with dozens of lives on board.'),('School bus mandate','Camera and monitoring fitment for school buses from 1 Oct 2026.'),('No eyes on the road','Operators can’t see what happens inside the cab until it’s too late.')],
 ('Long routes. Full buses. <span class="blue">Tired drivers.</span>',card('beep','Instant in-cab alert','The driver is woken the moment eyes close or attention drifts.',True)+card('pin','Live fleet view','Every alert and location reaches the depot on CoPilot AI™.')+card('users','Passenger confidence','A visible safety system on every journey.')),
 ('Ready for <span class="blue">DDAWS and school buses.</span>',PB+PC),'Make every route safer.','From intercity coaches to school runs, we’ll show Blinksmart™ live on your bus.','Public transport &amp; school buses | Sapience Automata™','AI driver drowsiness warning for buses, state transport and school fleets, ready for the CMVR 2025 DDAWS rules.')
seg('logistics.html','Solutions · Logistics &amp; fleet','Long hauls. <span class="blue">Zero blind spots.</span>','Trucks, cabs and staff transport run around the clock. CoPilot AI™ watches every driver and every vehicle, and turns alerts into coaching.','<img src="assets/dashboard.webp" alt="CoPilot AI dashboard" width="1338" height="792">',
 [('Fatigue on long hauls','Drivers push through the night to hit delivery windows.'),('Distraction and phones','A glance away at speed is all it takes.'),('Cost of one crash','Downtime, cargo, claims and lives, from a single moment.')],
 ('Your drivers are tired. <span class="blue">Your data knows it.</span>',card('beep','Real-time alerts','Drowsiness, distraction, overspeed and rash driving, caught live.',True)+card('chart','Driver scores','Rank, reward and coach drivers with event snapshots.')+card('plug','Diagnostics','GPS, OBD and CAN data on the same platform.')),
 ('Built for <span class="blue">fleets that never stop.</span>',PB+PC),'Cut risk across your fleet.','See CoPilot AI™ with your own vehicles and routes.','Logistics &amp; fleet safety | Sapience Automata™','Driver monitoring, live alerts and driver scores for trucks, cabs and staff transport fleets.')
seg('oem.html','Solutions · OEM integration','Factory-fit AI safety, <span class="blue">built in-house.</span>','Hardware, firmware and AI that we design and engineer ourselves, so it integrates cleanly into your vehicle programme.','<img src="assets/device-front.webp" alt="Blinksmart AI camera" width="1100" height="1100" style="max-width:420px;margin-inline:auto">',
 [('DDAWS on new models','Required on new bus and truck models from 1 Oct 2027.'),('Integration effort','Bolt-on systems rarely talk to the vehicle network.'),('One supplier, many systems','DMS today, more ADAS modules tomorrow.')],
 ('Compliance deadlines are <span class="blue">already on the calendar.</span>',card('layers','Modular ADAS','DDAWS, BSIS, MOIS, LDWS and FCW on one edge platform.',True)+card('plug','Vehicle-native','CAN bus ready, OBD and open APIs.')+card('lock','Full control','Our own hardware, firmware and models, tuned for your platform.')),
 ('One platform, <span class="blue">every module.</span>',PC+PB),'Plan your DDAWS programme.','Talk to our engineering team about factory-fit integration.','OEM integration | Sapience Automata™','Factory-fit DMS and modular ADAS for bus, truck and special-vehicle OEMs, CAN bus ready with open APIs.')
seg('defense.html','Solutions · Defense &amp; special vehicles','Mission vehicles need <span class="blue">alert drivers too.</span>','Long convoys, night movement and harsh terrain. Our edge AI runs on the vehicle and raises alerts in the cab without waiting on the cloud.','<img src="assets/device-side.webp" alt="Blinksmart device" width="1000" height="1000" style="max-width:420px;margin-inline:auto">',
 [('Long convoys and night moves','Fatigue builds over hours at the wheel.'),('Patchy connectivity','Safety can’t depend on a network signal.'),('Special vehicles','Emergency and mission vehicles need custom fitment.')],
 ('Fatigue doesn’t <span class="blue">stand down.</span>',card('layers','Edge-first','Detection and alerts run on the device, in real time.',True)+card('plug','Configurable','From one AI camera to four, with OBD and CAN integration.')+card('lock','Built in-house','Our own hardware, firmware and AI stack.')),
 ('Configured for <span class="blue">your vehicles.</span>',PB+PC),'Discuss your requirement.','Our team works with defense and special-vehicle programmes on custom fitment.','Defense &amp; special vehicles | Sapience Automata™','Edge AI driver fatigue monitoring and ADAS for convoys, emergency and special-purpose vehicles.')

# ---------------- TECHNOLOGY ----------------
te=f'''
{hero('Technology','Full stack. <span class="blue">Built in-house.</span>','From the camera module to the AI model to the fleet dashboard, every layer is designed and engineered by our team in Bengaluru.')}
<section style="padding-top:0"><div class="wrap">{FLOW}</div></section>
<section id="platform" class="soft"><div class="wrap stack" style="gap:48px">
{head('Platform &amp; hardware','Edge compute that <span class="blue">lives on the vehicle.</span>')}
<div class="row">{card('layers','Edge + NPU','6–12 TOPS NPU runs vision models on the device, in real time.',True)}{card('eye','Up to 4 AI cameras','Driver, road, blind-spot and rear views on one platform.')}{card('plug','Vehicle interfaces','GPS, OBD and CAN bus ready.')}{card('pin','Connectivity','4G / 5G, Wi-Fi and Bluetooth, with OTA updates and MQTT.')}</div>
<div class="specs"><span>CoPilot AI™ edge platform</span><b>6–12 TOPS NPU</b><b>Up to 4 AI cameras</b><b>4G / 5G · Wi-Fi · BT</b><b>GPS + OBD</b><b>CAN bus ready</b><b>OTA · MQTT</b></div>
</div></section>
<section id="ai"><div class="wrap stack" style="gap:48px">
<div class="split" style="align-items:flex-end">{head('CoPilot AI™ vision &amp; ML','Computer vision that reads <span class="blue">the driver and the road.</span>')}<p class="lead">Eye, face and head-pose tracking across day and night, with and without spectacles. Alert accuracy above 95%.</p></div>
<div class="row">{card('sleep','DDAWS','Driver drowsiness &amp; attention warning.')}{card('away','BSIS','Blind spot information system.')}{card('users','MOIS','Moving off information system.')}</div>
<div class="row">{card('speed','LDWS','Lane departure warning.')}{card('sos','FCW / AEBS-ready','Forward collision warning, ready for advanced emergency braking.')}{card('eye','Sensor fusion','Camera, GPS, OBD and CAN signals combined, with V2V on the roadmap.')}</div>
</div></section>
<section id="compliance" class="tint"><div class="wrap split">
<div class="stack"><span class="eyebrow">Compliance &amp; standards</span><h2>Built for <span class="blue">the DDAWS mandate.</span></h2><p class="lead">The CMVR (Sixth Amendment) Rules, 2025 make Driver Drowsiness &amp; Attention Warning Systems compulsory on buses and trucks. Blinksmart™ is built for it, and retrofits existing fleets.</p></div>
<div class="tl" style="flex-direction:column"><div><b>1 Oct 2026</b><span>School buses: camera and monitoring fitment</span></div><div><b>1 Oct 2027</b><span>DDAWS on new bus and truck models</span></div><div><b>1 Jan 2028</b><span>DDAWS on existing models</span></div><p style="font-size:14px;color:var(--mute)">Source: G.S.R. 834(E), MoRTH, 11 Nov 2025.</p></div>
</div></section>
{CTA('Go deeper with our engineers.','Talk to our engineering team about integration, APIs and specifications.')}
'''
page('technology.html','Technology | Sapience Automata™','Edge AI platform with 6–12 TOPS NPU, up to 4 AI cameras, CAN/OBD, OTA and computer vision for DDAWS, BSIS, MOIS, LDWS and FCW.',te)

# ---------------- CUSTOMERS ----------------
cu=f'''
{hero('Customers','50+ businesses keep their drivers <span class="blue">alert with us.</span>','Intercity bus operators, state transport, cab platforms, coach builders, telematics partners and OEMs across India.')}
{STATS}
<section><div class="wrap stack" style="gap:40px">{head('Clients &amp; partners','Trusted on <span class="blue">India’s busiest routes.</span>')}{LOGOS}</div></section>
<section class="soft"><div class="wrap stack" style="gap:40px">
{head('Track record','<span class="blue">2 lakh+</span> alerts generated.')}
<div class="row"><div class="card"><p class="big">60K+</p><p>drowsiness alerts</p></div><div class="card"><p class="big">80K+</p><p>distraction alerts</p></div><div class="card"><p class="big">60K+</p><p>fatigue alerts</p></div><div class="card b"><p class="big" style="color:#fff">30%</p><p>better driver performance in 3 months</p></div></div>
</div></section>
<section><div class="wrap"><figure class="quote"><blockquote>“Long night drives demand constant focus. The alert system really helps me stay attentive and safer on the road.”</blockquote><figcaption><span class="av">M</span><span><b>Mashood</b><br>Driver, Punchiry Travels</span></figcaption></figure></div></section>
<section class="soft"><div class="wrap stack center" style="gap:16px;max-width:760px"><span class="eyebrow">Case studies</span><h2>Detailed case studies <span class="blue">coming soon.</span></h2><p class="lead">Want to see results from a fleet like yours? Ask us during your demo.</p></div></section>
{CTA('Join them.','See Blinksmart™ live in your vehicle.')}
'''
page('customers.html','Customers | Sapience Automata™','redBus, KSRTC, KKRTC, Volvo Eicher and 50+ businesses use Sapience Automata™ to keep drivers alert.',cu)

# ---------------- RESEARCH ----------------
re_=f'''
{hero('Research &amp; innovation','Seeing road risk <span class="blue">before it happens.</span>','10+ years of ADAS and self-driving R&amp;D, a granted patent and an advisory board from TU Delft and NTU Singapore.','<img src="assets/patent.webp" alt="Patent certificate No. 575297" width="800" height="1132" style="max-width:340px;margin-inline:auto;border-radius:8px;box-shadow:0 30px 60px rgba(11,30,91,.2);transform:rotate(3deg)">',False)}
<section><div class="wrap stack" style="gap:48px">
{head('Patents','A patent wall around <span class="blue">the full stack.</span>')}
<div class="row"><div class="card b"><p class="big" style="color:#fff">575297</p><p>Granted 5 Dec 2025, Government of India. A system and method for early prediction of potential risks surrounding an autonomous vehicle.</p></div><div class="card"><p class="big">Under exam</p><p>Application 202441075380: AI-based crash prevention ADAS.</p></div><div class="card"><p class="big">10+</p><p>Patents in process across hardware, firmware and design.</p></div></div>
</div></section>
<section class="soft"><div class="wrap stack" style="gap:48px">
{head('R&amp;D focus areas','Where we’re <span class="blue">pushing next.</span>')}
<div class="row">{card('eye','Driver state','Drowsiness, fatigue and attention from face and eye signals.')}{card('sos','Predictive risk','Forecasting hazards around the vehicle before they develop.')}{card('layers','Edge efficiency','Running more models on low-power automotive NPUs.')}{card('speed','Two-wheeler safety','Bringing ADAS to riders through Bike ADAS.')}</div>
</div></section>
<section><div class="wrap stack" style="gap:40px">
{head('Advisory board','Guided by <span class="blue">leading researchers.</span>')}
<div class="row"><div class="card"><div class="person"><span class="av">AC</span><div><h3>Dr. Anupam Chattopadhyay</h3><p>NTU Singapore</p></div></div><p>Hardware security, embedded systems and AI.</p></div><div class="card"><div class="person"><span class="av">JD</span><div><h3>Dr. Justin Dauwels</h3><p>TU Delft</p></div></div><p>AI researcher in autonomous systems.</p></div></div>
</div></section>
{CTA('Research partnerships welcome.','Universities, OEMs and labs: let’s work on road safety together.')}
'''
page('research.html','Research &amp; innovation | Sapience Automata™','Patent 575297, 10+ patents in process, and R&D in driver state, predictive risk and edge AI.',re_)

# ---------------- NEWS ----------------
nw=f'''
{hero('News &amp; media','What’s new at <span class="blue">Sapience Automata™.</span>','Announcements, milestones and press. For media enquiries, write to info@sapienceautomata.com.','',False)}
<section style="padding-top:0"><div class="wrap stack" style="gap:16px;max-width:900px">
<a class="card link news" href="research.html"><span class="eyebrow">Dec 2025 · Milestone</span><h3>Patent 575297 granted by the Government of India</h3><p>Our system for early prediction of risks surrounding a vehicle is now patented.</p></a>
<a class="card link news" href="technology.html#compliance"><span class="eyebrow">Nov 2025 · Regulation</span><h3>DDAWS becomes mandatory for buses and trucks</h3><p>What the CMVR (Sixth Amendment) Rules, 2025 mean for fleet owners, and how Blinksmart™ fits.</p></a>
<a class="card link news" href="https://www.linkedin.com/company/sapienceautomata/" target="_blank" rel="noopener"><span class="eyebrow">Follow along</span><h3>More updates on LinkedIn</h3><p>Product launches, deployments and team news.</p></a>
</div></section>
'''
page('news.html','News &amp; media | Sapience Automata™','News, milestones and media from Sapience Automata™.',nw)

# ---------------- CAREERS ----------------
ca=f'''
{hero('Careers','Build AI that <span class="blue">saves lives.</span>','We’re a deeptech team in Bengaluru building hardware, firmware and AI for safer roads. If that sounds like your kind of problem, we’d like to hear from you.','',False)}
<section style="padding-top:0"><div class="wrap stack" style="gap:48px">
<div class="row">{card('eye','Computer vision &amp; ML','Models that run on low-power automotive NPUs.')}{card('plug','Embedded &amp; hardware','Edge devices, firmware and vehicle interfaces.')}{card('chart','Cloud &amp; apps','CoPilot AI™ web and mobile for fleets.')}{card('truck','Field &amp; business','Deployments, fleet success and partnerships.')}</div>
<div class="card b" style="align-items:flex-start"><h3>No open role that fits?</h3><p>Send your CV and a line on what you’d build to info@sapienceautomata.com.</p></div>
</div></section>
'''
page('careers.html','Careers | Sapience Automata™','Join the Sapience Automata™ team in Bengaluru building edge AI for road safety.',ca)

open(os.path.join(D,'README.md'),'w').write('''# Sapience Automata website

Static site (HTML + CSS, no build step) for GitHub Pages.

## Publish on GitHub Pages
1. Create a repo (e.g. `sapience-site`) and upload everything in this folder to the repo root.
2. Repo **Settings → Pages** → Source: *Deploy from a branch* → Branch: `main`, folder `/ (root)` → Save.
3. The site goes live at `https://<your-org>.github.io/<repo>/` in a minute or two.
4. Custom domain: add it under Settings → Pages, then point the domain's DNS to GitHub Pages.

## Edit
- Pages: `index.html`, `products.html`, `blinksmart.html`, `copilot-ai.html`, `bike-adas.html`, `solutions.html`, `public-transport.html`, `logistics.html`, `oem.html`, `defense.html`, `technology.html`, `about.html`, `customers.html`, `research.html`, `news.html`, `careers.html`, `contact.html`
- Styles: `style.css` (brand blue is `--blue`)
- Images and video: `assets/`
- `build.py` regenerates all pages if you prefer editing content in one place.
''')
print('built')
