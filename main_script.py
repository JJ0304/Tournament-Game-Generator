def get_number_of_teams():
    while True:
        num_teams = int(input("Enter the number of teams in the tournament: "))

        if num_teams >= 2:
            break

        print("The minimum number of teams is 2, try again")

    return num_teams