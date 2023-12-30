score=int(input("Enter score "))
if score>=90:
    print("Grade A")
else:
    if score>=80:
        print("Grade B")
    else:
        if score>=60:
            print("Grade C")
        else:
            if(score>=40):
                print("Grade D")
            elif(score<=40):
                    print("Failed!!!")
                