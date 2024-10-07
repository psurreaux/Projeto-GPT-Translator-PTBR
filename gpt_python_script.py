import sys
import openai

# Insira sua chave de API da OpenAI aqui
openai.api_key = 'sua_chave_aqui'

def ask_openai(prompt):
    try:
        # Usando o modelo GPT-3.5-turbo ou GPT-4 com o endpoint correto
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # ou "gpt-4" se tiver acesso
            messages=[{"role": "user", "content": prompt}],
            max_tokens=100,
            temperature=0.5
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    # Obtendo o texto selecionado vindo do AutoHotkey
    selected_text = sys.argv[1]

    # Criando um prompt para definir ou traduzir o texto selecionado
    prompt = f"Define or translate the following text: '{selected_text}'"
    
    # Obtendo o resultado da OpenAI
    result = ask_openai(prompt)
    
    # Registrando o resultado em um arquivo de log para depuração
    with open("C:\\Users\\surre\\Desktop\\CODES\\gpt translator\\python_output_log.txt", "w") as log_file:
        log_file.write(f"Selected text: {selected_text}\n")
        log_file.write(f"Result: {result}\n")

    # Imprimindo o resultado para o AutoHotkey capturar
    print(result)
