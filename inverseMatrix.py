import numpy as np
from numpy import *
from numpy.linalg import inv

a  =  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
c  =  [[0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0]]
tdm = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


# encode matrix

print ("Enter a square matrix")
n = int(input(("Enter number of columns in the matrix:")).strip())
m = int(input(("Enter number of rows in the matrix:")).strip())
print("Enter the matrix by space separated")
X = np.array([[0]*n for _ in range(m)])
for i in range(n):
    X[i] = [int(j) for j in input(("Enter Row Value and columns Value:")).strip().split(" ")]
print ("The Entered Input Matrix:")
print(X)
i = 0
l = 0

# Lists of Alphabets and its values
letters= [" ","a", "b", "c", "d", "e", "f", "g", "h",
              "i", "j", "k", "l", "m", "n", "o", "p", "q",
              "r", "s", "t", "u", "v", "w", "x", "y", "z"]
alphavalues = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
               13, 14, 15, 16, 17, 18, 19, 20, 21, 22,
               23, 24, 25, 26, 27]

# string to convert
b = input("Enter message: ")
listb = list(b)
lenb = len(listb)
d=len(listb)+1

print(d)

# Loop to convert Word to Values that
# are further useful for Encoding
for i in range(lenb):
    for j in range(27):
        if (listb[i] == letters[j]):
            a[i] = alphavalues[j]
            if (j == 23):
                j = 0
            break
if (lenb % 2 == 1):
    lenb = lenb + 1
a = a[0:lenb]
tb = b

# convert this array to 2D array for further
# multiplication with encoding matrix

j = 0
k = 0

# b[m][n] m is always 2
n = int(lenb / 2)
for i in range(0, lenb):
    if (j < n):
        c[k][j] = a[i]
        j = j + 1
    else:
        k = k + 1
        j = 0
        c[k][j] = a[i]
        j = j + 1

# Multiplay matrix by Encoding 2x2 matrix
c = np.matmul(X, c)

# Convert to 1D array for displaying
i = 0
j = 0
k = 0
for i in range(2):
    for j in range(int(lenb / 2)):
        a[k] = c[i][j]
        k = k + 1

a = a[0:lenb]
print("Encoding matrix  =  ", X)
print("encrypted form =  ", a)


# encoding matrix

# elements in Encrypted Matrix
lenb = d
n=int(input("Enter Number of elements:"))
a= zeros(n, dtype=int)
u=len(a)
q=0
w=0
while q < u:
    x=int(input("element:"))
    a[q] =x
    q+=1
    print(a)

sobj = slice(lenb)
a = a[sobj]

# convert array to 2d matrix to further
# multiplication with inverse of 2d matrix
j = 0
k = 0

# b[m][n] m is always 2
n = int(lenb / 2)
for i in range(0, lenb):
    if (j < n):
        tdm[k][j] = a[i]
        j = j + 1
    else:
        k = k + 1
        j = 0
        tdm[k][j] = a[i]
        j = j + 1

# Multiply by inverse matrix
dcm = inv(X)
dcm = np.matmul(dcm, tdm)

# Convert to 1d array for extracting word
i = 0
j = 0
k = 0
for i in range(2):
    for j in range(int(lenb / 2)):
        a[k] = dcm[i][j]
        k = k + 1

# Creating a decoded word
text = ""
for i in range(0, lenb):
    for j in range(0, 27):
        if (a[i] == alphavalues[j]):
            text = ''.join([text, letters[j]])

print("Decoded message = " + text)