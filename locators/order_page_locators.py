from selenium.webdriver.common.by import By


class OrderLocators:

    LOCATOR_COMPLETED_FOR_ALL_TIME = By.XPATH, "//p[contains(@class, 'OrderFeed_number__2MbrQ')]"
    LOCATOR_COMPLETED_FOR_TODAY = By.XPATH, "//p[contains(@class, 'OrderFeed_number__2MbrQ')]"
    LOCATOR_ORDER_NUMBER = (By.XPATH, "//li[contains(@class, 'text_type_digits-default')]")
