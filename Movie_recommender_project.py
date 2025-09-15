#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import pandas as pd 


# In[2]:


movies = pd.read_csv('tmdb_5000_movies.csv')
credits = pd.read_csv('tmdb_5000_credits.csv') 


# In[3]:


movies.head()


# In[4]:


movies.shape


# In[5]:


credits.head()


# In[6]:


movies = movies.merge(credits,on='title')


# In[7]:


movies.head()


# In[8]:


movies = movies[['movie_id','title','overview','genres','keywords','cast','crew']]


# In[9]:


movies.head()


# In[10]:


movies.isnull().sum() #missing data 


# In[11]:


movies.dropna(inplace=True)


# In[12]:


movies.isnull().sum()


# In[13]:


movies.duplicated().sum()


# In[14]:


import ast


# In[15]:


def convert(text):
    L = []
    for i in ast.literal_eval(text):
        L.append(i['name']) 
    return L 


# In[16]:


movies.dropna(inplace=True)


# In[17]:


movies['genres'] = movies['genres'].apply(convert)
movies.head()


# In[18]:


import ast
ast.literal_eval('[{"id": 28, "name": "Action"}, {"id": 12, "name": "Adventure"}, {"id": 14, "name": "Fantasy"}, {"id": 878, "name": "Science Fiction"}]')


# In[19]:


def convert3(text):
    L = []
    counter = 0
    for i in ast.literal_eval(text):
        if counter < 3:
            L.append(i['name'])
        counter+=1
    return L 


# In[20]:


movies['cast'] = movies['cast'].apply(convert)
movies.head()


# In[21]:


movies['cast'] = movies['cast'].apply(lambda x:x[0:3])


# In[22]:


import ast

def extract_list(text):
    items = []
    if isinstance(text, str):
        try:
            text = ast.literal_eval(text)
        except (ValueError, SyntaxError):
            return items
    if isinstance(text, list):
        for item in text:
            if isinstance(item, dict) and 'name' in item:
                items.append(item['name'])
            elif isinstance(item, str):
                items.append(item)
    return items

def fetch_director(text):
    L = []
    if isinstance(text, str):
        try:
            text = ast.literal_eval(text)
        except (ValueError, SyntaxError):
            return L
    if isinstance(text, list):
        for i in text:
            if isinstance(i, dict) and i.get('job') == 'Director':
                L.append(i.get('name'))
    return L


# In[23]:


movies['genres'] = movies['genres'].apply(extract_list)
movies['keywords'] = movies['keywords'].apply(extract_list)
movies['cast'] = movies['cast'].apply(lambda x: extract_list(x)[:3])
movies['crew'] = movies['crew'].apply(fetch_director)


# In[24]:


movies.sample(5)


# In[25]:


movies['overview'][0]


# In[26]:


movies['overview'] = movies['overview'].apply(lambda x:x.split())


# In[27]:


movies.head()


# In[28]:


def collapse(L):
    L1 = []
    for i in L:
        L1.append(i.replace(" ",""))
    return L1


# In[29]:


movies['cast'] = movies['cast'].apply(collapse) # or movies['cast'] = movies['cast'].apply(lambda x:[i.replace(" ","") for i in x])
movies['crew'] = movies['crew'].apply(collapse) # same for remaing all just chage the name 
movies['genres'] = movies['genres'].apply(collapse) 
movies['keywords'] = movies['keywords'].apply(collapse)


# In[30]:


movies.head()


# In[31]:


movies['tags'] = movies['overview'] + movies['genres'] + movies['keywords'] + movies['cast'] + movies['crew'] 


# In[32]:


movies.head()


# In[33]:


new = movies.drop(columns=['overview','genres','keywords','cast','crew'])


# In[34]:


new['tags'] = new['tags'].apply(lambda x: " ".join(x))
new.head()


# In[35]:


from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=5000,stop_words='english')


# In[36]:


vector = cv.fit_transform(new['tags']).toarray()


# In[37]:


vector.shape


# In[38]:


vector


# In[39]:


vector[0]


# In[40]:


import nltk


# In[41]:


from nltk.stem.porter import PorterStemmer # capital p and s 
ps = PorterStemmer()


# In[42]:


def stem(text):
    y = []
    
    for i in text.split():
        y.append(ps.stem(i))
        
    return " ".join(y)


# In[43]:


new['tags'] = new['tags'].apply(stem)


# In[44]:


from sklearn.metrics.pairwise import cosine_similarity


# In[45]:


similarity = cosine_similarity(vector)


# In[46]:


similarity[1]


# In[47]:


new[new['title'] == 'The Lego Movie'].index[0]


# In[48]:


def recommend(movie):
    index = new[new['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    for i in distances[1:6]:
        print(new.iloc[i[0]].title)


# In[50]:


recommend('Avatar')


# In[51]:


import pickle


# In[52]:


pickle.dump(new,open('movie_list.pkl','wb'))
pickle.dump(similarity,open('similarity.pkl','wb'))


# In[ ]:




