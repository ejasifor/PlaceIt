import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://auth.fourthwall.com/auth/realms/Fourthwall/protocol/openid-connect/auth?client_id=Dashboard&redirect_uri=https%3A%2F%2Fhero.fourthwall.com%2Fredirect%2Fbabez-n-baddiez-shop.fourthwall.com%2Fadmin%2Fdashboard%2Fstore-design-v2%2Fpages%2F&state=9be6dd39-fa64-406b-a9be-1e0746ab7196&response_mode=fragment&response_type=code&scope=openid&nonce=285dd9e3-17d1-46a7-82c2-a7515f7656c5&code_challenge=9fWLcWQzhKwPQ_u78czF003Eiv1qqJ1P5LUIqDEgrKw&code_challenge_method=S256")
    page.get_by_role("textbox", name="Email").click(timeout=700000)
    page.get_by_role("textbox", name="Email").fill("playwright codegen")
    page.get_by_role("textbox", name="Email").press("ControlOrMeta+z")
    page.get_by_role("textbox", name="Email").fill("ej.asifor@gmail.com")
    page.get_by_role("textbox", name="Password").click(timeout=600000)
    page.get_by_role("textbox", name="Password").fill("DVYzg3p2!38t9Qs")
    page.get_by_role("button", name="Log in").click(timeout=600000)
    page.goto("https://babez-n-baddiez-shop.fourthwall.com/admin/dashboard/store-design/pages/")
    page.get_by_role("link", name="Babez-N-Baddiez").click(timeout=600000)
    page.goto("https://babez-n-baddiez-shop.fourthwall.com/admin/products/as-colour-womens-premium-crop-top-dtg?selectedColor=Black")
    page.get_by_role("button", name="Design now").click(timeout=600000)
    page.get_by_role("button", name="Next").click(timeout=60000000)
    # time.sleep(120)
    # with page.expect_popup() as page1_info:
    #     page.goto("https://babez-n-baddiez-shop.fourthwall.com/admin/v3/designer/cud_CESBVM5RSRCwhfEkuIHpaQ?productSlug=as-colour-womens-premium-crop-top-dtg&selectedColors=Black")
    # page1 = page1_info.value
    # page1.once("dialog", lambda dialog: dialog.dismiss())
    # page1.close()
    # page.goto("https://babez-n-baddiez-shop.fourthwall.com/admin/v3/designer/cud_CESBVM5RSRCwhfEkuIHpaQ?productSlug=as-colour-womens-premium-crop-top-dtg&selectedColors=Black")

    # ---------------------
    input("✅ Booyah Achieved. Press Enter to close.")
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
