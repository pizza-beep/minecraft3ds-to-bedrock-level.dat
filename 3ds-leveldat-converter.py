import nbtlib
from nbtlib import Compound, Int, Long, Byte, Float, String

# 3DS level.dat file path
level_3ds_path = 'level_3ds.dat'  # Update this with your 3DS level.dat path
level_bedrock_path = 'level_bedrock.dat'  # Output path for Bedrock level.dat

# Load 3DS level.dat
level_3ds = nbtlib.load(level_3ds_path)

# Create a new structure for Bedrock level.dat
level_bedrock = Compound({
    "RandomSeed": Long(level_3ds["RandomSeed"]),
    "GameType": Int(level_3ds["GameType"]),
    "Difficulty": Int(level_3ds["Difficulty"]),
    "ForceGameType": Byte(level_3ds["ForceGameType"]),
    "SpawnX": Int(level_3ds["SpawnX"]),
    "SpawnY": Int(level_3ds["SpawnY"]),
    "SpawnZ": Int(level_3ds["SpawnZ"]),
    "Time": Long(level_3ds["Time"]),
    "LastPlayed": Long(level_3ds["LastPlayed"]),
    "LevelName": String(level_3ds["LevelName"]),
    "StorageVersion": Int(level_3ds["StorageVersion"]),
    "NetworkVersion": Int(level_3ds["NetworkVersion"]),
    "Platform": Int(level_3ds["Platform"]),
    "spawnMobs": Byte(level_3ds["spawnMobs"]),
    "Generator": Int(level_3ds["Generator"]),
    "LimitedWorldOriginX": Int(level_3ds["LimitedWorldOriginX"]),
    "LimitedWorldOriginY": Int(level_3ds["LimitedWorldOriginY"]),
    "LimitedWorldOriginZ": Int(level_3ds["LimitedWorldOriginZ"]),
    "DayCycleStopTime": Long(level_3ds["DayCycleStopTime"]),
    "worldStartCount": Long(level_3ds["worldStartCount"]),
    "currentTick": Long(level_3ds["currentTick"]),
    "rainLevel": Float(level_3ds["rainLevel"]),
    "rainTime": Int(level_3ds["rainTime"]),
    "lightningLevel": Float(level_3ds["lightningLevel"]),
    "lightningTime": Int(level_3ds["lightningTime"]),
    "hasBeenLoadedInCreative": Byte(level_3ds["hasBeenLoadedInCreative"]),
    "achievementsDisabled": Byte(level_3ds["achievementsDisabled"]),
    "eduLevel": Byte(level_3ds["eduLevel"]),
    "immutableWorld": Byte(level_3ds["immutableWorld"]),
    "MultiplayerGame": Byte(level_3ds["MultiplayerGame"]),
    "LANBroadcast": Byte(level_3ds["LANBroadcast"]),
    "XBLBroadcast": Byte(level_3ds["XBLBroadcast"]),
    "commandsEnabled": Byte(level_3ds["commandsEnabled"]),
    "texturePacksRequired": Byte(level_3ds["texturePacksRequired"]),
    "lastOpenedWithVersion": level_3ds["lastOpenedWithVersion"],
    "commandblockoutput": Byte(level_3ds["commandblockoutput"]),
    "dodaylightcycle": Byte(level_3ds["dodaylightcycle"]),
    "doentitydrops": Byte(level_3ds["doentitydrops"]),
    "dofiretick": Byte(level_3ds["dofiretick"]),
    "domobloot": Byte(level_3ds["domobloot"]),
    "domobspawning": Byte(level_3ds["domobspawning"]),
    "dotiledrops": Byte(level_3ds["dotiledrops"]),
    "doweathercycle": Byte(level_3ds["doweathercycle"]),
    "drowningdamage": Byte(level_3ds["drowningdamage"]),
    "falldamage": Byte(level_3ds["falldamage"]),
    "firedamage": Byte(level_3ds["firedamage"]),
    "keepinventory": Byte(level_3ds["keepinventory"]),
    "mobgriefing": Byte(level_3ds["mobgriefing"]),
    "pvp": Byte(level_3ds["pvp"]),
    "sendcommandfeedback": Byte(level_3ds["sendcommandfeedback"]),
    "fixedInventory": level_3ds["fixedInventory"],
    "SpawnRotX": Float(level_3ds["SpawnRotX"]),
    "SpawnRotY": Float(level_3ds["SpawnRotY"]),
    "StructuresForceGenerated": Byte(level_3ds["StructuresForceGenerated"]),
    "StructuresForceGeneratedAttempted": Byte(level_3ds["StructuresForceGeneratedAttempted"]),
    "ForcedMansionX": Int(level_3ds["ForcedMansionX"]),
    "ForcedMansionZ": Int(level_3ds["ForcedMansionZ"]),
    "worldStartCount": Long(level_3ds["worldStartCount"]),
})

# Save the new level.dat file in Bedrock format
level_bedrock_file = nbtlib.File(level_bedrock)
level_bedrock_file.save(level_bedrock_path)

print(f"Bedrock level.dat created at {level_bedrock_path}")

