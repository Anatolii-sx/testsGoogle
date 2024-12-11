import pytest
from playwright.sync_api import Page
from playwright.sync_api import sync_playwright
from tests_google.pages.main.main_page import MainPage
from tests_google.pages.results.results_page import ResultsPage


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chromium")
    parser.addoption("--headless", action="store", default="False")


def _str_to_bool(value):
    return value.lower() in ("yes", "true")


@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption("--browser_name")
    headless = _str_to_bool(request.config.getoption("--headless"))

    with sync_playwright() as p:
        if browser_name == "chromium" \
                or browser_name == "firefox" \
                or browser_name == "webkit":
            browser = getattr(p, browser_name).launch(headless=headless)
        else:
            raise ValueError(
                "Browser name must be 'chromium' or 'firefox' or 'webkit'"
            )

        yield browser
        browser.close()


@pytest.fixture(scope='function')
def context(browser):
    context = browser.new_context(locale="ru-RU")
    yield context
    context.close()


@pytest.fixture(scope='function')
def page(context):
    page: Page = context.new_page()
    page.set_viewport_size({'height': 1024, 'width': 1366})
    yield page
    page.close()


@pytest.fixture(scope='function')
def main_page(page):
    main_page = MainPage(page)
    yield main_page


@pytest.fixture(scope='function')
def results_page(page):
    yield ResultsPage(page)
