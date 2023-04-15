from yelpapi import YelpAPI
import pandas as pd
import nltk 
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

api_key = "HKUFCeKms6k3Qjs6uq0_cgs_xUu_SSBotsmR8-ukxo_AV9FKXXNBs-rm_xT9o7VXQi2pW5meTbKnl9XY-VSXo0OWtd3VPv9c8OGOZpywrs8yjwGUxOL5MePK04M3ZHYx"

yelp_api = YelpAPI(api_key)

#search_query
search_term = "bagel"
search_location="New York City, NY"
search_sort_by="rating" #best_match, rating review_count, distance
search_limit = 20

search_results = yelp_api.search_query(term=search_term, location=search_location, sort_by=search_sort_by,limit=search_limit, offset=20)

#print(search_results)

#for business in search_results['businesses']:
# print(business['name'])
# print(business['alias'])
# print("\n")

#result_df =pd.DataFrame.from_dict(search_results['businesses'])
#print(result_df['alias'])
#makes csv >>> result_df.to_csv("inclass_yelpapi.csv")


#reviews_query
''''
id_for_reviews="black-star-bakery-and-cafe-new-york-3"
reviews_result = yelp_api.reviews_query(id=id_for_reviews)
reviews_df=pd.DataFrame.from_dict(reviews_result['reviews'])


for review in reviews_df['text']:
    tokens=nltk.word_tokenize(review)
    pos_tokens=nltk.pos_tag(tokens)
    for token in pos_tokens:
        if token[1]=='JJ'or token[1]=='JJS' or token[1]=='NN':
            print(token[0])
    print(pos_tokens)

analyzer = SentimentIntensityAnalyzer()
id_for_reviews="black-star-bakery-and-cafe-new-york-3"
reviews_result = yelp_api.reviews_query(id=id_for_reviews)
reviews_df=pd.DataFrame.from_dict(reviews_result['reviews'])

for review in reviews_result['reviews']:
    sentiment_score = analyzer.polarity_scores(review)
    print(review)
    print(sentiment_score)
    print('\n')

id_for_reviews="the-lazy-llama-coffee-bar-new-york-2"
reviews_result = yelp_api.reviews_query(id=id_for_reviews)
reviews_df=pd.DataFrame.from_dict(reviews_result['reviews'])


for review in reviews_df['text']:
    tokens=nltk.word_tokenize(review)
    pos_tokens=nltk.pos_tag(tokens)
    for token in pos_tokens:
        if token[1]=='JJ'or token[1]=='JJS' or token[1]=='NN':
            print(token[0])
    print(pos_tokens)


id_for_reviews="avenue-x-bagels-brooklyn"
reviews_result = yelp_api.reviews_query(id=id_for_reviews)
reviews_df=pd.DataFrame.from_dict(reviews_result['reviews'])


for review in reviews_df['text']:
    tokens=nltk.word_tokenize(review)
    pos_tokens=nltk.pos_tag(tokens)
    for token in pos_tokens:
        if token[1]=='JJ'or token[1]=='JJS' or token[1]=='NN':
            print(token[0])
    print(pos_tokens)

id_for_reviews="brooklyn-bagel-and-coffee-company-astoria"
reviews_result = yelp_api.reviews_query(id=id_for_reviews)
reviews_df=pd.DataFrame.from_dict(reviews_result['reviews'])


for review in reviews_df['text']:
    tokens=nltk.word_tokenize(review)
    pos_tokens=nltk.pos_tag(tokens)
    for token in pos_tokens:
        if token[1]=='JJ'or token[1]=='JJS' or token[1]=='NN':
            print(token[0])
    print(pos_tokens)
'''
id_for_reviews="levain-bakery-new-york-new-york-2"
reviews_result = yelp_api.reviews_query(id=id_for_reviews)
reviews_df=pd.DataFrame.from_dict(reviews_result['reviews'])


for review in reviews_df['text']:
    tokens=nltk.word_tokenize(review)
    pos_tokens=nltk.pos_tag(tokens)
    for token in pos_tokens:
        if token[1]=='JJ'or token[1]=='JJS' or token[1]=='NN':
            print(token[0])
    print(pos_tokens)