import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://placeit.net/login-process?redirect_to=/folders/1283255",
               wait_until="domcontentloaded",
               timeout=6000000  # 600 seconds
        )
    page.locator("#login_user_email").fill("ej.aston1@outlook.com")
    # page.locator("#login_user_password").click()
    page.locator("#login_user_password").press("Tab")
    page.locator("#login_user_password").fill("Coldfusi0n!")
    page.get_by_role("button", name="Log In").click()
    page.get_by_role("button", name="Accept Cookies").click()

    # page.get_by_role("link", name="Mockup of a Happy Short-").click()
    page.goto("https://placeit.net/c/mockups/stages/mockup-of-a-happy-short-haired-woman-wearing-a-bella-canvas-crop-top-m14385/editor?draftId=59603927",
               wait_until="domcontentloaded",
               timeout=600000  # 60 seconds
        )
  # page.get_by_text("Remove", exact=True).click(timeout=500000)
  # Locate and click the dropdown button labeled "750x750px" precisely
    # Use a CSS selector to find the button that CONTAINS the text '750x750px'.
    # This bypasses issues with the button's accessible name.
    page.locator('button:has-text("750x750px")').click(timeout=200000)

    # Wait for the dropdown option to appear (it's an 'a' tag) and click it.
    # The original locator for this step is correct.
    page.locator("a").filter(has_text="Recently Uploaded").click(timeout=200000) 

  #   button = page.locator("button:has-text('750x750px')")
  #   button.wait_for(state="visible", timeout=60000)
  #   button.wait_for(state="stable", timeout=60000)
  #   button.scroll_into_view_if_needed()
  #   button.click()

  #   # Wait for the dropdown option and click it
  #   option = page.locator("a.dropdown-item", has_text="Recently Uploaded")
  #   option.wait_for(state="visible", timeout=30000)
  #   option.click()

  # # page.get_by_role("button", name="750x750px", exact=True).click()
  #   page.locator("a").filter(has_text="Recently Uploaded").click()
    page. locator("#recentlyUploadedModal").get_by_role("img").nth(1).click(timeout=600000)
    # page.locator("#recentlyUploadedModal").get_by_role("img").first.click()
    page.get_by_role("button", name="Crop").click(timeout=600000)
    # page.goto("https://placeit.net/c/mockups/stages/mockup-of-a-happy-short-haired-woman-wearing-a-bella-canvas-crop-top-m14385/editor?draftId=59603927&customG_0=t5euhr0125")
    with page.expect_popup() as page1_info:
      page.locator('button:has-text("Make a copy")').click(timeout=200000)
    page1 = page1_info.value
    page.close()
    page.goto("https://placeit.net/c/mockups/stages/mockup-of-a-happy-short-haired-woman-wearing-a-bella-canvas-crop-top-m14385/editor?draftId=59603927",
            wait_until="domcontentloaded",
            timeout=600000  # 60 seconds
    )
    
    page1.get_by_text("Replace").click(timeout=200000)
    # page1.locator('button:has-text("750x750px")').click(timeout=200000)
    page1.locator("#recentlyUploadedModal").get_by_role("img").nth(2).click(timeout=600000)
  
    page1.locator(".recommended-templates-elements").click()
    page1.get_by_text("Replace").click()
    page1.locator("#container div").filter(has_text="Other templates you might like! Back View Mockup of a Short-Haired Woman").nth(3).click()
    page1.get_by_role("button", name="750x750px", exact=True).click()
    page1.locator("a").filter(has_text="Recently Uploaded").click()
    page1.locator("#recentlyUploadedModal").get_by_role("img").nth(2).click()
    page1.get_by_role("button", name="Crop").click()
    page1.get_by_role("button", name="Save to").click()
    page1.goto("https://placeit.net/c/mockups/stages/mockup-of-a-happy-short-haired-woman-wearing-a-bella-canvas-crop-top-m14385/editor?draftId=59603927&draftId=59604260&customG_0=t5ew3g3aa0")
    # page1.get_by_role("button", name="New Folder").click()
    # page1.get_by_role("textbox", name="Folder Name").click()
    # page1.get_by_role("textbox", name="Folder Name").fill("Bella+Canvas 6681 Front All")
    # page1.get_by_role("button", name="Create Folder").click()
    # page1.get_by_role("button", name="Save", exact=True).click()
    # page1.goto("https://placeit.net/c/mockups/stages/mockup-of-a-happy-short-haired-woman-wearing-a-bella-canvas-crop-top-m14385/editor?customG_0=t5ew3g3aa0&draftId=59604608")
    # page1.get_by_role("link", name="Bella Canvas Sleeveless Tee").click()
    # page1.goto("https://placeit.net/c/mockups/stages/mockup-of-a-happy-short-haired-woman-wearing-a-bella-canvas-crop-top-m14385/editor?draftId=59603927&draftId=59604260&customG_0=t5ew3g3aa0")

    # ---------------------
    input("✅ Booyah Achieved. Press Enter to close.")
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
