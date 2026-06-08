# ==========================================================
# NUMPY CHEAT SHEET (ADVANCED + ML)
# ==========================================================

import numpy as np

# ==========================================================
# ARRAY CREATION
# ==========================================================

arr1 = np.array([10, 20, 30, 40, 50])

print("\nORIGINAL ARRAY")
print(arr1)

# ==========================================================
# ADVANCED INDEXING - FANCY INDEXING
# ==========================================================

print("\nFANCY INDEXING")
print(arr1[[0, 2, 4]])

# ==========================================================
# ADVANCED INDEXING - BOOLEAN INDEXING
# ==========================================================

print("\nBOOLEAN INDEXING (>25)")
print(arr1[arr1 > 25])

# ==========================================================
# ADVANCED INDEXING - 2D INDEXING
# ==========================================================

arr2 = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print("\n2D ARRAY")
print(arr2)

print("\n2D ADVANCED INDEXING")
print(arr2[[0,2], [1,2]])

# ==========================================================
# VECTORIZATION
# ==========================================================

numbers = [1,2,3,4,5]

result = []

for i in numbers:
    result.append(i * 2)

print("\nUSING PYTHON LOOP")
print(result)

# ==========================================================
# NUMPY VECTORIZATION
# ==========================================================

arr = np.array([1,2,3,4,5])

print("\nNUMPY VECTORIZATION")
print(arr * 2)

# ==========================================================
# VECTORIZATION EXAMPLE
# ==========================================================

arr = np.arange(1,11)

print("\nSQUARE OF ELEMENTS")
print(arr ** 2)

# ==========================================================
# LINEAR ALGEBRA - MATRIX MULTIPLICATION
# ==========================================================

A = np.array([
    [1,2],
    [3,4]
])

B = np.array([
    [5,6],
    [7,8]
])

print("\nMATRIX A")
print(A)

print("\nMATRIX B")
print(B)

print("\nMATRIX MULTIPLICATION")
print(A @ B)

# ==========================================================
# TRANSPOSE
# ==========================================================

A = np.array([
    [1,2,3],
    [4,5,6]
])

print("\nTRANSPOSE")
print(A.T)

# ==========================================================
# DETERMINANT
# ==========================================================

A = np.array([
    [1,2],
    [3,4]
])

print("\nDETERMINANT")
print(np.linalg.det(A))

# ==========================================================
# INVERSE MATRIX
# ==========================================================

print("\nINVERSE MATRIX")
print(np.linalg.inv(A))

# ==========================================================
# EIGEN VALUES AND EIGEN VECTORS
# ==========================================================

A = np.array([
    [1,2],
    [2,1]
])

eigenvalues, eigenvectors = np.linalg.eig(A)

print("\nEIGEN VALUES")
print(eigenvalues)

print("\nEIGEN VECTORS")
print(eigenvectors)

# ==========================================================
# STATISTICS - MEAN
# ==========================================================

arr = np.array([10,20,30,40,50])

print("\nMEAN")
print(np.mean(arr))

# ==========================================================
# MEDIAN
# ==========================================================

print("\nMEDIAN")
print(np.median(arr))

# ==========================================================
# STANDARD DEVIATION
# ==========================================================

print("\nSTANDARD DEVIATION")
print(np.std(arr))

# ==========================================================
# VARIANCE
# ==========================================================

print("\nVARIANCE")
print(np.var(arr))

# ==========================================================
# MINIMUM
# ==========================================================

print("\nMINIMUM")
print(np.min(arr))

# ==========================================================
# MAXIMUM
# ==========================================================

print("\nMAXIMUM")
print(np.max(arr))

# ==========================================================
# SUM
# ==========================================================

print("\nSUM")
print(np.sum(arr))

# ==========================================================
# CORRELATION
# ==========================================================

x = np.array([1,2,3,4,5])
y = np.array([2,4,6,8,10])

