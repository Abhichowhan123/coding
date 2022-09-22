A = []
a = {"2":"abc",
     "3":"def",
      "4":"ghi",
     "5":"jkl",
     "6":"mno",
     "7":"pqrs",
     "8":"tuv",
     "9":"wxyz",
     }
digits = ""

def rec(i,lenth):
     if digits == "":
          return [""]
     if len(lenth) == len(digits):
          A.append(lenth)
          return
     for j in a[digits[i]]:
          rec(i+1,lenth+j)

if digits:
     rec(0, "")
     print(A)





