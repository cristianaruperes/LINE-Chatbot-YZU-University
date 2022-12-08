from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
def ask(q):#
    import openai
    openai.api_key = "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"
                   
    response = openai.Completion.create(
    model="text-curie-001",
    prompt=q,
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    stop=["END"]
)                     
    story = response['choices'][0]['text'] 
    return story
