import allure

from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MainLocators
from locators.order_page_locators import OrderLocators
from pages.account_page import AccountPage


class OrderPage (AccountPage):

    @allure.step('Перейти на страницу Лента Заказов')
    def open_order_feed(self):
        self.close_modal_if_present()
        self.clic_on_element(MainLocators.LOCATOR_BUTTON_ORDER_FEED)


    @allure.step('Оформить заказ')
    def make_an_order(self, create_and_delete_user_with_data):
        self.close_modal_if_present()
        self.open_user_page(create_and_delete_user_with_data)
        self.close_modal_if_present()
        self.clic_on_element(MainLocators.LOCATOR_BUTTON_CONSTRUCTOR)
        self.drag_and_drop_element(MainLocators.LOCATOR_BUN, MainLocators.LOCATOR_OF_SELECTED)
        self.clic_on_element(MainLocators.LOCATOR_BUTTON_PLACE_AN_ORDER)
        order_number = self.wait_for_updated_order_number()
        self.clic_on_element(MainLocators.LOCATOR_CLOSE_ORDER_WINDOW)
        self.close_modal_if_present()
        return f"{int(order_number):07d}"



    @allure.step('Метод возвращает число заказов из графы "Выполнено за все время". Страница "Лента заказов"')
    def total_orders_all_time(self):
        return self.get_text_from_element(OrderLocators.LOCATOR_COMPLETED_FOR_ALL_TIME)

    @allure.step('Метод возвращает число заказов из графы "Выполнено за сегодня". Страница "Лента заказов"')
    def total_orders_today(self):
        return self.get_text_from_element(OrderLocators.LOCATOR_COMPLETED_FOR_TODAY)

    @allure.step('Ждём появления заказа В работе')
    def user_order_in_progress(self, expected_order_number):
        def order_number_appeared(driver):
            elements = driver.find_elements(*OrderLocators.LOCATOR_ORDER_NUMBER)
            visible_numbers = [el.text.strip() for el in elements if el.is_displayed()]
            return expected_order_number in visible_numbers

        WebDriverWait(self.driver, 10).until(order_number_appeared)
        return expected_order_number
