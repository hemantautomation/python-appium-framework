from appium.webdriver.common.mobileby import MobileBy
from src.helpers.appiumdriver import Driver


class HomeScreen(Driver):
    """
    home screen locators
    """
    loginMenu = (MobileBy.XPATH, "//android.view.ViewGroup[@content-desc='Login']/android.widget.TextView")
    formsMenu = (MobileBy.ACCESSIBILITY_ID, "Forms")
    homeMenu = (MobileBy.ACCESSIBILITY_ID, "Home")
    swipeMenu = (MobileBy.ACCESSIBILITY_ID, "Swipe")

    # swipeMenu = {'ANDROID': (MobileBy.ACCESSIBILITY_ID, "Swipe"),'IOS': (MobileBy.ACCESSIBILITY_ID, "Swipe")}

    def __init__(self, driver):
        super().__init__(driver)