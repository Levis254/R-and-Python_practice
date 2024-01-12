class flight():
    def __init__(self,capacity):
        self.capacity=capacity
        self.names=[]
    def add_passenger (self,name):
        self.names.append(name)
    
    def remaining_seat(self):
        if len(self.names)>self.capacity:
            print("the plane is overloaded")
        elif len(self.names)==self.capacity:
            print("the plane is full") 
        while len(self.names)<self.capacity:
            print(f"there are {self.capacity-len(self.names)} spaces") 

people=["Harry", "Ron", "Hermione", "Ginny"]


flight1=flight(4)


for person in people:
    flight1.add_passenger(person)

flight1.remaining_seat()