#-*- coding:utf-8 -*-

print("Hello, World!")

# no python as variaveis são criadas no momento que são instanciadas
idade = 125
nome = "Alex {}"
sobrenome = 'Junio'

print(nome,sobrenome,idade)

# no python não existe um modo de comentarios multlinha mas tem um jeito 
"""
Este bem estranho digasse de passagem1
Desde Python irá ignorar strings literais que não são atribuídos a uma variável,
 você pode adicionar uma cadeia de linhas múltiplas (três aspas) no seu código, 
 e colocá-lo comentar dentro dele:

"""
#atribuindo valor a multiplas variáveis em uma linha 
x,y,z = 'uni', 'duni','thê'
print(x,y,z)

#É possível  atribuir um mesmo valor a diversas variáveis
d= 'Salamémingué'
a =b =c = d

print(a,b,c)

numInt = 10 # numero inteiro
numFloat = 10.2 # numéro de pornto flutuante
numComplex = 1j # numéro complexo onda a parte imaginaria é representada por j
variSTR = 'String'

#conversões são feitas utilizando cast

convertFloar = float(numInt)
convertInt = int(numFloat)
convetComplex = complex(numComplex)

# importa um lib randam e gera um numéro randomico entre 1 e 10 
import random
numRandom = random.randrange(1,10) 

print (numRandom)


#desta forma é possível criar strings com sequencias de caractesre
textoSa = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(textoSa)

#como na maioria das linguagens de programção as strings no python são vetores

trabalhoComSTR = ' Essa frase é um vetor'

print("terceira possição do vetor =>" ,trabalhoComSTR[3])



#pegar os valores entre as string

print("Vetores entre as str" ,trabalhoComSTR[2:5])

#retira os espaços do inicio string

print(trabalhoComSTR.strip())

# retorna o complimento da string

print(len(trabalhoComSTR))

#retorna tudo em minusculo
print(trabalhoComSTR.lower())

# retorna tudo em maiusculo 
print(trabalhoComSTR.upper())

#retorna a substituição de strings 
print(trabalhoComSTR.replace("E","V"))

#divide a string no meio suprimindo o elemento divisor
print(trabalhoComSTR.split("é"))

#divide a string em linhas 
print(textoSa.splitlines())

#para inserir numeros em string 
print(nome.format(idade))

#trabalho com STR formate
quantidade = 200
item = "Mel solis"
preco = 10.20

print("A quandidade é: {}, do {} tem o preço de {}".format(quantidade,item,preco))


#Operadores Aritimeticos 

