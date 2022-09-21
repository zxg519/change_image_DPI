# encoding:utf-8
#------------------------------------------------------------------
#  modify DPI of given picture file
#    by Xiaoguo Zhang, Southeast University
#    2022-09-21
# We use Pillow, instead of PIL lib which now doesn't support python under version 3.5, to implement it
# command:
#        $python set_DPI.py Your_DPI_setting file1 file2 fil3 ... fileN  
# which means it can repeatly process all files you put in the command lines. For instance
#
#         $python set_DPI.py 300 1.jpg 2.jpg 3.jpg 4.jpg 
# 
# it will set images in 1.jpg, 2.jpg, 3.jpg, 4.jpg to 300DPI-formated, and the results are put in
#     1_new.jpg, 2_new.jpg, 3_new.jpg, 4_new.jpg
#--------------------------------------------------------------------
from PIL import Image
import sys

#========================================================
# get pure file name from a full name with appendex
#  aaa.txt -> aaa, txt
#========================================================
def get_pure_file_and_appendix(file):
    _pos = file.rfind('.')
    return file[:_pos],file[_pos+1:]

#========================================================
# change DPI of certain file
# a.jpg --> a_new.jpg, with DPI modified
# 
#========================================================
def change_DPI(file_name, dpi_value=(300,300)):
    im = Image.open(file_name)
    if im is None:
        print("\7\7\7 Error, fail to open:" +file_name)
        return
    new_file,ext = get_pure_file_and_appendix(file_name)
    new_file +='_new.'
    new_file +=ext
    im.save(new_file,dpi=dpi_value)
    
def help(argv):
    print("usage: "+argv[0]+" DPI_value file1 file2 file3 ... file_N")
    
def main(argv):
    if len(argv) <=2:
        help(argv)
        return
    # normal process ...
    print("you are running command:");
    for arg in sys.argv:
        print("%s " % arg, end="")
    dpi_v = int(argv[1])
    for arg in argv[2:]:
        print("transfering "+arg+" ...")
        change_DPI(arg, dpi_value=(dpi_v,dpi_v))     
    
if __name__=="__main__":
    main(sys.argv)    
