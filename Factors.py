class Factor:
  """ A class find the list of factors of a particular number """
    def __init__(self,number):
        self.number= int(number)

    def factors(self):
        items1= []
        for i in range(1,self.number+1):
            if self.number%i==0:
                items1.append(i)

        return items1


def most_factors(x,n):
  ''' Function to detect which number within a particular range has the most factors'''
    old_f,new_f=1,''
    for k in range(x,n+1):
        new_f= Factor(k)
        if len(new_f.factors())>old_f:
            m=k
            old_f=len(new_f.factors())
    return m
    
x= input('Enter lower range: ')
n= input('Enter upper range: ')
answer= most_factors(x,n)
print(answer)
