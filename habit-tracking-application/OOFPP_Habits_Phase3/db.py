import sqlite3
from tabulate import tabulate


def get_db(name):
    """
    This function is responsible for opening the db file.
        :param name: the name of the db file
    """

    db = sqlite3.connect(name)
    create_tables(db)
    return db


def create_tables(db):
    """
    This function is responsible for creating tables in the database file.
        :param db: the name of the db file
    """

    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS habit_data ("
                   "name varchar(250) NOT NULL, category text, frequency text, "
                   "duration varchar(250) NOT NULL, start_day varchar(250) NOT NULL,"
                   "marked_off INTEGER, last_completed_day varchar(250) NOT NULL, streak_days INTEGER, "
                   "longest_streak_days INTEGER)")
    db.commit()


def create_habits(db, name: str, category: str, frequency: str, start_date: str, duration: str,
                  marked_off: int, last_completed_day: str, streak_days: int, longest_st_days: int):
    """
    This function is responsible for storing data about habits in a database file.
        :param db: the name of the db file
        :param name: the name of the habit
        :param category: the category of the habit
        :param frequency: the frequency of the habit
        :param start_date: the date when this habit was created
        :param duration: how long the habit lasts
        :param marked_off: how many times the habit was performed
        :param last_completed_day: the day when the habit was marked as completed
        :param streak_days: the number of streak days
        :param longest_st_days: the number of the longest streak days
    """
    cur = db.cursor()
    cur.execute(f"INSERT INTO habit_data VALUES("
                f"'{name}', '{category}', '{frequency}', '{duration}','{start_date}', '{marked_off}', "
                f"'{last_completed_day}', '{streak_days}', '{longest_st_days}')")
    db.commit()


def get_table(db, thing, value):
    """
    This function is responsible for visualizing data about habits in a table.
        :param db: the name of the db file
        :param thing: the name of the column in the table
        :param value: the value of the column
    """
    cursor = db.cursor()

    if thing is None and value is None:
        rows = cursor.execute(f"SELECT * FROM habit_data;")
        db.commit()
    else:
        rows = cursor.execute(f"SELECT * FROM habit_data WHERE {thing} = '{value}';")
        db.commit()

    def table(l_rows):
        first_row = ['Name', 'Category', 'Frequency', 'Duration', 'Start Date', 'Marked off',
                     'Last Completed Day', 'Streak Days', 'Ln. Streak Days']
        rows_listed = [list(row) for row in l_rows]
        rows_listed.insert(0, first_row)
        return tabulate(rows_listed, headers='firstrow', tablefmt='pretty')

    table = table(l_rows=rows)
    return table
