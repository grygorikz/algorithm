products = {
    "яблоко": 100,
    "банан": 120
}

products["апельсин"] = 150

products["яблоко"] = 110

del products["банан"]

name = "яблоко"
print(products.get(name, "Нет товара"))