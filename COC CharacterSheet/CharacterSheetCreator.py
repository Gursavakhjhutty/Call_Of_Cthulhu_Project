import json
import os
import random
from dataclasses import dataclass, field
import tkinter as tk
from tkinter import ttk, messagebox
import tkinter.font as tkfont
from PIL import Image, ImageTk

# Ensure the characters folder exists
CHARACTER_FOLDER = "characters"
os.makedirs(CHARACTER_FOLDER, exist_ok=True)

@dataclass
class Character:
    # Core attributes
    name: str
    residence: str
    occupation: str
    birthplace: str
    age: int
    pronoun: str

    # Attributes
    STR: int
    CON: int
    DEX: int
    INT: int
    SIZ: int
    POW: int
    APP: int
    EDU: int
    hit_points: int
    magic_points: int
    luck: int
    sanity: int

    # Skills
    Accounting: int
    Animal_Handling: int
    Anthropology: int
    Appraise: int
    Archaeology: int
    Arts: int
    Charm: int
    Climb: int
    Credit_Rating: int
    Cthulhu_Mythos: int
    Disguise: int
    Dodge: int
    Drive: int
    Repair: int
    Fast_Talk: int
    Fighting_Brawl: int
    Firearms_Handgun: int
    Firearms_Rifle_Shotgun: int
    First_Aid: int
    Gambling: int
    History: int
    Intimidate: int
    Jump: int
    Language_alternative: int
    Law: int
    Library_Use: int
    Listen: int
    Locksmith: int
    Medicine: int
    Natural_World: int
    Navigate: int
    Occult: int
    Operate_H_Machine: int
    Persuade: int
    Pilot: int
    Psychology: int
    Ride: int
    Rope_Use: int
    Sciences: int
    Sleight_of_Hand: int
    Spot_Hidden: int
    Stealth: int
    Survival: int
    Swim: int
    Throw: int
    Track: int
    Trap: int

    # Conditions
    max_sanity: int
    temporary_insanity: bool = False
    indefinite_insanity: bool = False
    major_wound: bool = False
    unconscious: bool = False
    dying: bool = False


    def save_to_file(self):
        filename = os.path.join(CHARACTER_FOLDER, f"{self.name.lower().replace(' ', '_')}.json")
        with open(filename, "w") as f:
            json.dump(self.__dict__, f, indent=4)


