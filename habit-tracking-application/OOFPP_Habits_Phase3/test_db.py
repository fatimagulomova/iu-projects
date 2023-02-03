from system import *


class TestHabit:

    def test_add_new_habit(self):
        """This function is responsible for testing the “AddHabit” class."""
        habit = AddHabit()
        habit.add_habit(name='no-coffee', category='health', frequency='daily', duration='2 months',
                        file_db="files/predefined-habits.db")

    def test_edit_habit(self):
        """This function is responsible for testing the “EditHabit” class."""
        habit = EditHabit(habit_name="programming", choice="duration", new_value="6 months")
        habit.edit(file_db="files/predefined-habits.db")

    def test_analyse_habit(self):
        """This function is responsible for testing the “AnalyzeHabit” class."""
        habit = AnalyzeHabit()
        habit.check_off(name="programming", file_db="files/predefined-habits.db")
        habit.report(purpose='all habits', file_db="files/predefined-habits.db")

    def test_delete(self):
        """This function is responsible for testing the “DeleteHabit” class."""
        habit = DeleteHabit()
        habit.delete_the_habit(name="running", file_db="files/predefined-habits.db")
