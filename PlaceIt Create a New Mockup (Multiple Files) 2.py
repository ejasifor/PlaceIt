############################### LOGIN ##############################

import re
import time
from datetime import datetime, timedelta
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.locator("body").click(timeout=600000)

    ############################ LOG IN ############################
    page.goto("https://placeit.net/login-process?redirect_to=/my_placeit",
               wait_until="domcontentloaded",
               timeout=6000000  # 60 seconds  
               )
    # page.goto("https://placeit.net/login-process?redirect_to=/folders/1283255")
    page.locator("#login_user_email").click(timeout=600000)
    page.locator("#login_user_email").fill("ej.aston1@outlook.com")
    page.locator("#login_user_password").click(timeout=600000)
    page.locator("#login_user_password").fill("Coldfusi0n!")
    page.get_by_role("button", name="Log In").click(timeout=600000)
    
    ################################################################

    page.get_by_role("link", name="Bella Canvas Crop Top Mockup").nth(1).click(timeout=600000)
    page.goto("https://placeit.net/c/mockups/stages/bella-canvas-crop-top-mockup-of-a-woman-posing-in-a-studio-with-a-sublimated-bucket-hat-m40822/editor?draftId=59603215&customG_0=t6mkl22fa7&colorFolder_Crop%20Top%20Color=%23000000&draftId=59603215",
               wait_until="domcontentloaded",
               timeout=6000000  # 60 seconds  
               )
    # page.get_by_role("link", name="Bella Canvas Crop Top Mockup of a Woman Posing in a Studio With a Sublimated").click(timeout=600000)
    # page.get_by_role("list").filter(has_text="Mockup of a Happy Short-").get_by_role("link").click(timeout=600000)
    # page.goto("https://placeit.net/c/mockups/stages/bella-canvas-crop-top-mockup-of-a-woman-posing-in-a-studio-with-a-sublimated-bucket-hat-m40822/editor?draftId=59603215&draftId=59603215",
    # page.goto("https://placeit.net/c/mockups/stages/bella-canvas-crop-top-mockup-of-a-woman-posing-in-a-studio-with-a-sublimated-bucket-hat-m40822/editor?draftId=59603215&draftId=59603215",
            #    wait_until="domcontentloaded",
            #    timeout=6000000  # 60 seconds    
      
    page.get_by_role("button", name="Accept Cookies").click(timeout=600000)

    ###############################################################
    # Automated Mockup Workflow 📂
    ###############################################################
    file_numbers = [5, 6, 7, 8,9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21 ,22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]    #, 51, 52, 53, 55, 54, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91. 92, 93, 94, 95, 96, 97, 98, 99, 100]  # <<< update freely

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
        page.locator(".p-icon.p-sm.remove-gray").first.click(timeout=6000000)
        # page.locator(".p-icon.p-sm.remove-gray").filter(has_text="Remove").locator("span").click(timeout=150000)
        # page.locator("label").filter(has_text="Remove").locator("span").click(timeout=6000000)
        page.locator('button:has-text("750x750px")').click(timeout=600000)
        page.get_by_role("button", name="Insert Image 750x750px").set_input_files(f"{num}.png")
        # page.get_by_role("button", name="750x750px", exact=True).click(timeout=600000)

        ############################ CROP + DOWNLOAD ####################
        # page.get_by_role("button", name="Crop").click(timeout=150000)
        page.get_by_role("button", name="Crop", exact=True).click(timeout=600000)
        time.sleep(10)
        # page.goto("https://placeit.net/c/mockups/stages/bella-canvas-crop-top-mockup-of-a-woman-posing-in-a-studio-with-a-sublimated-bucket-hat-m40822/editor?draftId=59603215&draftId=59603215&customG_0=t6mcm7355a")
        page.get_by_role("button", name="Download").click(timeout=600000)
        with page.expect_download(timeout=600000) as download_info:
            page.get_by_role("link", name="Click here to download").first.click(timeout=600000)
        download = download_info.value

        ############################ CLEAR HISTORY ######################
        # page1 = context.new_page()
        # page1.goto("chrome://downloads/")
        # page1.get_by_role("button", name="Delete from history").click(timeout=600000)
        # page.goto("https://placeit.net/c/mockups/stages/mockup-of-a-happy-short-haired-woman-wearing-a-bella-canvas-crop-top-m14385/editor?draftId=59806181&multiFolder_Gradient=96bd8c66ebcf7b9d4ff11f54c7fe6938&colorFolder_Gradient=%2300619b&colorFolder_Shirt%20Color=%23000000&customG_0=t6axh5e71b&draftId=59833981",
                #   wait_until="domcontentloaded",
                #   timeout=600000)
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
