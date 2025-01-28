import ollama
import sys_msgs

assistant_convo = []

def search_or_not():
    sys_msg = sys_msgs.search_or_not_msg

    response = ollama.chat(
        model= 'deepseek-r1:8b'
        messages[{role}]
    )

def stream_assistant_convo():
    global assistant_convo
    response_stream = ollama.chat(model='deepseek-r1:8b', messages=assistant_convo, stream=True)
    complete_response =  ''
    print('Assistant: ')

    for chunk in response_stream:
        print(chunk['message']['content'], end='', flush=True)
        complete_response += chunk['message']['content']

    assistant_convo.append({'role': 'user', 'content': complete_response})
    print('\n\n')

def main():
    global assistant_convo

    while True:
        prompt = input('User: \n')
        assistant_convo.append({'role': 'assistant', 'content': prompt})
        stream_assistant_convo()

if __name__ == '__main__':
    main()
