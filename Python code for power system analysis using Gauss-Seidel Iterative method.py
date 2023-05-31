# Python code for power system analysis using Gauss-Seidel Iterative method given a Slack bus voltage as V1

import numpy as np

n= int(input('The number of buses?: '))
rows,columns= n,n

big=[]
for i in range(1, rows+1):
    small=[]
    for k in range(1, columns+1):
        Y= complex(input(f'Y{i}{k} = '))
        small.append(Y)

    big.append(small)


Ybus= np.array(big)
print(Ybus)

print('\n\t\t\tIntital Voltage, Supply and Demand Values')
Voltages, Supply, Demand= [],[],[]
for i in range(1,1+n):
    V= complex(input(f'Voltage{i}= '))
    Voltages.append(V)

for i in range(1,1+n):
    S= complex(input(f'Supply{i}= '))
    Supply.append(S)

for i in range(1,1+n):
    D= complex(input(f'Demand{i}= '))
    Demand.append(D)

print(Voltages)
print(Supply)
print(Demand)

def summation(V,Y,n,k):
    out=0
    for a in range(n):
        if a!=k:
            out+=V[a]*Y[k][a]

    return out

Iter= int(input('\nNumber of iterations:'))

final_answer={}
for i in range(Iter):
    values=[]
    for k in range(n):
        zigma= summation(Voltages,big,n,k)
        if k==0:
            Voltages[k]=Voltages[0]
        else:
            Voltages[k]= (((Supply[k]-Demand[k]).conjugate())/(Voltages[k].conjugate())-(zigma))/big[k][k]
        values.append(Voltages[k])

    final_answer[f'{i+1}']=values

for key,value in final_answer.items():
    print(f'Iteration{key}: {value}')
