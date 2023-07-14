import sys
import subprocess
import re

cmd_brand = "sysctl -n machdep.cpu.brand_string"
brand = subprocess.check_output(cmd_brand, shell=True).decode("utf-8").strip()

brand = brand.replace("(R)", "")
brand = brand.replace("(TM)", "")
brand = brand.replace("CPU", "")
brand = brand.split("@")[0].strip()

# Test Case 1: Intel Xeon E5-2697 v2 @ 2.70GHz
# Test Case 2: Intel Core i7-7700K
# Test Case 3: Intel Core Solo T1350 @ 1.86GHz
# brand = "Intel Core Solo T1350 @ 1.86GHz"


def CPUGeneration(brand):

    Clarkdale = ["i3-530", "i3-540", "i3-550", "i3-560", "i5-650", "i5-655", "i5-660", "i5-661", "i5-670"]
    Lynnfield = ["i5-750", "i5-760", "i7-860", "i7-870", "i7-875", "i7-880"]
    Bloomfield = ["i7-920", "i7-930", "i7-940", "i7-950", "i7-960", "i7-965", "i7-975"]
    Clarksfield = ["i7-720", "i7-740", "i7-820", "i7-840", "i7-920", "i7-940"]
    Gulftown = ["i7-970", "i7-980", "i7-990", "i7-995"]

    pattern = r"i\d+-(\d+)"
    match = re.search(pattern, brand)
    generation = match.group(1)[:-3] if match else "Unknown"

    pattern2 = r"(i\d+-\d+)"
    match2 = re.search(pattern2, brand)
    raw_string = match2.group(1) if match2 else "Unknown"

    if raw_string in Clarkdale:
        generation = "Clarkdale"
    elif raw_string in Lynnfield:
        generation = "Lynnfield"
    elif raw_string in Bloomfield:
        generation = "Bloomfield"
    elif raw_string in Clarksfield:
        generation = "Clarksfield"
    elif raw_string in Gulftown:
        generation = "Gulftown"


    elif generation == "2":
        generation = "Sandy Bridge"
    elif generation == "3":
        generation = "Ivy Bridge"
    elif generation == "4":
        generation = "Haswell"
    elif generation == "5":
        generation = "Broadwell"
    elif generation == "6":
        generation = "Skylake"
    elif generation == "7":
        generation = "Kaby Lake"
    elif generation == "8":
        generation = "Coffee Lake"
    elif generation == "9":
        generation = "Coffee Lake"
    elif generation == "10":
        generation = "Comet Lake"
    elif generation == "11":
        generation = "Rocket Lake"
    elif generation == "12":
        generation = "Alder Lake"
    elif generation == "13":
        generation = "Meteor Lake"
    
    elif "Core Solo" in brand:
        generation = "Core Solo"
    elif "Core Duo" in brand:
        generation = "Core Duo"
    elif "Core2 Duo" in brand:
        generation = "Core 2 Duo"



    return generation



