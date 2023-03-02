from .api_key import API_KEY
import openai
import os

class StartChat:

    # Definindo o método de inicialização da classe
    def __init__(self, IA_config):

        # Declarando a API e Histórico do chat
        openai.api_key = API_KEY
        self.IA_config = IA_config
        self.logs = {'mensagens': {'usuário': 0, 'IA': 0, 'total': 0}, 'tokens na conversa': 0}
        self.historico = [
            {"role": "system", "content": IA_config}, # Adicionando o primeiro contexto ao GPT
        ]

    # Definindo o método chat
    def chat(self, prompt_user):

        # Adicionando histórico
        self.historico.append({"role": "user", "content": prompt_user})

        # Logs
        self.logs['mensagens']['usuário'] += 1

        # Requisição ao GPT-3.5-TURBO
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.historico
        )

        # Resposta do GPT (Prompt e tokens)
        response_IA = response['choices'][0]['message']['content']
        tokens =  response['usage']['total_tokens']

        # Adcionando histórico e logs
        self.historico.append({"role": "assistant", "content": response_IA})
        self.logs['mensagens']['IA'] += 1
        self.logs['mensagens']['total'] = self.logs['mensagens']['usuário'] + self.logs['mensagens']['IA']
        self.logs['tokens na conversa'] += tokens

        # Retornando resposta para o usuário
        return response_IA
    
    # Definindo outros Métodos
    
    # Limpar a tela
    def clear(self):
        os.system("clear")

    # Logs
    def logs_method(self):
        return self.logs
    
