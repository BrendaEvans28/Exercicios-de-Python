#Exercicio02
segundos_str = input('Por favor, entre com o número de segundos que deseja converter:')
total_segundos = int(segundos_str)

adia = total_segundos // 86400
sobra_segundos = total_segundos % 86400
bhoras = sobra_segundos // 3600
sobra_segundos1 = sobra_segundos % 3600
cminutos = sobra_segundos1 // 60
sobra_segundosfinal = sobra_segundos1 % 60
dsegundos = sobra_segundosfinal

print(adia,'dias,',bhoras,'horas,',cminutos,'minutos e',dsegundos,'Segundos.')

