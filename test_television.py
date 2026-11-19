import pytest
from television import *

class Test:
    def setup_method(self):
        self.tv_one = Television()
    def teardown_method(self):
        del self.tv_one
    def test_init(self):
        assert self.tv_one.__str__() == 'Power = False, Channel = 0, Volume = 0'
    def test_power(self):
        self.tv_one.power()
        assert self.tv_one.__str__() == 'Power = True, Channel = 0, Volume = 0'
        self.tv_one.power()
        assert self.tv_one.__str__() == 'Power = False, Channel = 0, Volume = 0'
    def test_mute(self):
        self.tv_one.power()
        self.tv_one.volume_up()
        self.tv_one.mute()
        assert self.tv_one.__str__() == 'Power = True, Channel = 0, Volume = 0'
        self.tv_one.mute()
        assert self.tv_one.__str__() == 'Power = True, Channel = 0, Volume = 1'
        self.tv_one.power()
        self.tv_one.mute()
        assert self.tv_one.__str__() == 'Power = False, Channel = 0, Volume = 0'
        self.tv_one.power()
        self.tv_one.mute()
        assert self.tv_one.__str__() == 'Power = True, Channel = 0, Volume = 1'
    def test_channel_up(self):
        self.tv_one.channel_up()
        assert self.tv_one.__str__() == 'Power = False, Channel = 0, Volume = 0'
        self.tv_one.power()
        self.tv_one.channel_up()
        assert self.tv_one.__str__() == 'Power = True, Channel = 1, Volume = 0'
        self.test_channel_up()
        self.test_channel_up()
        self.test_channel_up()
        assert self.tv_one.__str__() == 'Power = True, Channel = 0, Volume = 0'
    def test_channel_down(self):
        pass
    def test_volume_up(self):
        pass
    def test_volume_down(self):
        pass