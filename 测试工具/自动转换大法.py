# -*- coding: utf-8 -*-

import xdrlib, sys

import xlrd
import json
import os
import codecs

from pip._vendor.distlib.compat import raw_input


class autochange():

    # 读取json文件并转换成dicts
    def readjson(jsonName):
        file = r'C:\Users\admin\PycharmProjects\测试工具\res\store-list.geojson'
        fb = open(file, 'r', encoding='UTF-8')
        dicts = json.load(fb)
        fb.close()
        print(dicts)
        #
        # for i in dicts:
        #     print(i["channel"])
        return dicts

        # 读取excel中的字段，存为

    def readexcel(filename, sheetnum):
        dir_case = 'C:\\Users\\admin\\PycharmProjects\\\测试工具\\res\\' + filename + '.xlsx'
        data = xlrd.open_workbook(dir_case)
        table = data.sheets()[sheetnum]
        nor = table.nrows
        nol = table.ncols
        dict = {}
        for i in range(1, nor):
            for j in range(nol):
                title = table.cell_value(0, j)
                value = table.cell_value(i, j)
                dict[title] = value
            yield dict

    # 比较excel和geojson中的数据
    # def compareData():


if __name__ == '__main__':
    for i in autochange.readexcel('test1', 0):
        print(i)
    autochange.readjson("store-list")
