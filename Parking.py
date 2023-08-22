import random
class Parking:


    def __init__(self, square_foot_size, spot_size = 96) -> None:
        slots = square_foot_size//spot_size
        self.slots = []
        self.slot_size = slots
        self.spot_numbers = {}

        for i in range(slots):
            self.spot_numbers[f'Spot-{i}'] = {
                "occupied": False,
                "vehicle": ''
             }

    
    def get_spot_id(self):
        random_spot_id = random.choice((list(self.spot_numbers.keys())))
        return random_spot_id
