import streamlit as st
import dill
import nltk
import random
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords



# Download if not already available
nltk.download('punkt')
nltk.download('stopwords')

# Load the trained chatbot
@st.cache_resource
def load_chatbot():
    with open("model.dill", "rb") as f:
        bot = dill.load(f)
    return bot

bot = load_chatbot()

# App title
st.title("🎓 College Admission Chatbot")
st.markdown("Ask me anything about college admissions, applications, scholarships, visa, and more!")

# User input
user_query = st.text_input("Enter your question:")

if user_query:
    response = bot.get_response(user_query)
    st.markdown("**Bot:** " + response)
