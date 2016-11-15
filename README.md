# QuakeLogParser
QuakeLogParser é uma biblioteca que analisa os logs gerados pelo servidor do Quake3. A sua proposta é analisar e agrupar informações sobre partidas que estão contidas de maneira desorganizada nos logs de servidor do Quake. 

### Requisitos
Necessita da versão do Python 3.x.x ou maior instalada na máquina. 

### Organização do projeto
```sh
C:.
|   main.py
|   README.md
|
+---lib
|   |   print_data_quake.py
|   |   quake3.py
|   |   __init__.py
|   |
|   \---__pycache__
|           print_data_quake.cpython-35.pyc
|           quake3.cpython-35.pyc
|           __init__.cpython-35.pyc
|
\---resources
        game.log

```
 
Organização:
  - ./main.py contém uma demonstração do parse em funcionamento;
  - ./lib/quake3.py namespace para a classe LogParser;
  - ./lib/print_data_quake.py contém uma função para exibir o log analisado pela LogParser;
  - ./resources/game.log log em formato bruto gerado pelo servidor do Quake.

### Modo de utilização
```python
import os
from lib.quake3 import LogParser

game_log_path = os.path.join(os.getcwd(), 'resources', 'game.log')
log_parser = LogParser()
data = log_parser.parse(fullpath= game_log_path)
```
Exemplo de saída do método .parse() da classe LogParser:

```python
{  
   'game-17':{  
      'total_kills':95,
      'kills_by_means':{  
         'MOD_SHOTGUN':6,
         'MOD_RAILGUN':10,
         'MOD_ROCKET_SPLASH':32,
         'MOD_FALLING':1,
         'MOD_TRIGGER_HURT':12,
         'MOD_ROCKET':27,
         'MOD_MACHINEGUN':7
      },
      'players':[  
         'Mal',
         'Zeh',
         'Dono da Bola',
         'Isgalamido',
         'Assasinu Credi',
         'Oootsimo'
      ],
      'kills':{  
         'Assasinu Credi':9,
         'Zeh':20,
         'Isgalamido':14,
         'Oootsimo':10,
         'Dono da Bola':14,
         'Mal':2
      }
   },
   'game-6':{  
      'total_kills':89,
      'kills_by_means':{  
         'MOD_SHOTGUN':1,
         'MOD_RAILGUN':12,
         'MOD_FALLING':6,
         'MOD_ROCKET_SPLASH':39,
         'MOD_TRIGGER_HURT':9,
         'MOD_ROCKET':18,
         'MOD_MACHINEGUN':4
      },
      'players':[  
         'Oootsimo',
         'Isgalamido',
         'Zeh',
         'Assasinu Credi',
         'Mal',
         'Dono da Bola'
      ],
      'kills':{  
         'Assasinu Credi':10,
         'Zeh':12,
         'Isgalamido':20,
         'Dono da Bola':3,
         'Oootsimo':16,
         'Mal':-2
      }
   }, 
   [...]
}
``` 
### Teste
```sh
C:\QuakeLogParser>python main.py
```
Exemplo de saída do teste: 

![](http://i.imgur.com/2HFZxg2.png)