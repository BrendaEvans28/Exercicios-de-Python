> 5>3
True
>>> 18
18
>>> ==
SyntaxError: invalid syntax
>>> 18 ==9 * 2
True
>>> x = 12345
>>> x < 0
False
>>> type(False)
<class 'bool'>
>>> type(x > 0)
<class 'bool'>
>>> x > 0 and x ** 2 > 100
True
>>> x < 0 and x == 12312
False
>>> x < 0 or x == 12312
False
>>> x > 0
True
>>> not x > 0
False
>>> not False
True
>>> not True
False
>>> 
>>> 
>>> fizerSol = True
>>> forFeriado = False
>>> vouParaPraia = fizerSol and forFeriado
>>> vouParaPria
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    vouParaPria
NameError: name 'vouParaPria' is not defined
>>> vouParaPria
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    vouParaPria
NameError: name 'vouParaPria' is not defined
>>> vouParaPraia
False
>>> forFeriado
False
>>> forFeriado = True
>>> vouParaaPraia
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    vouParaaPraia
NameError: name 'vouParaaPraia' is not defined
>>> vouParaPraia
False
>>>  vouParaPraia = fizerSol and forFeriado
 
SyntaxError: unexpected indent
>>>  vouParaPraia = fizerSol and forFeriado
 
SyntaxError: unexpected indent
>>> forFeriado = True
>>> vouParaPraia = fizerSol and forFeriado
>>> vouParaPraia
True
>>> 
>>> 
>>> paitrocinio = False
>>> rolarPromoção = true
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    rolarPromoção = true
NameError: name 'true' is not defined
>>> rolarPromoção = True
>>> vouaShow = paitrocinio or rolarPromoção
>>> vouaShow
True
>>> (x>0)or(x<=0)
True
>>> not(x>0)and (x>0)
False
>>> x=5
>>> y=3
>>> z=7
>>> x>y and x<z
True
>>> idade = 15
>>> maioridade = 18
>>> pode_dirigir = idade >= maioridade
>>> print(pode_dirigir)
False
>>> fruta = laranja
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    fruta = laranja
NameError: name 'laranja' is not defined
>>> x=10
>>> y=15
>>> z=25
>>> print(x==z-y and z!=y-x or not y != z - x)
True
>>> x=10
>>> y=20
>>> z=30
>>> print(x<=30 and y>=5)
True
>>> print(not y < 10 or y !=z-x)
True
>>> print(x>=10 or y!=z-x)
True
>>> print(not y>10 or not z > 10)
False
>>> a=1
>>> b=2
>>> a!= r b==1
SyntaxError: invalid syntax
>>> not(a==1)
False
>>> a!=1 or b==1
False
>>> math,sqrt(8)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    math,sqrt(8)
NameError: name 'math' is not defined
>>> import math
>>> math.sqrt(8)
2.8284271247461903
>>> math.sqtr(9)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    math.sqtr(9)
AttributeError: module 'math' has no attribute 'sqtr'
>>> math.sqrt(9)
3.0
>>> 1+1+1==3
True
>>> is_ready = bool
>>> if not is_ready == false
SyntaxError: invalid syntax
>>> not is_ready -- False
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    not is_ready -- False
TypeError: unsupported operand type(s) for -: 'type' and 'int'
>>> if not is_ready == False
SyntaxError: invalid syntax
>>> if is_ready:
	print(is_ready)

<class 'bool'>
>>> if (not is+ready == Falso):
	
SyntaxError: invalid syntax
>>> if (not is_ready == Falso):
	print(is_ready)

Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    if (not is_ready == Falso):
NameError: name 'Falso' is not defined
>>> x=10
>>> not(x==10)
False
>>> x!=10
False
>>> x !=20
True
>>> x=15
>>> y=30
>>> x>y and x<y
False
>>> if (a>0):
	if(b>0):
		print('tudo ok para decolagem ')
	else:
		print('tanque principal vazio; voando com combusivel reserva !')
else:
	if(c>0):
		print('foguete não tem piloto...')

		
tudo ok para decolagem 
>>> 
