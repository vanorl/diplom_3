import allure
from pages.home_page import HomePage


class TestMainPage:


    @allure.title('Переход по клику на Конструктор')
    def test_transition_to_constructor(self, driver):
        page = HomePage(driver)
        page.close_modal_if_present()
        current_url = page.transition_to_constructor()
        expected_url = page.expected_url_constructor()
        assert current_url == expected_url


    @allure.title('Перехода по клику на  Лента заказов')
    def test_transition_to_order_feed(self, driver):
        page = HomePage(driver)
        page.close_modal_if_present()
        current_url = page.transition_to_order_feed()
        expected_url = page.expected_url_order_feed()
        assert current_url == expected_url


    @allure.title('При клике на ингредиент появляется всплывающее окно с деталями')
    def test_ingredient_details_modal_window(self, driver):
        page = HomePage(driver)
        page.close_modal_if_present()
        page.open_window_ingredient_detail_sauce()
        assert page.window_ingredient_detail_sauce_present()


    @allure.title('Всплывающее окно ингредиента закрывается кликом по крестику')
    def test_close_ingredient_modal_window(self, driver):
        page = HomePage(driver)
        page.close_modal_if_present()
        page.open_window_ingredient_detail_sauce()
        page.close_window_ingredient_detail_sauce()
        assert  page.window_ingredient_detail_sauce_not_visible()
