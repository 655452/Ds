import Pyro4

rooms = [0, 0, 0, 0, 0]

def isRoomBooked(room_no):
    global rooms
    if rooms[room_no] == 1:
        return 1
    else:
        return 0

@Pyro4.expose
class Hotel(object):
    def bookRoom(self, room_no):
        if room_no > 5:
            return "Room number limit exceeded!!!"
        if not isRoomBooked(room_no-1):
            global rooms
            rooms[room_no-1] = 1
            return "Room No. " + str(room_no) + " is now booked for you."
        else:
            return "Room No. " + str(room_no) + " is already booked. Please select another room."

    def cancelRoom(self, room_no):
        if room_no > 5:
            return "Room number limit exceeded!!!"
        global rooms
        rooms[room_no-1] = 0
        return "Room No. " + str(room_no) + " is now vacant."

    def roomBill(self, no_of_days):
        total = 500 * no_of_days
        return "Your total bill for " + str(no_of_days) + " days is " + str(total) + "."

def main():
    daemon = Pyro4.Daemon()

    try:
        ns = Pyro4.locateNS()
    except Pyro4.errors.NamingError as e:
        print("Error locating the nameserver:", e)
        print("Make sure the Pyro4 nameserver is running.")
        return

    uri = daemon.register(Hotel)
    ns.register("example.hotel", uri)
    print("Hotel is now active.")
    daemon.requestLoop()

if __name__ == "__main__":
    main()
