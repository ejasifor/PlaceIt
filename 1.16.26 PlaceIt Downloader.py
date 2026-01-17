import re
import time
from playwright.sync_api import Playwright, sync_playwright, expect

def pause():
    input("Paused. Press ENTER to continue...")

def process_item(page, context):
    """ Runs one full workflow cycle — unchanged from your script. """

    page.click("ul.galcolumn:nth-of-type(1) a.itemLink")

    # with page.expect_download() as download_info:
# 
            # page.locator(".itemLink").first.click()
# 
    # download = download_info.value
    # print("Segment 1 running")
    # pause()

    # # --- GO BACK TO STOREFRONT 
    # page.goto("https://placeit.net/purchases", wait_until="domcontentloaded", timeout=7000000)
    # time.sleep(7)
    # page.goto("https://placeit.net/purchases", wait_until="domcontentloaded", timeout=7000000)
    # time.sleep(5)
    # page.reload()#timeout=7000000)
    # page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    

    
    # for _ in range(1):  # delete twice exactly as before
        
    #     # second image
    #     page.hover("ul.galcolumn:nth-of-type(2) a.itemLink")

    #     # first image
    #     # page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    #     page.get_by_role("button").nth(3).click(timeout=7000000)
    #     page.get_by_role("button", name="Delete").click()
    #     page.reload(timeout=7000000)


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=6500)
    context = browser.new_context()
    page = context.new_page()

    page.locator("body").click(timeout=7000000)
    page.goto("https://placeit.net/purchases")
    page.locator("#login_user_email").fill("ej.aston1@outlook.com")
    page.locator("#login_user_password").fill("Dr3amc@st!")
    page.get_by_role("button", name="Log In").click(timeout=7000000)
    page.get_by_role("button", name="Accept Cookies").click(timeout=7000000)

    # Go to purchases page
    # page.goto("https://placeit.net/purchases/", wait_until="domcontentloaded", timeout=7000000)
    # page.goto("https://placeit.net/purchases?page=72", wait_until="domcontentloaded", timeout=7000000)
    # page.reload()
    
    # page.reload(timeout=7000000)

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

        # page.goto("https://placeit.net/purchases/", wait_until="domcontentloaded", timeout=7000000)
        page.goto("https://placeit.net/purchases?page=72", wait_until="domcontentloaded", timeout=7000000)
        time.sleep(10)
        page.reload()


    print("\n🎉 All items completed!")
    input("Press ENTER to close browser...")
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
