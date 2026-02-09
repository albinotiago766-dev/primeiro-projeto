def analisar_lista(nums):
    if not nums:
        return 0, 0, None

    soma_primos = 0
    qtd_pares = 0
    maior_impar = None

    for n in nums:
        if n % 2 == 0:
            qtd_pares += 1
            continue

        if maior_impar is None or n > maior_impar:
            maior_impar = n

        if n <= 1:
            continue

        eh_primo = True
        limite = int(n ** 0.5) + 1

        for i in range(2, limite):
            if n % i == 0:
                eh_primo = False
                break

        if eh_primo:
            soma_primos += n

    return soma_primos, qtd_pares, maior_impar


if __name__ == "__main__":
    print(analisar_lista([3, 4, 7, 8, 11, 12, 13, 2]))
