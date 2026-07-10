"""
shipping-carrier-selector-skill: Client SDK
Auto-maps country zoning and weights to recommend shipping service providers.
"""
from __future__ import annotations
from typing import Optional


class ShippingCarrierSelectorClient:
    """
    SDK for logistics fulfillment mapping.
    """

    def select_carrier(
        self,
        country_code: str,
        package_weight_lbs: float,
        delivery_urgency: str = "standard",
    ) -> dict:
        cc = country_code.upper()
        speed = delivery_urgency.lower()

        if cc == "US":
            if speed == "express":
                carrier = "FedEx Overnight"
            elif package_weight_lbs > 10.0:
                carrier = "UPS Ground"
            else:
                carrier = "USPS Ground Advantage"
        else:
            # International routes
            if speed == "express":
                carrier = "DHL Express"
            else:
                carrier = "Asendia Priority"

        return {
            "selected_carrier": carrier,
            "shipping_method_label": "International Express" if cc != "US" and speed == "express" else "Domestic Ground"
        }
