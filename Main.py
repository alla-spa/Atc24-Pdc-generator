pyperclip_installed: bool = False

import random
import sys
try:
    import pyperclip
except ImportError:
    print("The Python package pyperclip is a tip for using this program as it makes the output auto copy into you clipboard, to install type \"pip install pyperclip\" on windows or \"pip3 install pyperclip\" on mac/linux into the terminal")
    pyperclip_installed: bool = False
else:
    pyperclip_installed = True
from datetime import datetime, timezone

Dep: str = ""
Station: str = ""
Freq: str = ""
Runway: str = ""
Selected_Trans: str = ""
Init: str = ""
Squawk: str = ""
timez: str = ""
Format: str = ""

Use_preferences: bool = False
Preferences_Set: bool = False
Format_Set: bool = False

PDep: str = ""
PStation: str = ""
PRwy: str = ""
Pint: str = ""
PFreq: str = ""

Generated_PDC: list = []
PDC_Generated: int = 0

Data_Station = {
    "IRCC": ("124.850", "IRFD", "IMLR", "IGAR", "IBLT", "ITRC"),
    "IRFD_CTR": ("124.850", "IRFD", "IMLR", "IGAR", "IBLT", "ITRC"),
    "IRFD_GND": ("120.400", "IRFD"),
    "IRFD_TWR": ("118.100", "IRFD"),
    "IMLR_TWR": ("133.850", "IMLR"),
    "IGAR_TWR": ("125.600", "IGAR"),
    "IBLT_TWR": ("120.250", "IBLT"),
    "ITRC_TWR": ("119.150", "ITRC"),
    "ICCC": ("126.300", "ILAR", "IPAP", "IIAB", "IHEN", "IBAR"),
    "ILAR_CTR": ("126.300", "ILAR", "IPAP", "IIAB", "IHEN", "IBAR"),
    "ILAR_GND": ("119.400", "ILAR"),
    "ILAR_TWR": ("121.200", "ILAR"),
    "IPAP_TWR": ("119.900", "IPAP"),
    "IIAB_TWR": ("127.250", "IIAB"),
    "IHEN_TWR": ("130.250", "IHEN"),
    "IBAR_TWR": ("118.750", "IBAR"),
    "IZCC": ("125.650", "IZOL", "IJAF", "ISCM"),
    "IZOL_CTR": ("125.650", "IZOL", "IJAF", "ISCM"),
    "IZOL_GND": ("121.900", "IZOL"),
    "IZOL_TWR": ("118.700", "IZOL"),
    "IJAF_TWR": ("119.100", "IJAF"),
    "ISCM_TWR": ("121.300", "ISCM"),
    "IOCC": ("132.300", "ITKO", "IDCS", "IBRD"),
    "ITKO_CTR": ("132.300", "ITKO", "IDCS", "IBRD"),
    "ITKO_GND": ("118.225", "ITKO"),
    "ITKO_TWR": ("118.800", "ITKO"),
    "IDCS_TWR": ("118.250", "IDCS"),
    "IBRD_TWR": ("118.350", "IBRD"),
    "IPCC": ("135.250", "IPPH", "ILKL"),
    "IPPH_CTR": ("135.250", "IPPH", "ILKL"),
    "IPPH_GND": ("121.700", "IPPH"),
    "IPPH_TWR": ("127.400", "IPPH"),
    "ILKL_TWR": ("120.150", "ILKL"),
    "IGCC": ("126.750", "IKFL", "ITEY"),
    "IKFL_CTR": ("126.750", "IKFL", "ITEY"),
    "IKFL_GND": ("121.750", "IKFL"),
    "IKFL_TWR": ("118.300", "IKFL"),
    "ITEY_TWR": ("119.425", "ITEY"),
    "IBCC": ("128.600", "IBTH", "ISKP"),
    "IBTH_CTR": ("128.600", "IBTH", "ISKP"),
    "IBTH_TWR": ("118.700", "IBTH"),
    "ISKP_TWR": ("123.250", "ISKP"),
    "ISCC": ("127.825", "ISAU"),
    "ISAU_CTR": ("127.825", "ISAU"),
    "ISAU_TWR": ("118.200", "ISAU"),
}

