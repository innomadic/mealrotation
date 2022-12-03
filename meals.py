"""
Prepares a 52 week meal plan, rotating through lists of meals for each day.

`python3 meals.py > plan.md`
"""
meals = {
    "Saturday": {
        "breakfast": ["Baked Oatmeal"],
        "lunch": [
            "Spaghetti",
            "Grilled Chicken with Vegetables",
            "Meatloaf",
            "Biscuits and Gravy with eggs",
            "Chicken Fried Rice",
        ],
        "dinner": ["Leftovers"],
    },
    "Sunday": {
        "breakfast": ["Waffles with Eggs", "Pancakes with Eggs"],
        "lunch": [
            "Butter Chicken",
            "Potato Curry",
            "Chili",
            "Potato Soup",
            "Chicken Noodle Soup",
            "Lentils",
            "Lasagna",
            "Soup Beans and Cornbread",
        ],
        "dinner": ["Leftovers"],
    },
    "Monday": {
        "breakfast": ["Crepes with Shakshuka/Eggs"],
        "lunch": [
            "Fried Chicken with Fries",
            "Korean Fried Chicken",
            "Chicken Parmesean",
        ],
        "dinner": ["Leftovers"],
    },
    "Tuesday": {
        "breakfast": ["Toast with Jelly and Eggs", "Cinnamon Toast with Eggs"],
        "lunch": ["Tacos", "Enchiladas", "Quesadillas"],
        "dinner": ["Leftovers"],
    },
    "Wednesday": {
        "breakfast": ["Hashbrowns with Eggs"],
        "lunch": [
            "Steak with Asian Slaw",
            "Steak with Vegetables and Rolls",
            "Steak with Baked/Mashed/Sweet Potatoes",
        ],
        "dinner": ["Leftovers"],
    },
    "Thursday": {
        "breakfast": ["French Toast", "Biscuits with Gravy and Eggs"],
        "lunch": ["Pizza", "Grilled Cheese", "Burgers with Fries", "Restaurant"],
        "dinner": ["Leftovers"],
    },
    "Friday": {
        "breakfast": ["Cinnamon Rolls", "Granola with Fruit and Yogurt"],
        "lunch": [
            "Restaurant",
            "Popcorn, Apples, Snacks",
            "Pita Chips, Vegetables, Hummus, Feta",
        ],
        "dinner": ["Leftovers"],
    },
}

sides = [
    "Salad",
    "Asian Slaw",
    "Roasted carrots, onions, beets",
    "Sauerkraut",
    "Grilled Zucchini",
    "Squash",
    "Mashed Potatoes",
    "Baked Potatoes",
    "Sweet Potatoes",
    "Raw carrots and cucumbers",
    "Roasted cabbage",
    "French fries",
    "Grean beans",
    "Beans",
]


print("# Sides\n")
for side in sides:
    print(f"* {side}")

print('<div style="page-break-after: always;"></div>\n')

print("# Meals\n")

for i in range(1, 53):
    print(f"## Week {i}\n")
    print(
        f" Day       | Breakfast                      | Lunch                                  | Dinner"
    )
    print(
        f"-----------|--------------------------------|----------------------------------------|--------------------------------"
    )
    for day, meal_choices in meals.items():

        breakfast = meal_choices["breakfast"][i % len(meal_choices["breakfast"])]
        lunch = meal_choices["lunch"][i % len(meal_choices["lunch"])]
        dinner = meal_choices["dinner"][i % len(meal_choices["dinner"])]
        print(f" {day:9} | {breakfast:30} | {lunch:38} | {dinner:35}")
    print("\n")
    if i % 2 == 0:
        print('<div style="page-break-after: always;"></div>\n')
