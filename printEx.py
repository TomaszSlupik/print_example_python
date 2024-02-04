# Użyj podanych zmiennych oraz formatowania zmiennoprzecinkowego z odpowiednią składnią, 
experiment_name = 'The Effects of Temperature on Enzyme Activity'
treatment_group = 'Group A'
enzyme_activity = 12.3456
enzyme_activity_round  = f"{enzyme_activity :.2f}"

print(f"Welcome to {experiment_name}!")
print("")
print(f"The {treatment_group} enzyme activity level is {enzyme_activity_round} units.")

print('---')

# W cudzysłowie
person_name = 'Albert Einstein'
quote = 'Imagination is more important than knowledge.'

message = f'{person_name} once said, \'{quote}\''
print(message)

print('---')

# tabelka z owocami i cenami
item1 = 'Apples'
resultOne = " " * (15 - len(item1))
quantity1 = 5
quantity1One = " " * (15 - 1)
price1 = 1.50
price1One = " " * (15 - 5)

item2 = 'Bananas'
reultTwo = " " * (15 - len(item2))
quantity2 = 7
quantity2Two = " " * (15 - 1)
price2 = 0.99

item3 = 'Oranges'
reultThree = " " * (15 - len(item3))
quantity3 = 4
quantity3Three = " " * (15 - 1)
price3 = 2.25


print(f"|{'-' * 15}|{'-' * 15}|{'-' * 15}|")
print(f"|{item1}{resultOne}|{quantity1}{quantity1One}|${price1 :.2f}{price1One}|")
print(f"|{item2}{reultTwo}|{quantity2}{quantity2Two}|${price2 :.2f}{price1One}|")
print(f"|{item3}{reultThree}|{quantity3}{quantity3Three}|${price3 :.2f}{price1One}|")

print('---')

# Dodanie Item, Quantity, Price      
item = 'Item'
resultItem= " " * (15 - len(item))
quantity = 'Quantity'
resultQuantity= " " * (15 - len(quantity))
price = 'Price'
resultPrice= " " * (15 - len(price))

print(f"|{'-' * 15}|{'-' * 15}|{'-' * 15}|")
print(f"|{item}{resultItem}|{quantity}{resultQuantity}|{price}{resultPrice}|")
print(f"|{'-' * 15}|{'-' * 15}|{'-' * 15}|")
print(f"|{item1}{resultOne}|{quantity1}{quantity1One}|${price1 :.2f}{price1One}|")
print(f"|{item2}{reultTwo}|{quantity2}{quantity2Two}|${price2 :.2f}{price1One}|")
print(f"|{item3}{reultThree}|{quantity3}{quantity3Three}|${price3 :.2f}{price1One}|")

print('---')

# Utworzenie skryptu do obsługi prostego sklepu internetowego: wcięcia itp. 

print("=" * 50)
print("> Main Menu")
print("=" * 50)
print("\t1. View all products")
print("\t2. Search for a product")
print("\t3. Add a new product")
print("\t5. Delete a products")
print("\t7. Checkout")
print("\t8. Exit")