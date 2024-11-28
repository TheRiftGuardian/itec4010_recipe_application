from enum import Enum

# Enumerators for additional recipe details:
class DietaryChoice(Enum):
    LOW_CARB = "low_carb"
    HIGH_PROTEIN = "high_protein"
    PLANT_BASED = "plant_based"
    DAIRY_FREE = "dairy_free"
    EVERYTHING = "everything"

class TimeSpent(Enum):
    QUICK = "Quick Bites (0–15 minutes)"
    SIMPLE = "Simple Meals (15–30 minutes)"
    BALANCED = "Balanced Dinners (30–45 minutes)"
    MEAL_PREP = "Meal Prep Sessions (45 minutes–1 hour)"
    SPECIAL_OCCASION = "Special Occasion Meals (1 hour +)"

class MealCost(Enum):
    SUPER_BUDGET = "Super Budget-Friendly ($0–$5 per serving)"
    AFFORDABLE = "Affordable Eats ($5–$10 per serving)"
    MODERATE = "Moderate Cost ($10–$15 per serving)"
    SPLURGE = "Splurge Meals ($15+ per serving)"

class MealTime(Enum):
    BREAKFAST = "breakfast"
    LUNCH = "lunch"
    DINNER = "dinner"
    SNACK = "snack"