Data_Runway = {
    "IRFD": ("25L", "25C", "25R", "07L", "07C", "07R"),
    "IMLR": ("25", "07"),
    "IGAR": ("22", "04"),
    "IBLT": ("19", "01"),
    "ITRC": ("36", "18"),
    "ILAR": ("24", "06"),
    "IPAP": ("35", "17"),
    "IIAB": ("27L", "27R", "09L", "09R"),
    "IHEN": ("35", "17"),
    "IBAR": ("01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36"),
    "IZOL": ("28", "10"),
    "IJAF": ("25", "07"),
    "ISCM": ("31", "13"),
    "ITKO": ("31", "02", "20", "13"),
    "IDCS": ("25", "07"),
    "IBRD": ("26", "08"),
    "IPPH": ("33", "29", "15", "11"),
    "ILKL": ("27", "09"),
    "IKFL": ("34", "25", "16", "07"),
    "ITEY": ("31", "13"),
    "IBTH": ("27", "09"),
    "ISKP": ("23", "05"),
    "ISAU": ("26", "08"),
}

Data_Sids = {
    "IRFD": (("DARRK3.SPACE", ("25L", "25C", "25R")), ("DARRK3.SEEKS", ("25L", "25C", "25R")), ("KENED2.RENDR", ("25L", "25C", "25R")), ("KENED2.JOOPY", ("25L", "25C", "25R")), ("KENED2.DINER", ("25L", "25C", "25R")), ("LOGAN4.RENDR", ("25L", "25C", "25R")), ("LOGAN4.DINER", ("25L", "25C", "25R")), ("OSHNN1.SILVA", ("25L", "25C", "25R")), ("OSHNN1.CYRIL", ("25L", "25C", "25R")), ("OSHNN1.GRASS", ("25L", "25C", "25R")), ("RFD6.RFD", ("25L", "25C", "25R", "07L", "07C", "07R")), ("TRN1.SILVA", ("25L", "25C", "25R")), ("TRN1.CYRIL", ("25L", "25C", "25R")), ("TRN1.GRASS", ("25L", "25C", "25R")), ("WNNDY3.NARXX", ("07L", "07C", "07R")), ("WNNDY3.SILVA", ("07L", "07C", "07R")),),
    "IMLR": (("BEANS3.SPACE", ("25",)), ("BEANS3.SEEKS", ("25",)), ("HAWFA1.OCEEN", ("25", "07")), ("HAWFA1.ANYMS", ("25", "07")), ("KENED2.RENDR", ("25", "07")), ("KENED2.DINER", ("25", "07")), ("MEL1.MLR", ("25", "07")), ("MEL1.NONE", ("25", "07")), ("SAWPE1.SPACE", ("07",)), ("SAWPE1.BEANS", ("07",)),),
    "IGAR": (),
    "IBLT": (),
    "ITRC": (),
    "ILAR": (("GRASS1.ANYMS", ("24",)), ("GRASS1.RENTS", ("24",)), ("LCK1.LCK", ("24", "06")), ("ODOKU1.ODOKU", ("24", "06")), ("RENTS1.ANYMS", ("06",)), ("RENTS1.CAWZE", ("06",)), ("RENTS1.JUSTY", ("06",)),),
    "IPAP": (("KIN1.GRASS", ("35", "17")), ("KIN1.ANYMS", ("35", "17")), ("KIN1.DEL", ("35", "17")), ("KIN1.JUSTY", ("35", "17")), ("PFO1.PFO", ("35", "17")),),
    "IIAB": (("IAB1.MCC", ("27L", "27R", "09L", "09R")),),
    "IHEN": (),
    "IBAR": (),
    "IZOL": (),
    "IJAF": (),
    "ISCM": (),
    "ITKO": (("ASTRO1.BLANK", ("31", "02")), ("ASTRO1.PROBE", ("31", "02")), ("ASTRO1.DINER", ("31", "02")), ("HONDA1.HONDA", ("20", "02")), ("LETSE1.RENDR", ("02")), ("LETSE1.PROBE", ("02")), ("LETSE1.DINER", ("02")), ("ONDER1.PROBE", ("20", "13")), ("ONDER1.DINER", ("20", "13")), ("TOKYO1.TOKYO", ("31", "20", "13", "02")),),
    "IDCS": (),
    "IBRD": (),
    "IPPH": (("CAMEL2.CAMEL", ("33", "29", "11")), ("DINER2.DINER", ("33", "29", "11")), ("NARXX1.NARXX", ("33", "29", "11")), ("PER2.PER", ("33", "29", "15", "11")),),
    "ILKL": (),
    "IKFL": (),
    "ITEY": (),
    "IBTH": (("SBH1.SBH", ("27", "09")), ("MONTN1.DINER", ("09")), ("MONTN1.PYN", ("09")), ("OCEAN1.ROM", ("27")), ("OCEAN1.OCEEN", ("27")), ("RES1.PIPER", ("27")), ("RES1.WELSH", ("27")), ("RES1.EASTN", ("27")), ("VOX1.TALIS", ("09")), ("VOX1.DUNKS", ("09")), ("VOX1.CYRIL", ("09")),),
    "ISKP": (),
    "ISAU": (("BRDR1.SAWPE", ("26", "08")), ("BRDR1.BEANS", ("26", "08")), ("ECHHO1.SPACE", ("26", "08")), ("ECHHO1.THACC", ("26", "08")), ("SAU1.SAU", ("26", "08")), ("SAU1.THACC", ("26", "08")), ("SAU1.SHREK", ("26", "08")), ("SAU1.SPACE", ("26", "08")), ("SAU1.BEANS", ("26", "08")), ("SAU1.ALDER", ("26", "08")), ("SAYOW1.GODLU", ("08")), ("SAYOW1.ODOKU", ("08")), ("ZZOOO.GODLU", ("26")),("ZZOOO.ODOKU", ("26")),)
}

