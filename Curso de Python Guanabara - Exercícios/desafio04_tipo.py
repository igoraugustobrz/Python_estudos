# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo e todas as informações possíveis sobre ele.
print("====== DESAFIO 4 ======")
algo = input("Digite algo: ")
print(f"O tipo do dado digitado é {type(algo)}")
print(f"O que foi digitado possui letras ou números? {algo.isalnum()}")
print(f"Todos os caracteres são ASCII? {algo.isascii()}")
print(f"Todos os caracteres são numéricos? {algo.isnumeric()}")
print(f"Todos os caracteres são decimais? {algo.isdecimal()}")
print(f"Todos os caracteres são espaços em brancos? {algo.isspace()}")
print(f"Todos os caracteres são dígitos? {algo.isdigit()}")
print(f"Caso seja uma string, ela é um identificador válido? {algo.isidentifier()}")
print(f"Todos os caracteres são imprimíveis? {algo.isprintable()}")
print(f"Caso seja uma string, todas as palavras do texto começam com uma letra maiúsculas? {algo.istitle()}")
print(f"Todas as letras (caso possua) estão maiúsculas? {algo.isupper()}")
print(f"Todas as letras (caso possua) estão minúsculas? {algo.islower()}")
print(f"Todos os caracteres são letras do alfabeto? {algo.isalpha()}")