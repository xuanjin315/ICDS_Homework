# get user input
while True:
    your_year =  input("Enter a year: ")

## you code needs to do the following things:
## 1. check if it is a integer; if not, ask the user to re input 
## 2. check if it is non negative; if not, ask the user to re input 
## 3. print the user's animal of the year on the screen
    if not your_year.isdigit():
        print("Please enter a valid integer year.")
  
    else:
        year=int(your_year)
        zodiac_animals = ["Rat.", "Ox.", "Tiger.", "Hare.", "Dragon.", "Snake.", "Horse.", "Goat.", "Monkey.", "Rooster.", "Dog.", "Pig."]
        zodiac_year_index=year%12-2008%12
        zodiac_year=zodiac_animals[zodiac_year_index]
        print(year,"is the year of",zodiac_year)
        break
     