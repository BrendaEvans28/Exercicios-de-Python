#EXEMPLOS DO CURSO DE PUTHON DAA USP

peso=78
altura=1.83

type(altura)
peso = 78
>>> altura = 1.83
>>> 
>>> peso
78
>>> type(altura)
<class 'float'>
>>> altura
1.83
>>> IMC= peso/(altura**2)
>>> IMC
23.291229956104985
>>> IMCinteiro=int(IMC)
>>> IMCinteiro
23
>>> texto = 'bom dia, tudo bem'
>>> len(texto)
17
>>> len(IMC)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    len(IMC)
TypeError: object of type 'float' has no len()
>>> temp= str(IMC)
>>> temp
'23.291229956104985'
>>> len(temp)
18
>>> len(str(IMC))
18

segundos_str = input('por favor, entre co o número d segundos que deseja converter:')
total_segs = int(segundos_str)

horas = total_segs//3600
segs_restantes= total_segs%3600
6minutos = segs_restantes//60
segs_restantes_final= segs_restante % 60
print(horas,'horas',minutos,'minutos e ', segs_restantes,'Segundos.')

