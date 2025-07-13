
import time
import json
import random

# ---------- Mock Tools ----------
def get_weather(location, date):
    """Mocked weather API."""
    weather = random.choice(["Sunny", "Cloudy", "Rainy"])
    print(f"[tool] Weather in {location} on {date}: {weather}")
    return weather

def find_attractions(location, date, budget):
    """Mocked attraction finder API."""
    attractions = [
        {"name": "Auckland Museum", "cost": 25},
        {"name": "Sky Tower", "cost": 30},
        {"name": "Waiheke Island Ferry", "cost": 45},
        {"name": "Mount Eden Walk", "cost": 0},
        {"name": "Auckland Art Gallery", "cost": 20}
    ]
    selected = [a for a in attractions if a["cost"] <= budget / 2]
    print(f"[tool] Found attractions under budget: {[a['name'] for a in selected]}")
    return selected[:3]

# ---------- Agent ----------
def plan_trip(prompt):
    print("[agent] Starting planning...")
    scratchpad = []

    # Extract details from prompt (simple parsing)
    location = "Auckland"
    budget = 500
    days = 2
    dates = ["2025-07-15", "2025-07-16"]

    total_cost = 0
    itinerary = []

    for day, date in enumerate(dates, start=1):
        print(f"\n[agent] Planning Day {day} ({date})")
        weather = get_weather(location, date)
        attractions = find_attractions(location, date, budget - total_cost)
        cost_today = sum(a["cost"] for a in attractions)
        total_cost += cost_today

        scratchpad.append({
            "day": day,
            "date": date,
            "weather": weather,
            "activities": attractions,
            "cost": cost_today
        })

        itinerary.append({
            "day": day,
            "date": date,
            "weather": weather,
            "activities": [a["name"] for a in attractions]
        })

        print(f"[agent] Total cost so far: ${total_cost:.2f}")
        if total_cost > budget:
            print("[agent] Warning: budget exceeded!")
            break

    result = {
        "location": location,
        "budget": budget,
        "total_cost": total_cost,
        "itinerary": itinerary,
        "log": scratchpad
    }

    print("\n[agent] Final Itinerary:")
    print(json.dumps(result, indent=2))
    return result

# ---------- Run ----------
if __name__ == "__main__":
    plan_trip("Plan a 2-day trip to Auckland for under NZ$500")