def create_character_gui():
    def save_character():
        character = Character(
            name=name_var.get(),
            residence=residence_var.get(),
            occupation=occupation_var.get(),
            birthplace=birthplace_var.get(),
            age=int(age_var.get()),
            pronoun=pronoun_var.get(),

            #Core Attributes
            STR=int(str_var.get()),
            CON=int(con_var.get()),
            DEX=int(dex_var.get()),
            INT=int(int_var.get()),
            SIZ=int(siz_var.get()),
            POW=int(pow_var.get()),
            APP=int(app_var.get()),
            EDU=int(edu_var.get()),
            hit_points=int(hp_var.get()),
            magic_points=int(mp_var.get()),
            luck=int(luck_var.get()),
            sanity=int(sanity_var.get()),
            max_sanity=int(max_sanity_var.get()),

            #Conditions
            temporary_insanity=temp_insanity_var.get(),
            indefinite_insanity=indef_insanity_var.get(),
            major_wound=major_wound_var.get(),
            unconscious=unconscious_var.get(),
            dying=dying_var.get(),

            #Skills
            Accounting=int(accounting_var.get()),
            Animal_Handling=int(animal_handling_var.get()),
            Anthropology=int(anthropology_var.get()),
            Appraise=int(appraise_var.get()),
            Archaeology=int(archaeology_var.get()),
            Arts=int(arts_var.get()),
            Charm=int(charm_var.get()),
            Climb=int(climb_var.get()),
            Credit_Rating=int(credit_rating_var.get()),
            Cthulhu_Mythos=int(cthulhu_mythos_var.get()),
            Disguise=int(disguise_var.get()),
            Dodge=int(dodge_var.get()),
            Drive=int(drive_var.get()),
            Repair=int(repair_var.get()),
            Fast_Talk=int(fast_talk_var.get()),
            Fighting_Brawl=int(fighting_brawl_var.get()),
            Firearms_Handgun=int(firearms_handgun_var.get()),
            Firearms_Rifle_Shotgun=int(firearms_rifle_shotgun_var.get()),
            First_Aid=int(first_aid_var.get()),
            Gambling=int(gambling_var.get()),
            History=int(history_var.get()),
            Intimidate=int(intimidate_var.get()),
            Jump=int(jump_var.get()),
            Language_alternative=int(language_alt_var.get()),
            Law=int(law_var.get()),
            Library_Use=int(library_use_var.get()),
            Listen=int(listen_var.get()),
            Locksmith=int(locksmith_var.get()),
            Medicine=int(medicine_var.get()),
            Natural_World=int(natural_world_var.get()),
            Navigate=int(navigate_var.get()),
            Occult=int(occult_var.get()),
            Operate_H_Machine=int(operate_heavy_machine_var.get()),
            Persuade=int(persuade_var.get()),
            Pilot=int(pilot_var.get()),
            Psychology=int(psychology_var.get()),
            Ride=int(ride_var.get()),
            Rope_Use=int(rope_use_var.get()),
            Sciences=int(science_var.get()),
            Sleight_of_Hand=int(sleight_of_hand_var.get()),
            Spot_Hidden=int(spot_hidden_var.get()),
            Stealth=int(stealth_var.get()),
            Survival=int(survival_var.get()),
            Swim=int(swim_var.get()),
            Throw=int(throw_var.get()),
            Track=int(track_var.get()),
            Trap=int(trap_var.get())
            

        )
        character.save_to_file()
        messagebox.showinfo("Success", f"Character '{character.name}' saved successfully in 'Characters' folder!")

    root = tk.Tk()
    Header_font = tkfont.Font(family='Arial', size=16, weight="bold")
    Subheader_font = tkfont.Font(family='Arial', size=14)
    root.title("Call of Cthulhu Character Creator")
    root.geometry("1400x788")
    bg_image = Image.open(r"C:\Users\gursa\projects\COC CharacterSheet\1_NtDgt5kj3SOeCbHhh9NijA.jpg")
    #bg_image = bg_image.resize(1400,788)
    bg_photo = ImageTk.PhotoImage(bg_image)
    canvas = tk.Canvas(root, width=3500, height=788)
    canvas.grid(row=0, column=0, rowspan=55, columnspan=25, sticky="nsew")
    canvas.create_image(0,0, image=bg_photo, anchor="nw")
    
    tk.Label(root, text="Name:", font=Header_font, ).grid(row=0, column=0)
    name_var = tk.Entry(root)
    name_var.grid(row=0, column=1)
    
    tk.Label(root, text="Residence:", font=Header_font).grid(row=0, column=2)
    residence_var = tk.Entry(root)
    residence_var.grid(row=0, column=3)
    
    tk.Label(root, text="Occupation:", font=Header_font).grid(row=0, column=4)
    occupation_var = tk.Entry(root)
    occupation_var.grid(row=0, column=5)
    
    tk.Label(root, text="Birthplace:", font=Header_font).grid(row=1, column=0)
    birthplace_var = tk.Entry(root)
    birthplace_var.grid(row=1, column=1)
    
    tk.Label(root, text="Age:", font=Header_font).grid(row=1, column=2)
    age_var = tk.Entry(root)
    age_var.grid(row=1, column=3)
    
    tk.Label(root, text="Pronoun:", font=Header_font).grid(row=1, column=4)
    pronoun_var = tk.Entry(root)
    pronoun_var.grid(row=1, column=5)
    
    attributes = ["STR", "CON", "DEX", "INT", "SIZ", "POW", "APP", "EDU", "HP", "MP", "Luck", "Sanity", "Max Sanity"]
    attribute_vars = {}
    row_offset = 3
    for i, attr in enumerate(attributes):
        if i % 4 == 0 and i != 0:
            row_offset += 1
        current_row = row_offset
        current_column = 0 + (i % 4) * 2

        tk.Label(root, text=f"{attr}:").grid(row=current_row, column=current_column)
        var = tk.Entry(root)
        var.grid(row=current_row, column=current_column + 1)
        attribute_vars[attr.lower().replace(' ', '_') + "_var"] = var
    
    str_var, con_var, dex_var, int_var, siz_var, pow_var, app_var, edu_var, hp_var, mp_var, luck_var, sanity_var, max_sanity_var = attribute_vars.values()
    
    tk.Label(root, text="Temporary Insanity:").grid(row=19, column=1)
    temp_insanity_var = tk.BooleanVar()
    tk.Checkbutton(root, variable=temp_insanity_var).grid(row=20, column=1)
    
    tk.Label(root, text="Indefinite Insanity:").grid(row=19, column=2)
    indef_insanity_var = tk.BooleanVar()
    tk.Checkbutton(root, variable=indef_insanity_var).grid(row=20, column=2)
    
    tk.Label(root, text="Major Wound:").grid(row=19, column=3)
    major_wound_var = tk.BooleanVar()
    tk.Checkbutton(root, variable=major_wound_var).grid(row=20, column=3)
    
    tk.Label(root, text="Unconscious:").grid(row=19, column=4)
    unconscious_var = tk.BooleanVar()
    tk.Checkbutton(root, variable=unconscious_var).grid(row=20, column=4)
    
    tk.Label(root, text="Dying:").grid(row=19, column=5)
    dying_var = tk.BooleanVar()
    tk.Checkbutton(root, variable=dying_var).grid(row=20, column=5)

    skills = [
    "Accounting", "Animal_Handling", "Anthropology", "Appraise", "Archaeology", 
    "Arts", "Charm", "Climb", "Credit_Rating", "Cthulhu_Mythos", "Disguise", 
    "Dodge", "Drive", "Repair", "Fast_Talk", "Fighting Brawl", "Firearms_Handgun", 
    "Firearms_Rifle_Shotgun", "First Aid", "Gambling", "History", 
    "Intimidate", "Jump", "Language_Alt", "Law", "Library Use", "Listen", 
    "Locksmith", "Medicine", "Natural World", "Navigate", "Occult", 
    "Operate_Heavy_Machine", "Persuade", "Pilot", "Psychology", "Ride", "Rope_Use", 
    "Science", "Sleight_of_Hand", "Spot_Hidden", "Stealth", "Survival", 
    "Swim", "Throw", "Track", "Trap"]
    skill_vars = {}
    column_offset = 0  # Keeps track of column shifts

    for i, skill in enumerate(skills):
        if i % 13 == 0 and i != 0:  # Shift every 7th skill
            column_offset += 2

        current_row = 24 + (i % 13)  # Row cycles within each column shift
        current_column = column_offset

        # Place label and entry field
        tk.Label(root, text=f"{skill.replace('_', ' ')}:").grid(row=current_row, column=current_column)
        var = tk.Entry(root)
        var.grid(row=current_row, column=current_column + 1)
        skill_vars[skill.lower()] = var

    
    accounting_var, animal_handling_var, anthropology_var, appraise_var, archaeology_var, arts_var, charm_var, climb_var, credit_rating_var, cthulhu_mythos_var, disguise_var, dodge_var, drive_var, repair_var, fast_talk_var, fighting_brawl_var, firearms_handgun_var, firearms_rifle_shotgun_var, first_aid_var, gambling_var, history_var, intimidate_var, jump_var, language_alt_var, law_var, library_use_var, listen_var, locksmith_var, medicine_var, natural_world_var, navigate_var, occult_var, operate_heavy_machine_var, persuade_var, pilot_var, psychology_var, ride_var, rope_use_var, science_var, sleight_of_hand_var, spot_hidden_var, stealth_var, survival_var, swim_var, throw_var, track_var, trap_var = skill_vars.values()

    save_button = tk.Button(root, text="Save Character", command=save_character, font=Header_font)
    save_button.grid(row=54, columnspan=8)
    
    root.mainloop()

if __name__ == "__main__":
    create_character_gui()
