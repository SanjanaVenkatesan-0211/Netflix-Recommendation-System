import sqlite3
import pandas as pd

conn = sqlite3.connect("netflix.db")

query = """
SELECT type,
COUNT(*) AS Total
FROM netflix
GROUP BY type;
"""

print(pd.read_sql(query, conn))


query = """
SELECT country,
COUNT(*) AS Total
FROM netflix
GROUP BY country
ORDER BY Total DESC
LIMIT 10;
"""

print(pd.read_sql(query, conn))


query = """
SELECT rating,
COUNT(*) AS Total
FROM netflix
GROUP BY rating
ORDER BY Total DESC;
"""

print(pd.read_sql(query, conn))

query = """
SELECT year_added,
COUNT(*) AS Total
FROM netflix
GROUP BY year_added
ORDER BY year_added;
"""

print(pd.read_sql(query, conn))


query = """
SELECT release_year,
COUNT(*) AS Total
FROM netflix
GROUP BY release_year
ORDER BY Total DESC
LIMIT 10;
"""

print(pd.read_sql(query, conn))

conn.close()