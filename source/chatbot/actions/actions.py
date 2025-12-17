from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict


class ValidateEngineeringSpecsForm(FormValidationAction):
    """Validates the engineering_specs_form slots."""

    def name(self) -> Text:
        return "validate_engineering_specs_form"

    def validate_industry_sector(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate industry_sector value."""
        if slot_value and slot_value.lower() in ["automotive", "industrial"]:
            return {"industry_sector": slot_value.lower()}
        else:
            dispatcher.utter_message(
                text="Please specify 'automotive' or 'industrial'."
            )
            return {"industry_sector": None}

    def validate_voltage_class(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate voltage_class value."""
        if slot_value and slot_value.lower() in ["hv", "lv", "high voltage", "low voltage"]:
            # Normalize to standard format
            if slot_value.lower() in ["hv", "high voltage"]:
                return {"voltage_class": "hv"}
            elif slot_value.lower() in ["lv", "low voltage"]:
                return {"voltage_class": "lv"}
        else:
            dispatcher.utter_message(
                text="Please specify 'HV' (High Voltage) or 'LV' (Low Voltage)."
            )
            return {"voltage_class": None}
