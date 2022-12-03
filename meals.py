"""
Prepares a 52 week meal plan, rotating through lists of meals for each day.

Outputs markdown to stdout.

`python3 meals.py`
"""

import json

f = open("data.json")
data = json.load(f)


print("# Sides\n")
for side in data["sides"]:
    print(f"* {side}")

print('\n<div style="page-break-after: always;"></div>\n')

print("# Meals\n")

for i in range(1, 53):
    print(f"## Week {i}\n")
    print(
        f" Day       | Breakfast                      | Lunch                                  | Dinner"
    )
    print(
        f"-----------|--------------------------------|----------------------------------------|--------------------------------"
    )
    for day, meal_choices in data["meals"].items():

        breakfast = meal_choices["breakfast"][i % len(meal_choices["breakfast"])]
        lunch = meal_choices["lunch"][i % len(meal_choices["lunch"])]
        dinner = meal_choices["dinner"][i % len(meal_choices["dinner"])]
        print(f" {day:9} | {breakfast:30} | {lunch:38} | {dinner:35}")
    print("\n")
    if i % 2 == 0:
        print('<div style="page-break-after: always;"></div>\n')
