import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

TOTAL_CHARACTERS = """
SELECT COUNT (DISTINCT character_id) AS "Number of Characters" FROM charactercreator_character
"""

TOTAL_SUBCLASS = """
SELECT COUNT(*) AS "Number of Characters", "Clercs" AS Subclass
FROM charactercreator_cleric
UNION ALL
SELECT COUNT(*) AS "Number of Characters", "Fighters" AS Subclass
FROM charactercreator_fighter
UNION ALL
SELECT COUNT(*) AS "Number of Characters", "Mages" AS Subclass
FROM charactercreator_mage
UNION ALL
SELECT COUNT(*) AS "Number of Characters", "Theives" AS Subclass
FROM charactercreator_thief
"""

TOTAL_ITEMS = """
SELECT COUNT (DISTINCT item_id) AS "Number of Items" FROM armory_item
"""

WEAPONS = """
SELECT COUNT (DISTINCT item_ptr_id) AS "Number of Weapons" FROM armory_weapon
"""

NON_WEAPONS = """
SELECT COUNT(*)
FROM (SELECT item_id
      FROM armory_item
          EXCEPT
      SELECT item_ptr_id
      FROM armory_weapon)
"""

CHARACTER_ITEMS = """
SELECT character_id, COUNT(*) n_items
FROM charactercreator_character_inventory as inventory
GROUP BY inventory.character_id
LIMIT 20
"""

CHARACTER_WEAPONS = """
SELECT character_id, COUNT(*) n_items
FROM charactercreator_character_inventory as inventory, armory_weapon as weapon
WHERE inventory.item_id = weapon.item_ptr_id
GROUP BY inventory.character_id
LIMIT 20
"""

AVG_CHARACTER_ITEMS = """
SELECT AVG(n_items)
FROM (
    SELECT character_id, COUNT(*) AS n_items
    FROM charactercreator_character_inventory as inventory
    GROUP BY inventory.character_id
)
"""

AVG_CHARACTER_WEAPONS = """
SELECT AVG(n_weapons)
FROM (
    SELECT character_id, COUNT(*) AS n_weapons
    FROM charactercreator_character_inventory as inventory, armory_weapon as weapon
    WHERE inventory.item_id = weapon.item_ptr_id
    GROUP BY inventory.character_id
)
"""
