class flight():

    def __init__(self, capacity):
        self.capacity=capacity
        self.passenger=[]
        

    def add_passenger(self, name):
        if self.open_seats()==0:
            return False
        self.passenger.append(name)
        return True

    def open_seats(self):
        self.openseats=self.capacity-len(self.passenger)
        return self.openseats












names=["Winnie","Kennito", "Damito", "Lavin"]

boeng1=flight(3) 


for name in names:
    boeng1.add_passenger(name)
    if boeng1.open_seats()==0:
        print ("The plane is full")
    else: 
        print(f"There are {boeng1.open_seats()}, remaining seats")
    


