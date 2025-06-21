import pytest
from selenium import webdriver
from data import Data
from helper import UserMethods
from urls import Urls


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):

	if request.param == "chrome":
		from selenium.webdriver.chrome.options import Options
		chrome_options = Options()
		#закрыть сообщение об утечке паролей
		chrome_options.add_experimental_option("prefs", {
			"profile.password_manager_leak_detection": False
		})
		driver = webdriver.Chrome(options=chrome_options)
		driver.set_window_size(1920, 1080)

	elif request.param == "firefox":
		driver = webdriver.Firefox()
		driver.set_window_size(1920, 1080)

	driver.get(Urls.URL_HOME_PAGE_STELLAR_BURGERS)
	yield driver
	driver.quit()


@pytest.fixture
def create_and_delete_user():
    user_data = Data.user_data
    user = UserMethods()
    # создание пользователя
    created_data = user.create_user(
        email=user_data["email"],
        password=user_data["password"],
        name=user_data["name"]
    )
    yield created_data
    token = created_data["response"].json().get("accessToken")
    user.delete_user(token)
