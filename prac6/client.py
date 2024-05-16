# python -m Pyro4.naming
import Pyro4

Hotel = Pyro4.Proxy("PYRONAME:example.hotel")

def menu():
    print("===================")
    print("1. Book Room")
    print("2. Cancel Room")
    print("3. Total Bill")
    print("4. Exit")
    x = int(input("Enter Your choice: "))
    return x

def get_room_no():
    return int(input("Enter the room no."))

def get_no_of_days():
    return int(input("Enter the total no of days."))

x = menu()
while x != 4:
    if x == 1:
        rno = int(get_room_no())
        print(Hotel.bookRoom(rno))
    elif x == 2:
        room_no = get_room_no()
        print(Hotel.cancelRoom(room_no))
    elif x == 3:
        no_of_days = get_no_of_days()
        print(Hotel.roomBill(no_of_days))
    elif x == 4:
        exit() 
    x = menu()
