# PLN
### Processamento de Linguagem Natural

<br>

#### TC 1.1

<details>
<summary>TERMINOLOGIA E CONCEITOS</summary>
Selecione uma obra literária de domínio público (ex. livros tais como Vinte mil léguas submarinas (de Júlio Verne), a Bíblia, etc.) e ilustre a variedade de dados presente. Considere, por exemplo a construção de frases, orações etc. e compare com expressões de uso corrente. Para respaldar sua resposta, elabore um programa que contabilize, por exemplo, o número de palavras diferentes. 

<br>

Hint: Utilizar obras mais antigas, textos infantis, etc. Pode ajudar você a ter insights relacionados a tal variedade. Considere textos de tamanho equivalente ou calcule um índice que permita dar a noção de variedade (ex: taxa de palavras distintas utilizadas em relação ao total de palavras do texto, para textos de tamanhos similares).

<br>

## Como executar

1. Clone o repositório:
  ```
  git clone https://github.com/amandavo/PLN.git
  ```
2. Entre nas pastas:
  ```
  cd PLN
  cd tc1_1
  ```
3. Instale o leitor de pdf:
  ```
  pip install pymupdf
  ```
4. Rode o programa:
  ```
  python count.py
  ```

</details>

<br>

#### PP 2.8

<details>
<summary>PRÁTICA DE PROGRAMAÇÃO</summary>
Exemplifique o funcionamento de um corretor ortográfico, aplicável à língua portuguesa, que efetue correção de palavras baseado em um corpus de texto considerado como referência e que utilize métricas de distância e estatísticas de ocorrência de palavras no corpus considerado. 

<br>

Alterar o corpus pode afetar o comportamento do corretor? Se sim, dê um exemplo prático utilizando dados diferentes para o corpus. 
A resposta a esse problema deverá ser um programa que: <br>
a) Leia uma frase digitada pelo usuário. <br>
b) Verifique se há ou não palavras potencialmente incorretas. <br>
c) Informe ao usuário a frase potencialmente corrigida ou então diga que a frase aparenta estar correta. 

<br>

## Como executar

1. Clone o repositório:
  ```
  git clone https://github.com/amandavo/PLN.git
  ```
2. Entre nas pastas:
  ```
  cd PLN
  cd pp2_8
  ```
3. Rode o programa:
  ```
  python corretor.py
  ```
  
</details>

<br>

#### PP 3.4

<details>
<summary>PRÁTICA DE PROGRAMAÇÃO</summary>
Demonstre a modelagem de tópicos, com LDA, utilizando alguns documentos representativos de revisões de produtos. Efetue todas as etapas de pré-processamento adequadas antes de efetuar a modelagem.

<br>

## Como executar

1. Clone o repositório:
  ```
  git clone https://github.com/amandavo/PLN.git
  ```
2. Entre nas pastas:
  ```
  cd PLN
  cd pp3_4
  ```
3. Crie a venv:
  ```
  python -m venv venv
  ```
4. Caso esteja pelo powershell, entre no command prompt: ``` cmd ```
5. Ative o ambiente virtual (venv):
  - No Windows, use:
    ```
    .\venv\Scripts\activate
    ```
  - No Linux/macOS, use:
    ```
    source venv/bin/activate
    ```
6. Instale as dependências do requirements.txt:
  ```
  pip install -r requirements.txt
  ```
7. Rode o programa:
  ```
  python app.py
  ```
  
</details>