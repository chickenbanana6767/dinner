import random

snacks = [
    "Takis",
    "yogurt",
    "almonds dipt yougurt",
    "PB&J dip",
    "dried mango",
    "cookies"
]

dinners = [
    "tacos",
    "pasta",
    "chicken and rice",
    "steak and potatoes",
    "fried rice",
    "salmon and noodles",
    "BBQ chicken",
    "chicken and potatoes",
    "beef and broccoli",
    "burger",
    "teriyaki chicken",
]

days = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Friday",
    "Saturday",
    "Sunday"
]

ingredients = {
    "tacos": ["tortillas/shells", "ground beef", "lettuce", "tomatoes", "salsa"],
    "pasta": ["pasta", "tomato sauce", "ground beef"],
    "chicken and rice": ["chicken", "rice", "broccoli"],
    "steak and potatoes": ["steak", "potatoes", "green beans"],
    "fried rice": ["rice", "eggs", "peas", "carrots", "soy sauce"],
    "salmon and noodles": ["salmon", "noodles", "broccoli", "soy sauce"],
    "BBQ chicken": ["chicken", "BBQ sauce", "corn"],
    "chicken and potatoes": ["chicken", "potatoes", "carrots"],
    "beef and broccoli": ["beef", "broccoli", "rice", "soy sauce"],
    "burger": ["burger patties", "burger buns", "lettuce", "tomatoes"],
    "teriyaki chicken": ["chicken", "rice", "teriyaki sauce", "broccoli"],
}

random.shuffle(dinners)

grocery_list = []

print("DINNER PLAN")
print("-----------")

for day in days:
    dinner = dinners.pop()

    print(day + ": " + dinner)

    for item in ingredients[dinner]:
        if item not in grocery_list:
            grocery_list.append(item)

print()
print("GROCERY LIST")
print("------------")

for item in grocery_list:
    print("- " + item)

print()
print("SNACK LIST")
print("----------")

random.shuffle(snacks)

for i in range(3):
    print("- " + snacks.pop())
