from datetime import date

from laptop_tech import Laptop
from mobile_tech import Mobile
from Sales_person import SalesPerson
from tech_products import Tech

phone_1 = Mobile("iphone_11", 60000, 500, 'Black', '1920-1080', 10)
phone_2 = Mobile("iphone_12", 70000, 500, 'Black', '1920-1080', 12)
phone_3 = Mobile("iphone_13", 80000, 500, 'Black', '1920-1080', 15)

laptop_1 = Laptop('Asus g14', 130000, 1.6, 'Moonlight Silver', 16, 'Ryzen 4800', 4000)
laptop_2 = Laptop('Asus g14', 180000, 1.7, 'Moonlight Silver', 64, 'Ryzen 4800', 6000)
laptop_3 = Laptop('Asus g14', 150000, 1.5, 'Moonlight Silver', 32, 'Ryzen 4800', 8000)


print(laptop_1)
print(phone_1)


phone_1.apply_discount()
print(phone_1.price)


print(Tech.get_total_products())


print(laptop_3.calculate_shipping_cost(10))


print(laptop_1.price)
laptop_1.set_double_price()
print(laptop_1.price)


print(laptop_3)
laptop_3.change_specs(32,1900)
print(laptop_3)

sale_person_1 = SalesPerson(
    'Smith', "John" , 49000 , date(2020,1,5)
)

sale_person_1.sell_product(phone_1)
sale_person_1.sell_product(phone_2)
sale_person_1.sell_product(laptop_1)
sale_person_1.sell_product(laptop_2)


print(sale_person_1.display_sales())

print(sale_person_1.calculate_commission(0.2))

sale_person_1.sort_by_price()
sale_person_1.display_sales()