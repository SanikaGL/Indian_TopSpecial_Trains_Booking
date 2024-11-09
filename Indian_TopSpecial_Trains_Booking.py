class Train:
    def __init__(self, train_name, seats, fare, class_type, departure_time, arrival_time):
        self.train_name = train_name
        self.seats = seats
        self.fare = fare
        self.class_type = class_type  # e.g., Sleep,Ac
        self.departure_time = departure_time  
        self.arrival_time = arrival_time    
        self.booked_seats = 0

    def book_ticket(self,numberofseats):
            self.seats -= numberofseats
            self.booked_seats += numberofseats
            

    def get_status(self):
        print(f"Train: {self.train_name}")
        print(f"Class: {self.class_type}")
        print(f"Departure Time: {self.departure_time}")
        print(f"Arrival Time: {self.arrival_time}")
        print(f"Total Seats: {self.seats + self.booked_seats}")
        print(f"Booked Seats: {self.booked_seats}")
        print(f"Available Seats: {self.seats}")

    def get_fare_info(self):
        print(f"The fare for {self.train_name} ({self.class_type}) is: ₹{self.fare}")
def book_train(train_number,numberofseats):#this fuction is called inside book function which checks all condition and process booking
    if train_number in trains:
        if numberofseats<=trains[train_number].seats and trains[train_number].seats!=0 and numberofseats <= trains[train_number].seats+trains[train_number].booked_seats and numberofseats!=0:
            trains[train_number].book_ticket(numberofseats)
            print(f"{numberofseats} ticket booked successfully on train {trains[train_number].train_name} ")
            print(f"remaining seats are {trains[train_number].seats}")
        else:
            if trains[train_number].seats ==0:
                print(f"Sorry ,there is no more seats to book on train {trains[train_number].train_name} ");
            elif numberofseats > trains[train_number].seats+trains[train_number].booked_seats:
                print("Unfortunately the requested number of seats are unavailable.\n please select a valid number of seats and try again ")
            elif numberofseats==0:
                print("Booking zero seats is not permitted.\n please enetr a valid number of seats and proceed with your booking")
            elif numberofseats > trains[train_number].seats:
                print("Unfortunately the requested number of seats are unavailable.\n please select a valid number of seats and try again ")
    else:
        print("Train not found.")
        print("please provide a valid train number and book again")
def book(): #to book a seats by taking user input and then calling book_train function by passing the user input as parameters
    train_number = int(input("enter the train number"))
    print(f"the deatails of the train {trains[train_number].train_name} :")
    trains[train_number].get_status()
    trains[train_number].get_fare_info()
    numberofseats = int(input("how many seats u wanna book"));
    print("processing....")
    book_train(train_number,numberofseats)        
trains = {
    12345: Train("Vande Bharat Express", 100, 2000, "AC", "06:00 AM", "12:00 PM"),
    54321: Train("Rajdhani Express", 120, 1500, "Sleeper", "05:00 PM", "08:00 AM"),
    34566: Train("Maharaja's Express", 120, 1500, "Sleeper", "05:00 PM", "08:00 AM"),
    23451: Train("Gatimaan Express", 120, 1500, "Sleeper", "05:00 PM", "08:00 AM"),
    56723: Train("Tejas Express", 120, 1500, "Sleeper", "05:00 PM", "08:00 AM"),
    17452: Train("Royal Rajasthan on Wheels", 120, 1500, "Sleeper", "05:00 PM", "08:00 AM"),
    12344: Train("Shatabdi Express", 120, 1500, "Sleeper", "05:00 PM", "08:00 AM"),
    19257: Train("The Deccan Odyssey", 120, 1500, "Sleeper", "05:00 PM", "08:00 AM"),
    31567: Train("Palace on Wheels", 120, 1500, "Sleeper", "05:00 PM", "08:00 AM"),
    23457: Train("Golden Chariot", 120, 1500, "Sleeper", "05:00 PM", "08:00 AM")
}

#Displaying train numbers and corresponding train names
print("Available Trains:")
for train_number, train_obj in trains.items():
    print(f"Train Number: {train_number} - Train Name: {train_obj.train_name}")
print("Do u wanna chech details of any train ? ")# to check the details of the desired train
y = input(" yes/no : ")
if y == "yes":
    train_number = int(input("enetr the train number:"))
    print(f"\nDetails for Train Number: {train_number}")
    if train_number in trains:
        trains[train_number].get_status()
    else:
        print("Train not found.")
elif y == "no":
    print("no problem,thank you")

print("-------Book a train here-------");
y = input("do u want book a ticket (yes/no) : ").lower()
if y=="yes":
    book()
elif y == "no":
    print("Thank u for using our service , have a great day");
else:
    print("give proper choice");
print("\n")
while True: #allowing user to book as many trains as they want by using loop
    anothertrain = input("Do you want to continue booking tickets?(yes/no) : ");
    if anothertrain!="yes": #user can continue booking until they choose no
        print("ok thank you")
        break
    else:
        book()
        print("\n")
        
    
                       
                       

    

    
    
