from database import init_db
from ollama import chat
from tools import tool_map, tools

init_db()

messages = []


while True:
    user_input = input("\n You: ")
    if user_input.lower() == "quit":
        break
    print("Thinking.......")
    messages.append(
        {
            "role": "user",
            "content": user_input,
        }
    )

    response = chat(
        model="qwen3:4b",
        messages=messages,
        tools=tools,
    )

    if response.message.tool_calls:
        for tool_call in response.message.tool_calls:
            name = tool_call.function.name
            arguments = tool_call.function.arguments

            print(f"Tool requested: {name}")
            print(f"Arguments: {arguments}")

            tool = tool_map[name]
            result = tool(**arguments)

            print(f"Tool result: {result}")

            messages.append(response.message)
            messages.append(
                {
                    "role": "tool",
                    "content": result,
                }
            )
        print("Fetching final response.....")

        final_response = chat(
            model="qwen3:4b",
            messages=messages,
            tools=tools,
        )

        print(f"\nAssistant: {final_response.message.content}")
    else:
        print(f"\nAssistant: {response.message.content}")
