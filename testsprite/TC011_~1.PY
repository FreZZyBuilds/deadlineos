import asyncio
import re
import time
from datetime import datetime, timedelta
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

        title = f"E2E Task - Full lifecycle {int(time.time())}"
        deadline = (datetime.now() + timedelta(days=1)).replace(second=0, microsecond=0)
        deadline_str = deadline.strftime("%Y-%m-%dT%H:%M")

        await page.locator("#task-input").fill(title)
        await page.locator("#dl-in").fill(deadline_str)
        await page.locator(".urg-row .ubtn[data-u='3']").click()
        await page.locator("#add-btn").click()

        card = page.locator("#task-list .tc", has_text=title).first
        await expect(card).to_be_visible()

        prio = card.locator("select.prio-select")
        await prio.select_option("1")
        await expect(prio).to_have_value("1")

        chk = card.locator("input.tchk")
        await chk.check()
        await expect(chk).to_be_checked()
        await expect(card).to_have_class(re.compile(r".*\\bdone\\b.*"))

        await card.locator("button.tbtn.del").click()
        await expect(page.locator("#confirm-overlay")).to_be_visible()
        await page.locator("#confirm-ok-btn").click()
        await expect(page.locator("#task-list")).not_to_contain_text(title)

    finally:
        if context:
            await context.close()
        if browser:
            await browser.close()
        if pw:
            await pw.stop()


asyncio.run(run_test())
    
