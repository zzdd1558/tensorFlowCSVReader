# -*- coding:utf-8 -*-
import numpy as np
import csv
from PIL import Image

'''
    Method
    __init__ : class 생성자.
    parseInt : 매개변수로 들어온 value를 정수로 바꿔준다.
    read_csv : 해당하는 csv파일을 읽고 data , label return
    showImage : numpy.ndarray Type의 trainData 넣어주면 image로 보여준다.
    
    2018.06.15 (금) 수정.
    최 윤진.
'''

class CSV :

    def __init__(self):
        print("CSV __init__")

    def parseInt(self , value):
        return int(value)

    '''
        CSV 파일 읽고 
        @:parameter 
         - csvFilePath : 파일의 경로
         - readWay : 읽기 방식 
    '''
    def read_csv(self , csvFilePath , readWay):
        data = []
        label = []

        with open(csvFilePath , readWay) as f:
            readData =  csv.reader(f)

            for line in readData:
                data.append(list(map(self.parseInt, line[1:])))
                label.append(line[:1])
            f.close()
        return (data , label)


    ''' 
        numpy.ndarray Type의 trainData 배열 하나만 넣어주면 image Show
        28 x 28 사이즈의 이미지로 출력함.
    '''
    def showImage(self, ndarrayData):
        print("CSVImage showImage()")
        showData = np.array(ndarrayData)
        showData = np.reshape(showData, (28, 28))
        img = Image.fromarray(showData.astype('uint8'))
        img.show()

if __name__ == "__main__":

    print ('CSV Class Main Success')

else :
    print('CSV Class Import Success')