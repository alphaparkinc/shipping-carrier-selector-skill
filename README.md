# genpark-shipping-carrier-selector-skill

> **GenPark AI Agent Skill** -- Shipping logistics courier selector.

## Quick Start

```python
from client import ShippingCarrierSelectorClient
client = ShippingCarrierSelectorClient()
res = client.select_carrier("CA", 5.0, "express")
print(res["selected_carrier"])
```
