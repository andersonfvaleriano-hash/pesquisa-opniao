# 📊 Pesquisa de Opinião - TudoWeb

Projeto desenvolvido em **Python** para realizar uma pesquisa de opinião com clientes da empresa de marketing **TudoWeb**, com o objetivo de identificar o grau de satisfação em relação ao atendimento prestado.

---

## 🎯 Objetivo

Desenvolver um programa utilizando **estrutura de repetição** para realizar uma pesquisa com **50 entrevistados**.

Para cada entrevistado, o programa solicita:

* Nome;
* Idade;
* Opinião sobre o atendimento.

As opções de atendimento são:

| Opção | Resposta  |
| ----- | --------- |
| `1`   | EXCELENTE |
| `2`   | BOM       |
| `3`   | RUIM      |

O programa permite que o entrevistado informe a opinião tanto pelo **número da opção** quanto pelo **nome da resposta**.

Por exemplo:

```text
1
```

ou:

```text
EXCELENTE
```

As duas entradas serão reconhecidas como **EXCELENTE**.

---

## 📝 Entrada das opiniões

O programa aceita as seguintes formas de entrada:

```text
1
2
3
```

ou:

```text
EXCELENTE
BOM
RUIM
```

A entrada também pode ser digitada em diferentes combinações de letras, como:

```text
Excelente
EXCELENTE
excelente
```

Isso é possível porque o programa utiliza:

```python
.lower()
```

para transformar a entrada em letras minúsculas antes de realizar as comparações.

---

## 📊 Contagem das respostas

Durante a pesquisa, o programa utiliza contadores para registrar as respostas **EXCELENTE** e **RUIM**.

Quando uma resposta EXCELENTE é identificada:

```python
quantidade_excelente += 1
```

Quando uma resposta RUIM é identificada:

```python
quantidade_ruim += 1
```

Ao final dos 50 entrevistados, os valores são apresentados na tela.

---

## 🖥️ Execução do programa

Para executar o programa pelo terminal do VS Code:

```bash
python app.py
```

Em alguns ambientes Windows, também pode ser utilizado:

```bash
py app.py
```

---

## 📁 Estrutura do projeto

```text
pesquisa-opiniao-tudoweb/
│
├── app.py
├── README.md
│
└── prints/
    ├── codigo.png
    ├── teste-10-entrevistados.png
    └── resultado.png
```

---

## 📸 Prints da atividade

O repositório deve conter os prints solicitados no enunciado, incluindo:

### Código

Print do arquivo `app.py` aberto no Visual Studio Code.

### Teste

Print da execução do programa durante o teste com 10 entrevistados.

### Resultado

Print mostrando a quantidade final de respostas:

```text
Quantidade de respostas EXCELENTE: 4
Quantidade de respostas RUIM: 3
```

---

## 🛠️ Tecnologias utilizadas

* **Python 3**
* **Visual Studio Code**
* **Git**
* **GitHub**

---

## 📚 Referência da atividade

Projeto desenvolvido como atividade acadêmica do curso Técnico em Desenvolvimento de Sistemas.
