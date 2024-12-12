import streamlit as st
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

# Download the necessary NLTK data (only needed once)
nltk.download('vader_lexicon')

# Initialize the Sentiment Analyzer
sia = SentimentIntensityAnalyzer()

# Function to analyze sentiment
def analyze_sentiment(text):
    scores = sia.polarity_scores(text)
    if scores['compound'] >= 0.05:
        sentiment = "Positive"
    elif scores['compound'] <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    return sentiment, scores

# Streamlit App
st.title("Sentiment Analysis Web App")
st.write("Analyze the sentiment of your text: Positive, Negative, or Neutral.")

# Input text box
user_input = st.text_area("Enter text to analyze:")

# Analyze button
if st.button("Analyze Sentiment"):
    if user_input.strip() == "":
        st.warning("Please enter some text to analyze.")
    else:
        sentiment, scores = analyze_sentiment(user_input)
        st.success(f"The sentiment is: **{sentiment}**")
        
        # Show detailed polarity scores
        st.subheader("Polarity Scores:")
        st.json(scores)
