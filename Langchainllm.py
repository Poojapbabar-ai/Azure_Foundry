from langchain.chat_models import init_chat_model
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.environ["API_KEY"]
model = os.environ["model"]
base_url = os.environ["base_url"]


llm = init_chat_model(
   model=model,
   base_url=base_url,
   api_key=api_key,
   )

response = llm.invoke("What is the capital of France?")
print(response.content)
