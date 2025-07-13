import gradio as gr
from transformers import pipeline

# Load pre-trained DistilBERT model
classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

# Define prediction function
def predict_sentiment(text):
    result = classifier(text)[0]
    return f"Sentiment: {result['label']}, Confidence: {result['score']:.4f}"

# Create Gradio interface
interface = gr.Interface(
    fn=predict_sentiment,
    inputs=gr.Textbox(lines=2, placeholder="Enter text to analyze sentiment..."),
    outputs="text",
    title="DistilBERT Sentiment Analysis",
    description="Enter a sentence to predict its sentiment (Positive/Negative) using DistilBERT."
)

# Launch the app
interface.launch()