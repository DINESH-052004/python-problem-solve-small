name = "dinesh"
attendance = 82
internal_mark = 18
external_mark = 56

if(name==""):
    print("Invalid student name")

elif attendance < 75:
    print("Not eligible due to low attendance")

else:
    total = internal_mark + external_mark

    if total >= 90:
        print("Grade: A")
    elif total >= 75:
        print("Grade: B")
    elif total >= 50:
        print("Grade: C")
    else:
        print("Fail")

print("Process completed")
