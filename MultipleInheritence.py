class Mobile():
    def generalProperties(self):
        print('Call')
        print('Text')

class Android():
    def specificProperties(self):
        print('Touch')
        print('Play Store')

class Ios(Mobile):
    def specificProperties(self):
        print('Security')
        print('App store')


class Mi(Mobile,Android):
    def miProperties(self):
        print('Mi A3')



A3=Mi()

A3.generalProperties()
A3.specificProperties()
A3.miProperties()



# pixel=Android() 

# pixel.specificProperties()
# pixel.generalProperties()

# iphoneX=Ios() 

# iphoneX.specificProperties()
# iphoneX.generalProperties()
