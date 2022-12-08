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
