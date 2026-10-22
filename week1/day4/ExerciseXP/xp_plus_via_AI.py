import random


# Update these values when running the exercise on a different date.
CURRENT_YEAR = 2025
CURRENT_MONTH = 6
CURRENT_DAY = 1


def get_age(year, month, day):
    age = CURRENT_YEAR - year
    if (month, day) > (CURRENT_MONTH, CURRENT_DAY):
        age -= 1
    return age


def can_retire(gender, date_of_birth):
    year, month, day = (int(part) for part in date_of_birth.split("/"))
    age = get_age(year, month, day)

    if gender.lower() == "m":
        retirement_age = 67
    elif gender.lower() == "f":
        retirement_age = 62 if (year, month) > (1947, 4) else 60
    else:
        raise ValueError("Gender must be 'm' or 'f'.")

    return age >= retirement_age


def sum_repeated_number(x):
    digits = str(x)
    return sum(int(digits * multiplier) for multiplier in range(1, 5))


def throw_dice():
    return random.randint(1, 6)


def throw_until_doubles():
    throws = 0
    while True:
        first_die = throw_dice()
        second_die = throw_dice()
        throws += 1
        if first_die == second_die:
            return throws


def main():
    gender = input("Enter your gender (m/f): ").strip().lower()
    date_of_birth = input("Enter your date of birth (yyyy/mm/dd): ").strip()
    if can_retire(gender, date_of_birth):
        print("You can retire.")
    else:
        print("You cannot retire yet.")

    results = [throw_until_doubles() for _ in range(100)]
    print(f"Total throws: {sum(results)}")
    print(f"Average throws to reach doubles: {sum(results) / len(results):.2f}")


if __name__ == "__main__":
    main()