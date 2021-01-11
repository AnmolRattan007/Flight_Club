import requests


class FlightSearch:
    def get_city(self, city):
        url = "https://tequila-api.kiwi.com/locations/query"
        headers = {"apikey": "MprcHCPStkgHufyajGIv6KaNjy4-nWzo"}
        parameters = {"term": city, "location_types": "city"}
        data = requests.get(url=url, params=parameters, headers=headers)
        data.raise_for_status()
        json = data.json()
        return json["locations"][0]["code"]
