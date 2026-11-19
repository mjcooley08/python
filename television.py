class Television:
    min_volume = 0
    max_volume = 2
    min_channel = 0
    max_channel = 3
    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = self.min_volume
        self.__channel = self.min_channel
        self.__old_volume = self.__volume
        #TODO get mute or volume methods to save old value of volume
    def power(self):
        if self.__status == False:
            self.__status = True
        else:
            self.__status = False
    def mute(self): #see if you can make O notation better if u have to check status.
        if self.__status == True:
            if self.__muted == True:
                self.__volume = self.__old_volume
                self.__muted = False
            else:
                self.__old_volume = self.__volume
                self.__volume = self.min_volume
                self.__muted = True
    def channel_up(self):
        if self.__status == True:
            if self.__channel != self.max_channel:
                self.__channel = self.__channel + 1
            else:
                self.__channel = self.min_channel
    def channel_down(self):
        if self.__status == True:
            if self.__channel > self.min_channel:
                self.__channel = self.__channel - 1
            else:
                self.__channel = self.max_channel
    def volume_up(self):
        if self.__status == True:
            if self.__muted == True:
                self.__volume = self.__old_volume
                self.__muted = False
            if self.__volume < self.max_volume :
                self.__volume = self.__volume + 1
    def volume_down(self):
        if self.__status == True:
            if self.__muted == True:
                self.__volume = self.__old_volume
                self.__muted = False
            if self.__volume > self.min_volume:
                self.__volume = self.__volume - 1
    def __str__(self):
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'