from ctypes import windll

def isAdmin():
        try:
            return windll.shell32.IsUserAnAdmin()
        except:
            return False