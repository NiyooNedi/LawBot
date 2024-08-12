import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "You are a lawyer"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Digital Lawyer", description = "Hi, I am Harvey Specter, the best closer in New York City, and your lawyer. Ask me any law related questions!", theme = gradio.themes.Soft())
demo.launch(share = True)
