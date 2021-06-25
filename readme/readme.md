# Das Kapital - The People's ROI Calculator
### Modernize OUR return, Post-modernize OUR aesthetics
### Version 1.0, Release Date - 5/3/21

Das Kapital is an ironically themed ROI (Return On Investment) calculator for landlords built with the ancient looking Tcl/Tk GUI library. Don't let the irony fool you though, while communism might look better than it works, this calculator works better than it looks.  

### Technical Features
Developed in Python using Tkinter, a Python GUI built on the Tcl/Tk library.  

Non-persistant SQLite database is created at runtime to track user data.  

Database currently only supports single record, single use.  But the code is ready for extension to support data persistance and multiple records (e.g. for multi-property analysis / comparison)  

Separation of database from application logic  

Multiple modules with high cohesion and loose coupling allow for easy extension / maintenance  

Docstrings and type-hinting for all public functions  

Comments where necessary to explain program function  


### User Interface
The user interface is a button driven GUI which launces a series of windows where users enter data and perform calculations using buttons.

### Main Window
![Main Window](https://github.com/hirejohnloveland/Das-Kapital-ROI-Kalkulator/blob/main/readme/Main_Screen.JPG "Main window")

### Income Window
![Income Window](https://github.com/hirejohnloveland/Das-Kapital-ROI-Kalkulator/blob/main/readme/Income_Window.JPG "Income window")

### Expense Window
![Expense Window](https://github.com/hirejohnloveland/Das-Kapital-ROI-Kalkulator/blob/main/readme/Expense_Window.JPG "Expense window")

### ROI Window
![ROI Window](https://github.com/hirejohnloveland/Das-Kapital-ROI-Kalkulator/blob/main/readme/ROI_Window.JPG "ROI window")
