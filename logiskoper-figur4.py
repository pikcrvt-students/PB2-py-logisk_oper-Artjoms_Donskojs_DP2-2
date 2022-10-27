from math import sqrt
point_x=float(input("Ievadiet x kord.:"))
point_y=float(input("Ievadiet y kord.:"))

R=sqrt(point_x**2+point_y**2)

if R>1:
    print("Punkts atrodas arpus figuras")
elif R==1:
    print("Punkts atrodas uz robezlinijas")
else:
    print("Punkts atrodas figuras ieksa")
