t = int(input())
for i in range(t):
    u = str(input())
    if (u=="B" or u=="b"):
        print("BattleShip")
    elif(u=="C" or u=="c"):
        print("Cruiser")
    elif (u == "D" or u == "d"):
        print("Destroyer")
    elif (u == "F" or u == "f"):
        print("Frigate")