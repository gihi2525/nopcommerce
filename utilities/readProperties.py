import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\config.ini")

class ReadConfig():
    #
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getApplicationUsername():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getApplicationPassword():
        password = config.get('common info', 'password')
        return password

    @staticmethod
    def getChromeSeleniumPath():
        ChromeSeleniumPath = config.get('selenium paths', 'chrome')
        return ChromeSeleniumPath

    @staticmethod
    def getFirefoxSeleniumPath():
        firefoxSeleniumPath = config.get('selenium paths', 'firefox')
        return firefoxSeleniumPath

    @staticmethod
    def getEdgeSeleniumPath():
        edgeSeleniumPath = config.get('selenium paths', 'edge')
        return edgeSeleniumPath