import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.chains.llm import LLMChain
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# Chat History
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# UI for AIChatBot
st.set_page_config(page_title='AI Health', page_icon='🩺')
st.title("🩺 AI Health Assistant")

# Get response
def get_response(query, chat_history):
    
    # Define the prompt template
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", 
             "You are a virtual health assistant. Firstly, greet the patient and ask about their well-being. Let them answer! "
             "Ask the user to rate their pain level on a scale from 1 to 10. Let them answer to your question! Then inquire about additional symptoms related to the disease. \
             Let them answer to your question! Let them answer! Ask Based on their answer, try to suggest ways to reduce their pain. "
             "Then encourage them to take early action. Answer follow-up questions if needed. Then, Provide Educational Information on the Condition if Needed.\
            Lastly, Recommend seeing a specialist and its field based on the symptoms. Then end the conversation."
             f"Chat history: {chat_history}"),
            ("human", "{query}")
        ]
    )
    
    # Initialize the LLM with the specified model and temperature
    llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0.5)
    
    # Create the chain with the prompt and LLM
    chain = prompt | llm | StrOutputParser()

    # Format the input for the chain
    response = chain.stream({
        "chat_history": chat_history,
        "query": query
    })

    return response

# Conversation
for message in st.session_state.chat_history:
    if isinstance(message, HumanMessage):
        with st.chat_message("Patient"):
            st.markdown(message.content)
    elif isinstance(message, AIMessage):
        with st.chat_message("AI Health"):
            st.markdown(message.content)

user_query = st.chat_input("Your message")

if user_query:
    st.session_state.chat_history.append(HumanMessage(content=user_query))

    with st.chat_message("Patient"):
        st.markdown(user_query)

    with st.chat_message("AI Health"):
        ai_response = st.write_stream(get_response(user_query, st.session_state.chat_history))

    st.session_state.chat_history.append(AIMessage(content=ai_response))
