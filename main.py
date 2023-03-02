from src.app import StartChat

conversa = StartChat('Você é um assistente inteligente e prestativo que conversa sobre vários temas')

while True:
        
    prompt_user = input('\033[1;34m[#KRS] >\033[0;0m ')
    
    if prompt_user == 'exit':
        conversa.clear()
        break

    elif prompt_user == 'clear':
        conversa.clear()

    elif prompt_user == 'logs':

        logs = conversa.logs_method()
        print('\n \033[1;33m', logs, '\n \033[0;0m')

    else:
        resposta = conversa.chat(prompt_user)

        print('_________________________________________________\n')

        print(f'\033[1;93m[#GPT]:\033[0;0m {resposta}\n')

        print('_________________________________________________\n')
