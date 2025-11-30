import re
import time
from playwright.sync_api import Playwright, sync_playwright, expect


def process_item(page, context):
    """ Runs one full workflow cycle — unchanged from your script. """

    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    page.get_by_role("button").nth(2).click(timeout=150000)
    page.get_by_role("link", name="Crop / Resize").click(timeout=150000)

    # Capture crop URL dynamically
    crop_url = page.url

    # Input 1200x1200
    page.get_by_role("spinbutton").first.click(timeout=150000)
    page.get_by_role("spinbutton").first.fill("1200")
    page.get_by_role("spinbutton").nth(1).click(timeout=150000)
    page.get_by_role("spinbutton").nth(1).fill("1200")

    # Rebuild new URL dynamically
    updated_url = f"{crop_url}&width=1200&height=1200"
    page.goto(updated_url, wait_until="domcontentloaded", timeout=600000)

    # Download
    page.get_by_role("spinbutton").nth(1).fill("1200")
    page.get_by_role("button", name="Download").click(timeout=150000)
    time.sleep(10)
    with page.expect_download() as download_info:
        page.get_by_role("link", name="Click here to download").first.click(timeout=150000)
    download = download_info.value

    # Open downloads
    page1 = context.new_page()
    page1.goto("chrome://downloads/")

    # Return + Delete twice (unchanged)
    page.goto("https://placeit.net/purchases/", wait_until="domcontentloaded", timeout=600000)
    for _ in range(2):  # delete twice exactly as before
        page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
        page.get_by_role("button").nth(3).click(timeout=150000)
        page.get_by_role("button", name="Delete").click()
        page.reload()


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=3000)
    context = browser.new_context()
    page = context.new_page()

    page.locator("body").click(timeout=150000)
    page.goto("https://placeit.net/login-process?redirect_to=/my_placeit")
    page.locator("#login_user_email").fill("ej.aston1@outlook.com")
    page.locator("#login_user_password").fill("Coldfusi0n!")
    page.get_by_role("button", name="Log In").click(timeout=150000)
    page.get_by_role("button", name="Accept Cookies").click(timeout=150000)

    # Go to purchases page
    page.goto("https://placeit.net/purchases/", wait_until="domcontentloaded", timeout=600000)

    print("\n🚀 Starting automated workflow...\n")

    start_time = time.time()
    count = 0

    while True:
        # Check if one more item exists
        items = page.locator("#container .page-container.downloads a.itemLink .img-wrapper").count()
        if items == 0:
            break  # nothing left → exit loop

        count += 1
        elapsed = time.time() - start_time
        avg = elapsed / count
        eta = avg * (items - 1)

        print(f"📄 Processing item {count}  |  Remaining: {items-1}  |  ETA: {eta/60:.1f} min")

        process_item(page, context)  # Run one full workflow iteration

        page.goto("https://placeit.net/purchases/", wait_until="domcontentloaded", timeout=600000)

    print("\n🎉 All items completed!")
    input("Press ENTER to close browser...")
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
