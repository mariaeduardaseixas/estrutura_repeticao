
# 3. Sanitização de Nome de Arquivo
# Remover espaços e converter para minúsculas para evitar erros em servidores Linux.

# Lógica: Iterar sobre a string e reconstruí-la sem caracteres inválidos.

# Resultado Esperado: String limpa (ex: "relatorio_final.pdf").

# nome_arquivo = input("Digite o nome do seu arquivo: ")

nome_arquivo = input("Digite o nome do arquivo :")

resultado = nome_arquivo.replace(" ", "").lower()

print(resultado)


