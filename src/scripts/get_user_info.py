import asyncio
from pprint import pprint  # Print pretty
from typing import List, Optional, TypedDict


# Define the resources type
class Resources(TypedDict):
    wood: int
    clay: int
    iron: int


class Troops(TypedDict):
    spears: int
    swords: int


# Define the Village type
class Village(TypedDict):
    id: int
    coordinate: dict
    production: Resources
    resources: Resources
    storage: int
    inactive_troops: Troops
    total_troops: Troops
    buildings: dict
    researchs: dict
    attacks: dict


# Define the User type
class User(TypedDict):
    world: int
    current_village_id: Optional[int]
    villages: List[Village]
    last_attack_barbarian_id: Optional[int]
    barbarian_ids: List[int]


# Global user object
user: User = {
    "world": 141,
    "current_village_id": 47430,
    "villages": [],
    "last_attack_barbarian_id": 46773,
    "barbarian_ids": [46773, 46512, 47505],
}


# Get the user information
async def get_user_info(page) -> User:
    global user  # Declare user as global to modify it
    try:
        first_village: Village = {
            "id": 47430,
            "inactive_troops": {"spears": 72, "swords": 20},
        }

        await page.goto(
            "https://en141.tribalwars.net/game.php?village=47430&screen=main"
        )

        # Get the resources number
        wood_element = await page.wait_for_selector("span#wood")
        wood_number = await page.evaluate(
            "(element) => element.textContent", wood_element
        )
        clay_element = await page.wait_for_selector("span#stone")
        clay_number = await page.evaluate(
            "(element) => element.textContent", clay_element
        )
        iron_element = await page.wait_for_selector("span#iron")
        iron_number = await page.evaluate(
            "(element) => element.textContent", iron_element
        )
        first_village["resources"] = {
            "wood": int(wood_number),
            "clay": int(clay_number),
            "iron": int(iron_number),
        }

        # Get the storage number
        storage_element = await page.wait_for_selector("span#storage")
        storage_number = await page.evaluate(
            "(element) => element.textContent", storage_element
        )
        first_village["storage"] = int(storage_number)

        # TODO: Get the troops number
        # await page.goto(
        #     "https://en141.tribalwars.net/game.php?village=47430&screen=barracks"
        # )
        # # Find the first td element with the text "?/?"
        # troops_element = await page.wait_for_selector("td:text-matches('\\d+/\\d+')")
        # # Get the text content of the td element
        # troops_number = await page.evaluate(
        #     "(element) => element.textContent", troops_element
        # )
        # # Split the text content to get the individual troop numbers
        # troops = troops_number.split("/")
        # # Convert the troop numbers to integers
        # troops = [int(troop) for troop in troops]
        # # Create a dictionary with the troop names as keys and the troop numbers as values
        # troop_names = ["spear", "sword"]  # Add more troop names as needed
        # troops_dict = dict(zip(troop_names, troops))
        # Update the first village's troops
        # first_village["troops"] = troops_dict

        # Update the user object
        user["villages"] = [first_village]  # Update the first village

        await asyncio.sleep(5)

        print("\nUser info:")
        pprint(user)
        return user
    except Exception as e:
        print(f"Error while getting user information: {e}")
        return user
