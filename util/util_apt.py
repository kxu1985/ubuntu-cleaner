#!/usr/bin/python3
import os
import logging

class UtilApt():
    def __init__(self):
        self.apt_cache_path = '/var/cache/apt/archives/'
        self.pattern = '.deb'
        self.apt_deb_list = []
        pass

    def getList(self):
        """Get the full list of apt cache"""
        logging.info('Getting the list from %s...',self.apt_cache_path)
        apt_deb_list = os.listdir(self.apt_cache_path)
        for apt_deb in apt_deb_list:
            if apt_deb.endswith(self.pattern):
                self.apt_deb_list.append(apt_deb)
                logging.info('Got %s', apt_deb)
        logging.info('Got %d cached installation packages.', len(self.apt_deb_list))

    def deleteFiles(self):
        """Delete all the files in the list"""
        logging.info('Removing the files from %s...',self.apt_cache_path)
        for f in self.apt_deb_list:
            os.remove(self.apt_cache_path + f)
            logging.info('Removed %s', f)
        logging.info('Removed %d old files.', len(self.apt_deb_list))
