# DistilBERT Sentiment Analysis Web App

This project is a web application that uses the DistilBERT model to perform sentiment analysis on text input. Built with Gradio, it provides an interactive interface where users can enter text (e.g., movie reviews) and receive sentiment predictions (Positive or Negative) with confidence scores.

## Features
- Analyzes text sentiment using a pre-trained DistilBERT model.
- Interactive web interface powered by Gradio.
- Lightweight and optimized for low-resource systems (e.g., 8GB RAM, CPU-only).

## Prerequisites
- Python 3.8 or higher
- Windows operating system (other OS compatible with minor adjustments)
- ~5GB free disk space for libraries and model weights

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/mgajapure6/AI.git
   cd AI
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv myenv
   myenv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install gradio transformers torch --index-url https://download.pytorch.org/whl/cpu
   ```

## Usage

1. **Run the Web App**:
   ```bash
   python distilbert_gradio_app.py
   ```

2. **Access the Interface**:
   - Open the provided URL (e.g., `http://127.0.0.1:7860`) in your web browser.
   - Enter text (e.g., "This game is super fun!") in the textbox and click "Submit".
   - View the sentiment prediction (e.g., "Sentiment: POSITIVE, Confidence: 0.9997").

## Example
- Input: "The app crashed and was frustrating."
- Output: "Sentiment: NEGATIVE, Confidence: 0.9989"

## Project Structure
```
distilbert-sentiment-app/
│
├── distilbert_gradio_app.py  # Main script for the Gradio web app
├── README.md                 # Project documentation
├── .gitignore                # Ignores virtual env and large files
└── requirements.txt          # List of dependencies
```

## Notes
- **Model Weights**: The DistilBERT model is downloaded automatically by the `transformers` library. Avoid committing large model files to GitHub (use `.gitignore`).
- **Performance**: Optimized for CPU (e.g., Intel i5, 8GB RAM). Expect slight delays (~30-60s) when loading the model.
- **Customization**: Modify `distilbert_gradio_app.py` to add new NLP tasks (e.g., question answering) or adjust the Gradio interface.

## Requirements
To regenerate the environment:
```bash
pip install -r requirements.txt
```

Generate `requirements.txt`:
```bash
pip freeze > requirements.txt
```

## Contributing
Feel free to fork this repository, submit pull requests, or open issues for bugs and feature requests.

## License
This project is licensed under the MIT License.

## Acknowledgments
- Built with [Hugging Face Transformers](https://huggingface.co/docs/transformers)
- Powered by [Gradio](https://gradio.app)
- Model: `distilbert-base-uncased-finetuned-sst-2-english`