print("USED FOR IFR ONLY, NON AIRLINE CALLSIGNS WILL BREAK SYSTEM")

def Init_code(allow_no=False):
        global Pint, Init
        while True:
            if allow_no == True:
                Value = Input_code("Initial climb? (JUST THE FL/FT WITHOUT ADDING FL/FT AT THE START/END), MAX FL 999 (NO TO NOT SAVE) ")
                if Value == "NO":
                    Pint = "NO"
                    break
            else:
                Value = Input_code("Initial climb? (JUST THE FL/FT WITHOUT ADDING FL/FT AT THE START/END), MAX FL 999, MIN FT 1000")
            try:
                Value = int(Value)
            except ValueError:
                print("Input could not be turned into a intreger, please try again")
            else:
                if Value >= 1000:
                    Fih = f"{Value}ft"
                else:
                    Fih = f"FL{Value}"
                if allow_no:
                    Pint = Fih
                else:
                    Init = Fih
                break

def Dep_Station_Freq_code(P: bool = False):
    global PDep, Dep, Station, PStation, PFreq, Freq
    while True:
        Value1 = Input_code("Departure airport? ")
        if Value1 in Data_Runway:
            break
        print("Departure not found, please input a valid departure airport")
            
    while True:
        Value2 = Input_code("Station? ")
        if Value2 in Data_Station:
            if Value1 not in Data_Station[Value2][1:]:
                print("Station not valid for Departure airport, please input the correct station")
                continue
            break
        print("Station not found, please input a valid station")

    if P:
        PDep = Value1
        PStation = Value2
        PFreq = Data_Station[Value2][0]
    else:
        Dep = Value1
        Station = Value2
        Freq = Data_Station[Value2][0]

def Runway_code(P: bool = False):
    global PRwy, Runway
    while True:
        if P:
            Value1 = Input_code("Runway? (ENTER NO NOT TO SAVE A RUNWAY) ")
        else:
            Value1 = Input_code("Runway? ")
        if len(Value1) == 1:
            Value1 = f"0{Value1}"  
        if P: 
            if Value1 == "NO" or Value1 in Data_Runway[PDep]:
                PRwy = Value1
                break
        else:
            if Value1 in Data_Runway[Dep]:
                Runway = Value1
                break
        print("Runway not found, please input a valid runway for the departure airport")

