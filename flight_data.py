from datetime import datetime as dt, timedelta
import requests

FROM_CITY = "LON"


class FlightData:

    @classmethod
    def search_cheap_flights(self, to_city):
        url = "https://tequila-api.kiwi.com/v2/search"
        headers = {"apikey": "MprcHCPStkgHufyajGIv6KaNjy4-nWzo"}
        date_from = dt.now().strftime("%d/%m/%Y")
        date_to = (dt.now() + timedelta(days=180)).strftime("%d/%m/%Y")
        parameters = {"fly_from": FROM_CITY, "fly_to": to_city, "date_from": date_from, "date_to": date_to,
                      "curr": "GBP"}
        data = requests.get(url=url, params=parameters, headers=headers)
        data.raise_for_status()
        json = data.json()
        return json
