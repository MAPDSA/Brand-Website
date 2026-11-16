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
if(bad.length){msg.textContent='Please fill in the highlighted fields.';msg.className='fnote bad';bad[0].focus();return}
var ep=f.getAttribute('data-endpoint'),btn=f.querySelector('button');
if(!ep){msg.textContent='Online form isn’t connected yet. Please email info@sapienceautomata.com or call +91 81006 75937.';msg.className='fnote bad';return}
btn.disabled=true;btn.textContent='Sending…';
var data={};new FormData(f).forEach(function(v,k){data[k]=v});fetch(ep,{method:'POST',headers:{'Content-Type':'application/json','Accept':'application/json'},body:JSON.stringify(data)}).then(function(r){if(!r.ok)throw 0;f.reset();msg.textContent='Thanks! Our sales team will get back to you within one working day.';msg.className='fnote ok'}).catch(function(){msg.textContent='Couldn’t send. Please email info@sapienceautomata.com or call +91 81006 75937.';msg.className='fnote bad'}).then(function(){btn.disabled=false;btn.textContent='Contact sales →'})});})();
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
  m.innerHTML='<div class="vm-back" data-close></div><div class="vm-box"><button class="vm-x" type="button" data-close aria-label="Close video">✕</button><div class="vm-body"></div><p class="vm-foot"><a href="https://youtu.be/'+ID+'" target="_blank" rel="noopener">Watch on YouTube ↗</a></p></div>';
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
 [].forEach.call(m.querySelectorAll('li.dd'),function(li){var a=li.querySelector(':scope>a');var t=document.createElement('button');t.type='button';t.className='ddt';t.setAttribute('aria-expanded','false');t.setAttribute('aria-label','Show '+a.textContent.trim()+' pages');t.innerHTML='<svg viewBox="0 0 12 12" aria-hidden="true"><path d="M3 4.5l3 3 3-3"/></svg>';a.after(t);
  if(a.classList.contains('on')){li.classList.add('open');t.setAttribute('aria-expanded','true')}
  t.addEventListener('click',function(){var o=li.classList.toggle('open');t.setAttribute('aria-expanded',String(o))})});
 function sync(){var o=m.classList.contains('open')&&mq.matches;document.documentElement.classList.toggle('menu-open',o);b.textContent=o?'Close':'Menu'}
 b.addEventListener('click',function(){setTimeout(sync,0)});
 m.addEventListener('click',function(e){var a=e.target.closest('a');if(a&&mq.matches){m.classList.remove('open');b.setAttribute('aria-expanded','false');sync()}});
 document.addEventListener('keydown',function(e){if(e.key==='Escape'&&m.classList.contains('open')){m.classList.remove('open');b.setAttribute('aria-expanded','false');sync();b.focus()}});
 mq.addEventListener&&mq.addEventListener('change',sync);
})();
