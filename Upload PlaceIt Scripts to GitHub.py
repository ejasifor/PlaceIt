import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://github.com/ejasifor/PlaceIt/upload/main")
    page.get_by_role("link", name="Sign in").click()
    page.get_by_role("textbox", name="Username or email address").click()
    page.get_by_role("textbox", name="Username or email address").fill("emiko.asifor@gmail.com")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("SYWDiTHa7R3sJZ@")
    page.get_by_role("button", name="Sign in", exact=True).click()
    # page.get_by_role("link", name="ejasifor/Work").click()
    # page.get_by_label("Account").get_by_role("link", name="ejasifor/Python-Scripts").click()
    # page.get_by_role("button", name="Add file").click()
    # page.get_by_role("menuitem", name="Create new file").click()
    # page.goto("https://github.com/ejasifor/Python-Scripts")
    # page.get_by_role("button", name="Add file").click()
    # page.get_by_role("menuitem", name="Upload files").click()
    # page.get_by_role("button", name="Choose your files").click()
    # page.get_by_role("button", name="Choose your files").set_input_files(["Hot Strings Basic (1st Job in Queue).py", "Hot Strings Basic (2nd Job in Queue).py", "Hot Strings Basic (3rd Job in Queue).py", "Hot Strings Full (1st Job in Queue).py", "Hot Strings Full (2nd Job in Queue).py", "Hot Strings Full (3rd Job in Queue).py"])
    # page.get_by_role("button", name="Commit changes").click()
    # page.goto("https://github.com/ejasifor/Python-Scripts")

    # ---------------------
    input("✅ Booyah Achieved. Press Enter to close.")
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)



