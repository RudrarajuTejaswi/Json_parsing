import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
import inspect
import logging


@pytest.mark.usefixtures("browser_access")
class BaseClass():

    def explicitwait_presence_of_item(self, enteredText):
        explicit_wait = WebDriverWait(self.driver,20)
        explicit_wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,enteredText)))

    def select_dropdown_by_text(self,text,locator):
        dropdown = Select(locator)
        dropdown.select_by_visible_text(text)
        # dropdown.select_by_index(0)

    def getLogger(self):
        loggerName = inspect.stack()[1][3]#to get the testcase name (method name)
        #logger = logging.getLogger(__name__)  # name gives the filename else root will be printed
        logger = logging.getLogger(loggerName)
        # below is the industry msg standard but can vary
        # asctime - date time format yyyy-mm-dd hh:mm:ss
        # levelname -debug or info or warning or error or critical
        # name - is the file name (to recognized from where the msg is generated)
        msgFormat = logging.Formatter(
            "%(asctime)s:%(levelname)s:%(name)s:%(message)s")  # s to get in string so that message can be concatinated
        filehandler = logging.FileHandler("logFile.log")
        filehandler.setFormatter(msgFormat)
        logger.addHandler(filehandler)  # logger obj is mapped to filehandler(having msg format n logfile location)
        logger.setLevel(logging.DEBUG)  # to set what messages shud be printed
        return logger