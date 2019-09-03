Write a code that if we are in business hours 9 AM - 5 PM
writes the following lines at the end of the file `file.txt`, otherwise 
deletes the lines.
The other lines at the beginings of the "file.txt" should not be changed  
*this can be used for blocking some URLs at some spesific time of a day*

---

The tricking part in this small project is that the script should check id the lines
have been already added to the `file.txt`, it should not add more of that lines at the end.

---

#### the `file.txt` can be *`hosts`* file located in `/etc/hosts` in Mac/Linux
#### or `C:\Windows\System32\drivers\etc` in windows to block specific blocked URLs