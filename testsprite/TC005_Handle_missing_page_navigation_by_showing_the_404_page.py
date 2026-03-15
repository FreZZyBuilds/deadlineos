import asyncio
import re
from playwright import async_api
from playwright.async_api import expect


async def run_test():
    pw = None
    browser = None
    context = None

    try:
        pw = await async_api.async_playwright().start()
        browser = await pw.chromium.launch(
            headless=True,
            args=["--window-size=1280,720", "--disable-dev-shm-usage", "--ipc=host", "--single-process"],
        )
        context = await browser.new_context()
        context.set_default_timeout(10000)
        page = await context.new_page()

        await page.goto("http://localhost:5173/404.html")

        await expect(page).to_have_title(re.compile("404"))
        await expect(page.locator(".err-code")).to_have_text("404")
        await expect(page.get_by_role("heading", level=1)).to_contain_text("Page not found")

    finally:
        if context:
            await context.close()
        if browser:
            await browser.close()
        if pw:
            await pw.stop()


asyncio.run(run_test())
    
