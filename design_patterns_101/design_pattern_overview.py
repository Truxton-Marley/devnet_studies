#Recommended book: Design Patterns, Elements of Reusable Object-Orientated Software
#Notes for CBT Nuggets DevNet course

#################################################
########   Singleton Design Pattern   ###########
#################################################

#Singleton Design: ONLY INSTANCIATED ONCE!!!
#Database connections could be an example

#BF: "A class with a private instance variable representing its only 
# it's only instance, a public get_instance() method to retrieve the object,
# and a constructor to enforce self-instantiation."

class ConfigValues():

    _instance = None

    @staticmethod
    def getInstance():
        if ConfigValues._instance == None:
            ConfigValues()
        return ConfigValues._instance

    def __init__(self):
        """ As close to a private constructor as Python gets """
        if ConfigValues._instance != None:
            raise Exception("It's just a singleton!!!")
        else:
            ConfigValues._instance = self

s = ConfigValues.getInstance()
print(s)

#Still prints the same instance
s = ConfigValues.getInstance()
print(s)

#Singleton pattern is not "built-in" in Python


#################################################
########   Observer Design Pattern   ############
#################################################

class Observer():
    def update(self, subject):
        print("Stuff is changing!")
        print("Subject's state it now " + str(subject._state))


class Subject():
    
    _state = 0
    _observers = []

    def attach(self, observer):
        self._observers.append(observer)
    
    def detach(self, observer):
        self._observers.remove(observer)
    
    def notify(self):
        print("Updating the observers")
        for observer in self._observers:
            observer.update(self)

    def updateState(self, n):
        print("Updating State")
        
        self._state = n
        self.notify()

s = Subject()

s._state = 5

observer1 = Observer()
observer2 = Observer()
observer3 = Observer()

s.attach(observer1)
s.attach(observer2)
s.attach(observer2)

s.updateState(42)


#################################################
##########   Model View Controller   ############
#################################################

# Django is a 'related' example in Python, but the names
# are different

# model stores the data
class Device:
    hostname = ""
    ipAddress = ""
    port = ""

# view displays the data
class DevicesView:
    
    def showDevices(self, devices):
        for device in devices:
            print("--------")
            print(" " + device.hostname)
            print(" " + device.ipAddress)
            print(" " + device.port)
            print("--------")

# controller
class DevicesController:
    def __init__(self):
        #create dummy device for testing
        device = Device()
        device.ipAddress = "192.168.23.234"
        device.port = "3911"
        device.hostname = "kitty printer"
        devices = [device]

        v = DevicesView()

        v.showDevices(devices)

c = DevicesController()


