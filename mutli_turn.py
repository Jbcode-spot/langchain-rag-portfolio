import os

from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()

def main():
    # Initialize the ChatOpenAI model
    model = ChatOpenAI(
        model="gpt-4o-mini",
        api_key=os.getenv("AI_API_KEY"),
        base_url=os.getenv("AI_ENDPOINT"),
    )

    messages = [ 
       SystemMessage(content="You are a helpful assistant, but a little bastard"),
       HumanMessage(content="What the fuck is Python?"),
   ]

    print("User: What is python?")

    response1 = model.invoke(messages)
    print(f"/n Assistant: {response1.content}")
    messages.append(AIMessage(content=response1.content))
    messages.append(HumanMessage(content="Can you tell me more about it?"))

    response2 = model.invoke(messages)
    messages.append(AIMessage(content=response2.content))
    print(f"/n Assistant: {response2.content}")

    print("User: Can you tell mme something funny about it?")
    messages.append(HumanMessage(content="Can you tell me something funny about it?"))

    response3 = model.invoke(messages)
    messages.append(AIMessage(content=response3.content))
    print(f"/n Assistant: {response3.content}")

if __name__ == "__main__":
    main()