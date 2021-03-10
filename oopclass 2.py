class Vehicle:
    licensecode = ""
    serialcode = ""
    def turnonairconditioner(self):
        print("Turn on : Air")


class Cars(Vehicle):
    pass

class pickup(Vehicle):
    pass

class Van(Vehicle):
    pass

class Estatecars(Vehicle):
    pass

Car1 = Cars()
Pickup1 = pickup()
van1 = Van()
estatecar1 = Estatecars()

Car1.turnonairconditioner()
Pickup1.turnonairconditioner()
estatecar1.turnonairconditioner()
Pickup1.turnonairconditioner()


