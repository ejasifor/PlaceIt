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
    page.locator("#login_user_email").click(timeout=150000)
    page.locator("#login_user_email").fill("ej.aston1@outlook.com")
    page.locator("#login_user_password").click(timeout=150000)
    page.locator("#login_user_password").fill("Dr3amc@st!")
    page.get_by_role("button", name="Log In").click(timeout=150000)

    ################################################################

    page.get_by_role("list").filter(has_text="Mockup of a Happy Short-").get_by_role("link").click(timeout=150000)
    page.goto("https://placeit.net/c/mockups/stages/mockup-of-a-woman-wearing-a-crop-top-and-bike-shorts-in-the-sun-42382/editor?draftId=59603913&colorFolder_Crop%20Top%20Color=%23ffffff&colorFolder_Short%20Color=%23ffffff&draftId=59603913",
               wait_until="domcontentloaded",
               timeout=600000  # 60 seconds    
                )
    page.get_by_role("button", name="Accept Cookies").click(timeout=150000)
    
    #delete right shorts image#
    right_short = page.locator(
        "label.file-upload-title:has-text('Right short design')"
    ).locator("xpath=ancestor::div[contains(@class,'custom-graphic-control')]")
    right_short.locator("button.dropdown-toggle").click(timeout=600000)
    timeout=600000     
    # right_short.locator("a.remove-placeholder").click(timeout=600000)
    page.get_by_role("listitem").filter(has_text="Remove this Image").locator("a").click(timeout=600000)
    
    #delete left shorts image#        
    left_short = page.locator(
        "label.file-upload-title:has-text('Left short design')"
    ).locator("xpath=ancestor::div[contains(@class,'custom-graphic-control')]")
    left_short.locator("button.dropdown-toggle").click(timeout=600000)
    # left_short.locator("a.remove-placeholder").click(timeout=600000)
    
    page.get_by_role("listitem").filter(has_text="Remove this Image").locator("a").click(timeout=600000)
    
    
    #delete top shorts image#
    top_short = page.locator(
        "label.file-upload-title:has-text('Top short design')"
    ).locator("xpath=ancestor::div[contains(@class,'custom-graphic-control')]")
    top_short.locator("button.dropdown-toggle").click(timeout=600000)
    # top_short.locator("a.remove-placeholder").click(timeout=600000)
    
    
    page.get_by_role("listitem").filter(has_text="Remove this Image").locator("a").click(timeout=600000)

    #delete crop top image#  
    crop_top = page.locator(
        "label.file-upload-title:has-text('Crop top design')"
    ).locator("xpath=ancestor::div[contains(@class,'custom-graphic-control')]")

    crop_top.locator("button.dropdown-toggle").click(timeout=600000)
    
    page.get_by_role("listitem").filter(has_text="Remove this Image").locator("a").click(timeout=600000)

    #works
    crop_top.locator("button.dropdown-toggle").click(timeout=600000)
    # page.get_by_role("button", name="Insert Image 750x750px").set_input_files(f"{num}.png")
    
    #works
    # page.get_by_role("listitem").filter(has_text="Upload From Your Device").locator("a").click(timeout=600000) 
    #works
    page.get_by_role("button", name="Upload Image 750x750px").set_input_files("318.png") 

    page.get_by_role("button", name="Crop", exact=True).click(timeout=600000)
    time.sleep(10)
    page.get_by_role("button", name="Download").click(timeout=600000)
    with page.expect_download(timeout=600000) as download_info:
        page.get_by_role("link", name="Click here to download").first.click(timeout=600000)
    download = download_info.value
    # time.sleep(10)
    # page.get_by_role("listitem").filter(has_text="Remove this Image").locator("a").click(timeout=600000)
    page.locator(".p-icon.p-sm.remove-gray").first.click(timeout=6000000)
    
    ###############################################################
                    # Automated Mockup Workflow 📂
    ###############################################################

    file_numbers = [319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350] 
        # <<< update freely
    #201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350] # <<< update freely

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

        page.reload(timeout=600000)

        #works
        crop_top.locator("button.dropdown-toggle").click(timeout=600000)
    
        # page.get_by_role("button", name="Insert Image 750x750px").set_input_files(f"{num}.png")
        # page.get_by_role("button", name="Upload Image 750x750px").set_input_files(f"{num}.png")
        #1
        # page.get_by_role("button", name="Insert Image 750x750px").set_input_files(f"{num}.png")



        #delete right shorts image#
        right_short = page.locator(
            "label.file-upload-title:has-text('Right short design')"
        ).locator("xpath=ancestor::div[contains(@class,'custom-graphic-control')]")
        right_short.locator("button.dropdown-toggle").click(timeout=600000)
        timeout=600000     
        # right_short.locator("a.remove-placeholder").click(timeout=600000)
        page.get_by_role("listitem").filter(has_text="Remove this Image").locator("a").click(timeout=600000)

        #delete left shorts image#        
        left_short = page.locator(
            "label.file-upload-title:has-text('Left short design')"
        ).locator("xpath=ancestor::div[contains(@class,'custom-graphic-control')]")
        left_short.locator("button.dropdown-toggle").click(timeout=600000)
        # left_short.locator("a.remove-placeholder").click(timeout=600000)

        page.get_by_role("listitem").filter(has_text="Remove this Image").locator("a").click(timeout=600000)


        #delete top shorts image#
        top_short = page.locator(
            "label.file-upload-title:has-text('Top short design')"
        ).locator("xpath=ancestor::div[contains(@class,'custom-graphic-control')]")
        top_short.locator("button.dropdown-toggle").click(timeout=600000)
        # top_short.locator("a.remove-placeholder").click(timeout=600000)


        page.get_by_role("listitem").filter(has_text="Remove this Image").locator("a").click(timeout=600000)








        page.get_by_role("button", name="Upload Image 750x750px").set_input_files(f"{num}.png") 
        # page.get_by_role("button", name="Upload Image 750x750px").set_input_files(f"{num}.png")


        ############################ CROP + DOWNLOAD ####################
        page.get_by_role("button", name="Crop", exact=True).click(timeout=600000)
        time.sleep(10)
        page.get_by_role("button", name="Download").click(timeout=600000)
        with page.expect_download(timeout=600000) as download_info:
            page.get_by_role("link", name="Click here to download").first.click(timeout=600000)
        download = download_info.value
        # time.sleep(10)
        # page.get_by_role("listitem").filter(has_text="Remove this Image").locator("a").click(timeout=600000)
        page.locator(".p-icon.p-sm.remove-gray").first.click(timeout=6000000)
        
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

