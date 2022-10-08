num = 5
id(num) //bellekteki adresi verir
a = 10
b = a
id(a)
id(b) // a ile b aynu adres çýkar
id(10) //yine ayný adres çýkar
k = 10
id(k) //yine ayný adres çýkar


num = 2.5
type(num) //deðiþkenin tipini verir
a = int(num) //sayýyý integer'e çevirir
a = float(num) //sayýyý float'a çevirir
b = 10
k = 6
a = complex(b,k) //sayýyý complex sayý türüne çevirir
bool = b < k //false deðerini atar çünkü b k'den küçük deðil
lst = [25,35,14,72] //bu listedir köþeli parantez ile baþlar ve biter
s = {25,65,45,78} //bu settir süslü parantez ile baþlar ve biter
tpl = (54,68,74,12) //bu tupledir normal parantez ile baþlar ve biter
str = "Hüseyin" //bu stringdir
s = 'H' //bu da stringdir
list(range(10)) //þu deðeri verir [0.1.2.3.4.5.6.7.8.9] 0'dan 10'a kadar sayar
list(range(2,10,2)) //þu deðeri verir [2,4,6,8]
dictionary = {"Hüseyin":"Yok","Rümeysa":"Vestel","Yasin":"Huawei"} // buna dictionary denir ayný javadaki map ve hashmap'a benzer
dictionary.keys() // keyleri verir
dictionary.values() //valueleri verir
dictionary['Hüseyin'] // yoku verir
dictionary.get("Yasin") //huaweiyi verir


bin(25) //25'i binary sayý sistemine çevirir
oct(25) //25'i octo decimal sayý sistemine çevirir
hex(25) //25'i hexa decimal sayý sistemine çevirir

~13 //tersini verir yani eksiyi
12 & 13
12 | 13
12 ^ 13
12 << 13
12 >> 13

import math //math modulunu import eder
x = math.sqrt(25)
print(math.floor(2.9)) //sonucu 2 çýkar
print(math.ceil(2.2)) //sonucu 3 çýkar
print(math.pow(3,2)) //sonucu 9.0 çýkar
print(math.pi) //sonucu 3.14 küsür çýkar
print(math.e) //sonucu 2.71 küsür çýkar
import math as m
m.sqrt(25) //sonucu 5 çýkar
from math import sqrt,pow
pow(4,5) //sonucu 1024.0 çýkar

python mycode.py //dosyayý çalýþtýrýr

x = int(input("1. sayýyý giriniz: "))
y = int(input("2. sayýyý giriniz: "))
z = x + y;
print(z)

ch = input("karakter giriniz: ")
print(ch[0])

ch = input("karakter giriniz: ")[0]
print(ch)

result = eval(input("ifadeyi giriniz: ")) //2 + 5 - 1 ifadesi girilebilir
print(result)

import sys
x = int(sys.argv[1])
y = int(sys.argv[2])
z = x + y
print(z)

x = 8
r = x % 2
if(r==0):
	print("X'in 2ye bölümünden geriye kalan sýfýrýdýr")
	if(x>5):
		print("X 5den büyük")
	else:
		print("X 5den büyük deðil")
else:
	print("X'in 2ye bölümünden geriye kalan sýfýr deðildir")
print(bye)

x = 1
if(x==1):
	print("bir")
elif(x==2):
	print("iki")
elif(x==3):
	print("üç")
else:
	print("Hiçbiri")

i = 1
j = 1
while i<=5:
	print("merhaba", end="")
	j = 1	
	while j<=4
		print("Selam", end="")
		j = j + 1
	i = i + 1
	print()

x = ["Hüseyin",65,2.4]
for i in x:
	print(i)

for i in [2,6,'Hüseyin']:
	print(i)

for i in range(10):
	print(i)

for i in range(11,21,2):
	print(i)

for i in range(5):
	if(i == 3):
		continue
	print("Hello",i)
	if(i == 4)
		pass

for i in range(1,101):
	if(i%2!=0):
		pass
	else:
		print(i)
print("bye")

nums = [10,16,18,21,26]
for num in nums:
	if(num % 5 == 0):
		print(num)
		break
else:
	print("bulunamadý")

num = 10
for i in range(2,num):
	if(num % i == 0):
		print("bölünebilir")
		break
else:
	print("bölünemez")

for i in range(4):
	for j in range(4):
		print("#",end="")
	print()

for i in range(4):
	for j in range(i):
		print("#",end="")
	print()

from array import *
vals = array("i",[5,9,8,7,4])
for e in vals:
	print(e)

