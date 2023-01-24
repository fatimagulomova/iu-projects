from system import *


class TestHabit:

    def test_add_new_habit(self):
        habit = AddHabit()
        habit.add_habit(name='piano class', category='hobby', frequency='weekly', duration='15 months',
                        file_db="files/predefined-habits.db")

    def test_edit_habit(self):
        habit = EditHabit(habit_name="programming", choice="duration", new_value="6 months")
        habit.edit(file_db="files/predefined-habits.db")

    def test_analyse_habit(self):
        habit = AnalyzeHabit()
        habit.check_off(name="programming", file_db="files/predefined-habits.db")
        habit.report(purpose='all habits', file_db="files/predefined-habits.db")

    def test_delete(self):
        habit = DeleteHabit()
        habit.delete_the_habit(name="no_coffee", file_db="files/predefined-habits.db")
