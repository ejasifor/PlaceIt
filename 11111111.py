import re
import time
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.locator("html").click(timeout=200000)
    page.goto("https://placeit.net/login-process?redirect_to=/my_placeit")
    page.locator("#login_user_email").fill("ej.aston1@outlook.com")
    page.locator("#login_user_email").press("Tab")
    page.locator("#login_user_password").fill("Coldfusi0n!")
    page.get_by_role("button", name="Log In").click(timeout=200000)
    page.get_by_role("button", name="Accept Cookies").click(timeout=200000)

    page.goto("https://placeit.net/c/mockups/stages/mockup-of-a-happy-short-haired-woman-wearing-a-bella-canvas-crop-top-m14385/editor?draftId=59806181&multiFolder_Gradient=96bd8c66ebcf7b9d4ff11f54c7fe6938&colorFolder_Gradient=%2300619b&colorFolder_Shirt%20Color=%23000000&customG_0=t69pmtcdf1&draftId=59833981",
               wait_until="domcontentloaded",
               timeout=600000
            )
    
    page.locator("label").filter(has_text="Remove").locator("span").click(timeout=200000)
    page.locator('button:has-text("750x750px")').click(timeout=200000)
    page.locator("a").filter(has_text="Upload From Your Device").click(timeout=200000)
    page.get_by_role("button", name="Insert Image 750x750px").set_input_files("2.png")


    page.get_by_role("button", name="Crop").click(timeout=200000)
    time.sleep(10)   # wait 10 seconds
    page.get_by_role("button", name="Download").click(timeout=200000)
    
    time.sleep(15)   # wait 10 seconds

    page.goto("https://placeit.net/image-cropper?customG_0=t6a1lma164")
    page.get_by_role("spinbutton").first.click(timeout=200000)
    page.get_by_role("spinbutton").first.fill("1200")
    page.get_by_role("spinbutton").nth(1).click(timeout=200000)
    page.get_by_role("spinbutton").nth(1).fill("1200")
    time.sleep(5)   # wait 5 seconds
    page.get_by_role("button", name="Download").click(timeout=200000)
    with page.expect_download() as download_info:
        page.get_by_role("link", name="Click here to download").first.click(timeout=200000)
    download = download_info.value
    page1 = context.new_page()
    page1.goto("chrome://downloads/")
    page1.get_by_role("button", name="Copy download link").click(timeout=200000)

    # ---------------------
    input("🎉 All Done! Press Enter to close.")
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
