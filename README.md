# Job Insights


  <strong>👨‍💻 O que foi desenvolvido</strong><br />
  <p align="center">
    <img src="images/job.png" alt="Logo Aplicação" width="300"/>
  </p>
  
  Neste projeto implementei análises a partir de um conjunto de dados sobre empregos.
  Os dados foram extraídos do site [Glassdoor](https://www.glassdoor.com.br/) e obtidos através do [Kaggle](https://www.kaggle.com/atharvap329/glassdoor-data-science-job-data), uma plataforma disponiblizando conjuntos de dados para cientistas de dados.
  <br>
  <br>
  🚵 Habilidades trabalhadas:
  <ul>
    <li>Utilizar o terminal interativo do Python.</li>
    <li>Utilizar estruturas condicionais e de repetição.</li>
    <li>Utilizar funções built-in do Python.</li>
    <li>Utilizar tratamento de exceções.</li>
    <li>Realizar a manipulação de arquivos.</li>
    <li>Escrever funções.</li>
    <li>Escrever testes com Pytest.</li>
    <li>Escrever seus próprios módulos e importá-los em outros códigos.</li>
  </ul>
<details>
  <summary><strong>⚠ Clonando É executando o projeto</strong></summary><br />

  1. Clone o repositório

  - Use o comando: `git clone git@github.com:jandui-Rodrigues/job-insights.git
  - Entre na pasta do repositório que você acabou de clonar:
    - `cd sd-031-b-project-job-insights`

  2. Crie o ambiente virtual para o projeto

  - `python3 -m venv .venv && source .venv/bin/activate`
  
  3. Instale as dependências

  - `python3 -m pip install -r dev-requirements.txt`
</details>
<!-- <details>
    <summary>
      🐳 <strong>Rodando o projeto com Docker</strong>
    </summary>
    <br>

Clone este repositório

    $ git clone git@github.com:jandui-Rodrigues/FutebolClub.git

Acesse a pasta do projeto no terminal/cmd

    $ cd job-insights

iniciando com compose o docker compose

    $ docker-compose up -d

Para remover os conteiners do docker-compose

    $ docker-compose compose-down

Criando uma imagem Docker

    $  docker build -t job-insights .
Criando um conteiner Docker

    $  docker run -d -it --name job-container -v .:/projeto job-insights

</details> -->
<details>
  <summary><strong>🏕️ Ambiente Virtual</strong></summary><br />
  O Python oferece um recurso chamado de ambiente virtual, onde permite sua máquina rodar sem conflitos, diferentes tipos de projetos com diferentes versões de bibliotecas.

  1. **criar o ambiente virtual**

  ```bash
  $ python3 -m venv .venv
  ```

  2. **ativar o ambiente virtual**

  ```bash
  $ source .venv/bin/activate
  ```

  3. **instalar as dependências no ambiente virtual**

  ```bash
  $ python3 -m pip install -r dev-requirements.txt
  ```
