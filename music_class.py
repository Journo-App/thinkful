class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds

    def solo(self, length):
        for i in range(length):
            print self.sounds[i % len(self.sounds)],
        print ""

class Bassist(Musician): # The Musician class is the parent of the Bassist class
    def __init__(self):
        # Call the __init__ method of the parent class
        super(Bassist, self).__init__(["Twang", "Thrumb", "Bling"])

class Guitarist(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super(Guitarist, self).__init__(["Boink", "Bow", "Boom"])

    def tune(self):
        print "Be with you in a moment"
        print "Twoning, sproing, splang"

class Drummer(Musician):
    def __init__(self):
        super(Drummer, self).__init__(['bang,', 'boom', 'bust'])

    def addup(self, stop_value=5): 
        count = 0 
        for n in range(1, stop_value):
            if n <= stop_value:
                count += 1
        print "The drummer is counting to", count
        

class Band(Musician):
    def __init__(self):
        super(Band, self).__init__(['screetch'])

    def band_play(self):
        print "and now for the band"
        

if __name__ == '__main__':
    
    mary = Drummer()
    mary.solo(3)
    mary.addup()
    print "Now she is spontaneously combusting"

    nigel = Guitarist()
    nigel.solo(6)
    #print nigel.sounds

    devin = Bassist()
    devin.solo(5)

    
    print "You're all fired"



