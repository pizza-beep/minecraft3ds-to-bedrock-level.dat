import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from nbtlib import Compound, Int, Long, Byte, Float, String, List, load, File
import os

class MinecraftConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Minecraft 3DS to Bedrock Converter")
        self.root.geometry("400x300")

        self.create_widgets()

    def create_widgets(self):
        # Frame for file selection
        self.frame = ttk.Frame(self.root, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.open_btn = ttk.Button(self.frame, text="Open MC3DS Level Data File", command=self.open_file)
        self.open_btn.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

        self.save_btn = ttk.Button(self.frame, text="Save As Bedrock Level Data File", command=self.save_file)
        self.save_btn.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

        self.convert_btn = ttk.Button(self.frame, text="Convert", command=self.convert_file)
        self.convert_btn.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)

        self.status_label = ttk.Label(self.frame, text="Status: Waiting for input...")
        self.status_label.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)

        # Variables
        self.level_3ds_path = None
        self.level_bedrock_path = None

    def open_file(self):
        self.level_3ds_path = filedialog.askopenfilename(
            defaultextension=".dat",
            filetypes=[("Minecraft 3DS level.dat Files", "*.dat")],
            initialdir=os.getcwd(),
            title="Open MC3DS Level Data File"
        )
        if self.level_3ds_path:
            self.status_label.config(text=f"Selected file: {os.path.basename(self.level_3ds_path)}")

    def save_file(self):
        self.level_bedrock_path = filedialog.asksaveasfilename(
            defaultextension=".dat",
            filetypes=[("Bedrock Edition level.dat File", "*.dat")],
            initialdir=os.getcwd(),
            title="Save As Bedrock Level Data File"
        )
        if self.level_bedrock_path:
            self.status_label.config(text=f"Save location: {os.path.basename(self.level_bedrock_path)}")

    def detect_version(self, data):
        # Check for fields unique to specific versions to determine the format version
        if "LANBroadcast" in data:
            return "1.3"
        elif "achievementsDisabled" in data:
            return "1.2"
        elif "LevelSize" in data:
            return "1.1 or 1.0"
        else:
            return "Unknown"

    def convert_to_bedrock(self, level_3ds, version):
        # Common fields across all versions
        level_bedrock = Compound({
            "RandomSeed": Long(get_value(level_3ds, "RandomSeed", 0)),
            "GameType": Int(get_value(level_3ds, "GameType", 1)),
            "Difficulty": Int(get_value(level_3ds, "Difficulty", 0)),
            "ForceGameType": Byte(get_value(level_3ds, "ForceGameType", 0)),
            "SpawnX": Int(get_value(level_3ds, "SpawnX", 0)),
            "SpawnY": Int(get_value(level_3ds, "SpawnY", 64)),
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
            "eduLevel": Byte(get_value(level_3ds, "eduLevel", 0)),
            "immutableWorld": Byte(get_value(level_3ds, "immutableWorld", 0)),
            "MultiplayerGame": Byte(get_value(level_3ds, "MultiplayerGame", 0)),
            "LANBroadcast": Byte(get_value(level_3ds, "LANBroadcast", 0)),
            "XBLBroadcast": Byte(get_value(level_3ds, "XBLBroadcast", 0)),
            "commandsEnabled": Byte(get_value(level_3ds, "commandsEnabled", 0)),
            "texturePacksRequired": Byte(get_value(level_3ds, "texturePacksRequired", 0)),
            "lastOpenedWithVersion": List(Int, get_value(level_3ds, "lastOpenedWithVersion", [1, 1, 0, 0])),
            "fixedInventory": Compound({
                "fixedInventoryItems": List(Compound, get_value(level_3ds, "fixedInventory", {"fixedInventoryItems": []})["fixedInventoryItems"])
            }),
        })

        # Add fields for specific versions
        if version == "1.2" or version == "1.3":
            level_bedrock["achievementsDisabled"] = Byte(get_value(level_3ds, "achievementsDisabled", 0))

        if version in ["1.3", "1.4", "1.5"]:
            level_bedrock["LANBroadcast"] = Byte(get_value(level_3ds, "LANBroadcast", 0))

        if version in ["1.6", "1.7", "1.8"]:
            level_bedrock["SpawnRotX"] = Float(get_value(level_3ds, "SpawnRotX", 0.0))
            level_bedrock["SpawnRotY"] = Float(get_value(level_3ds, "SpawnRotY", 0.0))

        if version in ["1.7", "1.8"]:
            level_bedrock["commandblockoutput"] = Byte(get_value(level_3ds, "commandblockoutput", 1))

        if version == "1.9":
            level_bedrock["dodaylightcycle"] = Byte(get_value(level_3ds, "dodaylightcycle", 1))
            level_bedrock["doentitydrops"] = Byte(get_value(level_3ds, "doentitydrops", 1))
            level_bedrock["dofiretick"] = Byte(get_value(level_3ds, "dofiretick", 1))
            level_bedrock["domobloot"] = Byte(get_value(level_3ds, "domobloot", 1))
            level_bedrock["domobspawning"] = Byte(get_value(level_3ds, "domobspawning", 1))
            level_bedrock["dotiledrops"] = Byte(get_value(level_3ds, "dotiledrops", 1))
            level_bedrock["doweathercycle"] = Byte(get_value(level_3ds, "doweathercycle", 1))
            level_bedrock["keepinventory"] = Byte(get_value(level_3ds, "keepinventory", 0))
            level_bedrock["mobgriefing"] = Byte(get_value(level_3ds, "mobgriefing", 1))
            level_bedrock["StructuresForceGenerated"] = Byte(get_value(level_3ds, "StructuresForceGenerated", 0))
            level_bedrock["StructuresForceGeneratedAttempted"] = Byte(get_value(level_3ds, "StructuresForceGeneratedAttempted", 1))
            level_bedrock["ForcedMansionX"] = Int(get_value(level_3ds, "ForcedMansionX", -2147483648))
            level_bedrock["ForcedMansionZ"] = Int(get_value(level_3ds, "ForcedMansionZ", -2147483648))

        return level_bedrock

    def convert_file(self):
        if not self.level_3ds_path or not self.level_bedrock_path:
            messagebox.showwarning("Input Error", "Please select both input and output files.")
            return

        try:
            with open(self.level_3ds_path, 'rb') as file:
                level_3ds_data = load(file)

            version = self.detect_version(level_3ds_data)
            if version == "Unknown":
                messagebox.showerror("Conversion Error", "Unknown or unsupported version format.")
                return

            level_bedrock_data = self.convert_to_bedrock(level_3ds_data, version)

            with open(self.level_bedrock_path, 'wb') as file:
                level_bedrock_data.dump(file)

            messagebox.showinfo("Success", f"Conversion successful to version {version}.")
            self.status_label.config(text=f"Converted file saved: {os.path.basename(self.level_bedrock_path)}")

        except Exception as e:
            messagebox.showerror("Conversion Error", f"An error occurred: {e}")
            self.status_label.config(text="Conversion failed.")

def get_value(data, field, default):
    return data.get(field, default)

if __name__ == "__main__":
    root = tk.Tk()
    app = MinecraftConverterApp(root)
    root.mainloop()
