import os
import shutil


from_dir="C:\\Users\\kavit\\C101"
to_dir="C:\\Users\\Public\\"

list_of_files=os.listdir(from_dir)

# move all image files from kavit to public

for file_name in list_of_files:
    name,extension=os.path.splitext(file_name)
    
    if extension =='':
        continue
    
    if extension in ['.txt', '.pdf', '.doc', '.docx']:
        
        path1= from_dir +'/'+ file_name
        path2= to_dir +'/'+ "Document_Files"
        path3= to_dir+'/'+"Document_Files"+'/'+file_name
        
        
        if os.path.exists(path2):
            print("Moving "+file_name + "..:")
            
            shutil.move(path1,path2)
            
            
        else:
            os.makedirs(path2)
            print("Moving "+file_name+".....") 
            shutil.move(path1,path2)   

    
