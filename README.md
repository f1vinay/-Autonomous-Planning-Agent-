# Task 3.3 – Autonomous Planning Agent

This project implements a simple autonomous planning agent that plans a two-day trip to Auckland under a specified budget. The assistant uses mock tools to simulate external API calls for weather forecasting and attraction suggestions. The goal is to demonstrate tool-calling, constraint adherence, and structured output using natural language input.

## Overview

The assistant:
- Accepts a travel planning prompt
- Queries two mocked tools:
  - `get_weather(location, date)` – returns sample weather conditions
  - `find_attractions(location, date, budget)` – returns attractions within budget
- Generates a structured daily itinerary
- Observes constraints such as budget and dates
- Outputs a JSON-formatted result with logs

## Project Files


## Prerequisites

- Python 3.8 or higher
- A local Python environment capable of running scripts

## Running the Assistant

### Windows

Double-click `try_3_3.bat` to run the assistant interactively.

### macOS / Linux

Run the script manually from terminal:

```bash
python agent.py
[agent] Planning Day 1 (2025-07-15)
[tool] Weather in Auckland on 2025-07-15: Sunny
[tool] Found attractions under budget: ['Auckland Museum', 'Mount Eden Walk']
[agent] Total cost so far: $25.00
...
[agent] Final Itinerary:
{
  "location": "Auckland",
  "budget": 500,
  "total_cost": 75,
  "itinerary": [...],
  "log": [...]
}
