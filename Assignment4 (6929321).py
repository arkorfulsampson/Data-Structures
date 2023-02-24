#https://github.com/arkorfulsampson
#List of available cars and their prices
cars = {"Toyota Corolla": 22645, "Ford Explorer": 38255, "Dodge\
Challenger": 32140, "Chevrolet Equinos": 27995, "BMW X3": 46395, "Jeep \
Compass": 31590, "Lexus ES 350": 42590, "Tesla Model S": 96380, "Mercedes \
Benz GLC-Class": 44900, "Bently Bentayga": 196125, "Porsche Macan": 58950, "Jaguar \
F-PACE": 53675, "Lamborghini Urus": 225501, "Mercedes Benz EQS SUV": 105395, "Aston \
Martin DB11": 220086, "Cardiac Lyric": 61795, "Kia Sportage": 26290, "Mazda \
CX-50": 27550, "Land Rover Defender": 53500, "Buik Envision": 33400, "Land Rover \
Discovery Sport": 43300, "GMC Hummer Ev": 108700, "Toyota BZ4X": 42000, "Toyota \
Tundra": 63690, "Toyota RAV4": 37680, "Hyundai Elantra": 34000, "Honda \
Accord": 29610, "Honda CR-V": 28410, "Acura Integra": 39850, "Audi A3": 36900}
#get user input for car name
car_name = input("Enter a car_name: ")
if car_name in cars:
    print("Yes, car is available")
    car_price = cars[car_name]
    print(f"The price of {car_name} is ${car_price}") 
else: 
    print(f"Sorry, {car_name} is not available")
 