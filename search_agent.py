import ollama
import sys_msgs

assistant_convo = [sys_msgs.assistant_msg]

def search_or_not():
    sys_msg = sys_msgs.search_or_not_msg

    response = ollama.chat(
        model= 'deepseek-r1:8b'
        messages[{'role': 'system', 'content': sys_msg}, assistant_convo[-1]]
    )

    content = response['message']['content']
    print("SEARCH CONTENT: ", content)  

    if 'true' in content.lower():
        return True
    else:
        return False
    
def query_generator():
    sys_msgs = sys_msgs.query_msg
    query_msg = f'CREATE A SEARCH QUERY FOR THIS PROMPT: {assistant_convo[-1]}'

    response = ollama.chat(
        model= 'deepseek-r1:8b'
        messages[{'role': 'system', 'content': sys_msgs}, {'role': 'user', 'content': query_msg}]
    )

    return response['message']['content']
    
def ai_search():
    context = None
    print('GENERATING SEARCH QUERY')
    search_query = query_generator()

    if search_query[0] == '"':
        search_query = search_query[1:-1]

    
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
        
        if search_or_not():
            context = ai_search()

        stream_assistant_convo()
if __name__ == '__main__':
    main()
