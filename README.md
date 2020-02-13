### game-simulator

```
$ tree .
.
├── application.py - Classe responsável por iniciar aplicação
├── apps - pacote onde contem os objetos de negocios, serviços expostos e toda a regra do game
│   └── __init__.py
├── config.py - arquivo de configurações
├── __init__.py
├── README.md
└── setup.py - informações do projeto
```
### Objetos de negocio

- gameBoard.py Classe usada para definir um objeto que representaria o tabuleiro do jogo, em toda a simulação ele é iniciado com as 20 posições, com as suas respectivas propriedades(house.py) de cada posição.
- house.py Representa as propriedades a venda em cada posição do jogo, ao serem inicializadas no gameBoard, elas ja assumem um valor de venda e locação gerados por uma função que geranumeros aleatórios.
- player.py - Representa o jogador
- playerType.py - Enum com o tipo de jogador
- positionBoard.py - Classe que no momento do jogo vai armarzar as informações se uma determinada posição a propriedade tem um dono, que é o dono, etc.
- business.py - Onde contem toda a logica de negocio do jogo, bem como os metodos que que vão gerar o relatório de saída
- api.py - Classe responsavel por expor um serviço REST, que irá retornar algumas informações sobre a simulação do jogo


### Pré Requisitos

Antes de rodar o projeto precisamos verificar a versão do python e importar as seguintes libs

python-version = python 3,8
pip3,8 install pandas
pip3,8 install flask
pip3,8 install flask-restful
pip3.8 install python-dotenv


### RUN

Para executar e testar o projeto, basta ir até raiz do projeto e executar o seguinte comando

```python
python3.8 application.py
```
Acessar o navegador em [App](http://0.0.0.0:5000/)

