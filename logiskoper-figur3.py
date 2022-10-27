point_x = float(input("Ievadiet x kord.: "))
point_y = float(input("Ievadiet y kord.: "))

if point_y > 0 and point_x > 0 and round(point_y*1000)/1000 > round((-1.5*point_x+3)*1000)/1000:
    print("Punkts atrodas arpus robezas!")
elif point_y == 0 or point_x == 0 or round(point_y*1000)/1000 == round((-1.5*point_x+3)*1000)/1000:
    print("Punkts atrodas robezlinija!")
else:
    print("Punkts ir figuras ieksa!")
