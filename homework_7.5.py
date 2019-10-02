# def compare_prices(cars : dict, cars1: dict):
#     result = [True for summ in cars if ]
#
#     print(cars, cars1)

#
# compare_prices({'BMW': 20000, 'Nissan': 15000}, {'Mustang': 30000, 'Renault': 5000})

a = ({'BMW': 20000, 'Nissan': 15000}, {'Mustang': 30000, 'Renault': 5000})
b = []

for element in a:
    for key, value in element:
        b.append(value)



print(b)
