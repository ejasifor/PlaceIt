############################### LOGIN ##############################

import re
import time
from datetime import datetime, timedelta
from playwright.sync_api import Playwright, sync_playwright, expect


def upload_image(page, file_path):
    """Handles the new Upload From Your Device flow safely"""
    with page.expect_file_chooser() as fc_info:
        page.locator("a.upload-from-device", has_text="Upload From Your Device").click(timeout=60000)
    fc_info.value.set_files(file_path)


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.locator("body").click(timeout=60000000)

############################### LOGIN ##############################

import re
import time
from datetime import datetime, timedelta
from playwright.sync_api import Playwright, sync_playwright, expect


def upload_image(page, file_path):
    """Handles the new Upload From Your Device flow safely"""
    with page.expect_file_chooser() as fc_info:
        page.locator("a.upload-from-device", has_text="Upload From Your Device").click(timeout=60000)
    fc_info.value.set_files(file_path)


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.locator("body").click(timeout=60000000)

    ############################ LOG IN ############################
    page.goto(
        "https://placeit.net/login-process?redirect_to=/my_placeit",
        wait_until="domcontentloaded",
        timeout=6000000
    )

    page.locator("#login_user_email").fill("ej.aston1@outlook.com")
    page.locator("#login_user_password").fill("Dr3amc@st!")
    page.get_by_role("button", name="Log In").click(timeout=60000000)

    page.goto(
        "https://placeit.net/login-process?redirect_to=/my_placeit",
        wait_until="domcontentloaded",
        timeout=6000000
    )

    page.locator("#login_user_email").fill("ej.aston1@outlook.com")
    page.locator("#login_user_password").fill("Dr3amc@st!")
    page.get_by_role("button", name="Log In").click(timeout=60000000)
    time.sleep(10)
    ################################################################

    page.goto(
        "https://placeit.net/c/mockups/stages/bella-canvas-crop-top-mockup-of-a-woman-posing-at-a-studio-m14384/editor?draftId=59603909&draftId=59603909&colorFolder_Shirt%20Color%20%20Color=%23ffffff",
        wait_until="domcontentloaded",
        timeout=6000000
    )

    page.get_by_role("button", name="Accept Cookies").click(timeout=60000000)

    ######################## FIRST UPLOAD ##########################
    page.locator('button:has-text("750x750px")').click(timeout=1000000)

    # Now, locate and click the "Recently Uploaded" link that appears in the dropdown.
    # The element must be visible after the dropdown is clicked.
    page.locator("a.upload-from-device").click(timeout=1000000)
    # page.locator("a").filter(has_text="Recently Uploaded").click(timeout=1000000)
    # --- END OF CORRECTED BLOCK ---

    # The original script had this block which seems redundant after the fix above
    # and was partially responsible for the confusion. We are leaving it out.
    # page.locator("#recentlyUploadedModal").get_by_role("img").first.click(timeout=1000000)
    # page.get_by_role("button", name="Crop").click(timeout=1000000)
    
    # page.locator("#recentlyUploadedModal").get_by_role("img").first.click(timeout=1000000)
    page.get_by_role("button", name="Crop").click(timeout=1000000)
    time.sleep(10)

    page.get_by_role("button", name="Download").click(timeout=60000000)
    with page.expect_download(timeout=600000) as download_info:
        page.get_by_role("link", name="Click here to download").first.click(timeout=60000000)
    download = download_info.value

    ###############################################################
    # Automated Mockup Workflow 📂
    ###############################################################

    file_numbers = [109, 248]  #201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350,

    total = len(file_numbers)
    start_time = time.time()

    for index, num in enumerate(file_numbers, start=1):
        cycle_start = time.time()

        #################### 📊 PROGRESS + ETA ####################
        elapsed = time.time() - start_time
        avg_time = elapsed / index
        remaining = avg_time * (total - index)
        finish_time = datetime.now() + timedelta(seconds=remaining)

        print(f"\n----------------------------------------")
        print(f"🔄 Processing {index}/{total} — {num}.png")
        print(f"⏱ Elapsed: {elapsed/60:.2f} min")
        print(f"🧮 ETA: {remaining/60:.2f} min")
        print(f"📅 Finish: {finish_time.strftime('%I:%M:%S %p')}")
        print("----------------------------------------\n")

        ######################## UPLOAD ########################

        page.get_by_text("Remove", exact=True).click(timeout=60000000)
        page.locator('button:has-text("750x750px")').click(timeout=60000000)

        upload_image(page, f"{num}.png")

        ######################## CROP + DOWNLOAD ########################

        page.get_by_role("button", name="Crop", exact=True).click(timeout=60000000)
        time.sleep(10)

        page.get_by_role("button", name="Download").click(timeout=60000000)
        with page.expect_download(timeout=600000) as download_info:
            page.get_by_role("link", name="Click here to download").first.click(timeout=60000000)
        download = download_info.value

        page.reload(timeout=600000)

        ######################## SUMMARY ########################

        cycle_time = time.time() - cycle_start
        print(f"✓ {num}.png complete ({cycle_time:.1f}s)\n")

    ###############################################################

    print("\n🎉 All processing complete!")
    print(f"Total time: {(time.time() - start_time)/60:.2f} min\n")
    input("Press ENTER to close.")

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)