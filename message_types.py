import os

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

load_dotenv()

def main():
    print("Lets Understand message types now")

    model = ChatOpenAI(
        model=os.getenv("AI_MODEL", "gpt-4o-mini"), 
        api_key=os.getenv("AI_API_KEY"), 
        base_url=os.getenv("AI_ENDPOINT"),
    )

    messages = [
        SystemMessage(content="You are a helpful assistant."),
        HumanMessage(content="What is LangChain?"),
    ]

    response = model.invoke(messages)
    print("AI:", response.content)

if __name__ == "__main__":
    main()