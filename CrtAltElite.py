# Group Name: Crt Alt Elite
# DB_Practical1
# Due Date: 6 August 2025

data = []  # list
try:
    with open('file.txt', 'r', encoding='utf-8') as file:   # reads in text file
        next(file)  # skips first line in file.txt (headings)
        for line in file:  # reads each line + strips + splits
            line = line.strip()
            entry = line.split(",")

            field = {  # created a dictionary
                "city": entry[0],
                "city_population": entry[1],
                "country_name": entry[2],
                "continent": entry[3],
                "region": entry[4],
                "land_mass": entry[5],
                "indep_year": entry[6],
                "country_population": entry[7],
                "life_expectancy": entry[8],
                "GNP": entry[9],
                "government_form": entry[10],
                "head_of_state": entry[11],
                "capital": entry[12],
                "language": entry[13],
                "percentage": entry[14]
            }
            data.append(field)  # adds each row to data list

except FileNotFoundError:
    print("Error:\nFile (file.txt) Not Found")
    exit()


# helper functions for data type conversion
def to_int(value):
    # convert string to int safely
    try:
        return int(value)
    except (ValueError, TypeError):
        return 0


def to_float(value):
    # convert string to float safely
    try:
        return float(value)
    except (ValueError, TypeError):
        return 0.0

# questions a-h functions

# a) how many country names end with the letter 'a'?
def question_a():
    countries = {row["country_name"].lower() for row in data if row["country_name"]}    #iterates through country_name to create a set to handle duplicates
    count = sum(1 for c in countries if c.endswith('a'))    #counts countries ending with 'a'
    return str(count)   # returns answer as string


# b) list the five cities that have the highest city population
def question_b():
    cities_sorted = sorted(data, key=lambda x: to_int(x["city_population"]), reverse=True)  # sorts all data rows by city_population in descending order

    top_5 = []
    seen = set()
    for row in cities_sorted:   # iterates over the sorted list, handling duplicates in 'city' using 'seen' set
        if row["city"] not in seen:
            top_5.append(f"{row['city']}: {to_int(row['city_population'])}")    # creates top 5
            seen.add(row["city"])
        if len(top_5) == 5:
            break
    return "\n".join(top_5)     # returns formatted answer


# c) list the five countries that have the largest land mass
def question_c():
    countries_sorted = sorted(data, key=lambda x: to_float(x["land_mass"]), reverse=True)   # sorts all data rows by land_mass in descending order

    top_5 = []
    seen = set()
    for row in countries_sorted:    # iterates over the sorted list, handling duplicates in 'country_name' using 'seen' set
        if row["country_name"] not in seen:
            top_5.append(f"{row['country_name']}: {to_float(row['land_mass'])}")    # creates top 5
            seen.add(row["country_name"])
        if len(top_5) == 5:
            break
    return "\n".join(top_5)     # returns formatted answer


# d) how many countries gained independence between 1960 and 1980 (inclusive)?
def question_d():
    countries = {
        row["country_name"] for row in data
        if row["indep_year"].isdigit() and 1960 <= int(row["indep_year"]) <= 1980
    }   # create set of country names where the digit of indep_year is from 1960-1980
    return f"Count: {len(countries)}"   # returns answer


# e) which countries gained independence between 1830 and 1850 (inclusive)?
def question_e():
    countries = {
        row["country_name"] for row in data
        if row["indep_year"].isdigit() and 1830 <= int(row["indep_year"]) <= 1850
    }   # create set of country names where the digit of indep_year is from 1830-1850
    return ", ".join(sorted(countries))     # returns formatted answer


# f) list the five African countries that have the highest life expectancy
def question_f():
    africa = [row for row in data if row["continent"] == "Africa"]  # filters rows to continent of Africa
    africa_sorted = sorted(africa, key=lambda x: to_float(x["life_expectancy"]), reverse=True)      # sorts all africa rows by life_expectancy in descending order

    top_5 = []
    seen = set()
    for row in africa_sorted:   # iterates over the sorted list, handling duplicates in 'country_name' using 'seen' set
        if row["country_name"] not in seen:
            top_5.append(f"{row['country_name']}: {to_float(row['life_expectancy'])}")  # creates top 5
            seen.add(row["country_name"])
        if len(top_5) == 5:
            break
    return "\n".join(top_5)     # returns formatted answer

# g) which are the 5 most commonly spoken languages in the world?
def question_g():
    language_speakers = {}
    seen = set()

    for row in data:
        key = (row["country_name"], row["language"])#creates unique identifier for each country-language pair
        if key not in seen:
            seen.add(key)
            population = to_int(row["country_population"])
            percentage = to_float(row["percentage"])
            speakers = population * (percentage / 100.0)#calculates estimated number of speakers

            lang = row["language"]
            language_speakers[lang] = language_speakers.get(lang, 0) + speakers #adds speakers to the language total

    top_5 = sorted(language_speakers.items(), key=lambda x: x[1], reverse=True)[:5] #creates top 5
    return "\n".join([f"{lang}: {int(speakers):,} estimated speakers" for lang, speakers in top_5]) #returns formatted answer


# h) list the country names that end with the letter ‘a’, without any repetitions
def question_h():
    countries = {row["country_name"] for row in data if row["country_name"].endswith("a")}      # creates a set of unique country names ending with 'a'
    return ", ".join(sorted(countries))     # returns formatted answer


# create a list to format the answers
questions = [
    ("Question a:", question_a()),
    ("Question b:", question_b()),
    ("Question c:", question_c()),
    ("Question d:", question_d()),
    ("Question e:", question_e()),
    ("Question f:", question_f()),
    ("Question g:", question_g()),
    ("Question h:", question_h()),
]

# open new file to write answers
with open("file2.txt", "w") as output:
    for question, answer in questions:
        output.write(f"{question}\n{answer}\n\n")

print('All answers have been written to "file2.txt".')
