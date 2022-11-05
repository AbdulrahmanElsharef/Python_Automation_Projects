import os
print(f" current dir is **{os.getcwd()}** ")
# current dir is **J:\Abdo_BackEnd\Django_FullStack_Project\Python_Dev\01_Python_Basics\intermediat_python**
os.mkdir('new_folder_by_os')
# creat anew file "new_folder_by_os"
os.chdir('new_folder_byos')
# change dir to new file "new_folder_by_os"
print(f" current dir is **{os.getcwd()}** ")
# current dir is **J:\Abdo_BackEnd\Django_FullStack_Project\Python_Dev\01_Python_Basics\intermediat_python\new_folder_byos**
os.makedirs('new_folder_byos/jobs/2023')
# creat anew files into file "new_folder_by_os"
os.chdir('new_folder_byos/jobs/2023')
# change dir to new files "new_folder_byos/jobs/2023"
print(f" current dir is **{os.getcwd()}** ")
# current dir is **J:\Abdo_BackEnd\Django_FullStack_Project\Python_Dev\01_Python_Basics\intermediat_python\new_folder_byos\jobs\2023**
path = r"J:\Abdo_BackEnd\Django_FullStack_Project\Python_Dev\01_Python_Basics"
lis = os.listdir(path)
print(lis)
# ['.git', '01_Variable&opretors', '02_Conditions', '03_Functions_list_dict', '04_Loop', '05_OOP - BASICS', 'dataset',
# 'intermediat_python', 'test.py']
lis_file = os.walk(path)
# print(list of folders in path)
for dirpath, dirname, filname in lis_file:
    print(f"path : {dirpath}")
    print(f"folder name : {dirname}")
    print(f"file name  : {filname}")
    print(50*"-")
