# STRUCTURING DATA AND CLASSES


# ==========================================================================================
# ==========================================================================================


# carID = ["car_1", "car_2", "car_3", "car_4", "car_5", "car_6"]
# year = ["1975", "1980", "2018", "2015", "1965", "2017"]
# make = ["Ford", "Chevy", "BMW", "Toyota", "Chevy", "Chevy"]
# model = ["Mustang", "S-10", "325i", "Tacoma", "Camaro", "Suburban"]
# miles = ["12,300", "85,000", "60,000", "55,000", "68,000", "96,000"]
# price = ["45,000", "15,000", "20,000", "28,000", "43,000", "22,000"]

# print()
# print(make[0], model[0])
# print(make[1], model[1])
# print(make[2], model[2])
# print(make[3], model[3])
# print(make[4], model[4])
# print(make[5], model[5])
# print()


# ==========================================================================================
# ==========================================================================================


import json


with open ("Code_Review.json") as data:
    json_data = data.read()
json_dict = json.loads(json_data)

# print(json.dumps(json_dict, indent = 4))

for car_values in json_dict.values():
    if int(car_values["Price"].replace(",","")) <= 30000 and car_values["Make"] == "Chevy":
        print(f'{car_values["ID"]} {car_values["Year"]} {car_values["Make"]} {car_values["Model"]} {car_values["Miles"]} {car_values["Price"]}')

    # print(int(car_values["Price"].replace(",","")))

# ==========================================================================================
# ==========================================================================================


# class Car:

#     def __init__(self, year, make, model, miles, price):
#         self.year = year
#         self.make = make
#         self.model = model
#         self.miles = miles
#         self.price = price

#     def getdesc(self):
#         desc = f'Year                :{self.year}\n'\
#                f'Make                :{self.make}\n'\
#                f'Model               :{self.model}\n'\
#                f'Miles               :{self.miles}\n'\
#                f'Price               :{self.price}'
#         return desc

# car_1 = ['1975', 'Ford', 'Mustang', '12,300', '45,000']
# car_2 = ['1980', 'Chevy', 'S-10', '85,000', '15,000']
# car_3 = ['2018', 'BMW', '325i', '60,000', '20,000']
# car_4 = ['2015', 'Toyota', 'Tacoma', '55,000', '28,000']
# car_5 = ['1965', 'Chevy', 'Camaro', '68,000', '43,000']
# car_6 = ['2017', 'Chevy', 'Suburban', '96,000', '22,000']

# print (f'Car_1\n', car_1.getdesc(), '\n', sep='')
# print (f'Car_2\n', car_2.getdesc(), '\n', sep='')
# print (f'Car_3\n', car_3.getdesc(), '\n', sep='')
# print (f'Car_4\n', car_4.getdesc(), '\n', sep='')
# print (f'Car_5\n', car_5.getdesc(), '\n', sep='')
# print (f'Car_6\n', car_6.getdesc(), sep='')