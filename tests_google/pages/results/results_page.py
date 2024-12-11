from tests_google.pages.base.base_page import BasePage
from playwright.sync_api import expect
from tests_google.pages.results.locators import ResultsLocators


class ResultsPage(BasePage):
    def click_clear_button(self):
        self.click_on_element(
            locator=ResultsLocators.CLEAR_BUTTON,
            timeout=3000
        )

    def check_page_type(self):
        self.__wait_for_domcontent_loaded()
        expect(self.get_element(ResultsLocators.PAGE_TYPE)).to_be_visible(
            timeout=3000
        )

    def check_visibility_logo(self):
        expect(self.get_element(ResultsLocators.LOGO_LINK)).to_be_visible(
            timeout=3000
        )

    def check_results_count(self):
        search_results = self.__get_search_results_count()
        assert search_results != 0

    def check_pages_count(self):
        pages = self.__get_results_pages_count()
        assert pages != 0

    def check_visibility_clear_button(self):
        expect(self.get_element(ResultsLocators.CLEAR_BUTTON)).to_be_visible(
            timeout=3000
        )

    def check_search_field_is_empty(self):
        expect(self.get_element(ResultsLocators.SEARCH_TEXTAREA)).to_be_empty(
            timeout=3000
        )

    def __wait_for_domcontent_loaded(self, timeout=5000):
        self.page.wait_for_load_state(
            state='domcontentloaded',
            timeout=timeout
        )

    def __get_search_results_count(self):
        return self.get_element(ResultsLocators.SEARCH_RESULTS_LINKS).count()

    def __get_results_pages_count(self):
        return self.get_element(ResultsLocators.RESULTS_PAGES_LINKS).count()-2
