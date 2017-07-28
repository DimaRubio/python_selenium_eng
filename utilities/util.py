import time
import traceback
import random, string
import logging


class Util:

    def sleep(self, sec, info=""):
        try:
            time.sleep(sec)
        except InterruptedError:
            traceback.print_stack()

    def verifyTextContains(self, actualText, expectedText):

        if expectedText.lower() in actualText.lower():
            return True
        else:
            return False

    def verifyTextMatch(self, actualText, expectedText):

        if actualText.lower() == expectedText.lower():
            return True
        else:
            return False