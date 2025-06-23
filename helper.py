import allure
import requests

from urls import Urls


class UserMethods:

    @allure.step('Создать пользователя')
    def create_user(self, email, password, name):
        payload = {
            "email": email,
            "password": password,
            "name": name
            }

        response = requests.post(Urls.CREATE_USER, json=payload)

        return {
            "email": payload.get("email"),
            "password": payload.get("password"),
            "name": payload.get("name"),
            "response": response
        }

    @allure.step('Удалить пользователя')
    def delete_user(self, token):
        clean_token = token.replace("Bearer ", "") if token else token

        headers = {
            "Authorization": f"Bearer {clean_token}",  # Добавляем Bearer здесь
            "Content-Type": "application/json"
        }
        response = requests.delete(Urls.DELETE_USER, headers=headers)
        return response
