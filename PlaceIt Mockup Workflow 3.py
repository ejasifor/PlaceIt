import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://placeit.net/login-process?redirect_to=/folders/1283255",
               wait_until="domcontentloaded",
               timeout=600000  # 60 seconds
               )
    page.locator("#login_user_email").fill("ej.aston1@outlook.com")
    # page.locator("#login_user_password").click(timeout=200000)
    page.locator("#login_user_password").press("Tab")
    page.locator("#login_user_password").fill("Coldfusi0n!")
    page.get_by_role("button", name="Log In").click(timeout=200000)
    page.get_by_role("button", name="Accept Cookies").click(timeout=200000)

    # page.get_by_role("link", name="Mockup of a Happy Short-").click(timeout=200000)
    # page.goto("https://placeit.net/c/mockups/stages/mockup-of-a-happy-short-haired-woman-wearing-a-bella-canvas-crop-top-m14385/editor?draftId=59603927",
    page.goto("https://placeit.net/c/mockups/stages/mockup-of-a-happy-short-haired-woman-wearing-a-bella-canvas-crop-top-m14385/editor?customG_0=t5plym0549&draftId=59695564",
               wait_until="domcontentloaded",
               timeout=600000  # 60 seconds
    )
    page.locator('button:has-text("750x750px")').click(timeout=200000)
    page.locator("a").filter(has_text="Recently Uploaded").click(timeout=200000)
    page.locator("#recentlyUploadedModal").get_by_role("img").first.click(timeout=200000)
    # page.get_by_text("× × Crop & Trim Crop Reset").press("ControlOrMeta+-")
    page.get_by_role("button", name="Crop").click(timeout=200000)
    page.get_by_role("button", name="Save to").click(timeout=200000)
    page.get_by_role("button", name="Bella+Canvas Front Product").click(timeout=200000)
    page.get_by_role("button", name="Save", exact=True).click(timeout=200000)
    # page.goto("https://placeit.net/c/mockups/stages/mockup-of-a-happy-short-haired-woman-wearing-a-bella-canvas-crop-top-m14385/editor?draftId=59603927&draftId=59604260&customG_0=t5ph7eb49c"
    #           wait_until="domcontentloaded",
    #           timeout=600000  # 60 seconds
    #           )
    # page.locator("#popover343791 span").first.click(timeout=200000)
    # with page.expect_popup() as page1_info:
    #     page.get_by_role("button", name="Make a copy").click(timeout=200000)
    page.get_by_role("button", name="Make a copy").click(timeout=200000)
    #WORKS TILL HERE
    
    # page.goto("https://placeit.net/login-process?redirect_to=/folders/1283255")
    # page.locator("#login_user_email").click(timeout=200000)
    # page.locator("#login_user_email").fill("ej.aston1@outlook.com")
    # page.locator("#login_user_password").click(timeout=200000)
    # page.locator("#login_user_password").fill("Coldfusi0n!")
    # page.get_by_role("button", name="Log In").click(timeout=200000)
    # page.goto("https://placeit.net/folders/1283255")
    # page.get_by_role("button", name="Accept Cookies").click(timeout=200000)
    # page.get_by_role("link", name="Copy of Mockup of a Happy").click(timeout=200000)

    # # ---------------------
    # context.close()
    # browser.close()


    # with sync_playwright() as playwright:
    # run(playwright)

    # with page.expect_popup() as page1_info:
    #     page.get_by_role("button", name="Make a copy").click(timeout=200000)
    # page1 = page1_info.value
    # page1.get_by_text("Remove", exact=True).click(timeout=200000)
    # page1.locator('button:has-text("750x750px")').click(timeout=200000)
    # page1.locator("a").filter(has_text="Recently Uploaded").click(timeout=200000)
    # page1.locator("#recentlyUploadedModal").get_by_role("img").nth(1).click(timeout=200000)
    
    # page1 = page1_info.value
    # page1.goto("https://placeit.net/c/mockups/stages/mockup-of-a-happy-short-haired-woman-wearing-a-bella-canvas-crop-top-m14385/editor?draftId=59603927&customG_0=t5ph7eb49c&draftId=59694944")
    # page.close()

    # ---------------------
    input("✅ Booyah Achieved. Press Enter to close.")
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
