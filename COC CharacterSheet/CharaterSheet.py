import json
import os
import random
from dataclasses import dataclass, field
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

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

    @classmethod
    def load_from_file(cls, filename):
        with open(os.path.join(CHARACTER_FOLDER, filename), "r") as f:
            data = json.load(f)
        return cls(**data)


def load_character_list():
    return [f for f in os.listdir(CHARACTER_FOLDER) if f.endswith(".json")]

def create_gui():
    def load_character():
        selected_file = character_var.get()
        if not selected_file:
            messagebox.showerror("Error", "Please select a character to load.")
            return

        global character
        character = Character.load_from_file(selected_file)

        # Update UI labels with the loaded character data
        name_label.config(text=character.name)
        occupation_label.config(text=character.occupation)
        residence_label.config(text=character.residence)
        birthplace_label.config(text=character.birthplace)
        age_label.config(text=character.age)
        pronoun_label.config(text=character.pronoun)
        str_label.config(text=f"STR: {character.STR}")
        con_label.config(text=f"CON: {character.CON}")
        dex_label.config(text=f"DEX: {character.DEX}")
        int_label.config(text=f"INT: {character.INT}")
        siz_label.config(text=f"SIZ: {character.SIZ}")
        pow_label.config(text=f"POW: {character.POW}")
        app_label.config(text=f"APP: {character.APP}")
        edu_label.config(text=f"EDU: {character.EDU}")
        hp_label.config(text=f"HP: {character.hit_points}")
        mp_label.config(text=f"MP: {character.magic_points}")
        luck_label.config(text=f"Luck: {character.luck}")
        sanity_label.config(text=f"Sanity: {character.sanity}")
        maxsanity_label.config(text=f"Max Sanity: {character.max_sanity}")
        tempinsanity_label.config(text=f"Temp Insanity: {character.temporary_insanity}")
        indefiniteinsanity_label.config(text=f"Indefinite Insanity: {character.indefinite_insanity}")
        majorwound_label.config(text=f"Major Wound: {character.major_wound}")
        unconscious_label.config(text=f"Unconscious: {character.unconscious}")
        dying_label.config(text=f"Dying: {character.dying}")
        accounting_label.config(text=f"Accounting: {character.Accounting}")
        animal_handeling_label.config(text=f"Animal Handeling: {character.Animal_Handling}")
        anthropology_label.config(text=f"Anthropology: {character.Anthropology}")
        appraise_label.config(text=f"Appraise: {character.Appraise}")
        archaeology_label.config(text=f"Archaeology: {character.Archaeology}")
        arts_label.config(text=f"Arts: {character.Arts}")
        charm_label.config(text=f"Charm: {character.Charm}")
        credit_rating_label.config(text=f"Credit Rating: {character.Credit_Rating}")
        cthulhu_mythos_label.config(text=f"Cthulhu Mythos: {character.Cthulhu_Mythos}")
        disguise_label.config(text=f"Disguise: {character.Disguise}")
        dodge_label.config(text=f"Dodge: {character.Dodge}")
        drive_label.config(text=f"Drive: {character.Drive}")
        repair_label.config(text=f"Repair: {character.Repair}")
        fast_talk_label.config(text=f"Fast Talk: {character.Fast_Talk}")
        fighting_brawl_label.config(text=f"Fighting (Brawl): {character.Fighting_Brawl}")
        firearms_handgun_label.config(text=f"Firearms (Handgun): {character.Firearms_Handgun}")
        firearms_rifle_shotgun_label.config(text=f"Firearms (Rifle): {character.Firearms_Rifle_Shotgun}")
        first_aid_label.config(text=f"First Aid: {character.First_Aid}")
        gambling_label.config(text=f"Gambling: {character.Gambling}")
        history_label.config(text=f"History: {character.History}")
        intimidate_label.config(text=f"Intimidate: {character.Intimidate}")
        jump_label.config(text=f"Jump: {character.Jump}")
        language_alternative_label.config(text=f"Language (Alternative): {character.Language_alternative}")
        law_label.config(text=f"Law: {character.Law}")
        library_use_label.config(text=f"Library Use: {character.Library_Use}")
        listen_label.config(text=f"Listen: {character.Listen}")
        locksmith_label.config(text=f"Locksmith: {character.Locksmith}")
        medicine_label.config(text=f"Medicine: {character.Medicine}")
        natural_world_label.config(text=f"Natural World: {character.Natural_World}")
        navigate_label.config(text=f"Navigate: {character.Navigate}")
        occult_label.config(text=f"Occult: {character.Occult}")
        operate_h_machine_label.config(text=f"Operate Heavy Machine: {character.Operate_H_Machine}")
        persuade_label.config(text=f"Persuade: {character.Persuade}")
        pilot_label.config(text=f"Pilot: {character.Pilot}")
        psychology_label.config(text=f"Psychology: {character.Psychology}")
        ride_label.config(text=f"Ride: {character.Ride}")
        rope_use_label.config(text=f"Rope Use: {character.Rope_Use}")
        sciences_label.config(text=f"Sciences: {character.Sciences}")
        sleight_of_hand_label.config(text=f"Sleight of Hand: {character.Sleight_of_Hand}")
        spot_hidden_label.config(text=f"Spot Hidden: {character.Spot_Hidden}")
        stealth_label.config(text=f"Stealth: {character.Stealth}")
        survival_label.config(text=f"Survival: {character.Survival}")
        swim_label.config(text=f"Swim: {character.Swim}")
        throw_label.config(text=f"Throw: {character.Throw}")
        track_label.config(text=f"Track: {character.Track}")
        trap_label.config(text=f"Trap: {character.Trap}")

        messagebox.showinfo("Success", f"Character '{character.name}' loaded successfully!")


    root = tk.Tk()
    root.title("Call of Cthulhu Character Sheet")
    root.geometry("1400x788")
    bg_image = Image.open(r"C:\Users\gursa\projects\COC CharacterSheet\1_NtDgt5kj3SOeCbHhh9NijA.jpg")
    #bg_image = bg_image.resize(1400,788)
    bg_photo = ImageTk.PhotoImage(bg_image)
    canvas = tk.Canvas(root, width=3500, height=788)
    canvas.grid(row=0, column=0, rowspan=55, columnspan=25, sticky="nsew")
    canvas.create_image(0,0, image=bg_photo, anchor="nw")

    tk.Label(root, text="Select Character:").grid(row=0, column=0, sticky="w")
    character_var = tk.StringVar(value="")
    character_menu = ttk.Combobox(root, textvariable=character_var, values=load_character_list())
    character_menu.grid(row=0, column=1, sticky="w")
    load_button = tk.Button(root, text="Load Character", command=load_character)
    load_button.grid(row=0, column=2, sticky="w")

    # Character details
    tk.Label(root, text="Character Name:").grid(row=1, column=0, sticky="w")
    name_label = tk.Label(root, text="")
    name_label.grid(row=1, column=1, sticky="w")

    tk.Label(root, text="Occupation:").grid(row=1, column=2, sticky="w")
    occupation_label = tk.Label(root, text="")
    occupation_label.grid(row=1, column=3, sticky="w")

    tk.Label(root, text="Residence:").grid(row=1, column=4, sticky="w")
    residence_label = tk.Label(root, text="")
    residence_label.grid(row=1, column=5, sticky="w")

    tk.Label(root, text="Birthplace:").grid(row=3, column=0, sticky="w")
    birthplace_label = tk.Label(root, text="")
    birthplace_label.grid(row=3, column=1, sticky="w")

    tk.Label(root, text="Age:").grid(row=3, column=2, sticky="w")
    age_label = tk.Label(root, text="")
    age_label.grid(row=3, column=3, sticky="w")

    tk.Label(root, text="Pronoun:").grid(row=3, column=4, sticky="w")
    pronoun_label = tk.Label(root, text="")
    pronoun_label.grid(row=3, column=5, sticky="w")

    # Attributes
    tk.Label(root, text="Attributes:").grid(row=7, column=0, sticky="w")
    str_label = tk.Label(root, text="STR: ")
    str_label.grid(row=8, column=0, sticky="w")
    
    con_label = tk.Label(root, text="CON: ")
    con_label.grid(row=8, column=1, sticky="w")
    
    dex_label = tk.Label(root, text="DEX: ")
    dex_label.grid(row=8, column=2, sticky="w")
    
    int_label = tk.Label(root, text="INT: ")
    int_label.grid(row=8, column=3, sticky="w")
    
    siz_label = tk.Label(root, text="SIZ: ")
    siz_label.grid(row=8, column=4, sticky="w")
    
    pow_label = tk.Label(root, text="POW: ")
    pow_label.grid(row=8, column=5, sticky="w")
    
    app_label = tk.Label(root, text="APP: ")
    app_label.grid(row=8, column=6, sticky="w")
    
    edu_label = tk.Label(root, text="EDU: ")
    edu_label.grid(row=9, column=0, sticky="w")

    hp_label = tk.Label(root, text="Hit Points: ")
    hp_label.grid(row=9, column=1, sticky="w")

    mp_label = tk.Label(root, text="Magic Points: ")
    mp_label.grid(row=9, column=2, sticky="w")

    luck_label = tk.Label(root, text="Luck Points: ")
    luck_label.grid(row=9, column=3, sticky="w")
    
    sanity_label = tk.Label(root, text="Sanity: ")
    sanity_label.grid(row=9, column=4, sticky="w")

    maxsanity_label = tk.Label(root, text="Max Sanity: ")
    maxsanity_label.grid(row=9, column=5, sticky="w")

    tempinsanity_label = tk.Label(root, text="Temp Insanity: ")
    tempinsanity_label.grid(row=10, column=0, sticky="w")

    indefiniteinsanity_label = tk.Label(root, text="Indefinite Insanity: ")
    indefiniteinsanity_label.grid(row=10, column=1, sticky="w")

    majorwound_label = tk.Label(root, text="Major Wound: ")
    majorwound_label.grid(row=10, column=2, sticky="w")

    unconscious_label = tk.Label(root, text="Unconscious: ")
    unconscious_label.grid(row=10, column=3, sticky="w")

    dying_label = tk.Label(root, text="Dying: ")
    dying_label.grid(row=10, column=4, sticky="w")

    #Skills
    tk.Label(root, text="Skills :").grid(row=12, column=0, sticky="w")
    accounting_label = tk.Label(root, text="Accounting: ")
    accounting_label.grid(row=13, column=0, sticky="w")

    animal_handeling_label = tk.Label(root, text="Animal Handling: ")
    animal_handeling_label.grid(row=14, column=0, sticky="w")

    anthropology_label = tk.Label(root, text="Anthropolgy: ")
    anthropology_label.grid(row=15, column=0, sticky="w")

    appraise_label = tk.Label(root, text="Appraise: ")
    appraise_label.grid(row=16, column=0, sticky="w")

    archaeology_label = tk.Label(root, text="Archaeology: ")
    archaeology_label.grid(row=17, column=0, sticky="w")

    arts_label = tk.Label(root, text="Arts: ")
    arts_label.grid(row=18, column=0, sticky="w")

    charm_label = tk.Label(root, text="Charm: ")
    charm_label.grid(row=19, column=0, sticky="w")

    climb_label = tk.Label(root, text="Climb: ")
    climb_label.grid(row=13, column=2, sticky="w")

    credit_rating_label = tk.Label(root, text="Credit Rating: ")
    credit_rating_label.grid(row=14, column=2, sticky="w")

    cthulhu_mythos_label = tk.Label(root, text="Cthulhu Mythos: ")
    cthulhu_mythos_label.grid(row=15, column=2, sticky="w")

    disguise_label = tk.Label(root, text="Disguise: ")
    disguise_label.grid(row=16, column=2, sticky="w")

    dodge_label = tk.Label(root, text="Dodge: ")
    dodge_label.grid(row=17, column=2, sticky="w")

    drive_label = tk.Label(root, text="Drive: ")
    drive_label.grid(row=18, column=2, sticky="w")

    repair_label = tk.Label(root, text="Repair: ")
    repair_label.grid(row=19, column=2, sticky="w")

    fast_talk_label = tk.Label(root, text="Fast Talk: ")
    fast_talk_label.grid(row=13, column=4, sticky="w")

    fighting_brawl_label = tk.Label(root, text="Fighting (Brawl): ")
    fighting_brawl_label.grid(row=14, column=4, sticky="w")

    firearms_handgun_label = tk.Label(root, text="Firearms (Handgun): ")
    firearms_handgun_label.grid(row=15, column=4, sticky="w")

    firearms_rifle_shotgun_label = tk.Label(root, text="Firearms (Rifle/Shotgun): ")
    firearms_rifle_shotgun_label.grid(row=16, column=4, sticky="w")

    first_aid_label = tk.Label(root, text="First Aid: ")
    first_aid_label.grid(row=17, column=4, sticky="w")

    gambling_label = tk.Label(root, text="Gambling: ")
    gambling_label.grid(row=18, column=4, sticky="w")

    history_label = tk.Label(root, text="History: ")
    history_label.grid(row=19, column=4, sticky="w")

    intimidate_label = tk.Label(root, text="Intimidate: ")
    intimidate_label.grid(row=13, column=6, sticky="w")

    jump_label = tk.Label(root, text="Jump: ")
    jump_label.grid(row=14, column=6, sticky="w")

    language_alternative_label = tk.Label(root, text="Language (Alternative): ")
    language_alternative_label.grid(row=15, column=6, sticky="w")

    law_label = tk.Label(root, text="Law: ")
    law_label.grid(row=16, column=6, sticky="w")

    library_use_label = tk.Label(root, text="Library Use: ")
    library_use_label.grid(row=17, column=6, sticky="w")

    listen_label = tk.Label(root, text="Listen: ")
    listen_label.grid(row=18, column=6, sticky="w")

    locksmith_label = tk.Label(root, text="Locksmith: ")
    locksmith_label.grid(row=19, column=6, sticky="w")

    medicine_label = tk.Label(root, text="Medicine: ")
    medicine_label.grid(row=13, column=8, sticky="w")

    natural_world_label = tk.Label(root, text="Natural World: ")
    natural_world_label.grid(row=14, column=8, sticky="w")

    navigate_label = tk.Label(root, text="Navigate: ")
    navigate_label.grid(row=15, column=8, sticky="w")

    occult_label = tk.Label(root, text="Occult: ")
    occult_label.grid(row=16, column=8, sticky="w")

    operate_h_machine_label = tk.Label(root, text="Operate Heavy Machine: ")
    operate_h_machine_label.grid(row=17, column=8, sticky="w")

    persuade_label = tk.Label(root, text="Persuade: ")
    persuade_label.grid(row=18, column=8, sticky="w")

    pilot_label = tk.Label(root, text="Pilot: ")
    pilot_label.grid(row=19, column=8, sticky="w")

    psychology_label = tk.Label(root, text="Psychology: ")
    psychology_label.grid(row=13, column=10, sticky="w")

    ride_label = tk.Label(root, text="Ride: ")
    ride_label.grid(row=14, column=10, sticky="w")

    rope_use_label = tk.Label(root, text="Rope Use: ")
    rope_use_label.grid(row=15, column=10, sticky="w")

    sciences_label = tk.Label(root, text="Sciences: ")
    sciences_label.grid(row=16, column=10, sticky="w")

    sleight_of_hand_label = tk.Label(root, text="Sleight of Hand: ")
    sleight_of_hand_label.grid(row=17, column=10, sticky="w")

    spot_hidden_label = tk.Label(root, text="Spot Hidden: ")
    spot_hidden_label.grid(row=18, column=10, sticky="w")

    stealth_label = tk.Label(root, text="Stealth: ")
    stealth_label.grid(row=19, column=10, sticky="w")

    survival_label = tk.Label(root, text="Survival: ")
    survival_label.grid(row=13, column=12, sticky="w")

    swim_label = tk.Label(root, text="Swim: ")
    swim_label.grid(row=14, column=12, sticky="w")

    throw_label = tk.Label(root, text="Throw: ")
    throw_label.grid(row=15, column=12, sticky="w")

    track_label = tk.Label(root, text="Track: ")
    track_label.grid(row=16, column=12, sticky="w")

    trap_label = tk.Label(root, text="Trap: ")
    trap_label.grid(row=17, column=12, sticky="w")


    tk.Label(root, text="Dice Roller").grid(row=22, column=0)
    Attribute_var = tk.StringVar(value="Select Attribute")
    Attribute_menu = ttk.Combobox(
        root, 
        textvariable=Attribute_var, 
        values=[
            "STR", "CON", "DEX", "INT", "SIZ", "POW", "APP", "EDU", "Accounting", "Animal Handling", 
            "Anthropology", "Appraise", "Archaeology", "Arts", "Charm", "Climb", "Credit Rating", 
            "Cthulhu Mythos", "Disguise", "Dodge", "Drive", "Repair", "Fast Talk", "Fighting (Brawl)", 
            "Firearms (Handgun)", "Firearms (Rifle/Shotgun)", "First Aid", "Gambling", "History", 
            "Intimidate", "Jump", "Language (Alternative)", "Law", "Library Use", "Listen", "Locksmith", 
            "Medicine", "Natural World", "Navigate", "Occult", "Operate Heavy Machine", "Persuade", 
            "Pilot", "Psychology", "Ride", "Rope Use", "Sciences", "Sleight of Hand", "Spot Hidden", 
            "Stealth", "Survival", "Swim", "Throw", "Track", "Trap"
        ]
    )
    Attribute_menu.grid(row=22, column=1, sticky="w")

    def dice_roll():
        selected_attribute = Attribute_var.get()
        attribute_values = {
            "STR": character.STR,
            "CON": character.CON,
            "DEX": character.DEX,
            "INT": character.INT,
            "SIZ": character.SIZ,
            "POW": character.POW,
            "APP": character.APP,
            "EDU": character.EDU,
            "Accounting": character.Accounting,
            "Animal Handling": character.Animal_Handling,
            "Anthropology": character.Anthropology,
            "Appraise": character.Appraise,
            "Archaeology": character.Archaeology,
            "Arts": character.Arts,
            "Charm": character.Charm,
            "Climb": character.Climb,
            "Credit Rating": character.Credit_Rating,
            "Cthulhu Mythos": character.Cthulhu_Mythos,
            "Disguise": character.Disguise,
            "Dodge": character.Dodge,
            "Drive": character.Drive,
            "Repair": character.Repair,
            "Fast Talk": character.Fast_Talk,
            "Fighting (Brawl)": character.Fighting_Brawl,
            "Firearms (Handgun)": character.Firearms_Handgun,
            "Firearms (Rifle/Shotgun)": character.Firearms_Rifle_Shotgun,
            "First Aid": character.First_Aid,
            "Gambling": character.Gambling,
            "History": character.History,
            "Intimidate": character.Intimidate,
            "Jump": character.Jump,
            "Language (Alternative)": character.Language_alternative,
            "Law": character.Law,
            "Library Use": character.Library_Use,
            "Listen": character.Listen,
            "Locksmith": character.Locksmith,
            "Medicine": character.Medicine,
            "Natural World": character.Natural_World,
            "Navigate": character.Navigate,
            "Occult": character.Occult,
            "Operate Heavy Machine": character.Operate_H_Machine,
            "Persuade": character.Persuade,
            "Pilot": character.Pilot,
            "Psychology": character.Psychology,
            "Ride": character.Ride,
            "Rope Use": character.Rope_Use,
            "Sciences": character.Sciences,
            "Sleight of Hand": character.Sleight_of_Hand,
            "Spot Hidden": character.Spot_Hidden,
            "Stealth": character.Stealth,
            "Survival": character.Survival,
            "Swim": character.Swim,
            "Throw": character.Throw,
            "Track": character.Track,
            "Trap": character.Trap
        }
        if selected_attribute in attribute_values:
            roll_result =  random.randint(1, 100)
            Success = ""
            if roll_result > 98:
                Success = "Critical Failure"
            elif roll_result > attribute_values[selected_attribute]:
                Success = "Failure"
            elif roll_result < attribute_values[selected_attribute] and roll_result > (attribute_values[selected_attribute] / 2):
                Success = "Normal"
            elif roll_result < (attribute_values[selected_attribute] / 2) and roll_result > (attribute_values[selected_attribute] / 5):
                Success = "Great"
            elif roll_result < (attribute_values[selected_attribute] / 5) and roll_result > 1:
                Success = "Extreme"
            elif roll_result == 1:
                Success = "Critical"

            messagebox.showinfo("Dice Roll", f"You rolled: {roll_result} for {selected_attribute} (Value: {attribute_values[selected_attribute]}) (Success Type: {Success})")

    load_role = tk.Button(root, text="Roll D100", command=dice_roll)
    load_role.grid(row=22, column=2, sticky="w")

    root.mainloop()

if __name__ == "__main__":
    create_gui()