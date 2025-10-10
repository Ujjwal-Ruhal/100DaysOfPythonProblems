# use of for loop is : for example to print something to 100 time's so you dont copy paste for 100 time's so solve this type of problem's to solve using loop's
# for loop means : you diclair a condition so for loop check the condition and execute the code for if the condition are not false

#  for example :

l = ['apple',2,1021,'A',10.23]
# to see all data 
print(l)

# print all value's using for loop
for i in l:
    print(i)
    ''' output : apple
                 2
                 1021
                 A
                 10.23
                '''

# one more example
for x in ['hello','ji','kiya','haal','hai','aapke']:
    print(x)

# one more example like - print a tabal
for i in range(2,21,2):
    print(i)
# one more example like - print a tabal as a user input
n = int(input('Enter a number : '))
for i in range(1,11):
    num = i*n
    print(num)