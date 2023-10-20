L1 = input("Введите слова языка L1: ")
L1 = L1.split()
L2 = input("Введите слова языка L2: ")
L2 = L2.split()
flag = True
for i in L1:
    for j in L2:
        if len(i) > 100 or len(j) > 100:
            flag = False
if len(L1) <= 1000 and len(L2) <= 1000 and flag:
    L3 = []
    for i in L1:
        for j in L2:
            L3.append(i+j)
    print(f"Новый язык L3: {L3}")

else:
    print("Error")