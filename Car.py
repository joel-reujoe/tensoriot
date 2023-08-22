

class Car: 


    def __init__(self, license_plate) -> None:
        self.license_plate = license_plate

    def __repr__(self):
        return f'{self.license_plate}'

    def checkSpot(self, spotNumber, parkingSlot):
        parkingStatus = parkingSlot.spot_numbers[spotNumber]['occupied']
        return parkingStatus

    def park(self, spotNumber, parkingLot):
        

        parkingStatus = self.checkSpot(spotNumber, parkingLot)

        if not parkingStatus:
            parkingLot.slots.append(self)
            parkingLot.spot_numbers[spotNumber]['occupied']= True
            parkingLot.spot_numbers[spotNumber]['vehicle'] = self.license_plate
            return True, spotNumber
        else: 
            keys = parkingLot.spot_numbers.keys()

            for key in keys:
                if not self.checkSpot(key, parkingLot):
                    parkingLot.slots.append(self)
                    parkingLot.spot_numbers[key]['occupied'] = True
                    parkingLot.spot_numbers[key]['vehicle'] = self.license_plate
                    return True, key
        
        return False, ''