from array import *
vals = array("i",[5,9,8,7,4])
newArr = array(vals.typecode, (a*a for a in vals))
i = 0
while i<len(newArr):
	print(newArr[i])
	i = i + 1

from array import *
arr = array("i",[])
n = int(input("dizinin uzunluðunu giriniz: "))
for i in range(n):
	x = int(input("yeni deðeri giriniz: "))
	arr.append(x)
print(arr)
val = int(input("aramak istediðiniz deðeri giriniz: "))
k = 0
for e in arr:
	if(e == val)
		print(k)
		break;
	k += 1
print(arr.index(val))

from array import *
arr = array('i',[1,2,3],[4,5,6])

from numpy import *
arr = array([1,2,3,4,5,6],float)
print(arr.dtype)
print(arr)

from numpy import *
arr = linspace(0,15,16)
print(arr)

from numpy import *
arr = arange(1,15,2) //1den 15'e ikiþer ikiþerlik dizi oluþturur
print(arr)

from numpy import *
arr = logspace(1,40,5)
print(arr)

from numpy import *
arr = zeros(5) //5 tane 0 dizisi oluþturur
print(arr)

from numpy import *
arr = ones(5,int) //5 tane 1 dizisi oluþturur
print(arr)

from numpy import *
arr1 = array([1,2,3,4,5])
arr2 = array([6,7,8,9,10])
print(concatenate([arr1,arr2])) //arr1'i ve arr2'yi tek dizi haline getirir birbirine ekler

from numpy import *
arr1 = array([2,8,9,6,4])
arr2 = arr1.view() //buna shallow copy deniyor
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))

from numpy import *
arr1 = array([2,8,9,6,4])
arr2 = arr1.copy() //buna deep copy deniyor
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))

from numpy import *
arr1 = array([[1,2,3],[4,5,6]])
print(arr1.ndim) //sonucu (2) veriyor
print(arr1.shape) //sonucu (2,3) veriyor
print(arr1.size) //sonucu 6 veriyor çünkü boyutu 6
arr2 = arr2.flatten() //iki fakrlý diziyi birleþtirip arr2'ye atýyor
print(arr2)
arr3 = arr2.reshape(3,4)

from numpy import *
m = matrix('1 2 3; 6 4 5; 1 6 7') //bunu diziye çeviriyor 3 parça halinde
print(m)
print(m.min())
print(m.max())
print(diagonal(m))


from numpy import *
m1 = matrix(1 2 3; 6 4 5; 1 6 7)
m2 = matrix(1 2 3; 6 8 5; 2 6 7)
m3 = m1 * m2
print(m3)

def add_sub(x,y):
	c = x + y
	d = x - y
	return c,d

result1,result2 = add_sub(5,4)
print(result1, result2)

def update(x):
	print(id(x)) //burada x'in bellekdeki adresi a ile ayný
	x = 8
	print(id(x)) //burada x'in bellekdeki adresi deðiþiyor
	print("x ", x) //xin deðeri 8 çýkar

a = 10
update(a)
print("a ", a) // anýn deðeri 10 çýkar


def update(lst):
	print(id(lst))
	lst[1] = 25
	print(id(lst)) 
	print("lstd ", lst) 

lst = [10,20,30]
print(id(lst))
update(lst)
print("lst ", lst) 

def person(name,age=18):
	print(name)
	print(age)
person(age = 28, name = "Hüseyin")

def sum(a, *b):
	c = a
	for i in b:
		c = c + i
	print(c)
sum(5,6,34,78)

def person(name, **data):
	print(name)
	for i,j in data.items():
		print(i, j)
person("Hüseyin",age=24,city="Niðde",tel=555)

def person(name, lst={"age":"Yok","year":"var","donkey":"asdf"}):
	print(name)
	for i,j in lst.items():
		print(i, j)

lst={"age":"Yok","year":"var","donkey":"asdf"}

person("Hüseyin",lst)

a = 10
def something():
	global a //global a deðiþkenini fonksiyon içinde kullan
	a = 15
	print("a ", a)
something()
print("a ",a)

a = 10
print(id(a))
def something():
	a = 9
	x = globals()['a']
	print(id(x))
	print("a ", a)
	globals()['a'] = 15
something()
print("a ",a)

def count(lst):
    even = 0
    odd = 0
    for i in lst:
        if(i % 2 == 0):
            even += 1
            print("bölündü {}".format(i))
        else:
            odd += 1
            print("bölünemedi {}".format(i))
    return even,odd
lst = [74,65,14,48,95,55,36,75,25,12]
even,odd = count(lst)
print("Even: {} Odd: {}".format(even,odd))

