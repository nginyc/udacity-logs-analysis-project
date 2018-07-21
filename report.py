#!/usr/bin/env python

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
    '''
    Prints a section header
    '''
    print('\n')
    print(title)
    print('-' * len(title))


def print_footer():
    '''
    Prints a section footer
    '''
    print('\n')


def db_connect():
    '''
    Creates and returns a connection to the database defined by DB_NAME,
    as well as a cursor for the database.

    Returns:
    db, cursor - a tuple. The first element is a connection to the database.
            The second element is a cursor for the database.
    '''

    db = psycopg2.connect(database=DB_NAME)
    cursor = db.cursor()

    return db, cursor

def db_disconnect(db):
    '''
    Closes the database connection
    
    Args:
    db - the database connection
    '''
    db.close()


def execute_query(cursor, query):
    '''
    Executes the SQL query and returns the results as a list of tuples.

    Args:
    cursor - the database cursor
    query - an SQL query statement to be executed.

    Returns:
    A list of tuples containing the results of the query.
    '''

    cursor.execute(query)
    results = cursor.fetchall()
    return results


def print_top_articles(cursor):
    '''
    Prints out the top 3 articles of all time.

    Args:
    cursor - the database cursor
    '''

    print('Fetching top 3 articles of all time...')

    articles = execute_query(cursor, TOP_THREE_ARTICLES_QUERY)
        
    print_header('Top 3 Articles of All Time')

    for title, views in articles:
        print('"{}" - {} views'.format(title, views))
    
    print_footer()


def print_top_authors(cursor):
    '''
    Prints a list of authors ranked by article views.
    '''

    print('Fetching top article authors of all time...')

    authors = execute_query(cursor, TOP_ARTICLE_AUTHORS_QUERY)
        
    print_header('Top Article Authors of All Time')

    for name, views in authors:
        print('{} - {} views'.format(name, views))
    
    print_footer()


def print_days_with_high_error_rates(cursor):
    '''
    Prints out the days where more than 1% of logged access requests were errors.
    '''
    
    print('Fetching days with high error rates...')

    days = execute_query(cursor, DAYS_WITH_HIGH_ERROR_RATE_QUERY)
        
    print_header('Days with High Error Rates')

    for day, error_rate in days:
        print('{} - {:.1%} errors'.format(day, error_rate))
    
    print_footer()

if __name__ == '__main__':
    print('\n')
    db, cursor = db_connect()
    print_top_articles(cursor)
    print_top_authors(cursor)
    print_days_with_high_error_rates(cursor)
    db_disconnect(db)
