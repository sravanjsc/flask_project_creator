# flask_project_creator
The script will generate directories and files for a fresh Flask framework project.

<b>Project Structure</b>

sample_project<br>
sample_project/app.py<br>
sample_project/sample_project/__init__.py<br>
sample_project/sample_project/routes.py<br>
sample_project/sample_project/models.py<br>
sample_project/sample_project/forms.py<br>
sample_project/sample_project/templates<br>
sample_project/sample_project/templates/index.html<br>
sample_project/sample_project/static<br>
sample_project/sample_project/static/style.css<br>
                              
<b>How to run the file</b>
1. Paste the script in the location where you want to create the project
2. open terminal / commandline and type : python3 create.py *project_name


<b>How to run the script anywhere in the system (For Linux systems) </b>

<b>Required</b>

	a. python script
	b. path where the script is located

<b>Steps</b>

a. check the global python environment

    -> Open terminal type : which python3
    -> This will give the path where python3 is installed. Normally it will be in /usr/bin/python3 if you are using Linux system

b. add the python3 path as shebang in the script

    -> At the top of the script type : #!/usr/bin/python3

c. Get the path where python script is located.

    -> Open terminal in the directory where the script is located and type : pwd  . This will give the current path.
   	-> Or open the directory where script is located and press Ctrl+L to get the path from the address bar at the top

d. Add the path in $PATH variable.

    -> Open the terminal in the home directory
    -> Type : sudo (text_editor_name) .bashrc
    -> Add the line export PATH=$PATH:/home/... (script path)  at the bottom of the file. This will get added to the path variable. 
    -> Then type : source ~/.bashrc

e. Close the terminal and open again. Now we can run the python file directly from anywhere in the terminal by typing the file name.
   This does not need a python3 prefix to run the file. Example : If the file name is file.py, we can just type file.py rather than typing
   python3 file.py.
