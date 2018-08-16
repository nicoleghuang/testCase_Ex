def diction():
    d={'username1':'pw1','username2':'pw2'}


    print("Read username and password successfully!")
    return d

def website():
    url='http://test1.coinex.com/account/signin'
    print("Read url successfully!")
    return url

def login():
    id_accout='//*[@id="__nuxt"]/div[2]/div[3]/div/div[3]/div/div[2]/form/div[2]/div[1]/div/input'
    id_pw='//*[@id="__nuxt"]/div[2]/div[3]/div/div[3]/div/div[2]/form/div[2]/div[2]/div/input'
    act={id_accout:id_pw}
    return act

