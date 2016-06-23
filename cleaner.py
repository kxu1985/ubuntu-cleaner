import os
import logging

class Cleaner():
    def __init__(self):
        pass
        
    def getList(self):
        """Get the full list of apt cache"""
        logging.info('Getting the list...')
        self.apt_cache_path = '/var/cache/apt/archives/'
        self.pattern = '.deb'
        apt_deb_list = os.listdir(self.apt_cache_path)
        self.apt_deb_list = []
        for apt_deb in apt_deb_list:
            #print("Check:" + apt_deb)
            if apt_deb.endswith(self.pattern):
                self.apt_deb_list.append(apt_deb)
        logging.info("\n".join(self.apt_deb_list))

    def deleteFiles(self, file_path, file_list):
        for self.file in file_list:
            os.remove(file_path+self.file)

def main():
    logging.basicConfig(filename='/var/log/ubuntu-cleaner.log', level=logging.DEBUG)
    cleaner = Cleaner()
    cleaner.getList()
    #print("\n".join(cleaner.apt_deb_list))
    #cleaner.deleteFiles(cleaner.apt_cache_path, cleaner.apt_deb_list)
    
if __name__ == "__main__":
    main()