def Main_Menu():
    global Preferences_Set, PDep, PStation, PRwy, Format, Format_Set, Generated_PDC, PDC_Generated
    while True:
        if Preferences_Set:
            print("""Welcome to the main menu for this program
options on what to do:
1: Change prefered departure airport and station
2: Change prefered Runway
3: Change prefered Init
4: Credits
5: Change pdc format
6: View generated pdcs
6: Generate a new pdc
7: Stop the program""")
        else:
            print("""Welcome to the main menu for this program
options on what to do:
1: Set preferences
2: Credits
3: Change pdc format
4: View generated pdcs
4: Generate a new pdc
5: Stop the program""")
        
        Navigator = Input_code("What would you like to do? ")

        try:
            Navigator = int(Navigator)
        except ValueError:
            print("Input must be a intreger, please try again")
            continue
        

        if Navigator == 1 and Preferences_Set:
            while True:
                Old = PDep
                Dep_Station_Freq_code(True)
                if Old != PDep:
                    print("The System needs to reset the runways due to a change in airport")
                    Runway_code(True)
        elif Navigator == 2 and Preferences_Set:
            Runway_code(True)
        elif Navigator == 3 and Preferences_Set:
            Init_code(True)
        elif Navigator == 1 and not Preferences_Set:
            Dep_Station_Freq_code(True)
            
            Runway_code(True)
            
            Init_code(True)

            Preferences_Set = True

        elif Navigator == 2 and not Preferences_Set or Navigator == 4 and Preferences_Set:
            print("""Creator = alla_spa
Discord acc id = 1018961962664726578
Roblox acc id = 1885848627
Thanks for using this program!""")
        elif Navigator == 3 and not Preferences_Set or Navigator == 5 and Preferences_Set:
            print("""Welcome to the format editor!
How to use:
For a variable use {} with these inputs (Case sensetive):
Dep: The Deparure Airport
Station: The Departure Station
Freq: The Departure Station Frequensy
Runway: Deparure Runway
Selected_Sid: The Sid Or Rdv If No Sid
Selected_Trans: The Sid Trans If Avail (Blank Otherwise)
Init: Initial Alt
Squawk: The Squawk Code
timez: The time (Format: DDHHMMZ)""")
            Format = Input_code("Inset format here: (Reset sets the program to system defult) ")
            if Format == "RESET":
                Format_Set = False
            else:
                Format = f"```{Format}```"
                Format_Set = True
        elif Navigator == 4 and not Preferences_Set or Navigator == 6 and Preferences_Set and pyperclip_installed:
            while True:
                Temp_PDC = Generated_PDC[::-1]
                for index, PDCs in enumerate(Temp_PDC, start=1):
                    print(f"{index}: {PDCs}")
                temp = Input_code("To copy a old pdc, type its number ")
                if temp.isdigit() and 1 <= int(temp) <= len(PDCs):
                    pyperclip.copy(Sids[int(Sid) - 1])
                    print("Complete!")
                    break
                else:
                    print("Input error, input a valid integer for the list (Menu to go back)")
                
        elif Navigator == 5 and not Preferences_Set or Navigator == 7 and Preferences_Set:
            return
        elif Navigator == 6 and not Preferences_Set or Navigator == 8 and Preferences_Set:
            print("Ending program, have a nice day")
            sys.exit()
        else:
            print("Input out of rangem please try again")

def Input_code(Description):
    Temp = input(Description).strip().upper()
    if Temp == "MENU":
        Main_Menu() 
        return Input_code(Description)
    else:
        return Temp

if Input_code("Set preferences? (YES), Can be esdited/added in the menu later ") == "YES":

    Dep_Station_Freq_code(True)

    Runway_code(True)

    Init_code(True)

    Preferences_Set = True

