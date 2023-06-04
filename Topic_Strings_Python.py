Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
text="my name is shruthi"
print(text)
my name is shruthi
text[0:3]
'my '
text[0:7]
'my name'
text[0:9]
'my name i'
text[0:10]
'my name is'
text[0:17]
'my name is shruth'
text[0:19]
'my name is shruthi'
text[0:]
'my name is shruthi'
text[:7]
'my name'
>>> text="hello 'world'"
>>> print(text)
hello 'world'
>>> text='hello"world"'
>>> print(text)
hello"world"
>>> address='''120/59 ,soi 3c,soi watchiratamasatit
... bangna,bangkok
... Thailand 10260'''
>>> print(address)
120/59 ,soi 3c,soi watchiratamasatit
bangna,bangkok
Thailand 10260
>>> text='Thailand has number of states #'
>>> num=45
>>> str(num)
'45'
>>> print(text+str(num))
Thailand has number of states #45
>>> s1="hello"
>>> s2='world'
>>> print(s1+' 's2)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print(s1+' '+s2)
hello world
>>> text="I Love Bangalore"
>>> print(text)
I Love Bangalore
>>> s1="banglaore wether is the"
>>> s2="BEST"
>>> print(s1+ ' '+s2)
banglaore wether is the BEST
