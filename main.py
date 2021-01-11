from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData
from notification_manager import NotificationManager

fs = FlightSearch()
dataManager = DataManager(fs)
sheet_data = dataManager.get_sheet_data()
print(sheet_data)
cities = dataManager.get_city_codes()
for (index, city) in enumerate(cities):
    json = FlightData.search_cheap_flights(city)
    price = json["data"][0]["price"]
    city_to = json["data"][0]["cityTo"]
    low_cost = sheet_data[index]["lowestPrice"]
    if price < low_cost:
        NotificationManager.send_message(body=f"Flight from london to {city_to} at it's lowest cost {low_cost} only")
