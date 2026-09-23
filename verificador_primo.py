"""Verificador de números primos.

O módulo implementa uma verificação determinística de primalidade para
inteiros usando divisores até a raiz quadrada do número.
"""


def eh_primo(numero: int) -> bool:
    """Retorna True quando o inteiro informado é um número primo."""
    if not isinstance(numero, int) or isinstance(numero, bool):
        raise TypeError("O valor deve ser um número inteiro.")

    if numero <= 1:
        return False

    if numero <= 3:
        return True

    if numero % 2 == 0 or numero % 3 == 0:
        return False

    divisor = 5

    while divisor * divisor <= numero:
        if numero % divisor == 0 or numero % (divisor + 2) == 0:
            return False
        divisor += 6

    return True


def executar_teste() -> None:
    """Executa a interface de linha de comando do exercício."""
    print("=" * 50)
    print("LABORATÓRIO DE ALGORITMOS — VERIFICADOR DE PRIMOS")
    print("=" * 50)

    try:
        entrada = int(input("Digite um número inteiro para testar: "))
        resultado = "PRIMO" if eh_primo(entrada) else "NÃO é primo"
        print(f"Resultado: {entrada} {resultado}.")
    except ValueError:
        print("Erro: informe um número inteiro válido.")

    print("=" * 50)


if __name__ == "__main__":
    executar_teste()
