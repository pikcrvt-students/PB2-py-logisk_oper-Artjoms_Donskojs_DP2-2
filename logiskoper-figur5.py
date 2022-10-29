point_x = float(input("Ievadiet x kord.:"))
point_y = float(input("Ievadiet x kord.:"))

R=round((point_x + 2)**2 + (point_y - 2)**2,2)
sum = point_x + 5

if R>1 or point_y > sum:
    print("Punkts atrodas arpus figuras.")
elif R==1 or point_y == sum:
    print("Punkts atrodas uz robezlinijas.")
else:
    print("Punkts atrodas figuras ieksa.")
