print("Running Programm")
class User:
    def __init__(self):
        print("starting")
        self.fileCurrent = None
        self.run = True
    def createUser(self, name, psk0, psk1, moneyIn):
        if psk0 == psk1:
            try:
                file = open(str(name), mode='x')
                file.write(str(name))
                file.write('\n'+str(psk0))
                file.write('\n'+str(moneyIn))
                file.close()
                self.restart()
            except FileExistsError:
                print("WARNING: file already exists!!!")
        else:
            print("passwords do not match")

    def openUser(self, name, psswd):
        try:
            file = open(str(name), 'r')
            read = file.readlines(0)
            if read[1] == psswd+'\n':
                file.read()
                print()
##                self.dan = open('doNotDelete', 'a')
##                self.dan.write(str(name))
##                self.dan.close()
                self.fileCurrent = open(str(name), 'r')
                self.read = self.fileCurrent.readlines()
                print("line 1 is the user name")
                print("line 2 in the password")
                print("line 3 is the current balance")
                print()
                print(self.read)
                print()
################################################################################
                while self.run == True:
                    print("press Ctrl+C to exit")
                    try:
                        print()
                        print("Press 1 to deposit")
                        print("press 2 to withdraw")
                        userIn = input("type option and press enter:  ")
                        if userIn == '1':
                            amount = input("amount to deposit:  ")
                            user.deposit(amount)
                        if userIn == '2':
                            name = input("user name:  ")
                            psswd = input("password:  ")
                            user.openUser(name, psswd)
                    except KeyboardInterrupt:
                        print("exiting program")
                        self.run = False
                self.run = True
                self.restart()
            else:
                print("psswd incorect")

        except FileNotFoundError:
            print("user not found")

    def restart(self):
        print("restaring program...")
        print("press F5 to finish process after clicking OK")
        #quit()
    def deposit(self, dep):
        pass
    def withdraw(self, wit):
        pass
        
##init user:
user = User()

def main():
    print("press Ctrl+C to exit program")
    run = True
    while run == True:
        try:
            print()
            print("Press 1 to create new account")
            print("press 2 to open a account")
            userIn = input("type option and press enter:  ")
            if userIn == '1':
                name = input("user name:  ")
                psk0 = input("type password:  ")
                psk1 = input("confirm password:  ")
                moneyIn = input("total of first deposit:  ")
                user.createUser(name, psk0, psk1, moneyIn)
            if userIn == '2':
                name = input("user name:  ")
                psswd = input("password:  ")
                user.openUser(name, psswd)
        except KeyboardInterrupt:
            print("exiting program")
            run = False

##start main loop:
main()
