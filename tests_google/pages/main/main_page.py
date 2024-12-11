from tests_google.pages.base.base_page import BasePage
from tests_google.pages.main.locators import MainLocators
from tests_google.tests.test_data.base.routes import Routes
from tests_google.tests.test_data.main.search_data import SearchData


class MainPage(BasePage):
    def open_google(self):
        self.page.goto(Routes.BASE_URL)

    def type_text_in_search_field(self):
        self.type_text(
            locator=MainLocators.SEARCH_TEXTAREA,
            text=SearchData.TEXT['autotests']
        )

    def click_search_button(self):
        elements = self.get_element(MainLocators.SEARCH_BUTTON)
        for i in range(elements.count()):
            if elements.nth(i).is_visible():
                elements.nth(i).click(timeout=3000)
                break
