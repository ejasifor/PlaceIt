############################### LOGIN ##############################

import re
import time
from datetime import datetime, timedelta
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.locator("body").click(timeout=150000)

    ############################ LOG IN ############################
    page.goto("https://placeit.net/login-process?redirect_to=/my_placeit")
    page.locator("#login_user_email").fill("xxxxxxxx")
    page.locator("#login_user_password").fill("xxxxxxxx")
    page.get_by_role("button", name="Log In").click(timeout=150000)

    # Load mockup editor once
    editor_url = "https://placeit.net/c/mockups/stages/mockup-of-a-happy-short-haired-woman-wearing-a-bella-canvas-crop-top-m14385/editor?draftId=59806181&multiFolder_Gradient=96bd8c66ebcf7b9d4ff11f54c7fe6938&colorFolder_Gradient=%2300619b&colorFolder_Shirt%20Color=%23000000&customG_0=t6axh5e71b&draftId=59833981"
    page.goto(editor_url, wait_until="domcontentloaded", timeout=600000)

    page.get_by_role("button", name="Accept Cookies").click(timeout=150000)

    ###############################################################
    # Automated File List
    ###############################################################
    file_numbers = [26, 27, 28, 29]  # <<< update freely

    total = len(file_numbers)
    start_time = time.time()

    for index, num in enumerate(file_numbers, start=1):
        cycle_start = time.time()

        #################### 📊 PROGRESS + ETA DISPLAY ####################
        elapsed = time.time() - start_time
        avg_time = elapsed / index
        remaining = avg_time * (total - index)

        finish_time = datetime.now() + timedelta(seconds=remaining)

        print(f"\n----------------------------------------")
        print(f"   🔄 Processing image {index}/{total} — {num}.png")
        print(f"   ⏱ Elapsed: {elapsed/60:.2f} min")
        print(f"   🧮 ETA: {remaining/60:.2f} min remaining")
        print(f"   📅 Expected Finish: {finish_time.strftime('%I:%M:%S %p')}")
        print("----------------------------------------\n")

        ########################## UPLOAD FILE 📂 #######################
        page.locator("label").filter(has_text="Remove").locator("span").click(timeout=150000)
        page.locator('button:has-text("750x750px")').click(timeout=150000)
        page.get_by_role("button", name="Insert Image 750x750px").set_input_files(f"{num}.png")

        ############################ CROP + DOWNLOAD ####################
        page.get_by_role("button", name="Crop").click(timeout=150000)
        time.sleep(10)

        page.get_by_role("button", name="Download").click(timeout=150000)
        with page.expect_download() as download_info:
            page.get_by_role("link", name="Click here to download").first.click(timeout=150000)
        download = download_info.value

        ############################ CLEAR HISTORY ######################
        page1 = context.new_page()
        page1.goto("chrome://downloads/")
        page1.get_by_role("button", name="Delete from history").click()
        page.goto(editor_url, wait_until="domcontentloaded", timeout=600000)

        ########################🎉 PER-ITEM SUMMARY #####################
        cycle_time = time.time() - cycle_start
        print(f"   ✓ {num}.png complete (took {cycle_time:.1f}s)\n")

    ###############################################################
    print("\n\n🎉 All processing complete!")
    print(f"Total time: {(time.time()-start_time)/60:.2f} min\n")
    input("Press ENTER to close.")
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
