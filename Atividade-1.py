def mostrarmenu():
    print('Em qual temperatura vc deseja Converter:')
print ('[1] - Se você deseja converter uma temperatura de celsius para fahrenheit')
print ('[2] - Se você deseja converter uma temperatura de farenheit para celcius')

n1 = int (input('Digite sua opção: '))

def fahrenheit(c):
    fahrenheit =(c * 1.8) + 32
    return fahrenheit
def celsius(f):
    celsius = (f-32) * 5/9 
    return celsius
   

if n1==1:
    c = float (input('Digite a temperatura em celsius para a conversão:ºC '))
    print('O resultado será: ºF ' ,fahrenheit(c))
elif n1==2:
    f = float (input('Digite a temperatura em farenheit para a conversão:ºF '))
    print('O resultado será: ºC' ,celsius(f))
elif n1>2:
        raise ValueError