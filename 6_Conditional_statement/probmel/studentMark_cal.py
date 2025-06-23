# problem to solve and get enter all four subject mark and score 33% in each subject it';s comoulsort

sub1 = int(input("Enter a first subject number:"))
sub2 = int(input("Enter a sec subject number:"))
sub3 = int(input("Enter a third subject number:"))
sub4 = int(input("Enter a fourth subject number:"))

# check here should student score 33% in every subject

fSub1 = (sub1/100)*100
fSub2 = (sub2/100)*100
fSub3 = (sub3/100)*100
fSub4 = (sub4/100)*100


if fSub1 > 33 and fSub2 > 33 and fSub3 >33 and fSub4 >33:
     totalScore = sub1 + sub2 + sub3 + sub4
     percentage = totalScore/400*100

     print("Your final subject value is:", percentage,"%")
else:
    print("Student failed in few subjects.")
