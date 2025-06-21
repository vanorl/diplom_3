import allure
from selenium.common import TimeoutException, NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from seletools.actions import drag_and_drop


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    @allure.step('Найти нужный элемент')
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(locator)
        )
        return self.driver.find_element(*locator)

    @allure.step('Кликнуть по элементу')
    def click_on_element(self, locator, ignore_overlay_locator=None):
        if ignore_overlay_locator:
            try:
                WebDriverWait(self.driver, 3).until(
                    EC.invisibility_of_element_located(ignore_overlay_locator)
                )
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

    @allure.step('Закрыть модальное окно, если оно появилось')
    def close_modal_if_present(self, modal_locator, button_locator, overlay_locator=None):
        try:
            WebDriverWait(self.driver, 2).until(
                EC.visibility_of_element_located(modal_locator)
            )
            if overlay_locator:
                try:
                    WebDriverWait(self.driver, 3).until(
                        EC.invisibility_of_element_located(overlay_locator)
                    )
                except TimeoutException:
                    pass

            WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable(button_locator)
            ).click()

            WebDriverWait(self.driver, 2).until(
                EC.invisibility_of_element_located(modal_locator)
            )

        except TimeoutException:
            pass

    @allure.step('Ожидание валидного номера заказа, затем обновления')
    def wait_for_updated_order_number(self, number_locator, timeout=60):
        element = WebDriverWait(self.driver, timeout).until(
            lambda d: (
                (el := d.find_element(*number_locator)) and
                el.is_displayed() and
                el.text.strip().isdigit() and
                int(el.text.strip()) > 0
            ) and el
        )
        initial_text = element.text
        WebDriverWait(self.driver, timeout).until(
            lambda _: element.text != initial_text
        )
        return element.text.strip()

    @allure.step('Ожидание появления текста в элементах')
    def wait_for_text_among_elements(self, locator, expected_text, timeout=10):
        def condition(driver):
            try:
                elements = driver.find_elements(*locator)
                for el in elements:
                    try:
                        if el.is_displayed() and el.text.strip() == expected_text:
                            return True
                    except StaleElementReferenceException:
                        continue
                return False
            except Exception:
                return False

        WebDriverWait(self.driver, timeout).until(condition)
        return expected_text
