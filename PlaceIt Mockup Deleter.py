import re
import time
from playwright.sync_api import Playwright, sync_playwright, expect

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False) #,slow_mo=3000
    context = browser.new_context()
    page = context.new_page()
    page.locator("body").click(timeout=150000)
    page.goto("https://placeit.net/purchases/",)
    page.locator("#login_user_email").click(timeout=150000)
    page.locator("#login_user_email").fill("ej.aston1@outlook.com")
    page.locator("#login_user_password").click(timeout=150000)
    page.locator("#login_user_password").fill("Coldfusi0n!")
    page.get_by_role("button", name="Log In").click(timeout=150000)
    page.get_by_role("button", name="Accept Cookies").click(timeout=150000)

    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload

    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload

    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload

    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload

    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload

    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload

    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload

    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload

    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload

    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload   
 
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload

    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload

    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload

    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload

    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload

    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload

    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload

    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload

    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload

    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload

    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload

    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload

    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload

    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload

    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload

    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload

    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload

    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload

    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload

    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload   
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload

    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload

    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload

    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload

    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload

    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload

    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload

    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload

    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload

    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload   
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload

    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload

    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload

    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload

    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload

    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload

    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload

    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload

    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload

    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload   
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload

    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload

    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload

    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload

    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload

    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload

    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload

    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload

    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload

    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload   
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload

    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload

    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload

    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload

    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload

    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload

    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload

    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload

    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload

    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload   
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload

    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload

    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload

    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload

    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload

    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload

    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload

    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload

    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload

    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload
    
    page.hover("#container .page-container.downloads a.itemLink .img-wrapper")
    # delete button
    page.get_by_role("button").nth(3).click(timeout=150000)
    page.get_by_role("button", name="Delete").click()
    page.reload()  # Default reload   
    
    # ---------------------
    input("🎉 All Done! Press Enter to close.")
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)



