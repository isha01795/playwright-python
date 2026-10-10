from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

def test_successful_login(page: Page):
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")

    # Web-first assertion
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

def test_invalid_login_error(page: Page):
    login_page = LoginPage(page)
    login_page.login("invalid_user", "wrong_password")

    assert "Epic sadface" in login_page.get_error_text()