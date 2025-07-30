Input = input("Type something random: \n")
aplhabets = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
boole = Input.isalpha()

if boole == True:
    print("You typed a string.")
else:
    print("This is not a string")
    print("You did not type a string.")