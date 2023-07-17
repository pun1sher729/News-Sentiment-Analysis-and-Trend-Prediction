import joblib
import pandas as pd
from transformers import pipeline
import math
from math import pi
from datetime import datetime
import os
from django.conf import settings

file_ = open(os.path.join(settings.BASE_DIR, 'predict/model_rf1.joblib'), 'rb')

model = joblib.load(file_)

model_path = "mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis"
sentiment_model = pipeline("text-classification", model=model_path , tokenizer=model_path, max_length=600, truncation=True)

hf_name = 'pszemraj/led-large-book-summary'
summarizer = pipeline(
    "summarization",
    hf_name,
    device=-1,
)

def get_summary(article):
    result = summarizer(
            article,
            min_length=100,
            max_length=300,
            no_repeat_ngram_size=3,
            encoder_no_repeat_ngram_size=3,
            repetition_penalty=3.5,
            num_beams=4,
            early_stopping=True,
        )
    return result[0]['summary_text']

def one_hot_sentiment(sentiment):
    if sentiment == 'negative':
        return (1,0,0)
    elif sentiment == 'positive':
        return (0,0,1)
    else:
        return (0,1,0)

def get_sentiment(article):
    try:
        score = sentiment_model(article)
        sentiment = (score[0]['label'])
        res = one_hot_sentiment(sentiment)
    except RuntimeError:
        article = get_summary(article)
        score = sentiment_model(article)
        sentiment = (score[0]['label'])
        res = one_hot_sentiment(sentiment)
    except:
        return None
    return res

def transform_month(month):
    max_value = 12
    sin_values = math.sin((2*pi*month)/max_value)
    cos_values = math.cos((2*pi*month)/max_value)
    return (sin_values, cos_values)

def transform_day(day):
    max_value = 31
    sin_values = math.sin((2*pi*day)/max_value)
    cos_values = math.cos((2*pi*day)/max_value)
    return (sin_values, cos_values)

def transformation_dow(dow):
    max_value = 6
    sin_values = math.sin((2*pi*dow)/max_value)
    cos_values = math.cos((2*pi*dow)/max_value)
    return (sin_values, cos_values)

def get_company_index(symbol):
    companies = ['AAPL', 'ABBV', 'ABT', 'ACN', 'ADBE', 'AIG', 'AMD', 'AMGN', 'AMT', 'AMZN', 'AVGO', 'AXP', 'BA', 'BAC', 'BK', 'BKNG', 'BLK', 'C', 'CAT', 'CHTR', 'CL', 'CMCSA', 'COF', 'COP', 'COST', 'CRM', 'CSCO', 'CVS', 'CVX', 'DHR', 'DIS', 'DOW', 'DUK', 'EMR', 'EXC', 'F', 'FDX', 'GD', 'GE', 'GILD', 'GM', 'GOOG', 'GOOGL', 'GS', 'HD', 'HON', 'IBM', 'INTC', 'JNJ', 'JPM', 'KHC', 'KO', 'LIN', 'LLY', 'LMT', 'LOW', 'MA', 'MCD']
    return companies.index(symbol.upper())+1

#Features: day_sin, day_cos, month_sin, month_cos, year, dow_sin, dow_cos, symbol, negative, neutral, positive
def get_all_features(article, date:str, symbol):
    date = datetime.strptime(date, "%Y-%m-%d")
    year = date.year
    month = date.month
    day = date.day
    features = [i for i in transform_day(day)]
    for i in transform_month(month):
        features.append(i)
    features.append(year)
    for i in transformation_dow(date.weekday()):
        features.append(i)
    features.append(get_company_index(symbol))
    sentiment = get_sentiment(article)
    if sentiment == None:
        return None
    else:
        for i in sentiment:
            features.append(i)
    return pd.DataFrame(features).T

def get_prediction(features):
    return model.predict(features)
    



