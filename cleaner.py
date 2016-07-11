#!/usr/bin/python3
import sys
import os
import logging
sys.path.append(os.path.abspath('/usr/local/src/ubuntu-cleaner'))
import util.util_apt as util_apt

class Cleaner():
    def __init__(self):
        pass
        
    def cleanApt(self):
        self.cleaner_apt = util_apt.UtilApt()
        self.cleaner_apt.getList()
        self.cleaner_apt.deleteFiles()

def main():
    if (os.path.isfile('/var/log/ubuntu-cleaner.log') is True):
        os.remove('/var/log/ubuntu-cleaner.log')

    logging.basicConfig(format='[%(asctime)s][%(levelname)s] %(message)s', \
                        handlers=[logging.FileHandler('/var/log/ubuntu-cleaner.log'), \
                                    logging.StreamHandler()], \
                        level=logging.DEBUG)
    cleaner = Cleaner()
    cleaner.cleanApt()
    
if __name__ == "__main__":
    main()
