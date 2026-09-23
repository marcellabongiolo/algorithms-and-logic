# 🧠 Algorithms & Logic Lab

Laboratório de **algoritmos, lógica de programação e fundamentos de ciência da computação** usando Python.

O objetivo é manter implementações pequenas, claras e testáveis para praticar raciocínio algorítmico e análise de eficiência.

## 🔬 Projeto atual

### Verificador de números primos

O arquivo `verificador_primo.py` implementa `eh_primo()`, uma função que verifica se um número inteiro é primo.

A implementação usa divisores até a raiz quadrada e elimina previamente múltiplos de 2 e 3. Para os candidatos restantes, os testes avançam de 6 em 6, verificando as formas `6k - 1` e `6k + 1`.

A complexidade temporal é **O(√n)** no pior caso e o uso adicional de memória é **O(1)**.

## 🛠️ Tecnologias

- Python 3.10+
- `unittest`
- GitHub Actions
- PEP 8 e type hints

## ▶️ Como executar

```bash
python verificador_primo.py
```

Depois, informe um número inteiro quando solicitado.

## 🧪 Testes

Execute:

```bash
python -m unittest discover -s tests -v
```

Os testes cobrem números primos e compostos, valores menores que 2, entradas pares e múltiplas de 3 e casos de fronteira.

A integração contínua executa os testes automaticamente em pushes para `main` e pull requests.

## 📁 Estrutura

```text
algorithms-and-logic/
├── .github/
│   └── workflows/
│       └── tests.yml
├── tests/
│   └── test_verificador_primo.py
├── .gitignore
├── LICENSE
├── README.md
└── verificador_primo.py
```

## 🚀 Próximos passos

- adicionar busca binária e outros algoritmos clássicos;
- estudar estruturas de dados;
- comparar implementações por complexidade;
- adicionar exercícios de ordenação;
- documentar trade-offs de cada algoritmo.

## 👩‍💻 Autora

**Marcella Bongiolo**

Este repositório faz parte da prática de desenvolvimento e estudos em programação.

## 📄 Licença

Distribuído sob a licença MIT.
