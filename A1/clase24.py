def price(total,descuento=0):
    return total - descuento

print(price(10,3))

def ServirEncebollado(cebolla='Si'):
    return 'Encebollado' + cebolla +  ' tiene cebolla'


def prueba(a,b):
    print(a,b)
prueba(b=3,a=2)

a=10
b=15
c=20
d=5
e=10
def suma(*args):
    suma=0
    for i in args:
        suma+=i
    return f'La suma total es: {suma}'
print(suma(a,b,c,d,e))

f = 'Pedro'
q = 27
h = [1,2,3,4,5]
def manejo_disc(**kwargs):
    for key,value in kwargs.items():
        print(key,value)

manejo_disc(nombre=f,edad=q,lista=h)

list_num = [i for i in range(1,11)]
def ParesLista(lista):
    return list(filter(lambda x:x%2==0,lista))

def ParesLista2(lista):
    listaPares= [i for i in lista if i %2==0]
    return listaPares

def Num_Bool(num):
    return True if num%2==0 else  False

def pair_num(num):
    return num%2 ==0
print(ParesLista(list_num))
print(ParesLista2(list_num))
print(Num_Bool(7))
print(pair_num(7))

filtrado = filter(pair_num,list_num)
print(filtrado)
print(type(filtrado))
print(list(filtrado))

list_color = ['red','blue','green','yellow','black']
list_caracteres = list(filter(lambda x: len(x)==4, list_color))
print(list_caracteres)

def letters_color(color):
    return len(color) ==4
filtradoColor = filter(letters_color,list_color)
print(list(filtradoColor))

cuadrado = lambda x: x**2
print(cuadrado(5))
pair = lambda x: x % 2 ==0
filter_number=filter(pair,list_num)
filter_number = filter(lambda x: x%2==0,list_num)
filtrado_2 = filter(pair_num,list_num)

list_num2 = [i for i in range(1,11)]

def cuadrado(num):
    return num **2
num_cuadrado = map(cuadrado,list_num2)
print(list(num_cuadrado))

def recursive(num):
    if num ==0:
        return 1
    return num + recursive(num-1)
print(recursive(5))
print('Hola')