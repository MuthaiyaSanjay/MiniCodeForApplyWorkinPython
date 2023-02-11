def work():
    print("\nAre you Finished your ug Degree??")
    degree = input()
    no = 'no'
    if (degree == 'yes'):
        print("You are more Eligible to work")

    elif (degree == 'no'):
        print("Come after you Finished your UG Degree")
    else:
        print("enter Valid yes or no")
        work()
name=input("Enter Your Name\n")
print("Enter after 1990 Batches only to Eligible to work\n")
year=int(input("Enter your Birth Year\n"))
age=2023-year
if(year>1990 and year<2020):
    if(age>18):
        print("Your age is",age, 'so you are Eligible to apply')
        work()
else:
    print("You are don't eligibe to apply work")
