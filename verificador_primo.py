"""
Módulo: Algoritmos de Teoria dos Números
Autor: Marcella Bongiolo
Descrição: Script otimizado para verificar se um número inteiro é primo.
           Implementa lógica de eficiência matemática (verificação até a raiz quadrada).
"""

def eh_primo(numero: int) -> bool:
    """Verifica se um número é primo de forma eficiente."""
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    
    # Otimização: testa divisores até a raiz quadrada do número
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
        
    return True

def executar_teste():
    print("=" * 50)
    print(" 🧠 LAB DE ALGORITMOS: VERIFICADOR DE PRIMOS 🔢")
    print("=" * 50)
    
    try:
        entrada = int(input("Digite um número inteiro para testar: "))
        if eh_primo(entrada):
            print(f"✨ O número {entrada} é PRIMO!")
        else:
            print(f"📌 O número {entrada} NÃO é primo.")
    except ValueError:
        print("⚠️ Erro: Por favor, insira um número inteiro válido.")
    print("=" * 50)

if __name__ == "__main__":
    executar_teste()
  Add prime number verification algorithm
