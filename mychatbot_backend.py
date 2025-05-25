# Import LangChain modules: ChatBedrock/ChatBedrockConverse for AWS model integration,
# ConversationChain for chat orchestration, and memory modules to retain dialogue context

from langchain.memory import ConversationSummaryBufferMemory
from langchain.chains import ConversationChain
from langchain_aws import ChatBedrockConverse

# Define a function to create and return a ChatBedrockConverse instance.
# This sets up a connection to an AWS Bedrock-hosted model using a specified credentials profile,
# model ID, and inference parameters such as temperature and max_tokens.
# Useful for initializing the LLM client for testing or demo chatbot interactions.

def demo_chatbot():
    demo_llm=ChatBedrockConverse(
        credentials_profile_name='default',
        model="us.deepseek.r1-v1:0",
        temperature=0.1,
        max_tokens=1000)
    return demo_llm

# Define a function to initialize and return a ConversationSummaryBufferMemory instance.
# This memory buffer uses the demo LLM (from AWS Bedrock via ChatBedrockConverse) to summarize 
# and retain the conversation context within a specified token limit (max_token_limit).
# Useful for enabling long-term memory while managing token constraints in chat interactions.

def demo_memory():
    llm_data=demo_chatbot()
    memory=ConversationSummaryBufferMemory(llm=llm_data,max_token_limit=2000)
    return memory
    
# Define a function that sets up a conversational chain and generates a chat response.
# It initializes a LangChain ConversationChain with a Bedrock LLM and a memory buffer to retain context.
# The function then invokes the chain using the user's input text and returns the generated response.
# This enables context-aware replies in a chat-like setting, with memory-assisted continuity.
# The 'verbose=True' flag allows detailed logging for debugging or traceability.

def demo_conversation(input_text,memory):
    llm_chain_data=demo_chatbot()
    llm_conversation = ConversationChain(
    llm=llm_chain_data, 
    memory=memory,
    verbose=True
)
    chat_reply=llm_conversation.invoke(input_text)
    return chat_reply['response']
