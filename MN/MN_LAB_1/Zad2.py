dane = []
with open("wezly_2.txt",'r') as f:
    for wezel in f:
        wezel = wezel.strip()
        dane.append([float(wezel.split(" ")[0]),float(wezel.split(" ")[1])])

l_pkt = len(dane)




def wielomian_l(i,val):
    result = 1
    for j in range(0,l_pkt):
        if j == i:
            continue
        result *= ((val-dane[j][0])/(dane[i][0]-dane[j][0]))
    return result

def suma_wielomianow(val):
    result = 0
    for i in range(0,l_pkt):
        result += (dane[i][1] * wielomian_l(i,val))
    return result

val = float(input("Wpisz liczbe: "))

output = suma_wielomianow(val)

print(f"Liczba węzłów: {l_pkt}")
print("Dane:")
for i in range(0,l_pkt):
    print(f"x{i}: {dane[i][0]} = {dane[i][1]}")
print(f"Puknt w ktorym liczylismy wartosc wielomianu: {val}")
print(f"Wartosc wielomianu Lagrange'a w punkcie {val}: {output}")