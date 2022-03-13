# Snake
Snake is a clone of the classic game that we all used to play on our cellphones. You play this game 
on a simulated terminal, with a textual interface.

## Getting Started
---
Make sure you have Python 3.8.0 or newer and Raylib Python CFFI 3.7 installed and running on your machine. You can install Raylib Python CFFI by opening a terminal and running the following command.
```
python3 -m pip install raylib
```
After you've installed the required libraries, open a terminal and browse to the project's root folder. Start the program by running the following command.```

python3 snake 
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the 
project folder. Select the main module inside the hunter folder and click the "run" icon.

## Project Structure
---
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- snake               (source code for game)
  +-- game              (specific game classes)
  +-- __main__.py       (entry point for program)
+-- README.md           (general info)
```

## Required Technologies
---
* Python 3.8.0
* Raylib Python CFFI 3.7

## Authors
---
* TODO: Add your name and email here

Individual answer to question: How did you use method overriding in derived classes in the completed program?
This is best illustrated in the __main__.py file which often may have additional coding in def main() such as assigning constants or variable to the Actor/Artifact etc.  However, by applying Method Overriding which is also called Run time polymorphism, the def main() functions methods are simplified and utilise add.actor and add.action in as many situations as needs.  In particular the need to have two snakes, the additional snake was called simply by this specific code:
    cast.add_actor("snakes1", CycleOne())
    cast.add_actor("snakes2", CycleTwo())
    script.add_action("input", ControlActorsAction1(keyboard_service))
    script.add_action("input", ControlActorsAction2(keyboard_service))
I understand the above examples to be true, because a method is overridden in the derived class from the base class.
PS:  The Method Overriding term had me scratching my head for abit, but once linked to polymorphism I was ok again :)
