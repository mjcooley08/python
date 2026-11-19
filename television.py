class Television:
    min_volume = 0
    max_volume = 2
    min_channel = 0
    max_channel = 3
    def __init__(self) -> None:
        '''
        This method creates a television object. It declares the default values for this object.
        '''
        self.__status = False
        self.__muted = False
        self.__volume = self.min_volume
        self.__channel = self.min_channel
        self.__old_volume = self.__volume
        #I couldn't find a way to save the old volume without defining another variable in the init method.
    def power(self) -> None:
        '''
        This method changes the status of a television object.
        '''
        if self.__status == False:
            self.__status = True
        else:
            self.__status = False
    def mute(self) -> None:
        '''
        This method changes the mute status of a television object.
        It either changes the volume to the minimum volume or back to the volume it was before it was muted.
        '''
        if self.__status == True:
            if self.__muted == True:
                self.__volume = self.__old_volume
                self.__muted = False
            else:
                self.__old_volume = self.__volume
                self.__volume = self.min_volume
                self.__muted = True
    def channel_up(self) -> None:
        '''
        This method increases the channel of the television object by one.
        If the channel is already at its maximum, it sets it back to the minimum channel.
        '''
        if self.__status == True:
            if self.__channel < self.max_channel:
                self.__channel = self.__channel + 1
            else:
                self.__channel = self.min_channel
    def channel_down(self) -> None:
        '''
        This method decreases the channel of the television object by one.
        If the channel is already at its minimum, it sets it back to the maximum channel.
        '''
        if self.__status == True:
            if self.__channel > self.min_channel:
                self.__channel = self.__channel - 1
            else:
                self.__channel = self.max_channel
    def volume_up(self) -> None:
        '''
        This method increases the volume of the television object by one.
        If the volume is already at its maximum, it keeps it at the maximum volume.
        If the volume was muted, it gets unmuted and set back to its old volume.
        '''
        if self.__status == True:
            if self.__muted == True:
                self.__volume = self.__old_volume
                self.__muted = False
            if self.__volume < self.max_volume :
                self.__volume = self.__volume + 1
    def volume_down(self) -> None:
        '''
        This method decreases the volume of the television object by one.
        If the volume is already at its minimum, it keeps it at the minimum volume.
        If the volume was muted, it gets unmuted and set back to its old volume.
        '''
        if self.__status == True:
            if self.__muted == True:
                self.__volume = self.__old_volume
                self.__muted = False
            if self.__volume > self.min_volume:
                self.__volume = self.__volume - 1
    def __str__(self) -> str:
        '''
        This method returns a string describing the television object.
        :return: Television's power, channel, and volume
        '''
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'