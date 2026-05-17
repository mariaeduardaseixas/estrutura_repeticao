# Execícios extras sobre estruturas de decisão e repetição

# 1. Validador de Complexidade de Senha

# Garantir que uma senha tenha o comprimento mínimo e caracteres especiais.
# Regras:
# 1. Comprimento mínimo: 8 caracteres;
# 2. Um caracter maiúsculo;
# 3. Um caracter minúsculo;
# 4. Um caracter especial;
# 5. Um número;

# Lógica: Percorrer a string caractere por caractere para validar critérios.
# Resultado Esperado: "Senha forte" ou lista de requisitos ausentes.



senha = input("Digite sua senha: ")
especiais = "!@#$%¨&*(()))_{}[]^,.><;?/\|"

tem_maiuscula = False
tem_minuscula = False
tem_numero = False
tem_especial = False



for caracter in senha:
    if caracter.isupper():
        tem_maiuscula = True

erros = []
if not tem_maiuscula:
    erros.append("falta de carctere maiúsculo")
if len(erros) == 0:
    print("Senha forte!")
else:
    print("Senha inválida")
    print("Requisistos ausentes")

for caracter in senha:
    if caracter.islower():
        tem_minuscula = True
erros = []
if not tem_minuscula:
    erros.append("Falta de caractere minúsculo")
if len(erros) == 0:
    print("Senha forte!")
else:
    print("Senha inválida")
    print("Requisitos ausentes")

for caractere in senha:
    if caractere.isdigit():
        tem_numero = True
erros = []
if not tem_numero:
    erros.append("Falta de números")
if len(erros) == 0:
    print("Senha forte!")
else:
    print("Senha inválida")
    print("Requisistos ausentes")

for caractere in especiais:
    tem_especial = True
erros = []
if not tem_especial:
    erros.append("Falta de caracteres especiais")
if len(erros) == 0:
    print("Senha forte!")
else:
    print("Senha inválida")
    print("requisistos ausentes")
