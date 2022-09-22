s = "0P"
A = ["a",'b',"c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r",
     "s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0"]
B = set(A)
w = ""
for i in s:
    a= i.lower()
    if a in A or a.isnumeric():
        w+=a

if w == w[::-1]:
    print(True)
else:
    print(False)