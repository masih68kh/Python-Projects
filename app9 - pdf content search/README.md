# Search the content of all pdf files 
This application searches the contents of all pdf files of a desired directory.  

---

## How to run the app:
run the app by `python script_linux.py`   
this command asks the user to enter a **directory** to look in and a string of **word(s)** to look for in the given directory.   
   
      
---

## How the app works
The python script calls a bash script to look for all pdfs in the given directory and its subdirectories recursively and convert them to temporarly `.txt` files using `pdftotext` command.   
   
`pdftotext` is an app that is usually installed by default in many Linux distribution. If not, you can install it by:   
`sudo apt-get update && sudo apt-get install -y xpdf`   
or    
`sudo apt-get install poppler-utils`  
or you can go to their website and download .deb file.
