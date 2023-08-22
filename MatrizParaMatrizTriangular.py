def setPivo(mat, L):
    for c in range(len(mat)): 
        if(mat[L][c] != 0): 
            return [L, c]

def triang(mat):
    # Converte uma matriz quadrada qualquer para triangular inferior
    for L in range(len(mat)):   
        pivo = setPivo(mat, L) 
        #if (L!=len(mat)-1):
        for l in range(L+1, len(mat)):
            det = (mat[l][pivo[1]] / mat[pivo[0]][pivo[1]])     
            for c in range(len(mat)): 
                mat[l][c] -= mat[pivo[0]][c]*det 
           
    return mat

ij = int(input('Tamanho da matriz: '))
Mat = []

for i in range(ij):
    Mat.append([])
    for j in range(ij):
        Mat[i].append(int(input('Valor na posição '+str(i+1)+' '+str(j+1)+': ')))

print('Matriz:')
for i in range(ij):
    print(Mat[i])

print('\nTriangular: ')
triang(Mat)
for i in range(ij):
    print(Mat[i])
