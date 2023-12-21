import openai

# 设置你的 OpenAI API key
openai.api_key = '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'

def chat_with_gpt3(message):
    # 调用 OpenAI GPT-3 API
    response = openai.Completion.create(
        engine='text-davinci-003',  # GPT-3 引擎
        prompt=message,
        max_tokens=1024,   # 生成的回复的最大长度
        temperature=0.9,  # 控制回复的创造性，0.0 为保守、1.0 为创造性高
        n=1,              # 生成几个回复供选择
        stop=None,        # 可以指定一个字符串来终止生成的回复
        timeout=10,       # 超时时间
    )

    if response['choices'][0]['text']:
        return response['choices'][0]['text'].strip()
    else:
        return "error!"


def chat_gpt3(type,determiner):
    message= "请生成一份"+type+"优美的,关键词为"+determiner+"的表达爱意的话,注意不要以亲爱的开头"
    return chat_with_gpt3(message)

# 与 ChatGPT-3 进行对话
# while True:
#     user_input = input()
#     response = chat_with_gpt3(user_input)
#     print( response)