from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def get_element(self, locator: tuple, exact=None):
        if locator[0] == 'label':
            return self.page.get_by_label(locator[1], exact=exact)
        elif locator[0] == 'text':
            return self.page.get_by_text(locator[1], exact=exact)
        elif locator[0] == 'title':
            return self.page.get_by_title(locator[1], exact=exact)
        elif locator[0] == 'css' or locator[0] == 'xpath':
            return self.page.locator(locator[1])
        elif locator[0] == 'role':
            return self.page.get_by_role(
                role=locator[1], name=locator[2], exact=exact
            )
        else:
            return None

    def click_on_element(
            self,
            locator: tuple,
            timeout=None,
            click_count=1,
            exact=None
    ):
        self.get_element(locator, exact=exact).click(
            timeout=timeout,
            click_count=click_count
        )

    def type_text(self, locator: tuple, text: str, delay=25):
        self.get_element(locator).clear()
        self.get_element(locator).type(text, delay=delay)