#soma
print(1+2)
#subtração
print(1-2)
#divisão 
print(1/2)
#multiplicação
print(1*2)
#modulo
print(1%2)
#exponeciação
print(1**2)
#parte inteira da divisão
print(81//9)

#operadores de atribuição

x1 = 5
print(x1)
x1+=5
print(x1)
x1-=5
print(x1)
x1*=5
print(x1)
x1 /=5
print(x1)
x1%=5
print(x1)
x1+=5
print(x1)
x1**=5
print(x1)

#listas
listaDeFrutas = ['banana','maça', 'uva']
print(listaDeFrutas)

#print de elemento de uma lista 
print(listaDeFrutas[1])

#Edição de elemento da lista
listaDeFrutas[1] = 'laranja'
print(listaDeFrutas)

#adicionar sobrescrevendo elementos
listaDeFrutas = ['maça','pessego','limão']
print(listaDeFrutas)

#adicionar elemento a lista de forma incremental
listaDeFrutas.append('uva')
print(listaDeFrutas)

#adicionar elemento a lista de acordo com index informado
listaDeFrutas.insert(1,'mamão')
print(listaDeFrutas)

#remover um elemento pesquisado na lista
listaDeFrutas.remove('mamão')
print(listaDeFrutas)

#remove o ultimo elemento ou index definido na lista
listaDeFrutas.pop()
print(listaDeFrutas)

def funcao(): #criei essa função apenas para  poder percorrer o for 
    #percorrendo a lista com um vetor
    for x in listaDeFrutas:
     print(x)

funcao()

#mostra o comprimento da lista 
print(len(listaDeFrutas))

#Turplas 
#são escritas de formas imutáveis

turplasFrutas = ['pera','uva','maçã']
print(turplasFrutas)

#printa elemento de determinada possição de uma turpla
print(turplasFrutas[0])

#percorrer uma turpla imutavel 
for y in turplasFrutas:
    print(y)

#pesquisa um elemento na turpla
if 'pera' in turplasFrutas:
    print("Existe pera")

#mostra o comprimento da turpla
print(len(turplasFrutas))

#conjuntos de sets são listas desordenas e não indexadas

setFrutas = {'uva', 'pera', 'maçã'}
print(setFrutas)

#busca se existe algum elemento no SET
print("banana" in setFrutas)

#Adicionar um elemento ao set
setFrutas.add("banana")
print(setFrutas)

#adicionar varios itens no set 

setFrutas.update(["morango", "manga", "tomate"])

print(setFrutas)

#comprimento de um set 
print(len(setFrutas))

#Não é possivel alterar itens depois que o conjunto é criado 

#remover um elemento pesquisado na lista se o item pesquisado não existir gera um erro
setFrutas.remove("tomate")
print(setFrutas)

# já no caso do discard se o elemento não existir não retornará um erro 
setFrutas.discard("tomate")
print(setFrutas)

#removendo o ultimo elemento do set 
setFrutas.pop()
print(setFrutas)

#esvaziar um conjunto
setFrutas.clear()
print(setFrutas)

#deletar o set
del setFrutas

#dicionários em python
dicionarioVendas = {
    "item"           : "Comida",
    "nome"           : "Peixe",
    "preco"          :  22.02,
    "dataValidade"   :  "15/07/2020"
}

print(dicionarioVendas)

#acessando determinado iten do dicionario
print(dicionarioVendas["nome"])
# utiliza o get tem a mesma equivalencia
print(dicionarioVendas.get("nome"))

#mostra o tamanho do dicionario
print(len(dicionarioVendas))

#alterar um lemento do dicionaio 
dicionarioVendas["nome"] = "Boi"
print(dicionarioVendas)

#percorre um dicionario 
for z in dicionarioVendas:
    print (z)

#percorre e printa os elemento do dicionario
for a in dicionarioVendas:
    print(dicionarioVendas[a])

#para retorna apenas os valores do dicionario
for b in dicionarioVendas.values():
    print(b)

#para adicionar mais um elemento ao dicionario
dicionarioVendas["id"] = 1
print(dicionarioVendas)

#remover um item do dicionario
dicionarioVendas.pop("item")
print(dicionarioVendas)

#remover o ultimo item do dicionario
dicionarioVendas.popitem()
print(dicionarioVendas)

#Se e Else
k = 10
u = 10

#operador de igualdade
print(k==u)

#operador diferente
print(k!=u)

#operador maior e menor 
print(k<u,k>u)

#operador marior igual e menor igual
print(k<=u, k>=u)

#se, se não se e se não
if k > u:
    print("{} é maior que {}".format(k,u))
elif k<u:
    print("{} é menor que {}".format(k,u))
else:
    print("{} é igual {}".format(k,u))


# laços de repetição 
m = 1
while m < 6:
    print(m)
   # m = (m + 1)
    m+=1

#parando um laço de repetição com Bleak
n = 1
while n < 10:
    print(n)
    if n == 5:
        break
    n+=1

#instrução continue 
o = 0
while o < 5:
    o += 1
    if o == 3:
        continue
    print(o)


# trabalhando com FOR
montadoras = ['BMW', 'Ferrari','Lamburguini', 'ConningSER', 'Chevrolet', 'Fiat']
for x in montadoras:
    print(x)

#para o fro possuirmos um break tambem

for x in montadoras:
    print(x)
    if x == 'Ferrari':
        break

# para o for utilize o continue 

for x in montadoras:
    print(x)
    if x == 'BWM':
        continue

#usando função com range tipo limite de contage do laço

for x in range(3):
    print(x)

# usando o ranger delimitado 

for x in (2,6):
    print(x)

#matriz
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)


#função uma função é um bloco de código que só é usado quando chamado 

#função sem parâmetros
def funcaoTeste():
    print("Esta função foi chamada")

funcaoTeste()

#função passando parâmetros
def funcaoComParametros(nome):
    print("Esse é o nome", nome)

funcaoComParametros("Alex")

