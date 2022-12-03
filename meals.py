meals = {
    "Saturday": {
        "breakfast": ["Baked oatmeal"],
        "other": [
            "Spaghetti",
            "Grilled Chicken with Vegetables",
            "Meatloaf",
            "Biscuits and Gravy with eggs",
        ],
    },
    "Sunday": {
        "breakfast": ["Waffles with Eggs", "Pancakes with Eggs"],
        "other": [
            "Butter Chicken",
            "Potato Curry",
            "Chili",
            "Potato Soup",
            "Chicken Noodle Soup",
            "Lentils",
            "Lasagna",
        ],
    },
    "Monday": {
        "breakfast": ["Crepes with Shakshuka/Eggs"],
        "other": [
            "Fried Chicken with Fries",
            "Korean Fried Chicken",
            "Chicken Parmesean",
        ],
    },
    "Tuesday": {
        "breakfast": ["Toast with Jelly and Eggs", "Cinnamon Toast with Eggs"],
        "other": ["Tacos", "Enchiladas", "Quesadillas"],
    },
    "Wednesday": {
        "breakfast": ["Hash browns with Eggs"],
        "other": [
            "Steak with Asian Slaw",
            "Steak with Vegetables and Rolls",
            "Steak with Baked Potatoes/Sweet Potatoes/Mashed Potatoes",
        ],
    },
    "Thursday": {
        "breakfast": ["French Toast", "Biscuits with Gravy and Eggs"],
        "other": ["Pizza", "Grilled Cheese", "Burgers with Fries", "Restaurant"],
    },
    "Friday": {
        "breakfast": ["Cinnamon Rolls", "Granola with Fruit and Yogurt"],
        "other": [
            "Restaurant",
            "Popcorn, Apples, Snacks",
            "Pita Chips, Vegetables, Hummus, Feta",
        ],
    },
}

for i in range(1, 53):
    print(f"{i}")
    for day, meal_choices in meals.items():
        print(f"    {day}")
        print(
            f'      Breakfast: {meal_choices["breakfast"][i%len(meal_choices["breakfast"])]}'
        )
        print(f'      Lunch: {meal_choices["other"][i%len(meal_choices["other"])]}')
