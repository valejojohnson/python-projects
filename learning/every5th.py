# This code is flash a message every
# 5th time a message appears

def message():
    counter = 1
    max = 51

    while counter < max:
        print(f"Generic message: {counter}")
        if counter % 5 == 0:
            print("This is a 5th")

        counter += 1


message()
