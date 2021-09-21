count = 0
time = 0
while count < 24:
    while time < 13:
        print(f"{time}.00 am")
        time += 1
        count += 1
    time = 1
    while time < 13:
        print(f"{time}.00 pm")
        time += 1
        count += 1