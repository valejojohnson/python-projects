# Create a program that will convert F degrees to C and vice versa

def f_to_c(temp):
    to_c = (temp - 32) * 5 // 9
    print(f"{temp}ºF = {to_c}ºC")


def c_to_f(temp):
    to_f = (temp * 9) // 5 + 32
    print(f"{temp}ºC = {to_f}ºF")


def get_temp():
    while True:
        try:
            return int(input("What is the local temp? \n"))
        except ValueError:
            print("Please enter an integer for temperature")


def get_unit():
    while True:
        unit = str(input("What is the unit of measure? Enter 'f' for Fahrenheit or 'c' for Celsius\n")).lower()

        if unit == 'c':
            return "c"
        elif unit == 'f':
            return "f"
        else:
            unit = str(input("Error. Please enter a valid unit of measure of 'f' or 'c' \n"))


def main():
    while True:
        temp = get_temp()
        measure = get_unit()

        if measure == "f":
            f_to_c(temp)
        elif measure == "c":
            c_to_f(temp)

        again = str(input("Do you want to enter another? ('yes' to continue, any other key to exit)\n")).lower()
        if not again in ['y', 'yes']:
            print("Exiting Program. Goodbye")
            break


if __name__ == "__main__":
    main()