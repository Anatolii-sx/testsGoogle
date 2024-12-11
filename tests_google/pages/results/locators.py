class ResultsLocators:
    LOGO_LINK = ('xpath', '//a[@id="logo"]')
    CLEAR_BUTTON = ('xpath', '//div[@aria-label="Очистить"]')
    SEARCH_TEXTAREA = ('xpath', '//textarea[@aria-label="Найти"]')
    PAGE_TYPE = ('xpath', '//html[contains(@itemtype, "SearchResultsPage")]')
    RESULTS_PAGES_LINKS = (
        'xpath',
        '//div[@id="botstuff"]//td'
    )
    SEARCH_RESULTS_LINKS = (
        'xpath',
        '//div[@id="search"]//div[not(contains(@jsshadow, "true"))]//a'
    )
