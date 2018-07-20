#!/usr/bin/env python3

import psycopg2

# Define constants & queries

DB_NAME = 'news'
CREATE_VIEW_PAGE_VIEWS_QUERY = \
    '''
    CREATE VIEW page_views AS (
        SELECT path, COUNT(id) AS views FROM log
        WHERE status = '200 OK'
        GROUP BY path
    );
    '''
CREATE_VIEW_ARTICLE_VIEWS_QUERY = \
    '''
    CREATE VIEW article_views AS (
        SELECT a.title, a.author, pv.views FROM articles a
        JOIN page_views pv ON pv.path = ('/article/'||a.slug)
    );
    '''
CREATE_VIEW_ARTICLE_AUTHORS_VIEWS_QUERY = \
    '''
    CREATE VIEW article_author_views AS (
        SELECT au.name AS name, SUM(av.views) AS views FROM article_views av
        JOIN authors au ON au.id = av.author
        GROUP BY au.name
    );
    '''
CREATE_VIEW_HITS_BY_DAY_QUERY = \
    '''
    CREATE VIEW hits_by_day AS (
        SELECT day, hits, errors, errors/hits::float AS error_rate
        FROM (
            SELECT
                TO_CHAR(time, 'FMMonth DD, YYYY') AS day,
                COUNT(*) AS hits,
                COUNT(CASE WHEN status != '200 OK' THEN 1 end) AS errors
            FROM log
            GROUP BY day
        ) t
    );
    '''

# Establish the DB connection

db = psycopg2.connect(database=DB_NAME)
cursor = db.cursor()

# Create views

print('\n')
print('Creating views...')

cursor.execute(CREATE_VIEW_PAGE_VIEWS_QUERY)
cursor.execute(CREATE_VIEW_ARTICLE_VIEWS_QUERY)
cursor.execute(CREATE_VIEW_ARTICLE_AUTHORS_VIEWS_QUERY)
cursor.execute(CREATE_VIEW_HITS_BY_DAY_QUERY)

print('\n')
print('Created views!')

# Commit DB changes

db.commit()

# Close the DB connection

db.close()
