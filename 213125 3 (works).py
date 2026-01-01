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
        "https://placeit.net/c/mockups/stages/bella-canvas-crop-top-mockup-of-a-woman-posing-at-a-studio-m14384/editor?draftId=59603909&colorFolder_Shirt%20Color%20%20Color=%23000000",
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

    file_numbers = [
        82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97,
        98, 99, 100, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111,
        112, 113, 114, 115, 116, 117, 118, 119, 120, 122, 123, 124,
        125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136,
        137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148,
        149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160,
        161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 180, 181,
        182, 183, 184, 185, 186, 187, 188, 189, 190
    ]

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
