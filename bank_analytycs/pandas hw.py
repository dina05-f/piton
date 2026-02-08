#HW 3 Pandas
# Тема: Pandas + обработка Excel-файла

import pandas as pd

# Чтение Excel-файла
df = pd.read_excel("C:/Users/User/Desktop/piton/bank_analytycs/1768191995289-sales.xlsx")
print("Исходная таблица:")
print(df)

# Доб. новый столбец total_price
df["total_price"] = df["price"] * df["quantity"]
print("\nТаблица с total_price:")
print(df)

#  Находим общую сумму продаж и среднюю цену
total_sales = df["total_price"].sum()
average_price = df["price"].mean()
print("\nОбщая сумма продаж:", total_sales)
print("Средняя цена:", average_price)

# Выводим только товары из категории Electronics
electronics = df[df["category"] == "Electronics"]
print("\nТовары из категории Electronics:")
print(electronics)

# Сох.обн.таблицу в новый файл
df.to_excel("sales_result.xlsx", index=False)
print("\nОбновлённая таблица сохранена в sales_result.xlsx")