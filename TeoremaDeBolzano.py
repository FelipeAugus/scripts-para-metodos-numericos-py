import matplotlib.pyplot as plt
import math

expoentes = 3  # x^0 x^1 x^2 x^3
# constantes = [3, -9, 0, 1]
constantes = [0.407, 0.077, 0.015]

print("I. Função: ")
# for x in range(exponentes):
#     print("Valor de X^", x, ": ", end="")
#     aux = int(input())
#     constantes.append(aux)
#print("")
for x in range(len(constantes)):
    print("+ (",constantes[x], "*X^",x,") ",end="")

print("\nII. INTERVALOS")
# a = int(input("\nIntervalo, A: "))
# b = int(input("Intervalo, B: "))
a = 1
b = 8
print("A: ", a, " B: ", b)

PosAnt = 0
SinAnt = 0    # > 0 < 
p = 0
intervalos = []
Ax = []
By = []
print("III. Efetuando cálculos.. Delta X = 0.0001")
for x in range(a, b+1):
    Fx = 0
    for e in range(expoentes): # 0 a 3
        Fx += constantes[e]*x**e          # x[0]^0 // x[1]^1 // x[2]^2 // x[3]^3
    if(not p): # se p = 0, primeiro loop 
        p=1
        PosAnt = x
        SinAnt = Fx
    else:   # senao, se outros loops
        if((SinAnt > 0 and Fx < 0) or (SinAnt < 0 and Fx > 0) or Fx == 0):
            intervalos.append([PosAnt, x])

    PosAnt = x
    SinAnt = Fx
    By.append(Fx)
    Ax.append(x)

ax = []
by = []
while(a != b+0.0001):
    Fx = 0
    for e in range(expoentes): # 0 a 3
        Fx += constantes[e]*a**e          # x[0]^0 // x[1]^1 // x[2]^2 // x[3]^3

    a += 0.0001
    a = float(format(a, '.4f'))
    
    by.append(Fx)
    ax.append(a)

print("IV. Plotando Gráfico...")
fig, (graf) = plt.subplots(nrows=1)
graf.plot(ax, by)
# remover linha a extrema direita e topo
graf.spines['top'].set_color('none')
graf.spines['right'].set_color('none')
# centralizar zeros
graf.spines['bottom'].set_position('zero')
graf.spines['left'].set_position('zero')
plt.grid(True)
plt.show()

print("V. Intervalos: \n", intervalos)
Y = By
X = Ax

print("VI. Sinais de acordo com valor de X: \n")
for x in X:
    print("|",x, "\t|", end="")
print("") 
for y in Y:
    if(y>0):print("|  +\t|", end="")
    else:print("|  -\t|", end="")
print("")

print("\n", 100*"-")
