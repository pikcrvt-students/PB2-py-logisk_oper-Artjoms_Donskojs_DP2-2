point_x=float(input("Ievadiet x kord.: "))
point_y=float(input("Ievadiet y kord.: "))

if point_y<1 or point_y>3 or point_x>-1 or point_y>round(2*point_x+11, 2):
    print("Punkts atrodas ārpus robežas")
elif point_y==1 or point_y==3 or point_x==-1 or point_y==round(2*point_x+11, 2):
    print("Punkts atrodas uz robežas")
else:
    print("Punkts atrodas figuras iekšā")
