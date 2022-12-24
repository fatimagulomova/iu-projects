from system import *


class TestHabit:

    def test_add_new_habit(self):
        habit = AddHabit()
        habit.add_habit(name='python_class', category='study', frequency='daily', duration='6 weeks', unitset='2 hours',
                        start_date='2022/12/15', file_db="test.db")

    def test_edit_habit(self):
        habit = EditHabit(habit_name="python_class", choice="unitset", new_value="2.5 hours")
        habit.edit(file_db="test.db")

    def test_analyse_habit(self):
        habit = AnalyzeHabit()
        habit.check_off(name="python_class", answer="yes", file_db="test.db")
        habit.report(purpose='all habits', file_db="test.db")

    def test_delete(self):
        habit = DeleteHabit()
        habit.delete_the_habit(name="python_class", file_db="test.db")
        import os
        os.remove("test.db")
