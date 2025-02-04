Call of Cthulhu Character Sheet Programs
========================================

Overview
--------

This project contains two Python programs designed for creating, saving, loading, and interacting with characters for the tabletop role-playing game "Call of Cthulhu." The programs feature a graphical user interface (GUI) built using the `tkinter` library and offer functionality for managing character details, attributes, conditions, and skills. The core features include a character creator and a character sheet viewer.

* * * * *

Program 1: Character Sheet Viewer
---------------------------------

### Description

This program allows users to load existing character files, view character details, and roll dice to determine the success or failure of actions based on the character's attributes or skills. The program reads character data from JSON files saved in the `characters` folder.

### Key Features

-   **Load Character:** Select and load character data from a list of existing JSON files.
-   **View Character Details:** Display core attributes, conditions, and skills in an organized GUI layout.
-   **Dice Rolling Mechanic:** Roll a 1d100 die to determine success based on selected attributes or skills, with varying success types (e.g., normal, great, extreme).

### How to Run

1.  Ensure the `tkinter` and `Pillow` libraries are installed:

    ```
    pip install pillow

    ```

2.  Place character JSON files in the `characters` directory.
3.  Run the program:

    ```
    python character_sheet_viewer.py

    ```

### User Interface Components

-   **Character Selection Menu:** Choose a character to load.
-   **Labels and Fields:** Display character details such as STR, CON, DEX, etc.
-   **Dice Roller:** Roll a d100 to check attribute or skill success.

### File Structure

-   `characters/`: Directory containing character JSON files.
-   `character_sheet_viewer.py`: Main program.

* * * * *

Program 2: Character Creator
----------------------------

### Description

This program provides a GUI interface for creating new Call of Cthulhu characters. Users can input character details, attributes, skills, and conditions, then save the character to a JSON file in the `characters` folder.

### Key Features

-   **Character Creation:** Input character name, age, pronoun, and other details.
-   **Attribute Assignment:** Set values for core attributes (e.g., STR, DEX, CON).
-   **Skill Assignment:** Assign values for various Call of Cthulhu skills.
-   **Condition Flags:** Set character conditions like temporary insanity or major wounds.
-   **Save Character:** Save the character to a JSON file for later use.

### How to Run

1.  Ensure the `tkinter` and `Pillow` libraries are installed:

    ```
    pip install pillow

    ```

2.  Run the program:

    ```
    python character_creator.py

    ```

### User Interface Components

-   **Entry Fields:** Input character details such as name, age, occupation, and pronoun.
-   **Attributes and Skills:** Assign values through entry boxes.
-   **Conditions:** Toggle conditions using checkboxes.
-   **Save Button:** Save the character to a JSON file.

### File Structure

-   `characters/`: Directory where character JSON files are saved.
-   `character_creator.py`: Main program.

* * * * *

JSON Character File Structure
-----------------------------

When a character is saved, the JSON file structure will include the following sections:

```
{
  "name": "John Doe",
  "residence": "London",
  "occupation": "Detective",
  "birthplace": "New York",
  "age": 30,
  "pronoun": "He/Him",
  "STR": 60,
  "CON": 50,
  "DEX": 70,
  "INT": 80,
  "SIZ": 65,
  "POW": 55,
  "APP": 50,
  "EDU": 75,
  "hit_points": 12,
  "magic_points": 11,
  "luck": 50,
  "sanity": 70,
  "max_sanity": 99,
  "temporary_insanity": false,
  "indefinite_insanity": false,
  "major_wound": false,
  "unconscious": false,
  "dying": false,
  "Accounting": 10,
  "Animal_Handling": 5,
  "Anthropology": 1,
  "Appraise": 5,
  "Archaeology": 1,
  "Arts": 5,
  "Charm": 15,
  "Climb": 20,
  "Credit_Rating": 10,
  "Cthulhu_Mythos": 0,
  "Disguise": 5,
  "Dodge": 35,
  "Drive": 20,
  "Repair": 10,
  "Fast_Talk": 5,
  "Fighting_Brawl": 25,
  "Firearms_Handgun": 20,
  "Firearms_Rifle_Shotgun": 25,
  "First_Aid": 30,
  "Gambling": 10,
  "History": 5,
  "Intimidate": 15,
  "Jump": 20,
  "Language_alternative": 1,
  "Law": 5,
  "Library_Use": 20,
  "Listen": 20,
  "Locksmith": 1,
  "Medicine": 1,
  "Natural_World": 10,
  "Navigate": 10,
  "Occult": 5,
  "Operate_H_Machine": 1,
  "Persuade": 10,
  "Pilot": 1,
  "Psychology": 10,
  "Ride": 5,
  "Rope_Use": 5,
  "Sciences": 1,
  "Sleight_of_Hand": 10,
  "Spot_Hidden": 25,
  "Stealth": 20,
  "Survival": 10,
  "Swim": 20,
  "Throw": 20,
  "Track": 10,
  "Trap": 10
}

```

* * * * *

Requirements
------------

-   Python 3.x
-   `tkinter` (comes with Python)
-   `Pillow`

### Installation

1.  Install dependencies:

    ```
    pip install pillow

    ```

2.  Run either program using:

    ```
    python character_sheet_viewer.py

    ```

    or

    ```
    python character_creator.py

    ```

* * * * *

Customization
-------------

-   **Character Attributes:** Modify the `Character` class in both programs to add or remove fields as needed.
-   **UI Adjustments:** Adjust label positions or add additional UI elements using the `tkinter` library.

* * * * *

Future Enhancements
-------------------

-   **Save and Load Custom Backgrounds:** Allow users to select custom images for their character sheets.
-   **Combat System:** Integrate basic combat mechanics and damage tracking.
-   **Skill Improvement Tracking:** Track and update skills dynamically as characters progress.

* * * * *

License
-------

This project is free to use and modify for personal or educational purposes.

* * * * *

Acknowledgments
---------------

-   Based on the mechanics of the "Call of Cthulhu" tabletop role-playing game.
-   Special thanks to the developers and maintainers of `tkinter` and `Pillow` libraries for making GUI development accessible in Python.
