print("Running Programm")
class User:
    def __init__(self):
        print("starting")
    def createUser(name, psk0, psk1):
        if psk0 == psk1:
            try:
                file = open(str(name), mode='x')
                file.write(str(name))
                file.write('\n'+str(psk0))
                file.close()
                restart()
            except FileExistsError:
                print("WARNING: file already exists!!!")
        else:
            print("passwords do not match")

    def openUser(name, psswd):
        print("in progress")
        try:
            file = open(str(name), 'r')
            read = file.readlines(0)
            if read[1] == psswd:
                file.read()
                print()
                fileCurrent = open(str(name), 'r')
                print()
            else:
                print("psswd incorect")

        except FileNotFoundError:
            print("user not found")

    def restart():
        print("restaring program...")
        print("press F5 to finish process after clicking OK")
        #quit()
##init user:
user = User()

def main():
    print("press Ctrl+C to exit program")
    run = True
    while run == True:
        try:
            print("Press 1 to create new account")
            print("press 2 to open a account")
            userIn = input("type option and press enter:  ")
            if userIn == '1':
                name = input("user name:  ")
                psk0 = input("type password:  ")
                psk1 = input("confirm password:  ")
                createUser(name, psk0, psk1)
            if userIn == '2':
                name = input("user name:  ")
                psswd = input("password:  ")
        except KeyboardInterrupt:
            print("exiting program")
            run = False

##start main loop:
main()