#função com padrão de dados passado 
def funcaComParametrosPadrao(nomePais="Brasil"):
    print("O nome do pais é: ", nomePais)

funcaComParametrosPadrao("India")
funcaComParametrosPadrao()

# função com resturn

def funcaoComRetorno(x):
    return x * x

print (funcaoComRetorno(10))


#função recursiva 
def funcaorecursiva(valorK):
    if valorK > 1:
        valorK -= 1
        print(valorK)
        funcaorecursiva(valorK)
    else:
        print("Fim da recursão", valorK)

funcaorecursiva(6)

#função lambda
x2 = lambda a:a +10 
print(x2(5))

#funçcão lambda multiplicando
x6 = lambda f , g : f * g

print(x6(10,10))

#funcão lambda com muitos elementos
x7 =lambda  i,j,k : i + j + k 

print(x7(1,2,3))

#Arrays são usados como matrizes de dados para armazenas varios valorees em uma unica variável

carros =  ["Ford", "Volvo", "BMW", "Fiat"]

#Acessando um elemento na matriz

print(carros[2])

#comrimento da array

print(len(carros))

# percorrendo o vetor

for x in carros:
    print(x)


#adicionar um elemento ao vetor
carros.append("Honda")
print(carros)

#remover um elemento no final  da matriz ou um index
carros.pop()
print(carros)

#remover por pesquisa de primeira ocorrência
carros.append("Volvo")
carros.remove("Volvo")
print(carros)

# método esporádico  que retorna media 

def media(a,b):
    media = (a + b)/2
    print(media)

media(2,2)

#Python é uma linguagem orientada a objetos quase tudo é um um obejeto com suas propiedades e métodos.
# Uma classe é como um construtor de obejetos, ou um modelo para criar um objeto

#criar uma classe
class NovaClass:
    x = 5

# lendo objeto da classe

p1 = NovaClass()
print(p1.x)


#Iterators
# Um interator  é um objeto que contém um numéro de valores contáveis.
# um Interator é um objeto que pode ser incrementado por cima,

listaFrutas = ("Apple", "Banna", "Cherry")
interator = iter(listaFrutas)

print(next(interator))
print(next(interator))
print(next(interator))

#percorrendo turpla fom laço 
for x in listaFrutas:
     print(x)


#inteiração dentro de uma string
strFruta = "Banana"
for x in strFruta:
    print(x)


# para criar um obejeto com um interator é nescessário criar um obejtico no __init()__ e __next()__

class InteratorNumber:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

interatorNumber = InteratorNumber()
interatorNumber = iter (interatorNumber)

print(next(interatorNumber))
print(next(interatorNumber))
print(next(interatorNumber))
print(next(interatorNumber))


# chamada de modulos 

import TesteModulo as TM # um modulo pode ser nomedo por um alias

#TesteModulo.cumprimento("Yoga")
TM.cumprimento("Yoga")

#ab = TesteModulo.pessoa["idade"] # chamada de modulo especifico
ab = TM.pessoa["idade"] # chamada de modulo especifico
print(ab)

ac = TM.pessoa["nome"]
print(ac)

# trabalahando com datas em python

import datetime as dt

#imprime a data 
print(dt.datetime.now())

data = dt.datetime.now()

#retorna um objeto inteiro como int
print(data.year)

#Retorna o dia da semna em full vresion
print(data.strftime("%A"))

#Retorna a data rezumida 
print(data.strftime('%a'))

#Retorna o dia da semana em formato numerioco de 0-6
print(data.strftime("%w"))

#Retorna o dia do mês em formato numerico de 01-31
print(data.strftime("%d"))

#Retorna o  mês em formato resumido
print(data.strftime("%b"))

#Retorna o mês em full formate
print(data.strftime("%B"))

#Retorna o numero do mês de  1-12
print(data.strftime("%m"))

#Retorna o ano em versão resumida
print(data.strftime("%y"))

#Retorna o ano em versão full
print(data.strftime("%Y"))

#Retorna o hora em formato 24hrs
print(data.strftime("%H"))

#Retorna a hora em formato 12hrs
print(data.strftime("%I"))

#Retorna se é manha ou tarde 
print(data.strftime("%p"))

#Retorna os minutos
print(data.strftime("%M"))

