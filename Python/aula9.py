conta_1 = 1 + 1 ** 5 + 5  #7
print(conta_1)
#existem precedencia que deve ser seguidas, formulas dentro do ( ) vao ser exuctados primerio; depois em seugundo vai ser o **; o tercceiro vai ser *, /, //, %; e por ultimo vai ser o + e -
#se os operadores tiverem a mesma precendicas sera exucutados da esquerda pra direita.
#se quisermos outro resultado usaremos o ( ) pois ele vai excutar primerio a operação que estiver dentro dela
conta_2 = (1 + 1) ** (5 + 5) #aqui podemos ver q a soma foi executada primerio, por que a operação estava dentro do ( )
print(conta_2) # 1024

conta_3 = (1 + int(0.5 + 0.5)) ** (5 + 5)
print(conta_3) # 1024
