import math

a = float(input('Digite um valor para a: '))
b = float(input('Digite um valor para b: '))
c = float(input('Digite um valor para c: '))

delta = (b ** 2) - 4 *( a) * (c)

x = (-b + math.sqrt(delta)) / (2 * a)
y = (-b - math.sqrt(delta)) / (2 * a)

if delta == 0:
    print('A raiz desta equação é: ',x)
    
elif delta < 0:
        print('Esta equação não possuí raízes reais')
    
else:
    
    if x < y :
        print(x,'e',y)
            #print('As raízes da equação são',x,'e',y)
    else:
        print(y,'e',x)

        
 
    


   



            
        
         
           
          


            



              
