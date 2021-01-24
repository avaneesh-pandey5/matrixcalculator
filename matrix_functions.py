#----------INPUT MATRIX------------

def input_matrix():
    matrix=[]
    col=[]
    no_of_row=int(input('Enter no. of rows :: '))
    no_of_col=int(input('Enter no. of Columns :: '))
    
    for ir in range (1,no_of_row+1):
        for ic in range(1,no_of_col+1):
            print('Enter value of a',ir,ic)
            val=int(input())
            col.append(val)
        matrix.append(col)
        col=[]
    
    return no_of_row, no_of_col, matrix

#-----------ADDITION------------------

def addition_of_matrix(matrixA,matrixB):
    addition_matrix=[]
    addition_col=[]
    no_of_rowA=len(matrixA)
    no_of_colA=len(matrixA[0])
    no_of_rowB=len(matrixB)
    no_of_colB=len(matrixB[0])
    
    if no_of_rowA == no_of_rowB and no_of_colA == no_of_colB:
        for r in range (no_of_rowA):
            for c in range(no_of_colA):
                val=matrixA[r][c] + matrixB[r][c]
                addition_col.append(val)
            addition_matrix.append(addition_col)
            addition_col=[]
        
    return addition_matrix

#--------------SUBTRACTION---------------

def subtraction_of_matrix(matrixA,matrixB):
    subtraction_matrix=[]
    subtraction_col=[]
    no_of_rowA=len(matrixA)
    no_of_colA=len(matrixA[0])
    no_of_rowB=len(matrixB)
    no_of_colB=len(matrixB[0])
    
    if no_of_rowA == no_of_rowB and no_of_colA == no_of_colB:
        for r in range (no_of_rowA):
            for c in range(no_of_colA):
                val=matrixA[r][c] - matrixB[r][c]
                subtraction_col.append(val)
            subtraction_matrix.append(subtraction_col)
            subtraction_col=[]
        
    return subtraction_matrix

#---------------PRODUCT---------------

def product_of_matrix(matrixA,matrixB):
    product_matrix=[]
    product_col=[]
    no_of_rowA=len(matrixA)
    no_of_colA=len(matrixA[0])
    no_of_rowB=len(matrixB)
    no_of_colB=len(matrixB[0])
    
    val=0
    for i in range(no_of_rowA):
        for j in range(no_of_colB):
            for k in range(no_of_colA):
                val=val+(matrixA[i][k]*matrixB[k][j])
            product_col.append(val)
            val=0
        product_matrix.append(product_col)
        product_col=[]
        
    return product_matrix


#------------ADJOINT OF MATRIX-------------

def adjoint_matrix(matrix):
    cofac=cofactor_matrix(matrix)
    adjoint=transpose(cofac)
    return adjoint
    

#------------INVERSE OF A MATRIX-------------

def reduce_for_inverse(minor,i,j):
    row_len=len(minor)
    for k in range(row_len):
        del minor[k][j]
    del minor[i]
    return minor

def inverse_of_matrix(matrix):
    row_inverse=[]
    inverse_matrix=[]
    determinant=main_determinant(matrix)
    adjoint=adjoint_matrix(matrix)
    for i in adjoint:
        for v in i:
            inverse=v/determinant
            inverse=round(inverse,3)
            row_inverse.append(inverse)
        inverse_matrix.append(row_inverse)
        row_inverse=[]
    return inverse_matrix

#------------COFACTOR OF MATRIX------------

def cofactor_matrix(matrix):
    co_factor_matrix=[]
    row_cofactor=[]
    minor=[]
    temporary=[]
    for a in matrix:
        for b in a:
            temporary.append(b)
        minor.append(temporary)
        temporary=[]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            reduce_for_inverse(minor,i,j)
            cofactor=(((-1)**(i+j))*(main_determinant(minor)))
            minor=[]
            temporary=[]
            for a in matrix:
                for b in a:
                    temporary.append(b)
                minor.append(temporary)
                temporary=[]
            row_cofactor.append(cofactor)
        co_factor_matrix.append(row_cofactor)
        row_cofactor=[]
    return co_factor_matrix


#---------------DETERMINANT---------------


def reduce_for_determinant(minor,i):
    row_len=len(minor)
    for k in range(row_len):
        del minor[k][0]
    del minor[i]
    return minor

def main_determinant(matrix):
    if len(matrix) == 1:
        value=matrix[0][0]
    elif len(matrix) == 2:
        value=(matrix[0][0]*matrix[1][1]) - (matrix[1][0]*matrix[0][1])
    elif len(matrix) > 2:
        determinant=0
        minor=[]
        temporary=[]
        for a in matrix:
            for b in a:
                temporary.append(b)
            minor.append(temporary)
            temporary=[]
        for i in range(len(matrix)):
            reduce_for_determinant(minor,i)
            determinant= determinant+((matrix[i][0])*((-1)**(i))*(main_determinant(minor)))
            minor=[]
            temporary=[]
            for a in matrix:
                for b in a:
                    temporary.append(b)
                minor.append(temporary)
                temporary=[]
        
        return determinant
    return value

#---------------TRANSPOSE---------------

def transpose(matrix):
    row_len=len(matrix)
    col_len=len(matrix[0])
    row_tr=[]
    transpose_matrix=[]
    for z in range (row_len):
        for e in range (col_len):
            row_tr.append(matrix[e][z])
        transpose_matrix.append(row_tr)
        row_tr=[]
    return transpose_matrix

