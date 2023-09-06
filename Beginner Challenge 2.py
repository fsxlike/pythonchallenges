UserPoint = 0
countries = ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cabo Verde", "Cameroon", "Central African Republic", "Chad", "Comoros" , "Ivory Coast", "Djibouti", "Democratic Republic of the Congo", "Egypt", "Equatorial Guinea", "Eritrea", "Eswatini", "Ethiopia", "Gabon", "Gambia", "Ghana" , "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco" , "Mozambique", "Namibia", "Niger", "Nigeria", "Republic of the Congo", "Rwanda", "Sao Tome & Principe", "Senegal", "Seychelles", "Sierra Leone", "Somalia ", "South Africa", "South Sudan", "Sudan", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"]
for i in range(len(countries)):
    YourGuess = input("Guess an African country")
    if YourGuess in countries:
        print("Great you earned 1 point!")
        UserPoint = UserPoint + 1
        print("You have",UserPoint,"points")
        countries.remove(YourGuess)

    else:
        print("Ah oh wrong answer")
    if UserPoint == 54:
        break
print("Excellent young man!")
