import pytest
from playwright.sync_api import Page, APIRequestContext

@pytest.fixture(scope="session")
def base_url():
    return "https://www.saucedemo.com"

@pytest.fixture(scope="function", autouse=True)
def configure_page(page: Page, base_url: str):
    # Set default viewport and navigate to base URL
    page.set_viewport_size({"width": 1280, "height": 720})
    page.goto(base_url)
    yield page

@pytest.fixture(scope="session")
def api_request(playwright) -> APIRequestContext:
    # Set up global API context for REST API testing
    request_context = playwright.request.new_context(
        base_url="https://restful-booker.herokuapp.com"
    )
    yield request_context
    request_context.dispose()