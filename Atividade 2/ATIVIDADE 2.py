def calcular_idades():
    try:
        idade_homem1 = int(input("\n\tDigite a idade do primeiro homem: "))
        idade_homem2 = int(input("\n\tDigite a idade do segundo homem: "))
        idade_mulher1 = int(input("\n\tDigite a idade da primeira mulher: "))
        idade_mulher2 = int(input("\n\tDigite a idade da segunda mulher: "))
        
        if any(idade <= 0 for idade in [idade_homem1, idade_homem2, idade_mulher1, idade_mulher2]):
            print("\n\tErro: Todas as idades devem ser números inteiros positivos.")
            return

        homem_mais_velho = max(idade_homem1, idade_homem2)
        homem_mais_novo = min(idade_homem1, idade_homem2)
        
        mulher_mais_velha = max(idade_mulher1, idade_mulher2)
        mulher_mais_nova = min(idade_mulher1, idade_mulher2)

        soma = homem_mais_velho + mulher_mais_nova
        produto = homem_mais_novo * mulher_mais_velha

        print(f"\n\tSoma do homem mais velho com a mulher mais nova: {soma}")
        print(f"\n\tProduto do homem mais novo com a mulher mais velha: {produto}")

    except ValueError:
        print("\n\tErro: Certifique-se de inserir números inteiros válidos para as idades.")

calcular_idades()


