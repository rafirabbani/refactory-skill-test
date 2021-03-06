import json
from datetime import datetime

with open('Q2/profile_list.json') as json_read:
    data = json.load(json_read)

#check phone 

def phone_check():
    for phone in data:
        phone_data = phone['profile']['phones']
        if phone_data == []:
            print('username', phone['username'], 'does not have phone')
    print()

phone_check()


#check articles

def articles_check():
    for articles in data:
        articles_data = articles['articles:']
        if articles_data != []:
            print('username', articles['username'], 'does have some articles')
    print()

articles_check()

#check Annis

def check_annis():
    subString = 'Annis'
    for names in data:
        names_data = names['profile']['full_name']
        if subString in names_data:
            print('username', names['username'], 'contains Annis')
    print()

check_annis()

#check articles 2020

def articles_2020():
    user_with_article_list = []
    date_mark = datetime.strptime('2020-01-01T00:00:00', '%Y-%m-%dT%H:%M:%S')
    count = 0
    for articles in data:
        articles_data = articles['articles:']
        for date in articles_data:
            date_published = datetime.strptime(date['published_at'], '%Y-%m-%dT%H:%M:%S')
            if date_published > date_mark:
                user_with_article_list.append(articles['username'])
        article_count = user_with_article_list.count(articles['username'])
        if article_count > 0:
            print('username', articles['username'], 'has', article_count, 'articles in 2020')
        else:
            print('no one has article published in 2020')
        break
    print()

articles_2020()

#check user born in 1986

def born_1986():
    year = datetime.strptime('1986', '%Y')
    for birth in data:
        birth_data = birth['profile']['birthday']
        birth_date = datetime.strptime(birth_data[:4], '%Y')
        if birth_date == year:
            print('username', birth['username'], 'born in', datetime.strftime(year, '%Y'))
    print()

born_1986()

#check article contain tips
def article_tips():
    tips_list = []
    subString = 'Tips'
    for datas in data:
        articles = datas['articles:']
        for title in articles:
            if subString in title['title']:
                tips_list.append(datas['username'])
        tips_count = tips_list.count(datas['username'])
        if tips_count > 0:
            print('username', datas['username'], 'has article(s) with \"tips" on the title')
    print()

article_tips()

#article before august 2019

def aug_2019():
    article_list = []
    date_mark = datetime.strptime('2019-08-01T00:00:00', '%Y-%m-%dT%H:%M:%S')
    count = 0
    for articles in data:
        articles_data = articles['articles:']
        for date in articles_data:
            date_published = datetime.strptime(date['published_at'], '%Y-%m-%dT%H:%M:%S')
            if date_published < date_mark:
                article_list.append(date['title'])
    for item in article_list:
        print('Article',item, 'published before', datetime.strftime(date_mark, '%B %Y') )
    print()
        
aug_2019()