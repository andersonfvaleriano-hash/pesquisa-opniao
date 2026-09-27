# Pesquisa de Opinião - TudoWeb

print("=" * 55)
print("          PESQUISA DE OPINIÃO - TUDOWEB")
print("=" * 55)

# Contadores das respostas
quantidade_excelente = 0
quantidade_ruim = 0

# Pesquisa com 50 entrevistados
for entrevistado in range(1, 51):

    print(f"\n--- Entrevistado {entrevistado} de 50 ---")

    # Entrada dos dados pessoais
    nome = input("Digite o nome: ").strip()

    idade = int(input("Digite a idade: "))

    # Solicitação da opinião
    print("\nOpções de atendimento:")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")

    opiniao = input("Digite o número ou o nome da opção: ").strip().lower()

    # Enquanto a opinião não for uma opção válida,
    # o programa solicita uma nova resposta.
    while not (
        opiniao == "1"
        or opiniao == "2"
        or opiniao == "3"
        or opiniao == "excelente"
        or opiniao == "bom"
        or opiniao == "ruim"
    ):
        print("\nOpção inválida!")
        print("Digite 1, 2, 3, EXCELENTE, BOM ou RUIM.")

        opiniao = input("Digite novamente sua opinião: ").strip().lower()

    # Verifica se a resposta corresponde a EXCELENTE
    if opiniao == "1" or opiniao == "excelente":
        quantidade_excelente += 1
        descricao_opiniao = "EXCELENTE"

    # Verifica se a resposta corresponde a BOM
    elif opiniao == "2" or opiniao == "bom":
        descricao_opiniao = "BOM"

    # Verifica se a resposta corresponde a RUIM
    elif opiniao == "3" or opiniao == "ruim":
        quantidade_ruim += 1
        descricao_opiniao = "RUIM"

    # Condição complementar utilizando AND
    if idade >= 18 and idade <= 120:
        situacao_idade = "idade registrada corretamente."
    else:
        situacao_idade = "idade fora do intervalo esperado."

    print(f"\nObrigado pela participação, {nome}!")
    print(f"Idade: {idade} anos")
    print(f"Opinião registrada: {descricao_opiniao}")
    print(situacao_idade)


# Resultado final
print("\n" + "=" * 55)
print("              RESULTADO DA PESQUISA")
print("=" * 55)

print(f"Quantidade de respostas EXCELENTE: {quantidade_excelente}")
print(f"Quantidade de respostas RUIM: {quantidade_ruim}")

print("=" * 55)
print("Pesquisa finalizada. Obrigado pela participação!")
print("=" * 55)