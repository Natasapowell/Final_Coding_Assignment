#creating a README.md file
touch README.md

#upload it to github using git init, git status, git add, git commit (also adding a message), git push. Uploading to designated Final_Coding_Assignment folder.
git init
git status
git add README.md
git commit -m "Added README.md"

git remote add origin https://github.com/Natasapowell/Final_Coding_Assignment.git
git branch -M main
git push -u origin main


#checking current working directory
pwd

#creating new folder 
mkdir pythoncode

#move to new folder using cd command
cd pythoncode
pwd

#move main.py to new folder called pythoncode
mv main.py pythoncode

#rename main.py 01_folder_structure.py
mv main.py 1_folder_structure.py 

#create new file using touch command
touch 02_for_loop.py

touch main.py
mv main.py 02_for_loop.py

touch main.py
mv main.py 03_list_dictionary.py 


#github
git init
git status
