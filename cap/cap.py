import asyncio,sys
from playwright.async_api import async_playwright
S={'jarrettwroten':'https://jarrettwroten.com/','rainbow':'https://rainbow.jarrettwroten.com/','stirling':'https://stirling.jarrettwroten.com/','wrapstar':'https://wrapstar.jarrettwroten.com/','purpleflare':'https://purpleflare.jarrettwroten.com/','starbase':'https://starbase.jarrettwroten.com/','rana':'https://rana.jarrettwroten.com/','prorok':'https://prorok.jarrettwroten.com/'}
async def one(b,k,u):
    c=await b.new_context(viewport={'width':360,'height':640},device_scale_factor=3,is_mobile=True,has_touch=True)
    p=await c.new_page(); r=await p.goto(u,wait_until='load',timeout=60000)
    print(k,u,r.status,flush=True)
    for t in (3,5,7,9):
        await p.wait_for_timeout(2000 if t>3 else 3000)
        await p.screenshot(path=f'{k}_{t}.png')
    await c.close()
async def main():
    async with async_playwright() as pw:
        b=await pw.chromium.launch(args=['--autoplay-policy=no-user-gesture-required'])
        await asyncio.gather(*[one(b,k,u) for k,u in S.items()])
asyncio.run(main())
