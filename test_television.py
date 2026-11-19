import pytest
from television import *

class Test:
    def setup_method(self) -> None:
        self.tv_one = Television()
    def teardown_method(self) -> None:
        del self.tv_one
    def test_init(self) -> None:
        assert self.tv_one.__str__() == 'Power = False, Channel = 0, Volume = 0'
    def test_power(self) -> None:
        self.tv_one.power()
        assert self.tv_one.__str__() == 'Power = True, Channel = 0, Volume = 0'
        self.tv_one.power()
        assert self.tv_one.__str__() == 'Power = False, Channel = 0, Volume = 0'
    def test_mute(self) -> None:
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
        self.tv_one.channel_down()
        assert self.tv_one.__str__() == 'Power = False, Channel = 0, Volume = 0'
        self.tv_one.power()
        self.tv_one.channel_down()
        assert self.tv_one.__str__() == 'Power = True, Channel = 3, Volume = 0'
    def test_volume_up(self) -> None:
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
