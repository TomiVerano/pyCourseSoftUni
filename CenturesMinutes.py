centures = int(input())
years = centures * 100
days = int(years * (365.2422))
hours = days * 24
minutes = hours * 60
print('{0:.0f} centuries = {1:.0f} years = {2:.0f} days = {3:.0f} hours = {4:.0f} minutes'
      .format(centures, years, days, hours, minutes))