import random
input_numbers = []
n=10000000000
for i in range(1,n+1):
    
    # number = random.randint(1,10000000000000000000)
    # input_numbers.append(number)
    # input_numbers.sort()
    # print(len(input_numbers))
    input_numbers.insert(i-1,i)
print(input_numbers.index(n))

