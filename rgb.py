# !/usr/bin/env python3

# created by: Ahmad El-khawaldeh
# created on: Dec 2020
# this program is the "RGB code"

def main():

    counter_number1 = 0
    counter_number2 = 0
    counter_number3 = 0

    for counter_number1 in range(0, 256):
        for counter_number2 in range(0, 256):
            for counter_number3 in range(0, 256):
                print("RGB ({0}, {1}, {2})".format
                      (counter_number1, counter_number2, counter_number3))


if __name__ == "__main__":
    main()
