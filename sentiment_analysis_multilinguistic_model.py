# -*- coding: utf-8 -*-
"""Sentiment_Analysis_multilinguistic_model

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1J9UWasW9PjfCmJNAHCXxiAcLX6cGZjIk
"""

pip install deep_translator

pip install vaderSentiment

import codecs
from deep_translator import GoogleTranslator
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_sentiment(text):
    translated_text = GoogleTranslator(source='auto', target='en').translate(text)
    analyzer = SentimentIntensityAnalyzer()
    sentiment_dict = analyzer.polarity_scores(translated_text)

    print("\nTranslated Sentence =", translated_text, "\nDictionary =", sentiment_dict)
    if sentiment_dict['compound'] >= 0.05:
        print("It is a Positive Sentence")
    elif sentiment_dict['compound'] <= -0.05:
        print("It is a Negative Sentence")
    else:
        print("It is a Neutral Sentence")

# Option for user input or file upload
print("Choose an option:")
print("1. Enter text")
print("2. Upload a file")

option = input("Enter the option (1 or 2): ")

if option == '1':
    # User input
    lines = []
    print("Enter text. Press Enter on an empty line to finish:")
    while True:
        line = input()
        if not line:
            break
        lines.append(line)

    for line in lines:
        analyze_sentiment(line)

elif option == '2':
    # File upload
    file_path = input("Enter the path of the file: ")
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            analyze_sentiment(line)
else:
    print("Invalid option. Please select 1 or 2.")