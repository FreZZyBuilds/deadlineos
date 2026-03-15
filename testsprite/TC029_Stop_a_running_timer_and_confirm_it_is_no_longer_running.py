import asyncio
from playwright import async_api
from playwright.async_api import expect


async def login_if_needed(page):
    overlay = page.locator("#login-overlay")
    if not await overlay.is_visible():
        return
    profiles = overlay.locator("#login-profiles")
    await expect(profiles).to_be_visible()
    myself = profiles.get_by_text("Myself")
    if await myself.count():
        await myself.first.click()
    else:
        await profiles.locator("*").first.click()
    pin_section = overlay.locator("#pin-section")
    await expect(pin_section).to_be_visible()
    await pin_section.locator("#pin-in").fill("1234")
    try:
        await expect(overlay).to_be_hidden(timeout=3000)
        return
    except Exception:
        await pin_section.locator("#pin-btn").click()
        await expect(overlay).to_be_hidden()


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

        await page.goto("http://localhost:5173/deadlineos-v3.html")
        await login_if_needed(page)

        start_btn = page.locator("#start-btn")
        stop_btn = page.locator("#stop-btn")
        save_btn = page.locator("#save-btn")

        await expect(stop_btn).to_be_hidden()
        await expect(save_btn).to_be_hidden()

        await start_btn.click()
        await expect(stop_btn).to_be_visible()
        await expect(save_btn).to_be_hidden()

        await stop_btn.click()
        await expect(stop_btn).to_be_hidden()
        await expect(start_btn).to_be_visible()

    finally:
        if context:
            await context.close()
        if browser:
            await browser.close()
        if pw:
            await pw.stop()


asyncio.run(run_test())
    
