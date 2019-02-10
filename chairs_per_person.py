f = open("reservations.csv")

for reservation in f:
    name, number = reservation.split(",")
    chairs_per_person = 50 / int(number)
    print("{} will get {} chairs per person".format(name, chairs_per_person))
