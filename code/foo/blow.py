while True:
    try:
        n = raw_input("Please enter an integer: ")
        n = int(n)
        break
    except ValueError:
        print('\nPlease enter integer only')

print "\n\nCongrats, you have successfully entered an integer!"
