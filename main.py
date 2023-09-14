from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

flightSearch = FlightSearch()
dataManager = DataManager()
notificationManager = NotificationManager()

sheet_data = dataManager.get_data_prices()


for destination in sheet_data:
    flight = flightSearch.search(destination["iataCode"])

    if flight is None:
        continue
    if flight.price < destination["price"]:

        users = dataManager.get_emails()
        emails = [row["email"] for row in users]
        names = [row["first"] for row in users]

        
        message=f"Low price alert! Only ${flight.price} to fly from {flight.from_city}-{flight.from_airport} to {flight.to_city}-{flight.to_airport}, from {flight.out_date} to {flight.return_date}."
        
        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."

        message += f"\nThe link is here: {flight.link}"
        notificationManager.send_emails(emails, message)


print("Success")