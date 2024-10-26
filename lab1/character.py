from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict, List
import copy

@dataclass
class Stats:
    health: int
    strength: int
    agility: int
    intelligence: int

class Character:
    def __init__(self, name: str, character_class: str, stats: Stats):
        self.name = name
        self.character_class = character_class
        self.stats = stats
        self.level = 1
        self.inventory = []

    def __str__(self):
        return f"{self.name} - Level {self.level} {self.character_class}"

# Builder Pattern
class CharacterBuilder:
    def __init__(self):
        self.reset()
    
    def reset(self):
        self._character = None
        self._stats = Stats(0, 0, 0, 0)
        self._name = ""
        self._class = ""
    
    def set_name(self, name: str):
        self._name = name
        return self
    
    def set_class(self, char_class: str):
        self._class = char_class
        return self
    
    def set_stats(self, health: int, strength: int, agility: int, intelligence: int):
        self._stats = Stats(health, strength, agility, intelligence)
        return self
    
    def build(self) -> Character:
        character = Character(self._name, self._class, self._stats)
        self.reset()
        return character

# Prototype Pattern
class CharacterPrototype(ABC):
    @abstractmethod
    def clone(self):
        pass

class WarriorPrototype(CharacterPrototype):
    def __init__(self):
        self.character = Character(
            "Warrior",
            "Warrior",
            Stats(100, 15, 10, 5)
        )
    
    def clone(self):
        return copy.deepcopy(self.character)

class MagePrototype(CharacterPrototype):
    def __init__(self):
        self.character = Character(
            "Mage",
            "Mage",
            Stats(70, 5, 8, 20)
        )
    
    def clone(self):
        return copy.deepcopy(self.character)

# Singleton Pattern
class CharacterRegistry:
    _instance = None
    _characters: Dict[str, Character] = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CharacterRegistry, cls).__new__(cls)
        return cls._instance
    
    def register_character(self, character: Character):
        self._characters[character.name] = character
    
    def get_character(self, name: str) -> Character:
        return self._characters.get(name)
    
    def list_characters(self) -> List[str]:
        return list(self._characters.keys())

if __name__ == "__main__":
    # Using Builder
    builder = CharacterBuilder()
    custom_warrior = (
        builder.set_name("Conan")
        .set_class("Warrior")
        .set_stats(120, 18, 12, 6)
        .build()
    )
    print(f"Created using Builder: {custom_warrior}")

    # Using Prototype
    warrior_prototype = WarriorPrototype()
    warrior1 = warrior_prototype.clone()
    warrior1.name = "Thor"
    
    mage_prototype = MagePrototype()
    mage1 = mage_prototype.clone()
    mage1.name = "Gandalf"
    
    print(f"Created using Prototype: {warrior1}")
    print(f"Created using Prototype: {mage1}")

    # Using Singleton Registry
    registry = CharacterRegistry()
    registry.register_character(custom_warrior)
    registry.register_character(warrior1)
    registry.register_character(mage1)
    
    print("\nRegistered characters:", registry.list_characters())
    
    # Verify Singleton
    another_registry = CharacterRegistry()
    print("Singleton check - Same characters in new instance:", 
          another_registry.list_characters())