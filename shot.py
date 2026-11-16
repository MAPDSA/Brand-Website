import asyncio,sys
from playwright.async_api import async_playwright
P='file:///tmp/claude-0/-home-claude/36ed6ee1-ac85-5095-bab7-bfdc6df66195/scratchpad/site/blinksmart-home.html'
async def main():
  async with async_playwright() as p:
    b=await p.chromium.launch()
    errs=[]
    for w,h,n in [(1366,900,'d'),(390,844,'m'),(768,1024,'t'),(360,740,'s')]:
      pg=await b.new_page(viewport={'width':w,'height':h})
      pg.on('pageerror',lambda e:errs.append(str(e)))
      await pg.goto(P); await pg.wait_for_timeout(1200)
      sw=await pg.evaluate('document.documentElement.scrollWidth')
      bad=await pg.evaluate('''[...document.querySelectorAll("body *")].filter(e=>{const r=e.getBoundingClientRect();return r.width>0&&r.right>innerWidth+1&&!e.closest(".screen,.hero svg")}).slice(0,8).map(e=>e.className+"|"+e.tagName)''')
      print(n,w,'scrollW',sw,bad)
      await pg.screenshot(path=f'site/{n}.png',full_page=True)
      if n=='m':
        # walk the flow
        await pg.fill('#fPin','560102'); await pg.click('#nextBtn')
        await pg.click('[data-group=car] .chip'); await pg.click('#nextBtn')
        await pg.click('[data-group=slot] .chip'); await pg.click('#nextBtn')
        await pg.click('#nextBtn'); print('err',await pg.text_content('#fErr'))
        await pg.fill('#fName','Test'); await pg.fill('#fPhone','9876543210'); await pg.check('#fOk'); await pg.click('#nextBtn')
        print(await pg.get_attribute('#waBtn','href'))
        el=await pg.query_selector('#book'); await el.screenshot(path='site/m-book.png')
    print('errors',errs)
    await b.close()
asyncio.run(main())
