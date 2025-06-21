import allure
from pages.order_page import OrderPage


class TestFeedPage:

    @allure.title('При создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_done_order_counter_all_time_increased(self, driver, create_and_delete_user):
        page = OrderPage(driver)
        page.close_modal_if_present()
        page.transition_to_order_feed()
        was_total_orders_all_time = page.total_orders_all_time()
        page.make_an_order(create_and_delete_user)
        page.transition_to_order_feed()
        became_total_orders_all_time = page.total_orders_all_time()
        assert was_total_orders_all_time < became_total_orders_all_time


    @allure.title('При создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_done_order_counter_for_today_increased(self, driver, create_and_delete_user):
        page = OrderPage(driver)
        page.close_modal_if_present()
        page.transition_to_order_feed()
        was_total_orders_today = page.total_orders_today()
        page.make_an_order(create_and_delete_user)
        page.transition_to_order_feed()
        became_total_orders_today = page.total_orders_today()
        assert was_total_orders_today < became_total_orders_today


    @allure.title('После оформления заказа его номер появляется В работе')
    def test_number_created_order_is_in_progress(self, driver, create_and_delete_user):
        page = OrderPage(driver)
        user_order_number = page.make_an_order(create_and_delete_user)
        page.transition_to_order_feed()
        order_number_progress = page.user_order_in_progress(user_order_number)
        assert user_order_number == order_number_progress