def fib(n):
    a = 0
    b = 1
    print("a {}".format(a))
    print("b {}".format(b))
    for i in range(0,n):
        c = a + b
        a = b
        b = c
        print("c {}".format(c))
fib(100)

def fact(n):
    f = 1
    for i in range(1,n+1):
        print("{} x {} = {}".format(f,i,f*i))
        f = f * i
    return f
x = 4
result = fact(x)
print(result)

import sys
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())
i = 0
def greet():
    global i
    i += 1
    print("Hello",i)
    greet()
greet()

def fact(n):
    if(n == 0):
        return 1
    return n * fact(n-1)
result = fact(5)
print(result)

f = lambda a,b : a + b
result = f(10,5)
print(result)

from functools import reduce
nums = [3,2,6,8,4,6,2,9]
evens = list(filter(lambda n:n%2==0,nums))
print(evens)
doubles = list(map(lambda n:n*2,evens))
print(doubles)
sum = reduce(lambda a,b:a+b,doubles)
print(sum)

def div(a,b):
    print(a/b)
def smart_div(func):
    def inner(a,b):
        if(a<b):
            a,b = b,a
        return func(a,b)
    return inner
div = smart_div(div)
div(2,4)

def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def multi(a,b):
    return a * b
def div(a,b):
    return a / b
from Calc import *
result = add(10,10)
print(result)

print(__name__)
import Calc
print(__name__)
def main():
    print(__name__)
if __name__ == '__main__':
    main()

def add():
    print("add bura ",__name__)
def sub():
    print("sub bura")
def main():
    add()
    sub()
if __name__ == '__main__':
    main()
from Calc import add
def fun1():
    add()
    print("fun 1")
def fun2():
    print("fun 2")
def main():
    fun1()
    fun2()
main()

class Computer:
    def config(self):
        print("Bilgisayar i7 - 8GB RAM - 1TB SSHD")
com1 = Computer()
Computer.config("selam")
com1.config()

class Computer:
    def __init__(self,cpu,ram):
        print("init'in içinde")
        self.cpu = cpu
        self.ram = ram
    def config(self):
        print("Bilgisayar ",self.cpu,self.ram)
com1 = Computer("i5",8)
Computer.config(com1)
com1.config()

class Computer:
    def __init__(self):
        self.name = "Hüseyin"
        self.age = 25
    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False
    def set_age(self,age):
        self.age = age
c1 = Computer()
c2 = Computer()
c1.set_age(22)
if c1.compare(c2):
    print("eþit")
else:
    print("eþit deðil")

class Car:
    wheels = 4
    def __init__(self):
        self.mil = 30
        self.com = "BMW"
c1 = Car()
c2 = Car()
c1.mil = 8
Car.wheels = 10
Car.mil = 9
print(c1.mil,c1.com,c1.wheels)
print(c2.mil,c2.com,c2.wheels)

class Student:
    school="Niðde / Bor Meslek Yüksek Okulu"
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3
    @classmethod
    def get_school(cls):
        return cls.school
    @staticmethod
    def info():
        print("Burasý okul bilgisi")
s1 = Student(10,11,12)
print(s1.avg())
print(Student.get_school())
Student.info()

class Student:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.laptop = self.Laptop()
    def show(self):
        print(self.name, self.rollno)
        self.laptop.show()
    class Laptop:
        def __init__(self):
            self.brand = "HP"
            self.cpu = "i7"
            self.ram = 8
        def show(self):
            print(self.brand,self.cpu,self.ram)
s1 = Student("Hüseyin",221)
s1.show()
laptop = s1.Laptop()
laptop.show()

class A:
    def method1(self):
        print("selam")
class B:
    def method10(self):
        print("class B")
class C(A,B):
    def method2(self):
        print("selam 2")
a = A()
a.method1()
b = B()
b.method10()
c = C()
c.method1()
c.method2()
c.method10()

class A:
    def __init__(self):
        print("A init")
    def method1(self):
        print("selam")
class B:
    def __init__(self):
        print("B init")
    def method10(self):
        print("class B")
class C(A,B):
    def __init__(self):
        super().__init__()
        print("C init")
    def feat(self):
        super().method1()
c = C()
c.feat()

class PyCharm:
    def execute(self):
        print("çalýþýyor 1")
class MyEditor:
    def execute(self):
        print("çalýþýyor 2")
class Laptop:
    def code(self,ide):
        ide.execute()
pycharm = PyCharm()
myeditor = MyEditor()
laptop = Laptop()
laptop.code(pycharm)

