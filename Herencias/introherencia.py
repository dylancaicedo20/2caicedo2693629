class Vehicle:
    pass
class landvehicle(Vehicle):
    pass
class Trackedvehicle(landvehicle):
    pass
v=Vehicle()
lv=landvehicle()
tv=Trackedvehicle()
for cls1 in [v,lv,tv]:
    for cls2 in [Vehicle,landvehicle, Trackedvehicle]:
        print(isinstance(cls1, cls2), end="\t")
    print()