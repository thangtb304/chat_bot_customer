from rasa_sdk import Action
from rasa_sdk.events import SlotSet

class ActionGreet(Action):
    def name(self):
        return "utter_greet"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text="Hello! How can I help you today?")
        return []

class ActionBookFlight(Action):
    def name(self):
        return "utter_flight_booked"

    def run(self, dispatcher, tracker, domain):
        departure = tracker.get_slot('departure_city')
        destination = tracker.get_slot('destination_city')
        dispatcher.utter_message(text=f"Your flight from {departure} to {destination} has been booked!")
        return []

class ActionPriceInfo(Action):
    def name(self):
        return "utter_price_info"

    def run(self, dispatcher, tracker, domain):
        departure = tracker.get_slot('departure_city')
        destination = tracker.get_slot('destination_city')
        dispatcher.utter_message(text=f"The price for a flight from {departure} to {destination} is $200.")
        return []




# actions.py
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# from typing import Any, Text, Dict, List

# class ActionGreet(Action):
#     def name(self) -> Text:
#         return "action_greet"

#     def run(
#         self, dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any]
#     ) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message(text="Hello! How can I help you?")
#         return []
