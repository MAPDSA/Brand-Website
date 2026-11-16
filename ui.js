var HI=document.documentElement.lang==='hi';
(function(){
var d=document,R=matchMedia('(prefers-reduced-motion: reduce)').matches;
d.documentElement.classList.add('js');
var nav=d.querySelector('.nav');function sc(){nav&&nav.classList.toggle('scrolled',scrollY>8)}addEventListener('scroll',sc,{passive:true});sc();
var sel='main h2,main .lead,main .card,main .statcard,main .flow>*,main .clients,main .tl>div,main .bars>div,main .tags,main .quote,main details,main .specs,main .pic,main .gallery figure,main table';
var els=[].slice.call(d.querySelectorAll(sel));
if(!R&&'IntersectionObserver' in window){
 els.forEach(function(e){e.classList.add('rv')});
 var io=new IntersectionObserver(function(en){en.forEach(function(x){if(x.isIntersecting){var e=x.target,sib=e.parentElement?[].slice.call(e.parentElement.children).filter(function(c){return c.classList.contains('rv')}):[];e.style.transitionDelay=Math.min(sib.indexOf(e),6)*70+'ms';e.classList.add('in');io.unobserve(e)}})},{rootMargin:'0px 0px -8% 0px'});
 els.forEach(function(e){io.observe(e)});
}
function count(el){var t=el.textContent.trim(),m=t.match(/^([^\d]*)([\d][\d,]*\.?\d*)(.*)$/);if(!m||!/[+%]/.test(m[3]))return;var pre=m[1],num=parseFloat(m[2].replace(/,/g,'')),suf=m[3],dec=(m[2].split('.')[1]||'').length,com=m[2].indexOf(',')>-1,t0=null;
 function f(n){var s=n.toFixed(dec);if(com)s=Number(s).toLocaleString('en-IN');return pre+s+suf}
 function step(ts){if(!t0)t0=ts;var p=Math.min((ts-t0)/1400,1),e=1-Math.pow(1-p,3);el.textContent=f(num*e);if(p<1)requestAnimationFrame(step);else el.textContent=t}
 el.textContent=f(0);requestAnimationFrame(step)}
if(!R&&'IntersectionObserver' in window){var co=new IntersectionObserver(function(en){en.forEach(function(x){if(x.isIntersecting){count(x.target);co.unobserve(x.target)}})},{threshold:.6});
 [].forEach.call(d.querySelectorAll('.statcard b,.card .big'),function(e){co.observe(e)})}
[].forEach.call(d.querySelectorAll('.card'),function(c){c.addEventListener('pointermove',function(ev){var r=c.getBoundingClientRect();c.style.setProperty('--mx',(ev.clientX-r.left)+'px');c.style.setProperty('--my',(ev.clientY-r.top)+'px')})});
})();
(function(){var f=document.getElementById('leadForm');if(!f)return;var msg=document.getElementById('formMsg');
f.addEventListener('submit',function(e){e.preventDefault();var bad=[].filter.call(f.querySelectorAll('[required]'),function(x){return !x.value.trim()||(x.type=='email'&&!/^\S+@\S+\.\S+$/.test(x.value))});
[].forEach.call(f.querySelectorAll('[required]'),function(x){x.classList.toggle('err',bad.indexOf(x)>-1)});
if(bad.length){msg.textContent=(HI?'हाइलाइट किए गए फ़ील्ड भरें।':'Please fill in the highlighted fields.');msg.className='fnote bad';bad[0].focus();return}
var ep=f.getAttribute('data-endpoint'),btn=f.querySelector('button');
if(!ep){msg.textContent='Online form isn’t connected yet. Please email info@sapienceautomata.com or call +91 81006 75937.';msg.className='fnote bad';return}
btn.disabled=true;btn.textContent=(HI?'भेज रहे हैं…':'Sending…');
var data={};new FormData(f).forEach(function(v,k){data[k]=v});fetch(ep,{method:'POST',headers:{'Content-Type':'application/json','Accept':'application/json'},body:JSON.stringify(data)}).then(function(r){if(!r.ok)throw 0;f.reset();msg.textContent=f.dataset.ok||(HI?'धन्यवाद! हमारी सेल्स टीम एक कामकाजी दिन में आपसे संपर्क करेगी।':'Thanks! Our sales team will get back to you within one working day.');msg.className='fnote ok'}).catch(function(){msg.textContent=(HI?'भेजा नहीं जा सका। कृपया info@sapienceautomata.com पर ईमेल करें या +91 81006 75937 पर कॉल करें।':'Couldn’t send. Please email info@sapienceautomata.com or call +91 81006 75937.');msg.className='fnote bad'}).then(function(){btn.disabled=false;btn.textContent=f.dataset.btn||(HI?'सेल्स से बात करें →':'Contact sales →')})});})();
/* page transitions + start at top */
(function(){
 if('scrollRestoration' in history)history.scrollRestoration='manual';
 function top(){if(!location.hash)window.scrollTo({top:0,left:0,behavior:'instant'})}
 top();addEventListener('load',top);addEventListener('pageshow',function(e){document.body.classList.remove('leaving');if(e.persisted)top()});
 document.addEventListener('click',function(e){var a=e.target.closest&&e.target.closest('a[href]');if(!a||e.defaultPrevented||e.metaKey||e.ctrlKey||e.shiftKey||a.target==='_blank')return;
  var h=a.getAttribute('href');if(!h||/^(https?:|mailto:|tel:|#)/.test(h))return;
  var u=new URL(h,location.href);if(u.pathname===location.pathname){if(!u.hash){e.preventDefault();window.scrollTo({top:0,behavior:'smooth'})}return}
  e.preventDefault();document.body.classList.add('leaving');setTimeout(function(){location.href=u.href},180)});
})();
/* demo video modal */
(function(){
 var ID='9kMJqMemYnM',m,body,last;
 var preview=/claudeusercontent|claude\.ai/.test(location.hostname)||location.protocol==='file:';
 function build(){m=document.createElement('div');m.className='vmodal';m.setAttribute('role','dialog');m.setAttribute('aria-modal','true');m.setAttribute('aria-label','Blinksmart demo video');
  m.innerHTML='<div class="vm-back" data-close></div><div class="vm-box"><button class="vm-x" type="button" data-close aria-label="Close video">✕</button><div class="vm-body"></div><p class="vm-foot"><a href="https://youtu.be/'+ID+'" target="_blank" rel="noopener">'+(HI?'YouTube पर देखें ↗':'Watch on YouTube ↗')+'</a></p></div>';
  document.body.appendChild(m);body=m.querySelector('.vm-body');
  m.addEventListener('click',function(e){if(e.target.closest('[data-close]'))close()});
  document.addEventListener('keydown',function(e){if(e.key==='Escape'&&m.classList.contains('open'))close()})}
 function open(){if(!m)build();last=document.activeElement;
  body.innerHTML=preview?'<video src="feature.mp4" controls autoplay playsinline></video>':'<iframe src="https://www.youtube-nocookie.com/embed/'+ID+'?autoplay=1&rel=0&modestbranding=1" title="Blinksmart demo" allow="autoplay; encrypted-media; picture-in-picture; fullscreen" allowfullscreen></iframe>';
  m.classList.add('open');document.documentElement.classList.add('vm-lock');m.querySelector('.vm-x').focus();
  var hv=document.getElementById('heroVid');if(hv)hv.pause()}
 function close(){m.classList.remove('open');document.documentElement.classList.remove('vm-lock');body.innerHTML='';var hv=document.getElementById('heroVid');if(hv)hv.play().catch(function(){});if(last)last.focus()}
 document.addEventListener('click',function(e){var a=e.target.closest&&e.target.closest('a[href*="youtu.be/'+ID+'"],a[href*="youtube.com/watch?v='+ID+'"]');if(!a||a.closest('.vmodal'))return;e.preventDefault();open()});
})();
/* mobile menu: accordion, scroll lock, close label */
(function(){var b=document.getElementById('menuBtn'),m=document.getElementById('menu');if(!b||!m)return;
 var mq=matchMedia('(max-width:860px)');
 [].forEach.call(m.querySelectorAll('li.dd'),function(li){var a=li.querySelector(':scope>a');var t=document.createElement('button');t.type='button';t.className='ddt';t.setAttribute('aria-expanded','false');t.setAttribute('aria-label',HI?a.textContent.trim()+' के पेज दिखाएँ':'Show '+a.textContent.trim()+' pages');t.innerHTML='<svg viewBox="0 0 12 12" aria-hidden="true"><path d="M3 4.5l3 3 3-3"/></svg>';a.after(t);
  if(a.classList.contains('on')){li.classList.add('open');t.setAttribute('aria-expanded','true')}
  t.addEventListener('click',function(){var o=li.classList.toggle('open');t.setAttribute('aria-expanded',String(o))})});
 function place(){var n=b.closest('header');if(n)m.style.setProperty('top',Math.max(0,Math.round(n.getBoundingClientRect().bottom))+'px','important')}
 function sync(){var o=m.classList.contains('open')&&mq.matches;if(o)place();else m.style.removeProperty('top');document.documentElement.classList.toggle('menu-open',o);b.textContent=o?(HI?'बंद करें':'Close'):(HI?'मेन्यू':'Menu')}
 addEventListener('resize',function(){if(m.classList.contains('open'))place()});
 b.addEventListener('click',function(){setTimeout(sync,0)});
 m.addEventListener('click',function(e){var a=e.target.closest('a');if(a&&mq.matches){m.classList.remove('open');b.setAttribute('aria-expanded','false');sync()}});
 document.addEventListener('keydown',function(e){if(e.key==='Escape'&&m.classList.contains('open')){m.classList.remove('open');b.setAttribute('aria-expanded','false');sync();b.focus()}});
 mq.addEventListener&&mq.addEventListener('change',sync);
})();
(function(){var f=document.getElementById('leadForm');if(!f||!/[?&]report=/.test(location.search))return;
var s=f.querySelector('select[name=interest]');if(s){var o=document.createElement('option');o.textContent='Free Sapience Safety Report 2026';s.insertBefore(o,s.options[1]||null);s.value=o.textContent;}
var m=f.querySelector('textarea[name=message]');if(m&&!m.value)m.value='Please send me the free Sapience Safety Report 2026.';
var h=document.createElement('p');h.className='fnote ok';h.style.marginBottom='8px';h.textContent='Fill in your details and we’ll email you the free Sapience Safety Report 2026.';f.insertBefore(h,f.firstChild);
var b=f.querySelector('button');if(b)b.textContent='Get the report →';
f.dataset.ok='Thanks! The Sapience Safety Report 2026 is on its way to your inbox.';f.dataset.btn='Get the report →';})();
/* report download: collect email first */
(function(){
 var EP='https://submit-form.com/dsu9fGOOg',PDF='Sapience-Safety-Report-2026.pdf',m;
 function dl(){var a=document.createElement('a');a.href=PDF;a.download='Sapience-Safety-Report-2026.pdf';document.body.appendChild(a);a.click();a.remove()}
 function build(){m=document.createElement('div');m.className='vmodal rmodal';m.setAttribute('role','dialog');m.setAttribute('aria-modal','true');m.setAttribute('aria-labelledby','rmT');
  m.innerHTML='<div class="vm-back" data-close></div><div class="rm-box"><button class="vm-x" type="button" data-close aria-label="Close">✕</button>'+
  (HI?'<span class="eyebrow">मुफ़्त रिपोर्ट · PDF</span><h3 id="rmT">Sapience Safety Report 2026</h3><p class="rm-sub">DDAWS नियम: फ़्लीट, स्कूल और OEM के लिए इसका मतलब, और डेडलाइन से पहले क्या करें।</p>':'<span class="eyebrow">Free report · PDF</span><h3 id="rmT">Sapience Safety Report 2026</h3><p class="rm-sub">The DDAWS mandate: what it means for fleets, schools and OEMs, and what to do before the deadlines.</p>')+
  '<form class="form rm-form" novalidate><label>'+(HI?'ऑफ़िस ईमेल':'Work email')+'<input type="email" name="email" required autocomplete="email" placeholder="you@company.com"></label>'+
  '<label><span>'+(HI?'नाम <span class="rm-opt">(वैकल्पिक)</span>':'Name <span class="rm-opt">(optional)</span>')+'</span><input name="name" autocomplete="name"></label>'+
  '<button class="btn btn-p" type="submit">'+(HI?'रिपोर्ट डाउनलोड करें ↓':'Download the report ↓')+'</button><p class="rm-msg" role="status"></p>'+
  '<p class="rm-fine">'+(HI?'हम आपको कभी-कभी सड़क सुरक्षा अपडेट भी भेजेंगे। कोई स्पैम नहीं।':'We’ll also send you occasional road-safety updates. No spam.')+'</p></form></div>';
  document.body.appendChild(m);
  m.addEventListener('click',function(e){if(e.target.closest('[data-close]'))close()});
  document.addEventListener('keydown',function(e){if(e.key==='Escape'&&m.classList.contains('open'))close()});
  var f=m.querySelector('form'),msg=m.querySelector('.rm-msg'),btn=f.querySelector('button');
  f.addEventListener('submit',function(e){e.preventDefault();var em=f.email.value.trim();
   if(!/^\S+@\S+\.\S+$/.test(em)){f.email.classList.add('err');msg.textContent=(HI?'कृपया सही ईमेल डालें।':'Please enter a valid email.');msg.className='rm-msg bad';f.email.focus();return}
   f.email.classList.remove('err');btn.disabled=true;btn.textContent=(HI?'तैयार हो रहा है…':'Preparing…');
   fetch(EP,{method:'POST',headers:{'Content-Type':'application/json','Accept':'application/json'},body:JSON.stringify({email:em,name:f.name.value.trim(),interest:'Safety Report 2026 download',page:location.pathname})})
   .catch(function(){}).then(function(){try{localStorage.setItem('sa-report','1')}catch(x){}
     msg.innerHTML=(HI?'धन्यवाद! डाउनलोड शुरू हो गया है। ':'Thanks! Your download has started. ')+'<a href="'+PDF+'" download target="_blank" rel="noopener">'+(HI?'शुरू नहीं हुआ? यहाँ क्लिक करें।':'Didn’t start? Click here.')+'</a>';msg.className='rm-msg ok';btn.textContent=(HI?'डाउनलोड हो गया ✓':'Downloaded ✓');dl()})});
 }
 function open(){if(!m)build();m.classList.add('open');document.documentElement.classList.add('vm-lock');setTimeout(function(){m.querySelector('input').focus()},50)}
 function close(){m.classList.remove('open');document.documentElement.classList.remove('vm-lock')}
 document.addEventListener('click',function(e){var a=e.target.closest&&e.target.closest('a[href$="Sapience-Safety-Report-2026.pdf"]');if(!a||a.closest('.rmodal'))return;
  var seen=false;try{seen=!!localStorage.getItem('sa-report')}catch(x){}if(seen)return;e.preventDefault();open()});
})();
