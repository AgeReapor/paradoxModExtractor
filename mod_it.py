from zipfile import ZipFile
import os
import shutil

out_path = "Processed\\"

# get list of zip files
dir_files = os.listdir()
zip_names = []
for file in dir_files:
    if file.endswith(".zip"):
        zip_names.append(file)

# iterate through each zip fie
for zip_name in zip_names:    

    # extract zip
    with ZipFile(zip_name,'r') as newzip:        
        newzip.extractall(out_path)    
    
    # read descriptor.mod
    mod_name = ""
    dir_name = zip_name.removesuffix(".zip")
    descriptor_path = os.path.join(out_path,dir_name,"descriptor.mod")
    with open(descriptor_path,'r') as fp:
        for line in fp:
            if line.startswith("name="):
                mod_name = line.strip().removeprefix("name=\"").removesuffix('"')

    lines = []
    
    # add path to descriptor.mod, or replace if it exists            
    with open(descriptor_path,'r') as fp:
        lines = fp.readlines()
    for line in lines:
        if line.startswith("path="):
            lines.remove(line)
    with open(descriptor_path,'w') as fp:
        for line in lines:
            fp.write(line)

    # add path in descriptor.mod             
    with open(descriptor_path,'a') as fp:
        fp.write('\npath="mod/'+mod_name+'"')

    # rename descriptor.mod
    descriptor_new_name = os.path.join(out_path, dir_name, mod_name + '.mod')
    os.rename(descriptor_path,descriptor_new_name)
    
    # move descriptor.mod out of folder
    shutil.move(descriptor_new_name,out_path)
    
    # rename folder
    dir_old_name = os.path.join(out_path,dir_name)+"\\"
    dir_new_name = os.path.join(out_path,mod_name)+"\\"
    shutil.move(dir_old_name,dir_new_name)