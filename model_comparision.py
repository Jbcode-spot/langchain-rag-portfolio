from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
import time

load_dotenv()

def compare_models():
    print("Comparing different OpenAI models...")

    prompt = "What is LangChain?"
    models = ["gpt-4o-mini", "gpt-3.5-turbo", "gpt-4"]

    for model_name in models:
        print(f"\nUsing model: {model_name}")
        model = ChatOpenAI(
            model=model_name,
            api_key=os.getenv("AI_API_KEY"),
            base_url=os.getenv("AI_ENDPOINT"),
        )
        start_time = time.time()
        response = model.invoke(prompt)
        dur = (time.time() - start_time) *1000
        print(f"Response: {response.content}")
        print(f"Time taken: {dur:.2f} milliseconds")

if __name__ == "__main__":
    compare_models()