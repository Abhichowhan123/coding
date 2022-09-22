# tic tac toe board
"""
[
    [ _ , _ , _ ],
    [ _ , _ , _ ],
    [ _ , _ , _ ]

 ]
 input user Player1,Player2
 add it in the bord
 chacking winer:-row, colum, digonal
  """
bord = [
    [ "1" , "2" , "3" ],
    [ "4" , "5" , "6" ],
    [ "7" , "8" , "9" ]
 ]
def print_bord(bord):
    for i in bord:
        for j in i:
            print(j,end="  ")
        print()
def quit(user_input):
    if user_input=="q":
        return True
    else:
        return False

while True:
    user_input = input().lower()
    if quit(user_input ):break
print_bord(bord)
