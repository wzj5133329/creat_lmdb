import os
from os import listdir, getcwd
from os.path import join
if __name__ == '__main__':
    source_folder='/home/asd/Project/NCC_WZJ/YOLO/train/NCC/image'
    dest='/home/asd/Project/NCC_WZJ/YOLO/train/NCC/train.txt' 
    #dest2='/home/asd/Install/yolo-lite_train/train_people/VOCdevkit/VOC2007/ImageSets/Main/val.txt'  
    file_list=os.listdir(source_folder)       
    train_file=open(dest,'a')                 
    #val_file=open(dest2,'a')                  
    for file_obj in file_list:                
        file_path=os.path.join(source_folder,file_obj) 
       
        file_name,file_extend=os.path.splitext(file_obj)
       
        #file_num=int(file_name) 
        
        #if(file_num<8000):                                 
        train_file.write(file_path+'\n')  
        #else :
        #    val_file.write(file_name+'\n')    
    train_file.close()
#val_file.close()

