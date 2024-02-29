from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

response = client.chat.completions.create(
  messages=[
   {
      "role": "system",
      "content": "Listar apenas os nome dos produtos, sem a descrição"
    },
    {
      "role": "user",
      "content": "Liste 3 produtos sustentaveis"
    }
  ],
  model="gpt-3.5-turbo-1106"
)

print(response.choices[0].message.content)