# chatgpt-cli
Aplicação em Python de IA conversacional utilizando GPT-3.5-TURBO

## Instalação

Para executar a aplicação, é necessário ter Python 3.6 ou superior instalado. Além disso, é preciso instalar as seguintes bibliotecas:

- openai
- numpy
- nltk

Para instalar as bibliotecas, execute o seguinte comando no terminal:

```
pip install openai numpy nltk
```

## Utilização

Para utilizar a aplicação, basta executar o arquivo `main.py` no terminal:

```
python main.py
```

A aplicação irá iniciar e aguardará a entrada do usuário. Basta digitar uma pergunta ou mensagem e pressionar Enter para obter a resposta da IA.

## Configuração

Antes de executar a aplicação, é preciso configurar a chave de API da OpenAI. Para isso, edite o arquivo em:

```
/src/api_key.py
```

Substitua o conteúdo da variável pela sua chave de API da OpenAI.

### Comportamento da IA
edite o comportamento da sua IA alterando a string em `main.py` que serve de parâmetro para a class **StartChat()**
```python
conversa = StartChat('Você é um assistente prestativo')
```
