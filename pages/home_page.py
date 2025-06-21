import allure

from selenium.common import TimeoutException, NoSuchElementException
from seletools.actions import drag_and_drop
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MainLocators
from urls import Urls


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        # создать экземпляр WebDriverWait с таймаутом 10 секунд
        self.wait = WebDriverWait(self.driver, 10)


    @allure.step('Найти нужный элемент')
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 30).until(
            expected_conditions.presence_of_element_located(locator)
        )
        return self.driver.find_element(*locator)


    @allure.step('Кликнуть по элементу')
    def clic_on_element(self, locator):
        try:
            WebDriverWait(self.driver, 3).until(
                EC.invisibility_of_element_located(MainLocators.LOCATOR_OVERLAY_WINDOW_ORDER))
        except TimeoutException:
            pass

        element = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()


    @allure.step('Скролл и клик до элемента')
    def scroll_to_element(self, locator):
        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(locator)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)
        return element


    @allure.step('Текст элемента')
    def get_text_from_element(self, locator):
        element = self.find_element_with_wait(locator)
        return element.text


    @allure.step('Ввести текст в элемент')
    def set_text_to_element(self, locator, text):
        element = self.find_element_with_wait(locator)
        element.send_keys(text)


    @allure.step('Перенос ингредиента в корзину')
    def drag_and_drop_element(self, source, target):
        source_element = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(source)
        )
        target_element = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(target)
        )
        drag_and_drop(self.driver, source_element, target_element)

    @allure.step('Закрыть модальное окно')
    def close_modal_if_present(self):
        try:
            WebDriverWait(self.driver, 2).until(
                EC.visibility_of_element_located(MainLocators.LOCATOR_MODAL_WINDOW)
            )
            try:
                WebDriverWait(self.driver, 3).until(
                    EC.invisibility_of_element_located(MainLocators.LOCATOR_OVERLAY_WINDOW_ORDER)
                )
            except TimeoutException:
                pass

            WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable(MainLocators.LOCATOR_BUTTON_MODAL_WINDOW)
            ).click()

            WebDriverWait(self.driver, 2).until(
                EC.invisibility_of_element_located(MainLocators.LOCATOR_MODAL_WINDOW)
            )

        except TimeoutException:
            pass




    @allure.step('Элемент не виден на странице')
    def is_element_not_visible(self, locator):
        try:
            WebDriverWait(self.driver, 1).until(
                EC.invisibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False


    @allure.step('Элемент присутствует')
    def is_element_present(self, locator):
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False


    @allure.step('Переход на Конструктор текущий URL')
    def transition_to_constructor(self):
        self.clic_on_element(MainLocators.LOCATOR_PERSONAL_ACCOUNT)
        self.clic_on_element(MainLocators.LOCATOR_BUTTON_CONSTRUCTOR)
        return self.driver.current_url


    @allure.step('Ожидаемый URL Конструктор')
    def expected_url_constructor(self):
        expected_url = Urls.URL_PAGE_CONSTRUCTOR
        return expected_url


    @allure.step('Переход на вкладку Лента заказов и текущий URL')
    def transition_to_order_feed(self):
        self.clic_on_element(MainLocators.LOCATOR_BUTTON_ORDER_FEED)
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
        self.clic_on_element(MainLocators.LOCATOR_CLOSE_SAUCE_WINDOW)


    @allure.step('Окно с деталями ингредиента закрыто')
    def window_ingredient_detail_sauce_not_visible(self):
        return self.is_element_not_visible(MainLocators.LOCATOR_SAUCE_WINDOW)



    @allure.step('Ожидание реального номера заказа в окне заказа')
    def wait_for_updated_order_number(self):
        # ожидать появление элемента и что он содержит валидный номер заказа
        element = WebDriverWait(self.driver, 60).until(
            lambda d: (
                              (el := d.find_element(*MainLocators.LOCATOR_GET_ORDER_NUMBER)) and
                              el.is_displayed() and
                              el.text.strip().isdigit() and
                              int(el.text.strip()) > 0
                      ) and el
        )
        initial_text = element.text
        WebDriverWait(self.driver, 60).until(
            lambda _: element.text != initial_text
        )
        return element.text.strip()
