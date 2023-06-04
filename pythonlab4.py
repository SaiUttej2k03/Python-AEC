'''Write a Program to print the following pattern.
A
B C D
E F G H I
J K L M N O P
Q R S T U V W X Y'''

n = 5
count = 0
for i in range(1,n+1):
    for j in range(2*i-1):
        print(chr(ord('A')+count),end=' ')
        count+=1
    print()