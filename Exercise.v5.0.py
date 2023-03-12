import easygui

# variables
school_name = easygui.enterbox("Enter the name of the school")
max_children = easygui.integerbox("What is the maximum number of children allowed per class:\n"
                                  "Must be a number between 10 and 30")
children_number = easygui.integerbox(f"What is the total number of children at {school_name}:?\n"
                                     f"Note: Must be an integer between 10 and 1400",
                                     "Maximum number of students")
