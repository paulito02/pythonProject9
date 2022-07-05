print("welcome \n what will you like to do")
print("login          ",end="")
print("create an account")
if input() == "create an account":
   print( username=input("input your username : "))
   while True:
       pin = input("input your 4 digit pin : ")
       if (len(pin)==4):
           break
   print("welcome")
   while True:
        email = input('input your valid email : ')
        b = email[::-1]
        c = b[0:10]
        d = 'moc.oohay@'
        if (c == d):
            break
   print("good")
   print ("this is your puk number keep it save")
   from random import randrange
   for i in range(0, 8):  # produce 8 digit number
        puk = randrange(1, 10)  # generate random number in the range 1....6
        print(puk, end="")
   print('')
else:
    pin_attempts = 4
    puk_attempts = 8
    pin_count = 0
    puk_count = 0
    user_input = " "
    while user_input != pin and pin_count < pin_attempts:
        user_input = input("please enter your 4 digit pin : ")
        pin_count += 1
        remaining_attempts = str(pin_attempts - pin_count)
        if user_input == str(pin):
            print("✔ correct" "welcome")
            break
        elif user_input != pin and pin_count < pin_attempts:
            print("× incorrect pin please try again")
            print("you have " + remaining_attempts + " attempt(s) left")
            if pin_count == 3:
                print("you have 1 more chance or else you pin will be blocked😯")
            # else:

        else:
            print("your pin has been blocked!")
     # to unblock the pin
            while user_input != puk and puk_count < puk_attempts:
                user_input = input("input your puk number")
                puk_count += 1
                remaining_attempts = str(puk_attempts - puk_count)
                if user_input == puk:
                    print("✔ correct""your line has be unblocked")
                    break
                elif user_input != puk and puk_count < puk_attempts:
                    print("incorrect, please try again ")
                    print("you have " + remaining_attempts + "attempt(s) left")
                    if puk_count == 7:
                        print("you have 1 more chance or else you pin will be blocked😯")
                else:
                    print("your sim has been blocked")

                    print("will you like to reset your password?")
                    a = input()
                    c = 'yes'
                    if a == c:
                        while True:
                            b = (input("input your recovery email :"))
                            if b == email:
                                print("input your new pin")
                                p = input()
                                print("comfirm your new pin")
                                p = input()
                                pin = str(pin.replace(p))
                                break
                    # # else:
                    #     print("visit the nearest branch to fix the issue")
print ("you can now proceed")