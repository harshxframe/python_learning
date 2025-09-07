from functools import wraps


def authAccess(funk):
    def wrapper(access):
        print("Function began")
        if access == "admin":
             return funk(access)
        else:
            print("Access Denied, Admin only")
            return None
    return wrapper


@authAccess
def makeRequest(acc):
    print("Access Granted")


makeRequest("admin")