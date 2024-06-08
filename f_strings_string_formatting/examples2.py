
from datetime import datetime
from dataclasses import dataclass



### Aligning Text for Better Readability ### 
variable = "Hi my name is Charilaos"
# Align text to the right within a 30 character space
print(f"|{variable:>30}|")
# Align text to the left
print(f"|{variable:<30}|")
# Center text
print(f"|{variable:^30}|")
# Center text and fill spaces with a specific character
print(f"|{variable:*^30}|", "\n")



### Formatting Dates and Times Seamlessly ###
now = datetime.now()
# Display date in day-month-year format
print(f"Date: {now:%d-%m-%Y}")
# Display time in hour:minute:second format
print(f"Time: {now:%H:%M:%S}")
# Display locale's date and time
print(f"Locale's Date and Time: {now:%c}")
# Display time in 12-hour AM/PM format
print(f"Time in AM/PM format: {now:%I:%M %p}", "\n")



### Enhancing Readability of Large Numbers ###
n = 1000000000
# Using underscore as thousands separator
print(f"{n:_}")  # Outputs: 1_000_000_000
# Using comma as thousands separator
print(f"{n:,}", "\n")  # Outputs: 1,000,000,000



### Controlling Decimal Precision ###
num = 13.234
# Round the number to two decimal places
print(f"{num:.2f}")  # Result: 13.23
# Convert to whole number
print(f"{num:.0f}")  # Result: 13
# Print as percentage with two decimal places
value = 0.75321
print(f"{value:.2%}")  # Output: 75.32%
# Use thousands separator with percentage
print(f"{num:,.2%}", "\n")  # Result: 1,323.40%



### Quick Debugging with Inline Expressions ###
@dataclass
class Person:
    name: str
    age: int

person1 = Person(name="Tom", age=40)
person2 = Person(name="Ben", age=35)

# Debug output showing variable names and their values
print(f"{person1.name = }, age {person1.age = }, {person2.name = }, age {person2.age = }")


### Conditional Expressions within F-Strings ###
score = 85
# Conditional expression within an f-string
print(f"Your score is {score}, which is {'passing' if score >= 50 else 'failing'}.")





