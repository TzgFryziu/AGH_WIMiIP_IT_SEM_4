def f1(x):
    return -(x**3)+10*x+5
def df1(x):
    return -3*(x**2)+10


def f2(x):
    return x**5 - 10*x**4
def df2(x):
    return 5*(x**4) - 40*(x**3)



def styczne(x0,funkcja,pochodna, epsilon, max_iteracji):
    styczne_rozwiazania = [(x0,funkcja(x0)),]
    iteracje = 0
    for i in range(max_iteracji):
        x = styczne_rozwiazania[i][0] - funkcja(styczne_rozwiazania[i][0])/pochodna(styczne_rozwiazania[i][0])
        if abs(funkcja(x)) < epsilon:
            styczne_rozwiazania.append((x,funkcja(x)))
            iteracje+=1
            break
        iteracje+=1
        styczne_rozwiazania.append((x,funkcja(x)))
        
    return styczne_rozwiazania,iteracje


def sieczne(x0,x1,funkcja,epsilon,max_iteracji):
    sieczne_rozwiazania = [(x0,funkcja(x0)),(x1,funkcja(x1))]
    iteracje = 0
    for i in range(max_iteracji):
        x = sieczne_rozwiazania[i+1][0] - (funkcja(sieczne_rozwiazania[i+1][0])*(sieczne_rozwiazania[i+1][0]-sieczne_rozwiazania[i][0]))/(funkcja(sieczne_rozwiazania[i+1][0])-funkcja(sieczne_rozwiazania[i][0]))
        if abs(funkcja(x)) < epsilon:
            sieczne_rozwiazania.append((x,funkcja(x)))
            iteracje+=1
            break
        iteracje+=1
        sieczne_rozwiazania.append((x,funkcja(x)))
        
    return sieczne_rozwiazania,iteracje


print("Rozwiązania metodą stycznych dla funkcji -x^3 + 10x + 5: ")
rozwiazania,iteracje = styczne(6,f1,df1,0.00001,100)
for i in range(len(rozwiazania)):
    print(f"x{i} = {rozwiazania[i][0]} = {rozwiazania[i][1]} , iteracja: {i}")
print(f"Liczba iteracji: {iteracje}")

print("Rozwiązania metodą stycznych dla funkcji x^5 - 10x^4: ")
rozwiazania,iteracje = styczne(1,f2,df2,0.00001,100)
for i in range(len(rozwiazania)):
    print(f"x{i} = {rozwiazania[i][0]} = {rozwiazania[i][1]} , iteracja: {i}")
print(f"Liczba iteracji: {iteracje}")

print("Rozwiązania metodą siecznych dla funkcji -x^3 + 10x + 5: ")
rozwiazania,iteracje = sieczne(6,5,f1,0.00001,100)
for i in range(len(rozwiazania)):
    print(f"x{i} = {rozwiazania[i][0]} = {rozwiazania[i][1]} , iteracja: {i}")
print(f"Liczba iteracji: {iteracje}")

print("Rozwiązania metodą siecznych dla funkcji x^5 - 10x^4: ")
rozwiazania,iteracje = sieczne(1,2,f2,0.00001,100)
for i in range(len(rozwiazania)):
    print(f"x{i} = {rozwiazania[i][0]} = {rozwiazania[i][1]} , iteracja: {i}")
print(f"Liczba iteracji: {iteracje}")