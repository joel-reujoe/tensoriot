from Parking import Parking
from Car import Car
from random import randint
import json


def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def create_parking_dump(parkingSlot):
    spot_numbers = parkingSlot.spot_numbers
    with open('convert.json', 'w') as convert_file:
        convert_file.write(json.dumps(spot_numbers))

if __name__ == "__main__":
    parkingSlot = Parking(2000)

    number_of_cars = 21

    cars = []
    for i in range(number_of_cars):
        car = Car(random_with_N_digits(7))

        cars.append(car)


    for i in range(number_of_cars):
        car = cars[i]
        spotId = parkingSlot.get_spot_id()
        parkStatus, spotId = car.park(spotId, parkingSlot)
        if parkStatus:
            print(f'Car with license plate {car} parked successfully in spot {spotId}')
        else:
            print(f'Car with license plate {car} was not parked successfully')

    
    create_parking_dump(parkingSlot)