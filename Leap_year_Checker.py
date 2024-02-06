a=int(input('Enter year: '))
file=open("leapyear.txt",'w')
file.write("Enter year:")
file.write(str(a))
file.write('\n')
if(a%4==0):
    print('It is a leap year')
    file.write("It is a leap year")
else:
    print('Not a leap year')
    file.write("Not a leap year")
file.close()