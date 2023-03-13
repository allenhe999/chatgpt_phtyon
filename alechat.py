#导入openai 
import openai
# 导入用户key
openai.api_key = ""

conversation = []

#参数调整  
def generate_answer(messages):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.7,
        presence_penalty=0.6,
        frequency_penalty=0.5,
        max_tokens=1024

    )
    res_msg = completion.choices[0].message
    return res_msg["content"].strip()
# test
# try
if __name__ == '__main__':
    # 维护一个列表用于存储多轮对话的信息
    messages = [{"role": "system", "content": "你现在是很有用的助手！"}]
    while True:
        prompt = input("请输入你的问题:")
        messages.append({"role": "user", "content": prompt})
        res_msg = generate_answer(messages)
        messages.append({"role": "assistant", "content": res_msg})
        if prompt == "结束":
            break
        else:
            print(res_msg)
