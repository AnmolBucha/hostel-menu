from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

app = Flask(__name__)
CORS(app)

# Sample dataset: Menu items with nutritional and cost info
menu_data = pd.DataFrame({
    "item": ["Rice", "Dal", "Vegetables", "Chicken", "Fish", "Milk", "Eggs", "Fruits"],
    "cost": [20, 15, 25, 50, 60, 10, 5, 30],
    "calories": [200, 150, 50, 300, 250, 120, 70, 90],
    "protein": [4, 6, 2, 30, 20, 8, 6, 1]
})

@app.route('/generate-menu', methods=['POST'])
def generate_menu():
    data = request.get_json()
    budget = float(data['budget'])
    nutritional_goals = data['nutritionalGoals']

    # Parse nutritional goals
    goals = {}
    for goal in nutritional_goals.split(","):
        nutrient, value = goal.strip().split(":")
        goals[nutrient.strip()] = float(value.strip())

    # Generate menu using Linear Programming or Heuristic Rules
    selected_items = []
    total_cost = 0
    total_nutrition = {key: 0 for key in goals}

    for _, row in menu_data.iterrows():
        if total_cost + row["cost"] <= budget:
            selected_items.append(row["item"])
            total_cost += row["cost"]
            for nutrient, value in goals.items():
                if nutrient in menu_data.columns:
                    total_nutrition[nutrient] += row[nutrient.lower()]

    return jsonify({
        "menu": selected_items,
        "total_cost": total_cost,
        "total_nutrition": total_nutrition
    })

if __name__ == '__main__':
    app.run(debug=True)
