import chainlit as cl

@cl.on_message
async def main(message: cl.Message):

    user_input = message.content


    response = f"Aapne kaha: {user_input}. Yeh Chainlit ka basic chatbot hai."


    await cl.Message(content=response).send()