#Retorna os seguntos
print(data.strftime("%S"))

#Retorna os microsegundo entre 00000-999999
print(data.strftime("%f"))

#Retorna o UTC OOFSET
print(data.strftime('%z'))

#Retorna a timezone
print(data.strftime('%Z'))

#Retorna o dia do ano entre 1-365
print(data.strftime("%j"))

#Retora o dia da semana do ano entre 00-53
print(data.strftime("%U"))

#Retorna a versão local do date time
print(data.strftime("%c"))

#Retorna a versão local 
print(data.strftime("%x"))

#Retorna a versão full
print(data.strftime("%X"))

#Retorna..
print(data.strftime("%%"))


#Adicionar data fixada
import datetime as DR

xA = DR.datetime(2020, 5, 17)
print(xA)


#Json com python

import json as js

# Carga de um json no python é um dicionário 

# some JSON:
umJson =  '{ "name":"John", "age":30, "city":"New York"}'

#parse do json

pJson = js.loads(umJson)

#leitura do dicionario
print(pJson['name'])

#conversão de um dicionario para json

dicionarioJson = js.dumps(pJson)

print(dicionarioJson)

#formatar  json

jsonFormatado = js.dumps(pJson, indent=4)

print(jsonFormatado)

# print json com separato formatado
jsonFormatado = js.dumps(pJson, indent=4, separators=(".", "="))

print(jsonFormatado)

#Tambem com parametros ordenados
jsonFormatado = js.dumps(pJson, indent=4, separators=(".", "="), sort_keys=True)

print(jsonFormatado)

#RegEX ou Expressões regulares São um padrão de caracteres em pesquisa
#RegeEX pode ser usado para verificar se uma string tem um determindao padrão 

# no python tem um pacote incorporado nele

import re
txt12 = "The rain in Spain"
reX =  re.search("^The.*Spain$", txt12)
if reX:
    print("Deu match")
else:
    print("Não deu match")

print(txt12)
print(reX) # mostra o objeto de busca da string


#Returns a list containing all matches
#Retorna uma lista contendo todas as correspondências
txt11 = "a lua cheia clareia as ru@s do capão 1 "
reX = re.findall("as",txt11)
print(reX)

#Retorna um objeto Match se houver uma correspondência em qualquer lugar da string
reX = re.search("lua",txt11)
print(reX)

#Divide a string de acordo com uma ocorrencia definida
reX = re.split("clareia",txt11) # a palavra como argumento de divisão é suprimida
print(reX)

#Subistitui uma ocorrecia na string
reX = re.sub("\s", "*", txt11)
print(reX)

# Retorna se tem caracteres numericos de 0-9
reX = re.search("\d",txt11)
print(reX)

#busca uma sequencia inicidada em detereminado caractwes e teminda
reX= re.findall("clar..a", txt11)
print(reX)

#Caracteres iniciados
reX = re.search("^cheia",txt11)
print(reX)   

# teste de instalador de pacotes pip
import camelcase
c = camelcase.CamelCase()
txte = "hello world"
print(c.hump(txte))

#testanto o controle de exeções do python o bloco try permite verificar se existe um erro "tente"
#O trybloco permite testar um bloco de código para erros.
#O exceptbloco permite manipular o erro.
#O finallybloco permite executar código, independentemente do resultado do tentar- e, exceto blocos.

try:
    print(alfa)
except NameError:
    print("variavel não instanciada")

# entradas do teclado 
# no python 3 em diante se utiliza o input().
# no python 2.7 inferior se utiliza raw_input().

print("Diga seu nome")
#nome = input()
print("Olá ",nome)

#Formatar string 
#utilizar o metodo format() permite formatar partes selecionadas da string

preco = 49
txt = "Opreço é {} reais"
print(txt.format(preco))

#Formatar preço com 2 casas depois da virgyla
txt = "O preço é {:.2f} reais"
print(txt.format(preco))

# formatar string com varios valores
txt = "O preço de é {:.2f} reias, com desconto de {}%"
desconto = 10
print(txt.format(preco,desconto))

# formatar com index´s, podem ser repetidos tambem 
txt = "O preço de é {0:.2f} reias, com desconto de {1}% + {1}%"
print(txt.format(preco,desconto))

#Formatar com index´s nomeados 
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))

exit()

