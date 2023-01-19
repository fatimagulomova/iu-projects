import sqlite3
from tabulate import tabulate


def get_db(name):
    db = sqlite3.connect(name)
    create_tables(db)
    return db


def create_tables(db):
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS habit_data ("
                   "name varchar(250) NOT NULL, category text, frequency text, "
                   "duration varchar(250) NOT NULL, start_day varchar(250) NOT NULL,"
                   "marked_off INTEGER, last_completed_day varchar(250) NOT NULL, streak_days INTEGER, "
                   "longest_streak_days INTEGER)")
    db.commit()


def create_habits(db, name: str, category: str, frequency: str, start_date: str, duration: str,
                  marked_off: int, last_completed_day: str, streak_days: int, longest_st_days: int):
    cur = db.cursor()
    cur.execute(f"INSERT INTO habit_data VALUES("
                f"'{name}', '{category}', '{frequency}', '{duration}','{start_date}', '{marked_off}', "
                f"'{last_completed_day}', '{streak_days}', '{longest_st_days}')")
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
        first_row = ['Name', 'Category', 'Frequency', 'Duration', 'Start Date', 'Marked off',
                     'Last Completed Day', 'Current Streak Days', 'Longest Streak Days']
        rows_listed = [list(row) for row in l_rows]
        rows_listed.insert(0, first_row)
        return tabulate(rows_listed, headers='firstrow', tablefmt='pretty')

    table = table(l_rows=rows)
    return table
