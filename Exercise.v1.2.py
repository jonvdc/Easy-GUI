import easygui

while True:
    nz_word = easygui.enterbox("Please enter the NZ word", "Word to check")
    us_word = nz_word

    if "our" in nz_word:
        us_word = nz_word.replace("our", "or")
    elif "ise" in nz_word:
        us_word = nz_word.replace("ise", "ize")
    elif "yse" in nz_word:
        us_word = nz_word.replace("yse", "yze")

    another_word = easygui.buttonbox(f"The US spelling of {nz_word} is {us_word}"
                                     f"\n\nDo you want to try another word?", "Check another",
                                     choices=["Yes", "No"])

    if another_word == "No":
        break
