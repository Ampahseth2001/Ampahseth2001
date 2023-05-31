# Python code for power system analysis using Gauss-Seidel Iterative method given a Slack bus voltage as V1

import numpy as np

n= int(input('Enter number of buses?: ')) #takes number of busbars as input from the user
rows,columns= n,n

big=[]
for i in range(1, rows+1): #Allows the user to enter admittances as matrix input
    small=[]
    for k in range(1, columns+1):
        Y= complex(input(f'Y{i}{k} = '))
        small.append(Y)

    big.append(small)


Ybus= np.array(big) #Convert the list "big" into a matrix
print(Ybus)

print('\n\t\t\tIntital Voltage, Supply and Demand Values')
Voltages, Supply, Demand= [],[],[]
for i in range(1,1+n): #Allows the user to input the given Slack bus voltage(V1) and assume initial values for V2,V3...Vn 
    V= complex(input(f'Voltage{i}= '))
    Voltages.append(V)

for i in range(1,1+n): #Allows the user to input the given values for Supply Apparent Power as Si= Pi+jQi
    S= complex(input(f'Supply{i}= '))
    Supply.append(S)

for i in range(1,1+n): #Allows the user to input the given values for Demand Apparent Power as Si= Pi+jQi
    D= complex(input(f'Demand{i}= '))
    Demand.append(D)

print(Voltages)
print(Supply)
print(Demand)

def summation(V,Y,n,k):
    """ A function to calculate the summation part of the formula """
    out=0
    for a in range(n):
        if a!=k:
            out+=V[a]*Y[k][a]

    return out

Iter= int(input('\nNumber of iterations:')) # Allows you to enter the number of iterations

final_answer={}
for i in range(Iter):
    values=[]
    for k in range(n):
        zigma= summation(Voltages,big,n,k)
        if k==0:
            Voltages[k]=Voltages[0] # since Slack bus voltage remains constant for every iteration
        else:
            Voltages[k]= (((Supply[k]-Demand[k]).conjugate())/(Voltages[k].conjugate())-(zigma))/big[k][k] #Formula
        values.append(Voltages[k])

    final_answer[f'{i+1}']=values

for key,value in final_answer.items(): # Dictionary allows the user to display the values after each iteration
    print(f'Iteration{key}: {value}')
