from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
modelo = "gpt-3.5-turbo-1106"

def categoriza_produto(name, list_category):
	prompt_system = f"""
		Você é um categorizador de produtos.
		Você deve assumir as categorias presentes na lista abaixo.

		# Lista de Categorias Válidas
		{
			list_category.split(",")
   		}

		# Formato da Saída
		Produto: Nome do Produto
		Categoria: apresente a categoria do produto

		# Exemplo de Saída
		Produto: Escova elétrica com recarga solar
		Categoria: Eletrônicos Verdes
	"""

	

	response = client.chat.completions.create(
	messages=[
	{
			"role": "system",
			"content": prompt_system
		},
		{
			"role": "user",
			"content": name
		}
		],
		model=modelo,
		temperature=0,
		max_tokens=200
	)
	return response.choices[0].message.content

categorias_validas = input("Informe as categorias válidas, separando por vírgula: ")

while True:
    nome_produto = input("Digite o nome do produto: ")
    produto_categorizado = categoriza_produto(nome_produto, categorias_validas)
    print(produto_categorizado)
