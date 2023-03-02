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

Antes de executar a aplicação, é preciso configurar a chave de API da OpenAI. Para isso, crie um arquivo `.env` na raiz do projeto e adicione a seguinte linha:

```
OPENAI_API_KEY=YourAPIKeyHere
```

Substitua `YourAPIKeyHere` pela sua chave de API da OpenAI.

## Contribuição

Sinta-se à vontade para contribuir com este repositório fazendo um fork e enviando suas alterações através de pull requests.

## Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo `LICENSE` para obter mais informações.
