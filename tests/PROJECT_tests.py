from nose import *
import PROJECT.MODULE


def setup(): print "Set up your tests"


def teardown(): print "Clean up after the tests"


@with_setup(setup, teardown)
def test_something_fancy(): assert PROJECT.MODULE.do_something_fancy()
