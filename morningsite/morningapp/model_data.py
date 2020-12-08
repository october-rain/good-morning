class model_data():
    def add_profile(userID='',nickname='',headimg='',sex='',birth='',age='',school='',education='',sign=''):
        profile = {
            'userID':userID,
            'nickname':nickname,
            'headimg':headimg,
            'sex':sex,
            'birth':birth,
            'age':age,
            'school':school,
            'education':education,
            'sign':sign,
        }
        return profile
    
    def add_contact(weixin='',qq='',email='',github='',weibo=''):
        contact = {
            'weixin':weixin,
            'qq':qq,
            'email':email,
            'github':github,
            'weibo':weibo,
        }
        return contact