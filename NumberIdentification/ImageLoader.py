# -*- coding: UTF-8 -*-
from NumberIdentification import Loader

class ImageLoader(Loader):
    def get_picture(self, content, index):
        """
        get the picture from the file
        :param content: string data of the file
        :param index:
        :return:
        """
        start = index * 28 * 28 + 16
        picture = []
        for i in range(28):
            picture.append([])
            for j in range(28):
                picture[i].append(self.to_int(content[start + i * 28 + j]))
        return picture

    def get_one_sample(self, picture):
        sample = []
        for i in range(28):
            for j in range(28):
                sample.append(picture[i][j])
        return sample

    def load(self):
        content = self.get_file_content()
        date_set = []
        for index in range(self.count):
            date_set.append(self.get_one_sample(self.get_picture(content, index)))
        return date_set

