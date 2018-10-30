import os
from typing import List


def columnDic(filename):
    '''
    This function reads column information from a file in data folder, returns a column alias/full name dicitonary

    :param filename:
    :return: dictionray
    '''

    colDic = {}

    main_path=os.path.realpath(__file__)
    pos=main_path.index('src')
    main_path=main_path[:pos]
    full_file_path=main_path+'data/'+filename

    file_stream=open(full_file_path,"r")

    for line in file_stream:
        word_pair: List[str]=line.split(",")
        colDic[word_pair[0]]=word_pair[1]

    file_stream.close()

    return colDic




if __name__ == '__main__':
    testDic=columnDic('column_info.txt')
    print(testDic['hhsize'])
    print(testDic['r4t3'])





