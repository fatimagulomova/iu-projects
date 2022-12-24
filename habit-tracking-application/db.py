import sqlite3
from tabulate import tabulate


def get_db(name):
    db = sqlite3.connect(name)
    create_tables(db)
    return db


def create_tables(db):
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS habit_data (name varchar(250) NOT NULL, category text, frequency text, "
                   "duration varchar(250) NOT NULL, unitset varchar(250) NOT NULL, "
                   "start_date varchar(250) NOT NULL, end_date varchar(250) NOT NULL, completed INTEGER,"
                   "last_completed_day varchar(250) NOT NULL, streak_days INTEGER)")
    db.commit()


def create_habits(db, name: str, category: str, frequency: str, duration: str, unitset: str, start_date: str,
                  end_date: str, completed: int, last_completed_day: str, streak_days: int):
    cur = db.cursor()
    cur.execute(f"INSERT INTO habit_data VALUES('{name}', '{category}', '{frequency}', "
                f"'{duration}', '{unitset}', '{start_date}', '{end_date}', "
                f"'{completed}', '{last_completed_day}', '{streak_days}')")
    db.commit()


def get_table(db, thing, value):
    cursor = db.cursor()

    if thing is None and value is None:
        rows = cursor.execute(f"SELECT * FROM habit_data;")
        db.commit()
    else:
        rows = cursor.execute(f"SELECT * FROM habit_data WHERE {thing} = '{value}';")
        db.commit()

    def table(l_rows):
        first_row = ['Name', 'Category', 'Frequency', 'Duration', 'Unitset', 'Start Date', 'End Date',
                     'Completed', 'Last Completed Day', 'Streak Days']
        rows_listed = [list(row) for row in l_rows]
        rows_listed.insert(0, first_row)
        return tabulate(rows_listed, headers='firstrow', tablefmt='pretty')

    table = table(l_rows=rows)
    return table
