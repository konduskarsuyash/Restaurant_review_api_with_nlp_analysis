from transformers import pipeline

# Load the sentiment analysis pipeline
sentiment_pipeline = pipeline('sentiment-analysis')

def analyze_sentiment(text):
    """Analyze sentiment of the given text and return 'positive', 'negative', or 'neutral'."""
    result = sentiment_pipeline(text)[0]
    sentiment = result['label']
    score = result['score']
    
    # Define a threshold to classify neutral sentiments
    neutral_threshold = 0.4
    
    if sentiment == 'POSITIVE' and score > 0.5:
        return 'positive'
    elif sentiment == 'NEGATIVE' and score > 0.5:
        return 'negative'
    elif sentiment == 'NEGATIVE' and score < neutral_threshold:
        return 'neutral'
    else:
        return 'neutral'
