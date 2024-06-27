def banner(text):
    screen_width = 80
    if len(text) > screen_width - 4:
        print("EEK!!")
        print("the text is too long to fit in the specified width".upper())

    if text == "*":
        print("*" * screen_width)
    else:
        centered_text = text.center(screen_width - 4).upper()
        output_string = "**{0}**".format(centered_text)
        print(output_string)


banner("*")
banner("This is just a test")
banner("welcome to a DOD IS. If you are not authorized to be in this system")
banner("please leave now. Further actions will result in military action.")
banner("The penalty is up to, and including death.")
banner('*')
