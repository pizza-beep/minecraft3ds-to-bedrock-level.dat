from tkinter import filedialog, simpledialog, messagebox
from nbtlib import Compound, Int, Long, Byte, Float, String, List, load, File
import os

level_3ds_path = filedialog.askopenfilename( # Open PATH for 3DS level.dat
    defaultextension=".data",
    filetypes=[("Minecraft 3DS level.dat Files", "*.dat")],
    initialdir=os.getcwd(),
    title="Open MC3DS Level Data File"
)

level_bedrock_path = filedialog.asksaveasfilename( # Output path for Bedrock level.dat
    defaultextension=".dat",
    filetypes=[("Bedrock Edition level.dat File", "*.dat")],
    initialdir=os.getcwd(),
    title="Save-As Bedrock Level Data File"
)

# Load 3DS level.dat
try:
    level_3ds = load(level_3ds_path)
except FileNotFoundError:
    print(f"Error: The file {level_3ds_path} was not found.")
    os.system('pause')
    exit(1)
except Exception as e:
    print(f"Error loading the 3DS level.dat file: {e}")
    os.system('pause')
    exit(1)



# Helper function to safely get values with a default fallback
def get_value(data, key, default):
    return data[key] if key in data else default

# Create a new structure for Bedrock level.dat
level_bedrock = Compound({
    "RandomSeed": Long(get_value(level_3ds, "RandomSeed", 0)),
    "GameType": Int(get_value(level_3ds, "GameType", 1)),
    "Difficulty": Int(get_value(level_3ds, "Difficulty", 0)),
    "ForceGameType": Byte(get_value(level_3ds, "ForceGameType", 0)),
    "SpawnX": Int(get_value(level_3ds, "SpawnX", 0)),
    "SpawnY": Int(get_value(level_3ds, "SpawnY", 64)),  # Default to 64 if missing
    "SpawnZ": Int(get_value(level_3ds, "SpawnZ", 0)),
    "Time": Long(get_value(level_3ds, "Time", 0)),
    "LastPlayed": Long(get_value(level_3ds, "LastPlayed", 0)),
    "LevelName": String(get_value(level_3ds, "LevelName", "World")),
    "StorageVersion": Int(get_value(level_3ds, "StorageVersion", 0)),
    "NetworkVersion": Int(get_value(level_3ds, "NetworkVersion", 0)),
    "Platform": Int(get_value(level_3ds, "Platform", 0)),
    "spawnMobs": Byte(get_value(level_3ds, "spawnMobs", 1)),
    "Generator": Int(get_value(level_3ds, "Generator", 1)),
    "LimitedWorldOriginX": Int(get_value(level_3ds, "LimitedWorldOriginX", 0)),
    "LimitedWorldOriginY": Int(get_value(level_3ds, "LimitedWorldOriginY", 0)),
    "LimitedWorldOriginZ": Int(get_value(level_3ds, "LimitedWorldOriginZ", 0)),
    "DayCycleStopTime": Long(get_value(level_3ds, "DayCycleStopTime", -1)),
    "worldStartCount": Long(get_value(level_3ds, "worldStartCount", 0)),
    "currentTick": Long(get_value(level_3ds, "currentTick", 0)),
    "rainLevel": Float(get_value(level_3ds, "rainLevel", 0.0)),
    "rainTime": Int(get_value(level_3ds, "rainTime", 0)),
    "lightningLevel": Float(get_value(level_3ds, "lightningLevel", 0.0)),
    "lightningTime": Int(get_value(level_3ds, "lightningTime", 0)),
    "hasBeenLoadedInCreative": Byte(get_value(level_3ds, "hasBeenLoadedInCreative", 0)),
    "achievementsDisabled": Byte(get_value(level_3ds, "achievementsDisabled", 0)),
    "eduLevel": Byte(get_value(level_3ds, "eduLevel", 0)),
    "immutableWorld": Byte(get_value(level_3ds, "immutableWorld", 0)),
    "MultiplayerGame": Byte(get_value(level_3ds, "MultiplayerGame", 0)),
    "LANBroadcast": Byte(get_value(level_3ds, "LANBroadcast", 0)),
    "XBLBroadcast": Byte(get_value(level_3ds, "XBLBroadcast", 0)),
    "commandsEnabled": Byte(get_value(level_3ds, "commandsEnabled", 0)),
    "texturePacksRequired": Byte(get_value(level_3ds, "texturePacksRequired", 0)),
    "lastOpenedWithVersion": List(Int, get_value(level_3ds, "lastOpenedWithVersion", [1, 1, 0, 0])),
    "commandblockoutput": Byte(get_value(level_3ds, "commandblockoutput", 1)),
    "dodaylightcycle": Byte(get_value(level_3ds, "dodaylightcycle", 1)),
    "doentitydrops": Byte(get_value(level_3ds, "doentitydrops", 1)),
    "dofiretick": Byte(get_value(level_3ds, "dofiretick", 1)),
    "domobloot": Byte(get_value(level_3ds, "domobloot", 1)),
    "domobspawning": Byte(get_value(level_3ds, "domobspawning", 1)),
    "dotiledrops": Byte(get_value(level_3ds, "dotiledrops", 1)),
    "doweathercycle": Byte(get_value(level_3ds, "doweathercycle", 1)),
    "drowningdamage": Byte(get_value(level_3ds, "drowningdamage", 1)),
    "falldamage": Byte(get_value(level_3ds, "falldamage", 1)),
    "firedamage": Byte(get_value(level_3ds, "firedamage", 1)),
    "keepinventory": Byte(get_value(level_3ds, "keepinventory", 0)),
    "mobgriefing": Byte(get_value(level_3ds, "mobgriefing", 1)),
    "pvp": Byte(get_value(level_3ds, "pvp", 1)),
    "sendcommandfeedback": Byte(get_value(level_3ds, "sendcommandfeedback", 1)),
    "fixedInventory": Compound({
        "fixedInventoryItems": List(Compound, get_value(level_3ds, "fixedInventory", {"fixedInventoryItems": []})["fixedInventoryItems"])
    }),
    "SpawnRotX": Float(get_value(level_3ds, "SpawnRotX", 0.0)),
    "SpawnRotY": Float(get_value(level_3ds, "SpawnRotY", 0.0)),
    "StructuresForceGenerated": Byte(get_value(level_3ds, "StructuresForceGenerated", 0)),
    "StructuresForceGeneratedAttempted": Byte(get_value(level_3ds, "StructuresForceGeneratedAttempted", 1)),
    "ForcedMansionX": Int(get_value(level_3ds, "ForcedMansionX", -2147483648)),
    "ForcedMansionZ": Int(get_value(level_3ds, "ForcedMansionZ", -2147483648)),
    "worldStartCount": Long(get_value(level_3ds, "worldStartCount", 4294967293)),
})

# Save the new level.dat file in Bedrock format
try:
    level_bedrock_file = File(level_bedrock)
    level_bedrock_file.save(level_bedrock_path)
    print(f"Bedrock level.dat created successfully at {level_bedrock_path}")
except Exception as e:
    print(f"Error saving the Bedrock level.dat file: {e}")
