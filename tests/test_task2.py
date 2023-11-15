from dotenv import load_dotenv


import unittest
import os
import requests


class TestFolderCreation(unittest.TestCase):

        def setUp(self):
                load_dotenv()
                self.folder_name = '123'
                self.headers = {'Authorization': os.getenv('TOKEN')}
                self.params = {'path': f'{self.folder_name}'}

        def test_creation(self):
                response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                                        params=self.params,
                                        headers=self.headers)
                self.assertEqual(response.status_code, 201)
                # Проверка существования папки
                response = requests.get('https://cloud-api.yandex.net/v1/disk/resources',
                                        params=self.params,
                                        headers=self.headers)
                self.assertEqual(response.status_code, 200)

        # Попытка пересоздания существующей папки
        @unittest.expectedFailure
        def test_duplicate(self):
                headers = {'Authorization': self.token}
                params = {'path': f'{self.folder_name}'}
                response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                                        params=self.params,
                                        headers=self.headers)
                self.assertEqual(response.status_code, 201)

        # Попытка создания папки без авторизации
        @unittest.expectedFailure       
        def test_unauthorized_access(self):
                response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                                        params=self.params)
                self.assertEqual(response.status_code, 201)

        # Попытка использования недопустимого имени папки
        @unittest.expectedFailure
        def test_invalid_folder_name(self):
                params = {'path': '123:123'}
                response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                                        params=params,
                                        headers=self.headers)
                self.assertEqual(response.status_code, 201)

        # Удаление созданой папки после тестирования
        @classmethod
        def tearDownClass(self):
                self.folder_name = '123'
                self.headers = {'Authorization': os.getenv('TOKEN')}
                self.params = {'path': f'{self.folder_name}'}
                response = requests.delete('https://cloud-api.yandex.net/v1/disk/resources',
                                        params=self.params,
                                        headers=self.headers)



