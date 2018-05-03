# ex40a.py
# examples

import ex40a_mystuff

# call function from ex40a_mystuff
ex40a_mystuff.apple()
# call variable from ex40a_mystuff
print(ex40a_mystuff.tangerine)


mystuff = {'apple': 'I am apples!'}
# compare to call from dict
print(mystuff['apple'])


class MyStuff(object):

    def __init__(self):
        self.tangerine = "and now a thousand years between"

    def apple(self):
        print("I AM CLASSY APPLE")


print('-' * 10)
thing = MyStuff()
thing.apple()
print(thing.tangerine)
