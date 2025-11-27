import re
import time
from playwright.sync_api import Playwright, sync_playwright, expect



def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.locator("body").click(timeout=150000)
    page.goto("https://placeit.net/login-process?redirect_to=/my_placeit")
    page.locator("#login_user_email").click(timeout=150000)
    page.locator("#login_user_email").fill("ej.aston1@outlook.com")
    page.locator("#login_user_password").click(timeout=150000)
    page.locator("#login_user_password").fill("Coldfusi0n!")
    page.get_by_role("button", name="Log In").click(timeout=150000)
    page.get_by_role("button", name="Accept Cookies").click(timeout=150000)
    page.goto("https://placeit.net/purchases/",
               wait_until="domcontentloaded",
               timeout=600000  # 60 seconds
              )

    # page.locator("label").filter(has_text="Remove").locator("span").click(timeout=150000)
    # page.locator('button:has-text("750x750px")').click(timeout=150000)
    # page.get_by_role("button", name="Insert Image 750x750px").set_input_files("4.png")
    
    # page.get_by_role("button", name="Crop").click(timeout=150000)
    # time.sleep(10)   # wait 10 seconds
    # page.get_by_role("button", name="Download").click(timeout=150000)
    # with page.expect_download() as download_info:
    #     page.get_by_role("link", name="Click here to download").first.click(timeout=150000)
    # download = download_info.value
    # time.sleep(10)   # wait 10 seconds
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    page.get_by_role("button").nth(2).click(timeout=150000)
    page.get_by_role("link", name="Crop / Resize").click(timeout=150000)
    page.goto("https://placeit.net/image-cropper?customG_0=t6bl2u9d99")
    page.get_by_role("spinbutton").first.click(timeout=150000)
    page.get_by_role("spinbutton").first.fill("1200")
    page.get_by_role("spinbutton").nth(1).click(timeout=150000)
    page.get_by_role("spinbutton").nth(1).fill("1200")
    time.sleep(3)   # wait 10 seconds
    page.get_by_role("button", name="Download").click(timeout=150000)
    with page.expect_download() as download_info:
        page.get_by_role("link", name="Click here to download").first.click(timeout=150000)
    download = download_info.value
    page1 = context.new_page()
    page1.goto("chrome://downloads/")
    page.locator('button:has-text("Copy download link")').click(timeout=150000)

    # ---------------------
    input("🎉 All Done! Press Enter to close.")
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
