from md_convert import convert
import os
from cfg import d_02, d02f02


class Filenames:
    
    def __init__(self, filename, textmd, gptext) -> None:
        self.filename = filename #имя файла как путь
        self.textmd = textmd #
        self.gptext = gptext #конвертированый путь
    

    
    def create_2d_array(self, directory):
        
        #3 = размер подмассива [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        #нулевой элемент = название лекции
        #первый элемент = отправка мд файла
        #второй элемент = отправка краткой версии конспекта
        filenames = os.listdir(f"../{directory}")
        return[[elem, '', ''] for elem in filenames ]




def creating_list(directory):
    filenames = os.listdir(f"../{directory}")
    
    farray = []
    for i in filenames:
        farray.append(convert(directory, f"{i}"))
    
    return {filenames[i]: farray[i] for i in range(len(filenames))}


    



lec_2 = creating_list(d_02)
