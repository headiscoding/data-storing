def main():
    outfile = open('names.txt', 'a')

    fname = input("What's your first name?")
    lname = input("What's your last name?")

    outfile.write(fname + ' ')
    outfile.write(lname + '\n')

    print("Thanks for the personal info lol")

    outfile.close()

main()