import easygui

while True:
    bucket_list = easygui.enterbox("Enter the name of 5 places you would "
                                   "most like to visit\nSeparate them with a comma\n"
                                   "Enter bucket list: ")
    places = bucket_list.split(",")
    if len(places) > 5:
        easygui.msgbox(f"Sorry, but you have entered more than the required amount\n"
                       f"You can only enter a max of "
                       f"5 places\nYou entered {len(places)} places.\n",
                       f"Too many places")
    else:
        break

for place in places:
    output = f"\n*  ".join(places)
easygui.msgbox(f"Your bucket list is: \n\n*  {output}", "Travel bucket list")
