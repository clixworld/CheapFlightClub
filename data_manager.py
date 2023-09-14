import requests
from details import BEARER



PRICES_URL = "https://api.sheety.co/c98aca66b847bcdf4f7b2d1f5ef9ee27/flightDeals/prices"
NAMES_URL = "https://api.sheety.co/c98aca66b847bcdf4f7b2d1f5ef9ee27/flightDeals/names"

class DataManager:
    def __init__(self):
        pass

    def get_data_prices(self):
        headers = {
            "Authorization": f"Bearer {BEARER}"
        }
        response = requests.get(url=PRICES_URL, headers=headers)
        data = response.json()
        return data['prices']

    def get_user_info(self):
        first_name = input("What is your first name: ")
        last_name = input("What is your last name: ")
        def check_email(self):
            email = input("What is your email: ")
            email_check = input("Type your email again: ")
            return email, email_check
        email, email_check = check_email(self)
        if email == email_check:
            print("Your added to the system!")
        else:
            print("Email doesn't match")
            check_email(self)
        return first_name, last_name, email
        
    def add_info_to_sheet(self, first, last, email):
        parameters = {
            "name": {
                "first": first,
                "last": last,
                "email": email
            }
        }
        headers = {
          "Authorization": f"Bearer {BEARER}",
          "Content-Type": "application/json",
        }

        response = requests.post(url=NAMES_URL, json=parameters, headers=headers)
        response.raise_for_status()
        print(response.text)

    def get_emails(self):
        headers = {
            "Authorization": f"Bearer {BEARER}"
        }
        response = requests.get(url=NAMES_URL, headers=headers)
        data = response.json()
        return data['names']