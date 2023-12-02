# simple unpacking

users = ["tony", "andy", "james"]

user1, user2, user3 = users

#multiple levels of unpacking

attrs = [1, ['tony', 10], ['andy', 20]]
user_id, (user1, score), (user2, score) = attrs

def fun1(a, b, c):
    print(a, b, c)

def fun2(*args):
    # print(args)  #
    args = list(args)
    args[0] = 'Geeksforgeeks'
    args[1]  = 'Awesome'
    # print (args)

    fun1(*args)

# fun2("Hello", "beautiful", "world")
# print(user_id)
# print(user1, score)
#
# print(user1)
# print(user2, score)


def test(*args):
    if 1 in args:
        return args[3]
    print(args)
a=[1,2,3]
# print(test("hi","i", "am", "joy", 1,5819393))

def test1(a,b,c):
    print(a,b,c)

def fun(**kwargs):
    print(type(kwargs))
    print(kwargs)
    for key, value in kwargs.items():
        print(key, value)

fun(name="geeks", ID="101", language="Python")


d = {'a': 2, 'b':4, 'c': 10}
# test1(**d)