class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
    def __add__(self, other):
        s1 = self.m1 + other.m1
        s2 = self.m2 + other.m2
        s2 = Student(s1,s2)
        return s2
    def __gt__(self, other):
        s1 = self.m1 + self.m2
        s2 = other.m1 + other.m2
        if s1 > s2:
            return True
        else:
            return False
    def __str__(self):
        return "{} {}".format(self.m1,self.m2)
s1 = Student(10,10)
s2 = Student(10,11)
s3 = s1 + s2
if(s1 > s2):
    print("s1 büyük")
elif(s1 == s2):
    print("eþit")
else:
    print("s2 büyük")
print(s3)
print(s3.__str__())

class A:
    def show(self):
        print("a show")
class B(A):
    def show(self):
        super().show()
        print("b show")
b = B()
b.show()

class A:
    def sum(self,s1=None,s2=None,s3=None):
        if s1!=None and s2!=None and s3!=None:
            return s1 + s2 + s3
        elif s1!=None and s2!=None:
            return s1 + s2
        else:
            return s1
a = A()
t = a.sum(10,10)
print(t)

class TopTen:
    def __init__(self):
        self.num = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration
values = TopTen()
print(next(values))
for i in values:
    print(i)

def topten():
    n = 1
    while n<=10:
        sq = n*n
        yield sq
        n += 1
values = topten()
for i in values:
    print(i)

a = 5
b = 0
try:
    print(a/b)
except ZeroDivisionError as e:
    print("0'a bölünemez ",e)
except ValueError as e:
    print("boþ geçilemez: ",e)
finally:
    print("iþlem bitti")

from threading import *
from time import sleep
class Hello(Thread):
    def run(self):
        for i in range(5):
            sleep(1)
            print("Hello")
class Hi(Thread):
    def run(self):
        for i in range(5):
            sleep(1)
            print("Hi")
t1 = Hello()
t2 = Hi()
t1.start()
sleep(0.2)
t2.start()
t1.join()
t2.join()
print("bye")

f = open("resim.JPG","rb")
f1 = open("resim2.JPG","wb")
for i in f:
    print(i)
    f1.write(i)
f2 = open("dosya","r")
f3 = open("dosya2","w")
for i in f2:
    f3.write(i)
    print(i)

pos = -1
def search(list,n):
    i = 0
    while(i<len(list)):
        globals()["pos"] = i+1
        if(list[i] == n):
            return True
        i += 1
    return False
n = 9
list = [1,2,5,7,9,6,3,7]
if search(list,n):
    print("bulundu ",pos)
else:
    print("bulunamadý")

pos = -1
def search(list,n):
    l = 0
    u = len(list) - 1
    while l <= u:
        mid = (l + u)
        print("mid {}".format(mid))
        if list[mid] == n:
            globals()["pos"] = mid
            return True
        else:
            if list[mid] < n:
                l = mid + 1
            else:
                u = mid -1
n = 4
list = [4,7,8,12,45,99,102,702,10987,566666]
if search(list,n):
    print("bulundu ",pos)
else:
    print("bulunamadý")

def sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            print("j: {}".format(j))
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
lst = [5,3,8,6,7,2]
sort(lst)
print(lst)

def sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            print("j: {}".format(j))
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
lst = [5,3,8,6,7,2]
sort(lst)
print("en büyük ikici sayi : {}".format(lst[len(lst) -2]))

def sort(nums):
    print("nums len {}".format(len(nums)))
    for i in range(len(nums)):
        minpos = i
        for j in range(i,len(nums)):
            if nums[j] < nums[minpos]:
                minpos = j
        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp
lst = [5,3,8,6,7,2]
sort(lst)
print(lst)

def sort(nums):
    print("nums len {}".format(len(nums)))
    for i in range(len(nums)):
        minpos = minimumcuindexibul(nums,i)
        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp
def minimumcuindexibul(nums,i):
    minpos = i
    for j in range(i,len(nums)):
            if nums[j] < nums[minpos]:
                minpos = j
    print("minpos index {}".format(minpos))
    return minpos
lst = [5,3,8,6,7,2]
sort(lst)
print(lst)

def min_bul(lst):
    length = len(lst)
    min = 100
    for i in range(length):
        if lst[i] < min:
            min = lst[i]
    return min
lst = [5,4,2,3,9,1,7]
min = min_bul(lst)
print(min)

import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",passwd="toor",database="abc")
mycursor = mydb.cursor()
mycursor.execute("select * from student")
result = mycursor.fetchall()
for i in result:
	print(i)
