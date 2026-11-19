import pytest
from television import *

class Test:
    def setup_method(self) -> None:
        '''
        This method sets up a test object.
        '''
        self.tv_one = Television()
    def teardown_method(self) -> None:
        '''
        This method tears down the test object.
        '''
        del self.tv_one
    def test_init(self) -> None:
        '''
        This method tests the init method by making sure the variables are set to their default values.
        '''
        assert self.tv_one.__str__() == 'Power = False, Channel = 0, Volume = 0'
    def test_power(self) -> None:
        '''
        This method tests the power method by making sure the status changes.
        '''
        self.tv_one.power()
        assert self.tv_one.__str__() == 'Power = True, Channel = 0, Volume = 0'
        self.tv_one.power()
        assert self.tv_one.__str__() == 'Power = False, Channel = 0, Volume = 0'
    def test_mute(self) -> None:
        '''
        This method tests the mute method by checking the volume.
        '''
        self.tv_one.power()
        self.tv_one.volume_up()
        self.tv_one.mute()
        assert self.tv_one.__str__() == 'Power = True, Channel = 0, Volume = 0'
        self.tv_one.mute()
        assert self.tv_one.__str__() == 'Power = True, Channel = 0, Volume = 1'
        self.tv_one.mute()
        self.tv_one.power()
        assert self.tv_one.__str__() == 'Power = False, Channel = 0, Volume = 0'
        self.tv_one.power()
        self.tv_one.mute()
        assert self.tv_one.__str__() == 'Power = True, Channel = 0, Volume = 1'
    def test_channel_up(self) -> None:
        '''
        This method tests the channel_up method by checking the channel.
        '''
        self.tv_one.channel_up()
        assert self.tv_one.__str__() == 'Power = False, Channel = 0, Volume = 0'
        self.tv_one.power()
        self.tv_one.channel_up()
        assert self.tv_one.__str__() == 'Power = True, Channel = 1, Volume = 0'
        self.tv_one.channel_up()
        self.tv_one.channel_up()
        self.tv_one.channel_up()
        assert self.tv_one.__str__() == 'Power = True, Channel = 0, Volume = 0'
    def test_channel_down(self) -> None:
        '''
        This method tests the channel_up method by checking the channel.
        '''
        self.tv_one.channel_down()
        assert self.tv_one.__str__() == 'Power = False, Channel = 0, Volume = 0'
        self.tv_one.power()
        self.tv_one.channel_down()
        assert self.tv_one.__str__() == 'Power = True, Channel = 3, Volume = 0'
    def test_volume_up(self) -> None:
        '''
        This method tests the volume_up method by checking the volume.
        '''
        self.tv_one.volume_up()
        assert self.tv_one.__str__() == 'Power = False, Channel = 0, Volume = 0'
        self.tv_one.power()
        self.tv_one.volume_up()
        assert self.tv_one.__str__() == 'Power = True, Channel = 0, Volume = 1'
        self.tv_one.mute()
        self.tv_one.volume_up()
        assert self.tv_one.__str__() == 'Power = True, Channel = 0, Volume = 2'
        self.tv_one.volume_up()
        assert self.tv_one.__str__() == 'Power = True, Channel = 0, Volume = 2'
    def test_volume_down(self) -> None:
        '''
        This method checks the volume_down method by checking the volume.
        '''
        self.tv_one.volume_down()
        assert self.tv_one.__str__() == 'Power = False, Channel = 0, Volume = 0'
        self.tv_one.power()
        self.tv_one.volume_up()
        self.tv_one.volume_down()
        assert self.tv_one.__str__() == 'Power = True, Channel = 0, Volume = 0'
        self.tv_one.volume_up()
        self.tv_one.mute()
        self.tv_one.volume_down()
        assert self.tv_one.__str__() == 'Power = True, Channel = 0, Volume = 0'
        self.tv_one.volume_down()
        assert self.tv_one.__str__() == 'Power = True, Channel = 0, Volume = 0'
