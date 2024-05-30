#Task 1

attendees = input("Enter number of attendees: ")
count = int(attendees)
venue = ("large hall") if count >= 100 else ("conference room")
print(venue)

#Task 2
food_choice = input("Vegetarian meal? Yes/No ")
if food_choice == "Yes":
    print("Recommend Gourmet Meal Caterers")
else:
    pass
                    