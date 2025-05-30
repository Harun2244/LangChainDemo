from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")
os.environ["GOOGLE_API_KEY"] = google_api_key


llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    max_tokens=100,  
    temperature=0.7 
)

prompt = PromptTemplate.from_template(
    "You are a helpful assistant. Answer the question clearly.\n\nQuestion: {input}\nAnswer:"
)

chain = prompt | llm

query = "Koliko je 5+13?"
output = chain.invoke({"input": query})
print("Question:", query)
print("Answer:", output.content)