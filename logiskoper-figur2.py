point_x = float(input("Ievadiet x kord.: "))
point_y = float(input("Ievadiet y kord.: "))

if point_x < -5 or point_x > 2 and point_y > 3 or point_y < -1:
    print("Punkts atrodas arpus robezas!")
elif point_x == -5 or point_x == 2 or point_y == 3 or point_y == -1:
    print("Punkts atrodas robezlinija!")
else:
    print("Punkts ir figuras ieksa!")
