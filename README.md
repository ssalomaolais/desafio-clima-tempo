# Desafio ClimaTempo - Modelagem de Fenômenos Naturais

![Linguagem](https://img.shields.io/badge/Python-3776AB?logo=python)
![Bibliotecas](https://img.shields.io/badge/Bibliotecas-NumPy%20%7C%20Matplotlib-blue)

## 📖 Descrição do Projeto

Este projeto, parte do desafio "ClimaTempo", consiste na implementação, visualização e análise de duas funções matemáticas que modelam fenômenos naturais complexos. O objetivo é utilizar Python e bibliotecas de computação científica para plotar os gráficos das funções e identificar seus pontos de máximo e mínimo, demonstrando a aplicação da programação na análise de eventos climáticos.

## 📈 Modelos Matemáticos Analisados

As duas funções modeladas no desafio são:

1.  **Onda de Calor (T(t))**: Descreve a variação da temperatura em função do tempo (em meses).
    T(t) = 35 + (1 - e^{-\frac{t}{27}}) + te^{-34,33t} 

2.  **Movimentos Anômalos da Terra (e(x))**: Modela a intensidade na escala Richter com base na velocidade de deslocamento do solo (em m/s).
   e(x) = 5,47 + 1,85e^{-x}\cos(\sqrt{8}x - 19,47) + (x-1,365)e^{-34,33x} 

## 🛠️ Tecnologias Utilizadas

* **Python**: Linguagem principal para a implementação da lógica.
* **NumPy**: Para cálculos numéricos eficientes e manipulação de arrays.
* **Matplotlib**: Para a plotagem e visualização dos gráficos das funções.

## 🚀 Como Executar

Para executar o script e gerar os gráficos e a análise, siga os passos abaixo.

1.  **Clone este repositório:**
    ```bash
    git clone [https://github.com/SEU-USUARIO/desafio-clima-tempo.git](https://github.com/SEU-USUARIO/desafio-clima-tempo.git)
    cd desafio-clima-tempo
    ```

2.  **Crie e ative um ambiente virtual (recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

3.  **Instale as dependências necessárias:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute o script:**
    ```bash
    python desafio_clima_tempo.py
    ```
    * Ao executar, o script irá exibir uma janela com os gráficos das duas funções e salvará uma imagem (`graficos_clima_tempo.png`) no diretório do projeto.
    * Os resultados da análise (pontos de máximo e mínimo) serão impressos no terminal.

