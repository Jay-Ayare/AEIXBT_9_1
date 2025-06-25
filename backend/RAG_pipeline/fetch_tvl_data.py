import requests
import json
from datetime import datetime
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# DefiLlama protocols API endpoint
url = "https://api.llama.fi/protocols"
response = requests.get(url)

if response.status_code != 200:
    raise Exception(f"Failed to fetch data: {response.status_code}")

data = response.json()
formatted_data = []
skipped = 0

for item in data:
    tvl_value = item.get("tvl")
    if tvl_value is None:
        skipped += 1
        continue  # Skip entries with no TVL

    formatted_data.append({
        "project": item.get("name", "Unknown"),
        "symbol": item.get("symbol", "N/A"),
        "category": item.get("category", "N/A"),
        "tvl": f"${tvl_value:,.2f}",
        "chain": item.get("chain", "Multiple"),
        "gecko_id": item.get("gecko_id", "N/A"),
        "description": item.get("description", ""),
        "last_updated": datetime.utcnow().isoformat()  # just using current time for MVP
    })

# Save the JSON data
output_path = os.path.join(BASE_DIR, "../DATA/tvl_data.json")
with open(output_path, "w") as f:
    json.dump(formatted_data, f, indent=2)

print(f"✅ Saved {len(formatted_data)} TVL records to {output_path}")
if skipped:
    print(f"⚠️ Skipped {skipped} entries due to missing TVL.")
