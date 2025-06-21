import allure

from locators.main_page_locators import MainLocators
from urls import Urls
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Закрыть модальное окно')
    def close_modal_if_present(self):
        return super().close_modal_if_present(
            modal_locator=MainLocators.LOCATOR_MODAL_WINDOW,
            button_locator=MainLocators.LOCATOR_BUTTON_MODAL_WINDOW,
            overlay_locator=MainLocators.LOCATOR_OVERLAY_WINDOW_ORDER
        )

    @allure.step('Переход на Конструктор текущий URL')
    def transition_to_constructor(self):
        self.click_on_element(MainLocators.LOCATOR_PERSONAL_ACCOUNT)
        self.click_on_element(MainLocators.LOCATOR_BUTTON_CONSTRUCTOR)
        return self.driver.current_url

    @allure.step('Ожидаемый URL Конструктор')
    def expected_url_constructor(self):
        return Urls.URL_PAGE_CONSTRUCTOR

    @allure.step('Переход на вкладку Лента заказов и текущий URL')
    def transition_to_order_feed(self):
        self.click_on_element(MainLocators.LOCATOR_BUTTON_ORDER_FEED)
        return self.driver.current_url

    @allure.step('Ожидаемый URL Лента заказов')
    def expected_url_order_feed(self):
        return Urls.URL_PAGE_ORDER_FEED

    @allure.step('Окно с деталями ингредиента')
    def open_window_ingredient_detail_sauce(self):
        self.scroll_to_element(MainLocators.LOCATOR_SAUCE)

    @allure.step('Окно с деталями ингредиента открыто')
    def window_ingredient_detail_sauce_present(self):
        return self.is_element_present(MainLocators.LOCATOR_CLOSE_SAUCE_WINDOW)

    @allure.step('Окно с деталями ингредиента закрыто')
    def close_window_ingredient_detail_sauce(self):
        self.click_on_element(MainLocators.LOCATOR_CLOSE_SAUCE_WINDOW)

    @allure.step('Окно с деталями ингредиента закрыто')
    def window_ingredient_detail_sauce_not_visible(self):
        return self.is_element_not_visible(MainLocators.LOCATOR_SAUCE_WINDOW)

    @allure.step('Ожидание реального номера заказа в окне заказа')
    def wait_for_updated_order_number(self):
        return super().wait_for_updated_order_number(
            number_locator=MainLocators.LOCATOR_GET_ORDER_NUMBER
        )
