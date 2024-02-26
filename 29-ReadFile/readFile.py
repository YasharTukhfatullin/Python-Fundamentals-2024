try:
    with open(
        "C:\\Users\\yashar.tukhfatullin\\Desktop\\Computer Science Tutorial\\Python-Fundamentals-2024\\29-ReadFile\\test.txt"
    ) as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not file")
