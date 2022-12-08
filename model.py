from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
def ask(q):
    import openai
    openai.api_key = "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"
                   
    response = openai.Completion.create(
        model="davinci:ft-yuan-ze-university-2022-12-08-04-51-24",
        prompt=q,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=["\n", "END"]
)                     
    story = response['choices'][0]['text'] 
    return story
