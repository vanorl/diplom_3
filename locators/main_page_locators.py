from selenium.webdriver.common.by import By


class MainLocators:

    LOCATOR_PERSONAL_ACCOUNT = By.XPATH, '//a[.//p[text()="Личный Кабинет"]]'
    LOCATOR_MODAL_WINDOW = By.CSS_SELECTOR, "div[class*='modal_overlay']"
    LOCATOR_BUTTON_MODAL_WINDOW = By.CSS_SELECTOR, "div.Modal_modal_overlay__x2ZCr button"
    LOCATOR_BUTTON_CONSTRUCTOR = By.XPATH, '//p[@class="AppHeader_header__linkText__3q_va ml-2"][contains(text(), "Конструктор")]'
    LOCATOR_BUTTON_ORDER_FEED = By.XPATH, '//p[@class="AppHeader_header__linkText__3q_va ml-2"][contains(text(), "Лента Заказов")]'
    LOCATOR_SAUCE = By.XPATH, '//a[img[@alt="Соус Spicy-X"]]'
    LOCATOR_SAUCE_WINDOW = By.XPATH, '//h2[contains(text(), "Детали ингредиента")]'
    LOCATOR_CLOSE_SAUCE_WINDOW = By.XPATH, '//button[@class="Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK"]'
    LOCATOR_BUN = By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6c"]'
    LOCATOR_OF_SELECTED = By.CSS_SELECTOR, '.BurgerConstructor_basket__29Cd7'
    LOCATOR_BUTTON_PLACE_AN_ORDER = By.XPATH, '//button[contains(@class, "button_button__33qZ0") and contains(text(), "Оформить заказ")]'
    LOCATOR_GET_ORDER_NUMBER = By.CSS_SELECTOR, '.Modal_modal__title_shadow__3ikwq'
    LOCATOR_CLOSE_ORDER_WINDOW = By.XPATH, "//button[contains(@class, 'Modal_modal__close')]"
    LOCATOR_OVERLAY_WINDOW_ORDER = By.CLASS_NAME, "Modal_modal_overlay__x2ZCr"
    LOCATOR_INGREDIENT = [By.XPATH, '//img[@alt="Флюоресцентная булка R2-D3"]']
    LOCATOR_COUNTER_INGREDIENT = [By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]'
                                    '//p[@class="counter_counter__num__3nue1"]']