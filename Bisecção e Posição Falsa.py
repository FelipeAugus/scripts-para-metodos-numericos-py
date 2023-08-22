import matplotlib.pyplot as plt
import math

expoentes = 4  # x^0 x^1 x^2 x^3

print("I. Função: ")
# for x in range(exponentes):
#     print("Valor de X^", x, ": ", end="")
#     aux = int(input())
#     constantes.append(aux)
#print("")
constantes = [3, -9, 0, 1]
for x in range(len(constantes)):
    print("+ (",constantes[x], "*X^",x,") ",end="")

print("\nII. INTERVALOS")
# a = int(input("\nIntervalo, A: "))
# b = int(input("Intervalo, B: "))
a = -5
b = 5
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
plt.show()  # PLOTAR GRÁFICO

print("V. Intervalos: \n", intervalos)
Y = By
X = Ax

print("VI. Sinais de acordo com valor de X: \n")
for x in range(len(X)):
    print("|",X[x], "\t|", end="")
    if(Y[x]>0):print("|  +\t|", end="")
    else:print("|  -\t|", end="")
    if((x+1)%10==0): print("")    
print("")

print("\nEtapa 2 ", 100*"-")

def plotGraf(lx, ly):
    fig, (graf) = plt.subplots(nrows=1)
    graf.plot(ax, by)
    plt.plot(lx, ly)
    # remover linha a extrema direita e topo
    graf.spines['top'].set_color('none')
    graf.spines['right'].set_color('none')
    # centralizar zeros
    graf.spines['bottom'].set_position('zero')
    graf.spines['left'].set_position('zero')
    plt.grid(True)
    plt.show()

def f(x):
    F = 0
    for e in range(expoentes): # 0 a 3
            F += constantes[e]*x**e 
    return F

print("\n", 100*"-")
print("I. MÉTODO BISECÇÃO")
e = 0.001
print("II. ERRO CONFIGURADO: ", e)
for j in intervalos:
    vezes = 0
    i = [j[0], j[1]]
    while(True):
        vezes+=1
        X = (i[0]+i[1])/2
        
        fA = f(i[0])
        fB = f(i[1])
        fX = f(X)
        if(math.fabs(fX)<=e): break
        if((fX>0 and fA>0) or (fX<0 and fA<0)):
            i[0] = X  # a = x
        elif((fX>0 and fB>0) or (fX<0 and fB<0)):
            i[1] = X  # b = x
        
        plotGraf([i[0], i[1]], [10,10])
            
            
    print("\nINTERVALO: ", j,"// Raiz: ", X, "\tResultado f(X) = ", fX, "\tObtido após ", vezes, " vezes")

print("\n", 100*"-")
print("\n-->III. Quando { |f(X)| <= e } o algoritimo para. Isto é, se o resultado da função do X for menor que o erro definido então ele sai do loop e considera esse X como uma raiz aceitavél para o intervalo.")
print("\n", 100*"-")
print("IV. MÉTODO DA POSIÇÃO FALSA")

def fx(a, b):
    x = ( (a*f(b) )-( b*f(a) ))/(f(b) - f(a))
    return x

for j in intervalos:
    vezes = 0
    i = [j[0], j[1]]
    while(True):
        vezes+=1
        X = fx(i[0], i[1])
        
        fA = f(i[0])
        fB = f(i[1])
        fX = f(X)
        if(math.fabs(fX)<=e): break
        if((fX>0 and fA>0) or (fX<0 and fA<0)):
            i[0] = X  # a = x
        elif((fX>0 and fB>0) or (fX<0 and fB<0)):
            i[1] = X  # b = x
        plotGraf([i[0], i[1]], [f(i[0]), f(i[1])])
      
    print("\nINTERVALO: ", j,"// Raiz: ", X, "\tResultado f(X) = ", fX, "\tObtido após ", vezes, " vezes")
