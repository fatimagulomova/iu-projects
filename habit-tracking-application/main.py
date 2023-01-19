from logo import logo
from system import *
import questionary

print(logo)
print("Welcome to the Habit Tracker!\n")


def cli():

    i = True
    while i:

        purpose = questionary.select("What do you want to do?",
                                     choices=["Add a habit", "Edit the existing habit",
                                              "Report/Check-off", "Predefined Habits", "Delete the habit", "Off"]).ask()

        if purpose == "Add a habit":

            name = questionary.text("What habit do you want to add?: ").ask().lower()
            category = questionary.select("Please set a category for your habit",
                                          choices=['study', 'hobby', 'sport']).ask()

            frequency = questionary.select("Please set a frequency for your habit",
                                           choices=['daily', 'weekly']).ask()

            duration = questionary.text("Please set a duration for your habit e.g 20 days/3 weeks): ").ask().lower()

            create_habit = AddHabit()
            create_habit.add_habit(name, category, frequency, duration, file_db="files/data.db")
            print("\n")

        elif purpose == "Edit the existing habit":
            try:
                habit_name = questionary.select("Which habit do you want to change?",
                                                choices=habit_names_from_data(file_db="files/data.db")).ask()
                choice = questionary.select("What do you want to change?",
                                            choices=['name', 'category', 'duration']).ask()

                new_value = questionary.text(f"Type a new {choice} for the '{habit_name}' habit: ").ask().lower()

                manage_habit = EditHabit(habit_name, choice, new_value)
                manage_habit.edit(file_db="files/data.db")
                print("\n")

            except sqlite3.OperationalError and ValueError:
                print("Please, create a habit first")
                pass

        elif purpose == "Report/Check-off":
            try:
                analyze_habit = AnalyzeHabit()

                answer = questionary.select("Do you want to check or report?", choices=['check', 'report']).ask()

                if answer == "check":
                    name = questionary.select("Please select:\n",
                                              choices=habit_names_from_data(file_db="files/data.db")).ask().lower()
                    analyze_habit.check_off(name=name, file_db="files/data.db")

                elif answer == "report":
                    purpose = questionary.select("Do you want to report all habits or one habit?",
                                                 choices=['All Habits', 'All Daily Habits',
                                                          'All Weekly Habits', 'One Habit']).ask().lower()
                    analyze_habit.report(purpose, file_db="files/data.db")
                print("\n")

            except sqlite3.OperationalError and ValueError:
                print("Please, create a habit first")
                pass

        elif purpose == "Predefined Habits":
            habit = PredefinedHabits()
            habit.report_predefined_habits(file_db="files/predefined-habits.db")

        elif purpose == "Delete the habit":
            try:
                habit_name = questionary.select("Which habit do you want to delete?",
                                                choices=habit_names_from_data(file_db="files/data.db")).ask()
                habit = DeleteHabit()

                habit.delete_the_habit(name=habit_name, file_db="files/data.db")
                print("\n")

            except sqlite3.OperationalError and ValueError:
                print("Please, create a habit first")
                pass

        elif purpose == "Off":
            i = False

        else:
            pass


if __name__ == "__main__":
    cli()
