# Algoritmo para Criar um Autômato Finito
BCC/UESPI: Bloco VII

## 🗒️ Descrição: 
- No repositório existe uma pasta de teste (<strong>gramaticas</strong>);
- O argoritmo recebe as informações das gramáticas e cria um autômato finito;
- O algoritmo recebe uma palavra e verifica se o autômato a reconhece;
- Se reconhecer, imprime: "<strong>A palavra é reconhecida</strong>", caso contrário, imprime: "<strong>A palavra não é reconhecida</strong>".

## ▶️ Como usar
### 1- Para rodar o código: <br>
- O código já tem definidos uma gramática e uma palavra de teste;
- Para rodar, execute o arquivo <strong>main.py</strong>;
- Aparecerá o imput: "<strong>Insira uma palavra para verificar: </strong>", então digite a palavra desejada.
> Para escolher outra gramática, altere o arquivo a ser lido na <strong>linha 13</strong> no arquivo <strong>main.py</strong>.

### 2- Para definir uma nova gramática: <br>
- Na pasta <strong>gramaticas</strong>, crie um novo arquivo de texto;
- Insira as informações com base no exemplo a seguir:
  
![Captura de tela 2023-11-21 115730](https://github.com/juliamscc/automato-finito/assets/66495320/dc4b79a8-fa33-49d2-8160-5d323d0193e8)

  - Na linha 1, informe os estados separando-os com espaços;
  - Na linha 2, informe o estado inicial;
  - Na linha 3, informe os estados finais separando-os com espaços;
  - A cada nova linha, informe as transições seguindo o modelo: <<em>estado-atual</em>> <<em>caractere-lido</em>>:<<em>próximo estado</em>>
  - A cada nova linha, informe as transições seguindo o modelo <strong>A a:B</strong>, sendo:
    - A: estado atual;
    - a: caractere lido;
    - B: próximo estado. 
