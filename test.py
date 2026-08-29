### Quick Verification Test
###Create a quick test script (`test.py`) to ensure everything is wired up correctly:

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

def main():
    print ("Hello! This is a quick verification test for LangChain and OpenAI integration.")

    #CREATE A MODEL INSTANCE
    model = ChatOpenAI(
        model=os.getenv("AI_MODEL", "gpt-4o-mini"), 
        api_key=os.getenv("AI_API_KEY"), 
        base_url=os.getenv("AI_ENDPOINT"),
    )
# Initialize a simple model call
    response = model.invoke(
        "What is LangChain?"
    )
    print("AI:", response.content)

if __name__ == "__main__":
    main()
