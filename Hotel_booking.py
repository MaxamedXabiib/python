from datetime import date
class Hotel:
   def __init__(self):
        self.rooms = {}
        self.available_rooms = {'Damal': [103, 104, 105],'Crown': [203, 204, 205],'Dhoolayare': [407, 408, 409]}
        self.roomprice = {1:2000, 2:4000, 3:5000}

Hotel = ["1) Damal Hotel", "2) Crown Hotel", "3) Dhoolayare"]

while True:
    print("1) Damel Hotel")
    print("2) Crown Hotel")
    print("3) Dhoolayare Hotel")
    print("4) Exit")


    elif choose == '2':
        print("you booking Crown Hotel,thank you for booking")
        print("1) rooms")
        print("2) look up")
        print("3) Exit")
        choosen = input("Enter your choisen: ")
        if choosen == '1':
            room_no = int(input("Enter your room No: "))
        elif choosen == '2':
            input("look up your booking")
        elif choosen == '3':
            break
    elif choose == '3':
        print("you booking Dhoolayare Hotel,thank you for booking")
        print("1) rooms")
        print("2) look up")
        print("3) Exit")
        choosen = input("Enter your choisen: ")
        if choosen == '1':
            room_no = int(input("Enter your room No: "))
        elif choosen == '2':
            input("look up your booking")
        elif choosen == '3':
            break
    elif choose == '4':
        break
    else:
        print("Invalid Choosen!")
        break
