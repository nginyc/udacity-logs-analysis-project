#!/usr/bin/env python3

import psycopg2

# Define constants & queries

DB_NAME = 'news'
TOP_THREE_ARTICLES_QUERY = \
    '''
    SELECT title, views FROM article_views
    ORDER BY views DESC
    LIMIT 3;
    '''
TOP_ARTICLE_AUTHORS_QUERY = \
    '''
    SELECT name, views FROM article_author_views
    ORDER BY views DESC;
    '''
DAYS_WITH_HIGH_ERROR_RATE_QUERY = \
    '''
    SELECT day, error_rate FROM hits_by_day
    WHERE error_rate > 0.01
    ORDER BY error_rate DESC;
    '''


# Define utility functions

def print_header(title):
    print('\n')
    print(title)
    print('---------------------------------------------------')


def print_footer():
    print('\n\n')


# Establish the DB connection

db = psycopg2.connect(database=DB_NAME)
cursor = db.cursor()

# Fetch & print top 3 articles

print('\n')
print('Fetching top 3 articles of all time...')

cursor.execute(TOP_THREE_ARTICLES_QUERY)
articles = cursor.fetchall()

print_header('Top 3 Articles of All Time')

for article in articles:
    print('"{}" - {} views'.format(article[0], article[1]))

print_footer()

# Fetch & print top article authors

print('Fetching top article authors of all time...')

cursor.execute(TOP_ARTICLE_AUTHORS_QUERY)
authors = cursor.fetchall()

print_header('Top Article Authors of All Time')

for author in authors:
    print('{} - {} views'.format(author[0], author[1]))

print_footer()

# Fetch & print days with high error rates

print('Fetching days with high error rates...')

cursor.execute(DAYS_WITH_HIGH_ERROR_RATE_QUERY)
days = cursor.fetchall()

print_header('Days with High Error Rates')

for day in days:
    print('{} - {}% errors'.format(day[0], round(day[1] * 100, 1)))

print_footer()

# Close the DB connection

db.close()
