<div align="center">

<img src="/assets/image.png"> 

</div>

--- 

### Tecnolgias Utilizadas:

![python](https://img.shields.io/badge/PYTHON-29699c?&logo=python&logoColor=ffe25c&style=flat&logoWidth=30)

### Ferramentas Utilizadas:

![vscode](https://img.shields.io/badge/VS%20CODE-0078d7?&logo=visualstudiocode&logoColor=white&style=flat&logoWidth=30)

## Detalhes:
Iniciado no dia 07/03/23 e finalizado no dia 14/03/23.

Faça download de videos e musicas direto do youtube de forma rápida e facil pelo terminal.

---
## Como usar?

⚠ OBSERVAÇÃO: 
Para executar o projeto, é necessário possuir python v3.9 ou superior em seu computador.

⚠ RECOMENDAÇÃO: 
Possua o Visual Studio Code para melhor experiencia e execução dos comandos abaixo.

### 1. Clone esse repositório;

Para clonar esse repositório na sua maquina, utilize o comando git clone juntamente a URL desse repositório, assim:

```git clone https://github.com/JonathasSC/load-tube```

### 2. Criando ambiente virtual;

Após clonar o repositório em sua maquina, abra um terminal na raiz e efetue esse comando para criar um ambiente virtual: 
```python -m venv venv```

Perceba se foi criado uma pasta com o nome venv-todo na raiz, se sim, efetue esse comando para ativar seu ambiente virtual:
```./venv/Scripts/Activate```

### 3. Instale a lista de requerimentos necessários.

Para instalar todos os pacotes necessarios para que o projeto
 seja executado corretamente, será necessario efetuar esse comando:
```pip install -r requirements.txt```

### 4. Execute o projeto em seu computador:

Com tudo instalado, navegue até o arquivo main.py dentro do diretorio resources e execute-o


### 5. Selecione a opção de download desejada

Ao executar main.py, deverá aparecer um input pedindo uma das opções de download disponiveis.

digite a opção desejada e pressione ENTER

### 6. Copie e Cole o link:

Ao selecionar a opção desejada, perceba um input que espera o link do video desejado, vá até o youtube.com e copie o link do video que deseja baixar, cole-o nesse input e pressione ENTER.

### 7. Confira o download.

Espere o download terminar e confira-o na pasta downloads/musics ou downloads/videos.

--- 

## ERROS COMUNS:

### ModuleNotFoundError:

Ao ocorrer esse erro mesmo após instalação sem erros do requirements.txt, confira na sua IDE se seu interpretador python está configurado como o da venv criado anteriormente.