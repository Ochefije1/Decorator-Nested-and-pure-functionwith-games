
def isSubscribed(func):
    subscribers = ["America", 'Nina', 'Ayo']
    def wrapper(user):
        if user['name'] in subscribers:
            user.update({'subscribed':True})
            return func(user)

    return wrapper


def showMovie():
    print('Showing Movie')


@isSubscribed
def viewMovie(user):
    try:
        if user['isSubscribed']:
            showMovie()
    except:
        print('Subscription Needed. User not subscribed')


user = {'name': 'America'}

viewMovie(user)



