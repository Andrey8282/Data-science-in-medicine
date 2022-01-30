a = 7
print (a)
var_a = "Hello"
print (var_a)
a = 7
b = 8
c = 16
print (a + b) + c
n = "Hello"
print (n)
t = 17
o = 8
print (t + o)
import time
n = 11000
time_format = time.strftime("%H:%M:%S:", time.gmtime(n))
print ("Time in preferred format :-", time_format)
n = int(input("Enter the value of n: "))
temp = str(n)
t1 = temp + temp
t2 = temp + temp + temp
comp = n + int(t1) + int(t2)
print (comp)
number = int(input("insert num 0 to 9: "))
while number < 10:
    print (number)
    number = number + 1
print ("program complite")
a = int(input("day1="))
b = int(input("finish day="))
while b < 20:
    b += (a/100)*10
    a += 1
print (a+1)
x = int(input("x="))
mx = 0
while x > 0:
    c = x % 10
    if c >= mx: mx = c
    x//= 10
print (mx)













