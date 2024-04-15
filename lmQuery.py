import openai 
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

openai.api_type = config.get('openai', 'api_type')
openai.api_base = config.get('openai', 'api_base')
openai.api_version = config.get('openai', 'api_version')
openai.api_key = config.get('openai', 'api_key')

def query_gpt35(question, arabic=False, context=[]):
    try:
        content = "You are an AI assistant that helps people find information."
        content += " Please answer in arabic." if arabic else ""
        
        message_text = [{"role": "system", "content": content}]
        message_text.extend(context)
        message_text.append({"role": "user", "content": question})
        
        completion = openai.ChatCompletion.create(
          engine='adversarial',
          messages = message_text,
          temperature=0.7,
          max_tokens=800,
          top_p=0.95,
          frequency_penalty=0,
          presence_penalty=0,
          stop=None
        )
        
        answer = completion['choices'][0]['message']["content"]
    
    except:
        answer = ''
        
    return answer

def generate_winner_prompt(prompt, response1, response2):
    template = f"### Instruction\nBased on the above responses, decide which response is better.\n\n### Prompt\n{prompt}\n\n### Response 1\n{response1}\n\n### Response 2\n{response2}"
    return template

def generate_evaluate_prompt(prompt, response):
    template = f"### Instruction\nRate this response on a scale of 1 to 10.\n\n### Prompt\n{prompt}\n\n### Response\n{response}"
    return template

def generate_evaluate_chat_prompt(prompts, responses):
    template = f"### Instruction\nRate this response on a scale of 1 to 10."
    for prompt, response in zip(prompts, responses):
        template += f"\n\n### Prompt\n{prompt}\n\n### Response\n{response}"
    return template