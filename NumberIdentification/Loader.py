# -*-coding:utf-8-*-
import struct
from datetime import datetime

class Loader(object):
    def __int__(self, path, count):
        '''
        init the loader
        :param path:  date file path
        :param count: number of sample in the file
        :return:
        '''
        self.path = path
        self.count = count

    def get_file_content(self):
        """
        read the content of the file
        :return:
        """
        f = open(self.path, 'rb')
        content = f.read()
        f.close()
        return content

    def to_int(self, byte):
        """
        turn unsigned byte into int
        :param byte: string
        :return:
        """
        return struct.unpack('B', byte)
