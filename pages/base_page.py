from playwright.sync_api import Page, Locator

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def get_title(self) -> str:
        return self.page.title()

    def wait_for_url(self, url_pattern: str):
        self.page.wait_for_url(url_pattern)