def ticket_booking():
    total_seats = 10
    booked = 0
    while True:
        print(f"\nAvailable seats: {total_seats - booked}")
        print("1. Book Ticket\n2. Exit")
        if input("Choice: ") == '1':
            if booked < total_seats:
                booked += 1
                print("Ticket booked successfully!")
            else:
                print("House Full!")
        else:
            break
if __name__ == '__main__':
    ticket_booking()
