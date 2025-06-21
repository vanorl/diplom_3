import allure
from locators.login_page_locators import LoginLocators
from locators.main_page_locators import MainLocators
from pages.home_page import HomePage



class AccountPage(HomePage):

    @allure.step('Залогиниться')
    def open_user_page(self, user_data: dict):
        self.close_modal_if_present()
        self.clic_on_element(MainLocators.LOCATOR_PERSONAL_ACCOUNT)
        self.clic_on_element(LoginLocators.LOCATOR_FIELD_EMAIL_LOGIN)
        self.set_text_to_element(LoginLocators.LOCATOR_FIELD_EMAIL_LOGIN, user_data["email"])
        self.clic_on_element(LoginLocators.LOCATOR_FIELD_PASSWORD_LOGIN)
        self.set_text_to_element(LoginLocators.LOCATOR_FIELD_PASSWORD_LOGIN, user_data["password"])
        self.clic_on_element(LoginLocators.LOCATOR_BUTTON_LOGIN)
        self.close_modal_if_present()




