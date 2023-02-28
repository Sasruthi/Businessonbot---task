import random
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionSum(Action):
    def name(self) -> Text:
        return "action_sum"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        num1 = int(tracker.get_slot("number_1"))
        num2 = int(tracker.get_slot("number_2"))
        result = num1 + num2

        response = f"The sum of {num1} and {num2} is {result}."

        dispatcher.utter_message(response)

        return []

class ActionDifference(Action):
    def name(self) -> Text:
        return "action_difference"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        num1 = int(tracker.get_slot("number_1"))
        num2 = int(tracker.get_slot("number_2"))
        result = num1 - num2

        response = f"The difference between {num1} and {num2} is {result}