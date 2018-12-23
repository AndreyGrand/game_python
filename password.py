pwd = input("Введите пароль: ")
bg = False
sm = False
dg= False
sb = False
ln = len(pwd)
for s in pwd:
    if s.isupper():
        bg = True
        break
for s in pwd:
    if s.islower():
        sm = True
        break
for s in pwd:
    if s.isdigit():
        dg = True
        break
smb = "!@#$%^&*"
for s in smb:
    if pwd.find(s)>-1:
        sb = True
        break
if bg == True and sm == True and dg == True and sb == True and ln>5:
    print("Хороший пароль")
else:
    print("Плохой пароль")