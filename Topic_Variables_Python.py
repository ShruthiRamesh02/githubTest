Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
5+5
10
6+6
12
print("yay i installed python today")
yay i installed python today
rent=18000
gas=1000
groceries=5000
print(rent)
18000
print(gas)
1000
print(groceries)
5000
total=rent+gas+groceries
print(total)
24000
item1="rent"
item2="gas"
item3="groceries"
print(item1)
rent
print("total expenses:"item1,item2,item3)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print("total expenses:",item1,item2,item3)
total expenses: rent gas groceries
rent=18000
gas=500
groceries=5000
total=rent+gas+groceries
print(total)
23500
total=(rent+gas)-groceries
print(total)
13500
total=(rent-gas)+groceries
print(total)
22500
basesalary=100000
pf=6000
sso=800
incometax=3000
total=basesalary-pf-sso-incometax
print(total)
90200
rent=15000
gas=500
electricity=3000
water=1000
food=5000
outing=500
>>> transport=5000
>>> total=rent+gas+electricity+water+outing+food+transport
>>> print(total)
30000
>>> basesalary=87000
>>> total=basesalary-total
>>> print(total)
57000
>>> break=6
SyntaxError: invalid syntax
>>> true=7
>>> True=7
SyntaxError: cannot assign to True
>>> False=8
SyntaxError: cannot assign to False
>>> break=5
SyntaxError: invalid syntax
>>> birth_year=1990
>>> current_year=2023
>>> age=current_year-birth_year
>>> print(age)
33
>>> first_name="shruthi"
>>> middle_name="tatanahalli"
>>> last_name="rameshan"
>>> full_name=first_name+middle_name_last_name
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    full_name=first_name+middle_name_last_name
NameError: name 'middle_name_last_name' is not defined
>>> full_name=first_name+middle_name+last_name
>>> print(full_name)
shruthitatanahallirameshan
