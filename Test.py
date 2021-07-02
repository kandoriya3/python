import random
from operator import add, sub, truediv
from prettytable import PrettyTable

A = [166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,254,255,256,257,258,259,260,261,262,263,264,265,266,267,268,269,270,271,272,273,274,275,276,277,278,279,280,281,282,283,284,285,286,287,288,289,290,291,292,293,294]

B = [8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112]
random.shuffle(A)
random.shuffle(B)
C = list(map(add, A[:1], B[:1]))
D = [2000]
E = list(map(sub, D[:1] , C))
AA = A[:1] , E , B[:1]
print(" ")

F = list(map(add, A[:1], E))
G = list(map(add, F, B[:1]))

H = [20]
H1 = [100]
H2 = [0]
X1 = list(map(add, A[:1] , H2[:1]))
Y1 = list(map(add, B[:1] , H2[:1]))

I = list(map(truediv, A[:1] , H[:1]))
I1 = round(I[0] , 2)
J = list(map(truediv ,F, H[:1]))
J1 = round(J[0] , 2)
K = list(map(truediv, G , H[:1]))
K1 = round(K[0] , 2)


L = list(map(sub, H1[:1], I))
L1 = round(L[0], 2)
M = list(map(sub, H1[:1], J))
M1 = round(M[0], 2)
N = list(map(sub, H1[:1], K))
N1 = round(N[0], 2)

Z = [0,0.0,0.00,100.00]


table = PrettyTable(['size','RWt','CWt' ,'Pcum','pas'])
daku = ' '
table.title = "10 MM GRADATION"
table.add_column(daku , ["12.75mm","10.0mm","4.75mm","2.36mm","pan"])
table.add_column(daku , [Z[0],X1[0] , E[0] , Y1[0], Z[0]])
table.add_column(daku , [Z[1],X1[0] , F[0] , G[0], D[0]])
table.add_column(daku , [Z[2],I1, J1 , K1, K1])
table.add_column(daku , [Z[3],L1, M1 , N1,"-"])
print(table.get_string(fields=["size","RWt","CWt", "Pcum","pas"]))


import xlsxwriter

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('daku1.xlsx')
worksheet = workbook.add_worksheet()

# Some data we want to write to the worksheet.
expenses = (
    ["Size","Retained Weight","Cummulative Retained Weight","Percentage Of Cumm Weight","Passing"],
    ["12.75mm",Z[0],Z[1],Z[2],Z[3]],
    ["10.0mm",X1[0] , X1[0] , I1, L1],
    ["4.75mm",E[0],F[0] , J1,M1],
    ["2.36mm",Y1[0], G[0] , K1, N1],
    ["Pan",Z[0], D[0] , K1,"-"]
)

col = 0

# Iterate over the data and write it out row by row.
for row, (A, B, C, D, E) in enumerate((expenses)):
    worksheet.write(row, col, A)
    worksheet.write(row, col + 1, B)
    worksheet.write(row, col + 2, C)
    worksheet.write(row, col + 3, D)
    worksheet.write(row, col + 4, E)
workbook.close()
