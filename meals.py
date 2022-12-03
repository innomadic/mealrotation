'''
Prepares a 52 week meal plan, rotating through lists of meals for each day.

`python3 meals.py > plan.md`
'''
meals = {
    "Saturday": {
        "breakfast": ["Baked Oatmeal"],
        "lunch": [
            "Spaghetti",
            "Grilled Chicken with Vegetables",
            "Meatloaf",
            "Biscuits and Gravy with eggs",
        ],
        'dinner': ['Leftovers']
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
        ],
        'dinner': ['Leftovers']
    },
    "Monday": {
        "breakfast": ["Crepes with Shakshuka/Eggs"],
        "lunch": [
            "Fried Chicken with Fries",
            "Korean Fried Chicken",
            "Chicken Parmesean",
        ],
        'dinner': ['Leftovers']
    },
    "Tuesday": {
        "breakfast": ["Toast with Jelly and Eggs", "Cinnamon Toast with Eggs"],
        "lunch": ["Tacos", "Enchiladas", "Quesadillas"],
        'dinner': ['Leftovers'],
    },
    "Wednesday": {
        "breakfast": ["Hash browns with Eggs"],
        "lunch": [
            "Steak with Asian Slaw",
            "Steak with Vegetables and Rolls",
            "Steak with Baked Potatoes/Sweet Potatoes/Mashed Potatoes",
        ],
        'dinner': ['Leftovers']
    },
    "Thursday": {
        "breakfast": ["French Toast", "Biscuits with Gravy and Eggs"],
        "lunch": ["Pizza", "Grilled Cheese", "Burgers with Fries", "Restaurant"],
        'dinner': ['Leftovers']
    },
    "Friday": {
        "breakfast": ["Cinnamon Rolls", "Granola with Fruit and Yogurt"],
        "lunch": [
            "Restaurant",
            "Popcorn, Apples, Snacks",
            "Pita Chips, Vegetables, Hummus, Feta",
        ],
        'dinner': ['Leftovers']
    },
}

for i in range(1, 53):
    print(f"# Week {i}")
    for day, meal_choices in meals.items():
        print(f"## {day}")
        print(
            f'* Breakfast: {meal_choices["breakfast"][i%len(meal_choices["breakfast"])]}'
        )
        print(f'* Lunch: {meal_choices["lunch"][i%len(meal_choices["lunch"])]}')
        print(f'* Dinner: {meal_choices["dinner"][i%len(meal_choices["dinner"])]}')
