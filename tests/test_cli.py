from nose.tools import *
from phone2address import cli


def test_get_address():
    assert_equal(cli.get_address('13012345678'), ['重庆', ''])
    assert_equal(cli.get_address('110'), False)


def test_process_xlsx():
    pass
