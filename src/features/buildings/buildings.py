from typing import TypedDict, Optional, Literal
from playwright.async_api import Page
import asyncio
from common.save import save
from common.load import load


# Building name
BuildingName = Literal[
    "Headquarters",
    "Barracks",
    "Stable",
    "Workshop",
    "Academy",
    "Watchtower",
    "Smithy",
    "Rally point",
    "Market",
    "Timber camp",
    "Clay pit",
    "Iron mine",
    "Farm",
    "Warehouse",
    "Hiding place",
    "Wall",
]

# Max levels for each building
MAX_LEVELS = {
    "Headquarters": 30,
    "Barracks": 25,
    "Stable": 20,
    "Workshop": 15,
    "Academy": 3,
    "Watchtower": 20,
    "Smithy": 20,
    "Rally point": 1,
    "Market": 25,
    "Timber camp": 30,
    "Clay pit": 30,
    "Iron mine": 30,
    "Farm": 30,
    "Warehouse": 30,
    "Hiding place": 10,
    "Wall": 20,
}


# Building type
class Building(TypedDict):
    building_name: BuildingName
    level: int
    max_level: int


# Buildings class
class Buildings:
    # Initialize the class
    def __init__(self, village_id: int):
        self.village_id = village_id
        self.village = load(f"village_{village_id}.json")
        if self.village is not None:
            self.buildings = self.village.get("buildings", None)
        else:
            self.buildings = None

    # Save to a json file
    def save(self):
        if self.village is not None:
            self.village["buildings"] = self.buildings
            save(self.village, f"village_{self.village_id}.json")
        else:
            print("No village data to save.")

    # Get the buildings
    def get(self):
        print(self.buildings)
        return self.buildings

    # TODO: Construct the building for real
    # Construct a building
    def construct(self, building_name: BuildingName):
        if self.buildings is not None:
            # Check if the building already exists
            for building in self.buildings:
                if building["building_name"] == building_name:
                    print(f"\n{building_name} already exists.")
                    return

            # Add the new building
            new_building = {
                "building_name": building_name,
                "level": 1,
                "max_level": MAX_LEVELS[building_name],
            }
            self.buildings.append(new_building)
            print(f"\nConstructing {building_name} building to level 1...")
            self.save()

        else:
            print("\nNo buildings data available.")

    # TODO: Upgrade the building for real
    # Upgrade a building one level
    def upgrade(self, building_name: BuildingName):
        if self.buildings is not None:
            for building in self.buildings:
                if building["building_name"] == building_name:
                    max_level = MAX_LEVELS[building_name]
                    if building["level"] < max_level:
                        building["level"] += 1
                        self.save()
                        break
                    else:
                        print(
                            f"\n{building_name} is already at its maximum level of {max_level}."
                        )
                        break
        else:
            print("No buildings to upgrade.")

    # TODO: automate_construct_buildings

    # async def construct_building(self, page: Page, building_name: BuildingName):
    #     try:
    #         constructButton = await page.wait_for_selector(
    #             f"[id^='main_buildlink_{building_name}_'].btn-build"
    #         )
    #         await constructButton.click()
    #         print(f"Constructing {building_name} building...")
    #     except Exception as e:
    #         print(f"Error while constructing the building {building_name}: {e}")

    # async def construct_buildings(self, page):
    #     try:
    #         await page.goto(
    #             "https://en141.tribalwars.net/game.php?village=47430&screen=main"
    #         )

    #         while True:
    #             building_commands = {
    #                 # Add your building commands here
    #             }
    #             # Add logic to construct buildings based on commands
    #     except Exception as e:ars.net/game.php?village=47430&screen=main"
    #         )

    #         while True:
    #             building_commands = {
    #                 # Add your building commands here
    #             }
    #             # Add logic to construct buildings based on commands
    #     except Exception as e:
    #         print(f"Error while navigating to the page: {e}")
