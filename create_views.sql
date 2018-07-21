CREATE OR REPLACE VIEW page_views AS (
    SELECT path, COUNT(id) AS views FROM log
    WHERE status = '200 OK'
    GROUP BY path
);

CREATE OR REPLACE VIEW article_views AS (
    SELECT a.title, a.author, pv.views FROM articles a
    JOIN page_views pv ON pv.path = ('/article/'||a.slug)
);

CREATE OR REPLACE VIEW article_author_views AS (
    SELECT au.name AS name, SUM(av.views) AS views FROM article_views av
    JOIN authors au ON au.id = av.author
    GROUP BY au.name
);

CREATE OR REPLACE VIEW hits_by_day AS (
    SELECT 
        TO_CHAR(day, 'FMMonth DD, YYYY') AS day, 
        hits, 
        errors, 
        errors/hits::float AS error_rate
    FROM (
        SELECT
            time::date AS day,
            COUNT(*) AS hits,
            COUNT(CASE WHEN status != '200 OK' THEN 1 end) AS errors
        FROM log
        GROUP BY day
    ) t
);