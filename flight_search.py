import datetime as dt
from datetime import timedelta
import requests
from details import API_KEY
from flight_data import FlightData


class FlightSearch:
    def __init__(self):
        self.api_key = API_KEY
        self.url = "https://api.tequila.kiwi.com/v2/search"
        self.today = dt.datetime.now().strftime("%d/%m/%Y")
        self.sixmonths = dt.datetime.now() + timedelta(days=(6 * 30))
        self.next_date = self.sixmonths.strftime("%d/%m/%Y")

    def search(self, city_to_fly):
        header = {
            "apikey": self.api_key
        }

        parameters = {
            "fly_from": "DFW",
            "fly_to": city_to_fly,
            "date_fly": self.today,
            "date_to": self.next_date,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "one_for_city": 1,
            "curr": "USD",
            "flight_type": "round",
            "max_stopovers": 0
        }

        response = requests.get(url=self.url, params=parameters, headers=header)
        response.raise_for_status()

        try:
            data = response.json()["data"][0]
        except IndexError:
            parameters["max_stopovers"] = 1
            response = requests.get(url=self.url, headers=header, params=parameters)
            try:
                data = response.json()["data"][0]
            except IndexError:
                return None
            else:
                flight_info = FlightData(
                    price=data["price"],
                    from_city=data["route"][0]["cityFrom"],
                    from_airport=data["route"][0]["flyFrom"],
                    to_city=data["route"][1]["cityTo"],
                    to_airport=data["route"][1]["flyTo"],
                    out_date=data["route"][0]["local_departure"].split("T")[0],
                    return_date=data["route"][2]["local_departure"].split("T")[0],
                    link=data["deep_link"],
                    stop_overs=1,
                    via_city=data["route"][0]["cityTo"]
                )
                return flight_info
        else:
            flight_info = FlightData(
                price=data["price"],
                from_city=data["route"][0]["cityFrom"],
                from_airport=data["route"][0]["flyFrom"],
                to_city=data["route"][0]["cityTo"],
                to_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0],
                link=data["deep_link"]
            )
            return flight_info
