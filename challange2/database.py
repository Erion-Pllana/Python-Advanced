import sqlite3
from models import Recipe, RecipeCreate


def create_connection():
    connection = sqlite3.connect("recipes.db")
    connection.row_factory = sqlite3.Row
    return connection


def create_table():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS recipes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            chef TEXT NOT NULL,
            prep_time INT NOT NULL,
            instructions TEXT NOT NULL
        )
    """)
    connection.commit()
    connection.close()


create_table()


def create_recipe(recipe: RecipeCreate) -> int:
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO recipes (title, chef, instructions) VALUES (?, ?, ?)",
        (recipe.title, recipe.chef, recipe.instructions)
    )
    connection.commit()
    recipe_id = cursor.lastrowid
    connection.close()
    return recipe_id


def read_recipes():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM recipes")
    rows = cursor.fetchall()
    connection.close()

    recipes = [Recipe(id=row[0], title=row[1], chef=row[2], instructions=row[3]) for row in rows]
    return recipes


def read_recipe(recipe_id: int):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM recipes WHERE id = ?", (recipe_id,))
    row = cursor.fetchone()
    connection.close()

    if row is None:
        return None
    return Recipe(id=row["id"], title=row["title"], chef=row["chef"], instructions=row["instructions"])


def update_recipe(recipe_id: int, recipe: RecipeCreate) -> bool:
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE recipes SET title = ?, chef = ?, instructions = ? WHERE id = ?",
        (recipe.title, recipe.chef, recipe.instructions, recipe_id)
    )
    connection.commit()
    updated = cursor.rowcount
    connection.close()
    return updated > 0


def delete_recipe(recipe_id: int) -> bool:
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM recipes WHERE id = ?", (recipe_id,))
    connection.commit()
    deleted = cursor.rowcount
    connection.close()
    return deleted > 0