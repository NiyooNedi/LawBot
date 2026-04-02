import openai
import gradio


#inputting the api key into the openai libary/sdk for it to use when we call api's POST
openai.api_key = "gibberish"

#creating a list of dictionaries to be passed into the api; this will store the history of the conversation
#will be used to store the api and user's responses 
messages = [
    {
    #specifying who is currently making the directions for the ai: 
    #system - initialzing the ai's behavior as program creator & api's caller, user - person speaking to ai, assistant - for ai's responses to user
    "role": "system",
    #storing how the ai is meant to behave for the entirety of the conversation with the user 
    "content" : "You are a lawyer"
    }
]

#function that will actually handle the user's input and call on the api
def CustomChatGPT(user_input):
    
    #appending a new dictionary storing the user's request to the messages list
    messages.append({
        #specifying the role of the person posting the current content to the api
        "role": "user",
        #setting the content to be whatever the user has asked/typed
        "content": user_input
    })

    #calling on the openai libaries ChatCompletion class, and calling the create method
    #the create method CALLS ON THE API under the hood, sending a POST request with the information from the messages list, 
    #what's sent back from the api call and stored in response will be a json object stored as list of dicts
    response = openai.ChatCompletion.create(

        #specifying what model of ChatGPT to be used
        model = "gpt-3.5-turbo",
        #feeding the messages list of dicts into the api
        messages = messages
    )

    #diving deeply in the json object to get the reply of the AI
    ChatGPTReply = response["choices"][0]["message"]["content"]
    #storing the AI's reply in the messages list
    messages.append({"role": "assistant", "content": ChatGPTReply})
    return ChatGPTReply

#gradio is an easy-to-use interface that creates web demos for python functions, great with ML models
demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Digital Lawyer", description = "Hi, I am Harvey Specter, the best closer in New York City, and your lawyer. Ask me any law related questions!", theme = gradio.themes.Soft())
demo.launch(share = True)
