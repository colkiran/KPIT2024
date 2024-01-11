Month = ['dec', 'aug', 'apr', 'nov', 'feb', 'oct', 'jan', 'mar', 'may', 'jul', 'sep', 'jun']

calendar_months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
sorted_months = []
for month in calendar_months:
    if month in Month:
        sorted_months.append(month)
print("Sorted Months:", sorted_months)
