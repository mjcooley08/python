from television import *
import pytest

class Test:
    def setup_method(self):
        self.tv_one = Television()
        self.tv_two = Television()
    def teardown_method(self):
        del self.tv_one
        del self.tv_two
    def test_init(self):
        pass
    def test_power(self):
        pass
    def test_mute(self):
        pass
    def test_channel_up(self):
        pass
    def test_channel_down(self):
        pass
    def test_volume_up(self):
        pass
    def test_volume_down(self):
        pass