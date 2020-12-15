months_conversion= {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "Ma": "May",
    "Ju": "June",
    "Jul": "July",
    "Aug": "August",
    "Sept": "Sept",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

print(months_conversion.get("Dec"))
print(months_conversion.get("no"))

#For getting output other than none for key/char which ain't in dictinoary
print(months_conversion.get("no", "Not a valid key or char"))