class Git:
    def __init__(self,config):
        self.appid = config.getDados("GIT_REPO")
        self.dn = config.getDados("GIT_ACCOUNT")
        self.name = config.getDados("GIT_PASSWD")