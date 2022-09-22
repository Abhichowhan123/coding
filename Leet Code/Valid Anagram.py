s = "anagram"
t = "nagaram"
s = "".join(sorted(s))
t = "".join(sorted(t))
if s==t:
    print(True)
else:
    print(False)