from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from collections import defaultdict

app = FastAPI()

class Item(BaseModel):
    Flow_code: str
    Main_asset_code: str
    Ordering_Client: str
    Plant_code: str
    Asset_label: str
    quantity: int
    Inventory_Number: str
    WBS: str
    Supplier_code: int
    Location_supplier: Optional[str]
    Manufacturer: str
    Location_supplier_Adress: str
    Postal_code: str
    City: str
    Country_Code: str
    Supplier_name: str
    Manufacturer_country: str

# In-memory storage for demo
asset_counter = 10000
inventory_to_asset = {}
inventory_to_sub = {}
asset_to_subs = defaultdict(set)

@app.post("/get-asset-id")
def get_asset_id(data: list[Item]):
    result = []
    for item in data:
        inv = item.Inventory_Number
        flow = item.Flow_code
        if flow == "A":
            asset = str(asset_counter)
            asset_counter += 1
            sub = "0"
            inventory_to_asset[inv] = asset
            inventory_to_sub[inv] = sub
            asset_to_subs[asset].add(sub)
        elif flow == "B":
            if inv in inventory_to_asset:
                asset = inventory_to_asset[inv]
                subs = asset_to_subs[asset]
                sub = "0" if "0" not in subs else "1"  # Assuming next is 0 or 1
                inventory_to_sub[inv] = sub
                asset_to_subs[asset].add(sub)
            else:
                asset = "not_found"
                sub = "0"
        elif flow == "M":
            if inv in inventory_to_asset:
                asset = inventory_to_asset[inv]
                sub = inventory_to_sub[inv]
            else:
                asset = "not_found"
                sub = "0"
        else:
            asset = "unknown_flow"
            sub = "0"
        result.append({"asset_code": asset, "sub_asset": sub})
    return result

if __name__ == "__main__":
    import uvicorn
    import os
    port = int(os.environ.get("PORT", 8000))
    print(f"Starting on port {port}")
    print(f"Starting on port {port}")
    uvicorn.run(app, host="0.0.0.0", port=port)
