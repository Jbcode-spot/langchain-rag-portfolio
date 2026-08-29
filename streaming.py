from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()


def stream():

    print("Streaming responses from the model...")

    model = ChatOpenAI(
        model="gpt-4o-mini",
        api_key=os.getenv("AI_API_KEY"),
        base_url=os.getenv("AI_ENDPOINT"),
    )

    for piece in model.stream("Write a poem about a cat that is also a dog."):
        print(piece.content, end="", flush=True)

    print ("\n\nStreaming complete.")

if __name__ == "__main__":
    stream()

          