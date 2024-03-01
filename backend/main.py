from recipes import Recipes
import json

recipes = Recipes()
selected_recipes = {"selected_recipes": ["Песто омлет", "Карбонара"]}
# TODO: create def create_ignore_ingredients_list
ignore_ingredients = {"ignore_ingredients": ["соль", "вода", "перец"]}

# TODO: add def create_shopping_list (merge_ingredients_list to shopping_list + filter with ignore_ingredients_list)
ingredients_list = recipes.get_ingredients_list(selected_recipes)
with open('ingredients.json', 'w', encoding='utf-8') as f:
    json.dump(ingredients_list, f, ensure_ascii=False)

