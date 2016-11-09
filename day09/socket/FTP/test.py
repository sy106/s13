#!user/bin/env python
#-*-coding:utf-8 -*-
# Author: Sy106

def save_user(self):
    # dic_user = {'username': self.username, 'password': commons.md5(self.password)}
    DIC[self.username] = [commons.md5(self.password)]
    if os.path.exists('user_db'):
        pickle.dump(DIC, open('user_db'), 'ab')
    else:
        pickle.dump(DIC, open('user_db'), 'wb')


def user_create(self):
    if os.path.exists('user_db'):
        DIC = pickle.load(open('user_db'), 'rb')
        if self.username in DIC and commons.md5(self.password) == DIC[self.username][0]:
            result = userinfo(self.username, self.password)
            result.save_user()
            return 0
        else:
            return 1
    else:
        result = userinfo(self.username, self.password)
        result.save_user()
        print("the user is not exit !")
        return 1