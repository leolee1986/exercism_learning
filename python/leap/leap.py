# my own Solution
###------------------------------------------------
# def is_leap_year(year):
#         if year % 400 == 0:
#             return True
#         elif year % 100 == 0 and year % 4 == 0:
#             return False
#         elif year % 4 == 0:
#             return True
#         else:
#             return False
###-------------------------------------------------

## here is some other solutions by others
### ------------------------------------------------
# def is_leap_year(year):
#     if (year % 4 == 0):
#         if (year % 100 == 0 and year % 400 != 0):
#             return False
#         return True
###-------------------------------------------------

### This is the shortest one I see
###-------------------------------------------------
def is_leap_year(year):
    return ((year % 400 == 0) or (year % 4 == 0 and not year % 100 == 0))
###-------------------------------------------------
