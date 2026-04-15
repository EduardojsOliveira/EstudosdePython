adicao = 10 +10
print('Adição', adicao)

subtracao = 10 - 5
print('Subtração', subtracao)

multiplicacao = 10 * 10
print("Multiplicação", multiplicacao)

divisao = 10 / 2.2 #sempre o retorno vai ser float
print('Divisão', divisao)

#ele vai cortar, entregando o número inteiro, mas se houver um float na conta, o resultado final mantém o .0 . igual nesse exemplo o resultado fica 4.0
divisao_inteira = 10 // 2.2 

exponenciacao = 2 ** 10 #é um nunmero elevado a outro numero
print('Exponenciação', exponenciacao)

modulo = 25 % 5 #da o valor do resto da divisão
print('Modulo', modulo)

print(55 % 2) 

#usado o modulo posso ver se o numero é divisel pelo o nuemro que selecionei, se o resultado for 0 ele é divisive

#usando esse metodo da para saber se o numero é divisel pelo numero desejado
print(10 % 8 == 0)
print(16 % 8 == 0)
print(10 % 2 == 0)
print(15 % 2 == 0)