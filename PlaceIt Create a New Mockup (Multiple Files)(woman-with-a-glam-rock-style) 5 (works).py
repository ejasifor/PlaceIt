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
    page.locator("#login_user_email").click(timeout=600000)
    page.locator("#login_user_email").fill("ej.aston1@outlook.com")
    page.locator("#login_user_password").click(timeout=600000)
    page.locator("#login_user_password").fill("Dr3amc@st!")
    page.get_by_role("button", name="Log In").click(timeout=600000)
    time.sleep(5)
    ############################ LOG IN ############################
    page.goto("https://placeit.net/login-process?redirect_to=/my_placeit",
               wait_until="domcontentloaded",
               timeout=6000000  # 60 seconds  
               )
    page.locator("#login_user_email").click(timeout=600000)
    page.locator("#login_user_email").fill("ej.aston1@outlook.com")
    page.locator("#login_user_password").click(timeout=600000)
    page.locator("#login_user_password").fill("Dr3amc@st!")
    page.get_by_role("button", name="Log In").click(timeout=600000)
    # time.sleep(5)
    
    ################################################################
    
    page.goto("https://placeit.net/c/mockups/stages/bella-canvas-crop-top-mockup-featuring-a-woman-with-a-glam-rock-style-m35870/editor?draftId=59603239&draftId=59603239&colorFolder_Crop%20Top%20Color=%23000000",
         wait_until="domcontentloaded",
         timeout=6000000  # 60 seconds  
         )
    
    page.get_by_role("button", name="Accept Cookies").click(timeout=600000)

    page.locator('button:has-text("750x750px")').click(timeout=60000)

    page.get_by_role("button", name="Upload Image 750x750px").set_input_files("14.png")
    # page.get_by_role("button", name="Upload From Your Device").set_input_files("46.png")
    # page.get_by_role("button", name="Insert Image 750x750px").set_input_files("46.png")


    page.get_by_role("button", name="Crop", exact=True).click(timeout=600000)
    time.sleep(10)

    page.get_by_role("button", name="Download").click(timeout=600000)
    with page.expect_download(timeout=600000) as download_info:
        page.get_by_role("link", name="Click here to download").first.click(timeout=600000)
    download = download_info.value
         
    ###############################################################
    # Automated Mockup Workflow 📂
    ###############################################################
    file_numbers = [15, 16, 17, 18, 19, 20, 21 ,22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 47, 48, 49, 50, 51, 52, 53, 55, 54, 56, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 102, 103, 104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189]    #1, 2, 3, 4, 5, 6, 7, 8,9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21 ,22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 47, 48, 49, 50, 51, 52, 53, 55, 54, 56, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 102, 103, 104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189  # <<< update freely

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
        
        page.get_by_text("Remove", exact=True).click(timeout=600000)

        
        page.locator('button:has-text("750x750px")').click(timeout=600000)
        page.get_by_role("button", name="Insert Image 750x750px").set_input_files(f"{num}.png")

        ############################ CROP + DOWNLOAD ####################
        # page.get_by_role("button", name="Crop").click(timeout=150000)
        page.get_by_role("button", name="Crop", exact=True).click(timeout=600000)
        time.sleep(10)  

        page.get_by_role("button", name="Download").click(timeout=600000)
        with page.expect_download(timeout=600000) as download_info:
            page.get_by_role("link", name="Click here to download").first.click(timeout=600000)
        download = download_info.value

        # time.sleep(10)
        page.reload(timeout=600000)

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


