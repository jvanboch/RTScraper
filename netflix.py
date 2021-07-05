import pandas as pd
import scraper
df = pd.read_csv('netflix_titles.csv')

print(df['type'].value_counts())
df =df[df['type']=='Movie']
def add_ratings(row):
  return scraper.get_movie_rating(row['title'])
  
df['RT_Rating'] = df.apply(add_ratings,axis=1)  

def audience_rating(row):
  return row['RT_Rating'][0]
def critic_rating(row):
  return row['RT_Rating'][1]

df['RT_audience_rating'] = df.apply(audience_rating,axis=1)  
df['RT_critic_rating'] = df.apply(critic_rating,axis=1)  

df.to_csv('movies.csv')