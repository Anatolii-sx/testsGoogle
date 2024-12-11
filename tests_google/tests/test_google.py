class TestGoogle:
    def test_google(self, main_page, results_page):
        # 1. Переход на google.com
        main_page.open_google()
        # 2. Ввод в поле поиска "Автотесты"
        main_page.type_text_in_search_field()
        # 3. Нажатие кнопки "Поиск в Google"
        main_page.click_search_button()
        # 4. Проверка перехода на страницу с результатами поиска
        results_page.check_page_type()
        # 5. Проверка наличия логотипа
        results_page.check_visibility_logo()
        # 6. Проверка количества результатов поиска на странице (!=0)
        results_page.check_results_count()
        # 7. Проверка количества страниц (!=0)
        results_page.check_pages_count()
        # 8. Проверка наличия кнопки "Очистить"
        results_page.check_visibility_clear_button()
        # 9. Нажатие кнопки "Очистить" и проверка очищения строки поиска
        results_page.click_clear_button()
        results_page.check_search_field_is_empty()
