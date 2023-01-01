from py_edamam import Edamam

e = Edamam(nutrition_appid='c3d0e8a5', nutrition_appkey='d2af91e496fc2906ccec7c9bf0b46f40')

search_value = "12 apples"

print(f"{e.search_nutrient(search_value)['totalNutrients']['ENERC_KCAL']['quantity']} calories\nand {e.search_nutrient(search_value)['totalNutrients']['PROCNT']['quantity']}g of protein")