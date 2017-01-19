
def func2():
    print "Hello Worldy World!"

class TestClass(object):

    # Initiating function in new class
    def __init__(self, arg1, arg2, arg3):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3

    def hello(self):
        print "\nhello function in TestClass"
        print "I have these args: %s %s %s" % (self.arg1, self.arg2, self.arg3)

    def not_hello(self):
        print "\nnot_hello function in TestClass"
        print "I still have these in another function:"
	print "{} {} {}".format(self.arg1, self.arg2, self.arg3)


class ChildTestClass(object):

    def hello(self):
        print "\nhello function in ChildTestClass"
        print "I have these args: %s %s %s" % (self.arg1, self.arg2, self.arg3)


if __name__ == "__main__":
    print "This is main task for world.py"

    test_object = TestClass('mark', 'chris', 'tom')
    print
    print test_object.arg1, test_object.arg2, test_object.arg3
    test_object.hello()
    test_object.not_hello()
    print

    new_test_object = TestClass('pedro', 'josh', 'dennis')
    print
    print new_test_object.arg1, new_test_object.arg2, new_test_object.arg3
    new_test_object.hello()
    # new_test_object.not_hello()
    print


