import requests
from flight_search import FlightSearch


class DataManager:

    def __init__(self, fs: FlightSearch):
        self.fs = fs

    def get_sheet_data(self):
        url = "https://api.sheety.co/9282b33b30994ffc6a9f48bf60c93049/flightsDeal/prices"
        data = requests.get(url=url)
        # print(data.json())
        prices = data.json()["prices"]
        return prices

    def get_city_codes(self):
        prices = self.get_sheet_data()
        city_codes = [self.fs.get_city(city=dict["city"]) for dict in prices]
        return city_codes

    def update_sheets(self):
        prices = self.get_sheet_data()
        for (index, dict) in enumerate(prices):
            id = dict["id"]
            url = f"https://api.sheety.co/9282b33b30994ffc6a9f48bf60c93049/flightsDeal/prices/{id}"
            body = {
                "price": {"iataCode": self.get_city_codes()[index]}
            }
            data = requests.put(url=url, json=body)
            data.raise_for_status()
