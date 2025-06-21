import allure

from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MainLocators
from locators.order_page_locators import OrderLocators
from pages.account_page import AccountPage



class OrderPage(AccountPage):

    @allure.step('Перейти на страницу Лента Заказов')
    def open_order_feed(self):
        self.close_modal_if_present()
        self.click_on_element(MainLocators.LOCATOR_BUTTON_ORDER_FEED)


    @allure.step('Оформить заказ')
    def make_an_order(self, create_and_delete_user_with_data):
        self.close_modal_if_present()
        self.open_user_page(create_and_delete_user_with_data)
        self.close_modal_if_present()
        self.click_on_element(MainLocators.LOCATOR_BUTTON_CONSTRUCTOR)
        self.drag_and_drop_element(MainLocators.LOCATOR_BUN, MainLocators.LOCATOR_OF_SELECTED)
        self.click_on_element(MainLocators.LOCATOR_BUTTON_PLACE_AN_ORDER)
        order_number = self.wait_for_updated_order_number()
        self.close_modal_if_present()
        self.click_on_element(MainLocators.LOCATOR_CLOSE_ORDER_WINDOW)
        return f"{int(order_number):07d}"



    @allure.step('Число заказов Выполнено за все время')
    def total_orders_all_time(self):
        return self.get_text_from_element(OrderLocators.LOCATOR_COMPLETED_FOR_ALL_TIME)

    @allure.step('Число заказов Выполнено за сегодня')
    def total_orders_today(self):
        return self.get_text_from_element(OrderLocators.LOCATOR_COMPLETED_FOR_TODAY)

    @allure.step('Появление заказа В работе')
    def user_order_in_progress(self, expected_order_number):
        return self.wait_for_text_among_elements(
            locator=OrderLocators.LOCATOR_ORDER_NUMBER,
            expected_text=expected_order_number
        )
