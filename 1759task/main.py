from datetime import datetime

def days_lived(birth_date, death_date):
    date_format = "%d.%m.%Y"
    birth_date = datetime.strptime(birth_date, date_format)
    death_date = datetime.strptime(death_date, date_format)

    if birth_date > death_date:
        raise ValueError("Invalid input: Birth date is after death date")

    delta = death_date - birth_date
    return delta.days + 1

n = int(input())
max_days = 0
longest_lived = 0
prev_death_date = None

if n < 1:
    raise ValueError("Invalid input: No entries provided")  # Изменено на < 1

for i in range(n):
    entry = input().split()

    if len(entry) < 3:
        raise ValueError("Invalid input: Insufficient elements in entry")

    try:
        days = days_lived(entry[0], entry[2])
    except ValueError as e:
        raise ValueError(f"Invalid input in line {i + 1}: {str(e)}")

    if days > max_days:
        max_days = days
        longest_lived = i + 1

    prev_death_date = entry[2]

print(longest_lived)
