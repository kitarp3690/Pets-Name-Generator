from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()

#loading the api key from the .env file
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

#setting up the llm
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=GROQ_API_KEY,
    temperature=0.7,
)

#setting up the prompt template
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a creative pet naming assistant. "
        "When given an animal type and a color, you suggest 5 unique, fun, "
        "and fitting names. Return ONLY a numbered list of 5 names, nothing else."
    ),
    (
        "human",
        "Animal: {animal}\nColor: {color}\n\nSuggest 5 names for this {color} {animal}."
    )
])

#setting up the output parser
parser = StrOutputParser()

#chaining the prompt, llm, and parser together
chain = prompt | llm | parser

#function to get name suggestions based on the animal and color
def get_name_suggestions(animal: str, color: str) -> str:
    """Generate 5 name suggestions for a given animal and color."""
    result = chain.invoke({"animal": animal, "color": color})
    return result

#main function to run the program
if __name__ == "__main__":
    print("🐾 Animal Name Suggester (powered by Grok + LangChain)\n")
    print("-" * 45)
 
    animal = input("Enter animal name (e.g. cat, dog, rabbit): ").strip()
    color  = input("Enter color (e.g. golden, black, spotted): ").strip()
 
    if not animal or not color:
        print("❌ Please provide both an animal name and a color.")
    else:
        print(f"\n✨ Here are 5 name suggestions for your {color} {animal}:\n")
        suggestions = get_name_suggestions(animal, color)
        print(suggestions)
        print()