while True:

    Selected_Trans: str = ""
    Selected_Sid: str = ""
        
    if Preferences_Set:
        Use_preferences = Input_code("Use preferences? (YES): ") == "YES"

    if not Use_preferences:

        Dep_Station_Freq_code(False)

        Runway_code(False)

        Init_code(False)

    else:
        Dep = PDep
        Station = PStation
        Freq = PFreq
        if PRwy != "NO":
            Runway = PRwy
        else:
            Runway_code(False)
        if Pint != "NO":
            Init = Pint
        else:
            Init_code(False)

    while True:
        Callsign = Input_code("Callsign? ")
        if Callsign == "":
            print("Input invalid, please input a valid callsign")
        else:
            break

    while True:
        Arrival = Input_code("Arrival? ")
        if Arrival in Data_Runway:
            break
        print("Arrival not found, please input a valid arrival airport")

    while True:
        Sids = set()
        Transitions = set()

        if len(Data_Sids[Dep]) == 0:
            print("No SID data available for this departure airport. Using RDV.")
            Selected_Sid = "RDV"
            break

        for Data_Sid in Data_Sids[Dep]:
            sid = Data_Sid[0].split(".")[0]
            Valid_Runways = Data_Sid[1]
            if Runway in Valid_Runways:
                Sids.add(sid)

        Sids = sorted(Sids)

        for index1, sid in enumerate(Sids, start=1):
            print (f"{index1}: {sid}")
               
        Sid = Input_code("SID Number? (Number out of range = RDV)")

        if Sid.isdigit() and 1 <= int(Sid) <= len(Sids):
            Selected_Sid = Sids[int(Sid) - 1]
            break
        else:
            print("Skipping SIDs, inputting RDV in its place")
            Selected_Sid = "RDV"
            break

    if Selected_Sid != "RDV":

        for Trans in Data_Sids[Dep]:
            trans = Trans[0].split(".")
            if trans[0] == Selected_Sid:
                Transitions.add(trans[1])
        
        Transitions = sorted(Transitions)

        while True:
            if len(Transitions) == 1:
                Selected_Trans = f".{Transitions[0]}"
                print(f"The SID has only one transition, {Selected_Trans} has been autoselected")
                break

            for index2, trans in enumerate(Transitions, start=1):
                print (f"{index2}: {trans}")

            Tinput = Input_code("Transition Number?")

            if Tinput.isdigit() and 1 <= int(Tinput) <= len(Transitions):
                Selected_Trans = Transitions[int(Tinput) - 1]
                if not Format_Set:
                    Selected_Trans = f".{Selected_Trans}"
                break

            print("Transition not found. Please enter a valid transition for the selected SID.")

    while True:
        Squawk = "".join(str(random.randint(0, 7)) for _ in range(4))

        if Squawk not in ("1000", "7500", "7600", "7700"):
            break

    # UTC time in DDHHMMZ format
    timez = datetime.now(timezone.utc).strftime("%d%H%MZ")

    if not Format_Set:
        Format = f"""```PDC FOR {Callsign} GENERATED {timez}
CLR {Arrival} RWY {Runway} DEP {Selected_Sid}{Selected_Trans} CLB {Init}
SQUAWK {Squawk}
WHEN RDY CALL {Station} AT {Freq} WITH SQUAWK ONLY```"""
        print(Format)
    else:
        print(Format.format(DEP=Dep, STATION=Station, FREQ=Freq, RUNWAY=Runway, SELECTED_SID=Selected_Sid, SELECTED_TRANS=Selected_Trans, INIT=Init, SQUAWK=Squawk, TIMEZ=timez, CALLSIGN=Callsign, ARRIVAL=Arrival))

    if pyperclip_installed:
        try:
            pyperclip.copy(Format.format(DEP=Dep, STATION=Station, FREQ=Freq, RUNWAY=Runway, SELECTED_SID=Selected_Sid, SELECTED_TRANS=Selected_Trans, INIT=Init, SQUAWK=Squawk, TIMEZ=timez, CALLSIGN=Callsign, ARRIVAL=Arrival))
        except:
            print("Something went wrong while auto-copying, please copy it by hand instead")
        else:
            print("Output auto-copied to clipboard")
    else:
        print("""Pyperclip not installed, if it was installed it would copy it to your clipboard for you.
To get pyperclip type \"pip install pyperclip\" on Windows or \"pip3 install pyperclip\" on Mac/Linux.
Enter this command in your terminal, not in the program's input prompt.""")

    Generated_PDC.append(Format)
    PDC_Generated =+ 1

    Again = Input_code("Open the main menu? (Yes) To run the program again, simply input a string thats not \"yes\" ")
    if Again == "YES":
        Main_Menu()
