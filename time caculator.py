print("hello world ")


seconds = eval(input("please enter the number of second:"))

# first computing the number of hours in the given njumber of seconds
# note: integer division with possible truncation
hours = seconds // 3600
# // gives the direct division of hours rom the given seconds


# compute the remaining seconds after the hours are accounted for
seconds = seconds % 3600
# % returns the remainder of the division and set it to the new variable s


# compute the number of minutes in the remaining number of seconds
minutes = seconds // 60  # note 1 hr= 60 secs * 60 min = 3600
# and 60 secs = 1 min
# get the number of seconds


# compute the remaining seconds after the minutes are accounted for
seconds = seconds % 60

print(hours, "hrs", minutes, "mins", seconds, "secs")

#     year
#   8736 hrs =1 yr
yrs = hours // 8736

hours = hours % 8736

#  months
# month = 30_days
months = hours // 30

# weeks
# 720 hrs = 1 month

hours = hours % 720
weeks = hours // 52

# days
# 168 hrs  = 1 week
hours = hours % 168
days = hours // 24


print(yrs, "yrs", months, "months", weeks, "weeks", days, "days")


