from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()


def temperature_comparision():
    prompt = "What is emotion?"
    temperatures = [0, 1, 2]

    for temp in temperatures:
        print (f"Temperature: {temp}")
        
        model = ChatOpenAI(
            model="gpt-4o-mini",
            api_key=os.getenv("AI_API_KEY"),
            base_url=os.getenv("AI_ENDPOINT"),
            temperature=temp,
        )

        try:
            for i in range(1, 3):
                response = model.invoke(prompt)
                print(f"Response {i}: {response.content}")
        except Exception as e:
            #because some models might not accept certain values for temperature, we catch the exception and print it
            print( f"This model does not work with: {e}")
            print(f"Error: {e}")


if __name__ == "__main__":
    temperature_comparision()