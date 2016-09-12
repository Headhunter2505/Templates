

class SomeClass(object):
    @classmethod
    def it(cls):
        print('%s') % cls

    @staticmethod
    def uncommon():
        """this should be global function"""
        print('aaa')