print("\nCORRELATION MATRIX")
print(np.corrcoef(x,y))

# ==========================================================
# MACHINE LEARNING DATASET
# ==========================================================

data = np.array([
    [25,50000],
    [30,70000],
    [35,90000]
])

print("\nML DATASET")
print(data)

# ==========================================================
# FEATURES AND LABELS
# ==========================================================

X = data[:,0]
y = data[:,1]

print("\nFEATURES (AGE)")
print(X)

print("\nLABELS (SALARY)")
print(y)

# ==========================================================
# NORMALIZATION (Z-SCORE)
# ==========================================================

X = np.array([10,20,30,40,50])

normalized = (X - X.mean()) / X.std()

print("\nNORMALIZED DATA")
print(normalized)

# ==========================================================
# DOT PRODUCT
# ==========================================================

x = np.array([1,2,3])
w = np.array([4,5,6])

print("\nDOT PRODUCT")
print(np.dot(x,w))

# ==========================================================
# LINEAR REGRESSION FORMULA
# ==========================================================

x = np.array([1,2,3])

m = 2
b = 1

y = m*x + b

print("\nLINEAR REGRESSION PREDICTION")
print(y)

# ==========================================================
# RESHAPE
# ==========================================================

arr = np.arange(1,13)

print("\nRESHAPE")
print(arr.reshape(3,4))

# ==========================================================
# FLATTEN
# ==========================================================

arr = np.array([
    [1,2,3],
    [4,5,6]
])

print("\nFLATTEN")
print(arr.flatten())

# ==========================================================
# CONCATENATE
# ==========================================================

a = np.array([1,2,3])
b = np.array([4,5,6])

print("\nCONCATENATE")
print(np.concatenate((a,b)))

# ==========================================================
# STACK
# ==========================================================

print("\nVERTICAL STACK")
print(np.vstack((a,b)))

print("\nHORIZONTAL STACK")
print(np.hstack((a,b)))

# ==========================================================
# RANDOM NUMBERS
# ==========================================================

print("\nRANDOM FLOATS")
print(np.random.rand(5))

print("\nRANDOM INTEGERS")
print(np.random.randint(1,100,5))

# ==========================================================
# UNIQUE VALUES
# ==========================================================

arr = np.array([1,2,2,3,3,3,4])

print("\nUNIQUE VALUES")
print(np.unique(arr))

# ==========================================================
# ARGMAX AND ARGMIN
# ==========================================================

arr = np.array([10,40,20,80,50])

print("\nARGMAX INDEX")
print(np.argmax(arr))

print("\nARGMIN INDEX")
print(np.argmin(arr))

# ==========================================================
# SORTING
# ==========================================================

print("\nSORTED ARRAY")
print(np.sort(arr))

# ==========================================================
# SEARCHING
# ==========================================================

print("\nINDEX OF VALUE 80")
print(np.where(arr == 80))

# ==========================================================
# BROADCASTING
# ==========================================================

arr = np.array([1,2,3])

print("\nBROADCASTING (+10)")
print(arr + 10)

# ==========================================================
# LOGICAL OPERATIONS
# ==========================================================

arr = np.array([10,20,30,40,50])

print("\nGREATER THAN 25")
print(arr > 25)

print("\nFILTERED VALUES")
print(arr[arr > 25])

# ==========================================================
# NUMPY FUNCTIONS MOST USED IN ML
# ==========================================================
#
# np.array()
# np.arange()
# np.linspace()
# np.reshape()
# np.flatten()
# np.concatenate()
# np.vstack()
# np.hstack()
# np.mean()
# np.median()
# np.std()
# np.var()
# np.sum()
# np.min()
# np.max()
# np.corrcoef()
# np.dot()
# np.linalg.inv()
# np.linalg.det()
# np.linalg.eig()
# np.random.rand()
# np.random.randint()
# np.unique()
# np.argmax()
# np.argmin()
# np.where()
# np.sort()
#
# ==========================================================