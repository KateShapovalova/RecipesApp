import json


class Recipes:
    def __init__(self):
        with open("recipes.json", "r", encoding='utf-8') as f:
            self.recipes = json.load(f)

    def get_ingredients_list(self, selected_recipes):
        ingredients_list = []
        for recipe in self.recipes["recipes"]:
            if recipe["dish_name"] in selected_recipes["selected_recipes"]:
                ingredients_list.append(recipe["ingredients"])
        return ingredients_list

    def add_recipe(self):
        '''
        input: recipes.json
        загрузить recipes.json в SQLite DB "Recipes.db"
        :return: void
        '''
        pass
