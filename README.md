We are aspiring to be web developers and software Engineers. At ALX SE Programme, one of the requirements thta makes you stand out and become a formidable software Engineer, is to create an AirBnB Clone. Our first ste to developing this web application is to create a Command Line Interpreter(CLI) to help us manage our project's objects. This step is very important because we will be building and including static and dynamic contents: HTML/CSS/JS templates, DB storage, File Storage, API(Application Programming INterface) and Front-End Integration.

What is a CLI (Command Line Interpreter)?
A CLI is a text-based User-interface(UI) that runs commands and programes. It manages computer files and interact with the computer. Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

1. Create a new object (ex: a new User or a new Place)
2. Retrieve an object from a file, a database etc…
3. Do operations on objects (count, compute stats, etc…)
4. Update attributes of an object
5. Destroy an object

Learning Objectives

During and after the cause of this project, we will be able to do the following:

1. Know how to create a Python package
2. Know how to create a command interpreter in Python using the cmd module
3. Know what is Unit testing and how to implement it in a large project
4. Know how to serialize and deserialize a Class
5. Know how to write and read a JSON file
6. Know how to manage datetime
7. Know what is an UUID
8. Know what is *args and how to use it
9. Know what is **kwargs and how to use it
10. Know how to handle named arguments in a function

Requirements

Python Scripts

Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the pycodestyle (version 2.8.*)
All your files must be executable
The length of your files will be tested using wc
All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

Python Unit Tests

Allowed editors: vi, vim, emacs
All your files should end with a new line
All your test files should be inside a folder tests
You have to use the unittest module
All your test files should be python files (extension: .py)
All your test files and folders should start by test_
Your file organization in the tests folder should be the same as your project
e.g., For models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py
e.g., For models/user.py, unit tests must be in: tests/test_models/test_user.py
All your tests should be executed by using this command: python3 -m unittest discover tests
You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
We strongly encourage you to work together on test cases, so that you don’t miss any edge case

How Program is Executed
Your shell should work like this in interactive mode:

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
But also in non-interactive mode: (like the Shell project in C)

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
All tests should also pass in non-interactive mode: $ echo "python3 -m unittest discover tests" | bash

Quiting the Console

To quit the console, you can type in any of the following:

EQF
quit

or do the following key combinations on your keyboarf

CMD+D (Unix) / CRTL+C (Windows)

(hbnb) quit
$

or

(hbnb) EOF
$

or

(hbnb) (CTRL+C)
$

Getting Help

To get help generally

(hbnb) help

Documented commands (type help <topic>):
========================================
EOF all create destroy help quit show update

(hbnb)

To get help for a particular command

(hbnb) help all

The `all` command displays the string representation of all class instances

Usage:
(hbnb) all User


(hbnb) help update

The `update` command update a specified instance of a using the class name and the ID of the instance, and the specifying the attribute to update or adding a new attribute plus the value.

Usage:
(hbnb) update User 1234-5678 email 'test@oop.com'

(hbnb)

Presently, we have nothing in the flat file database, We will create a New User and a BaseModel

(hbnb) all
[]
(hbnb)

Firstly, we have to get help on how to create an instance of a models are available

$ ./console.py
(hbnb) help create

The `create	 command creates an instance of a class saves it to the storage and prints out the ID of the instancecreated.

Models available includes;

	Amenity
	Basemodel
	City
	Place
	Review
	State
	User

Usage:
(hbnb) create User

(hbnb)


Authors

Adugbo Justine @justine1285, and Iyanu Olatomide @Oiyanu are formidable Interns at the ALX Africa Software Engineering programme 2022/2023 schedule.
