#Create the template for datascience project similar to cookiecutter

import os

#These folders needs to be created
dirs=[
    os.path.join("data","raw"),
    os.path.join("data","processed"),
    "notebooks",
    "saved_models",
    "src"
]

#This code will create the folders mentioned. The below folders will be empty in beginning so inorder for to push them in git we will require a file so we will create empty .gitkeep
for dir_ in dirs:
    #exist_ok means if the direc is already available then it will not throw an error
    os.makedirs(dir_,exist_ok=True)
    #The below folders will be empty in beginning so inorder for to push them in git we will require a file so we will create empty .gitkeep
    with open(os.path.join(dir_,".gitkeep"),"w") as f:
        pass

#Create files
files=[
    "dvc.yaml",
    "params.yaml",
    ".gitignore",
    #To ensure that the project has packages we use the below file
    os.path.join("src","__init__.py"),
    "README"
]

#Store the above as filenames
for file_ in files:
    with open(file_,"w") as f:
        pass
