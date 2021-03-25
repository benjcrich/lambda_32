import sqlite3
import pandas as pd

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

character_count_query = """
SELECT *
FROM charactercreator_character
         LEFT JOIN charactercreator_character_inventory
                   on charactercreator_character.character_id =
                      charactercreator_character_inventory.character_id
"""

curs.execute(character_count_query)
results = curs.fetchall()

df = pd.DataFrame(results)

print(df.head())
