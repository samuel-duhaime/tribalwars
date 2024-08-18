import asyncio
from pprint import pprint  # Print pretty
from typing import List, Optional, TypedDict
from playwright.async_api import Page
from .get_barbarian_villages import get_barbarian_villages


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
    "barbarian_ids": [],
}


# Function to safely convert text content to integer
def safe_int_conversion(text: str | int) -> int:
    try:
        return int(text)
    except ValueError:
        return int(0)


# Get the user information
async def get_user_info(page: Page) -> User:
    global user  # Declare user as global to modify it
    try:
        first_village: Village = {
            "id": 47430,
            "coordinate": {},
            "production": {"wood": 0, "clay": 0, "iron": 0},
            "resources": {"wood": 0, "clay": 0, "iron": 0},
            "storage": 0,
            "inactive_troops": {"spears": 0, "swords": 0},
            "total_troops": {"spears": 0, "swords": 0},
            "buildings": {},
            "researchs": {},
            "attacks": {},
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
            "wood": safe_int_conversion(wood_number),
            "clay": safe_int_conversion(clay_number),
            "iron": safe_int_conversion(iron_number),
        }

        # Get the storage number
        storage_element = await page.wait_for_selector("span#storage")
        storage_number = await page.evaluate(
            "(element) => element.textContent", storage_element
        )
        first_village["storage"] = int(storage_number)

        # TODO: Get the total troops number

        # Get the inactive troops number
        await page.goto(
            "https://en141.tribalwars.net/game.php?village=47430&screen=place&mode=units"
        )
        # Get the troops from defends
        defenses_element = await page.wait_for_selector("table#units_home")
        if defenses_element is not None:
            spears_defenses_element = await defenses_element.wait_for_selector(
                "th.unit-item-spear"
            )
            spears_defenses_number = await page.evaluate(
                "(element) => element.textContent", spears_defenses_element
            )
            first_village["inactive_troops"]["spears"] = safe_int_conversion(
                spears_defenses_number
            )
            swords_defenses_element = await defenses_element.wait_for_selector(
                "th.unit-item-sword"
            )
            swords_defenses_number = await page.evaluate(
                "(element) => element.textContent", swords_defenses_element
            )
            first_village["inactive_troops"]["swords"] = safe_int_conversion(
                swords_defenses_number
            )

        # Update the user object
        user["villages"] = [first_village]  # Update the first village

        # Get the barbarian villages ids
        user["barbarian_ids"] = await get_barbarian_villages(page)

        print("\nUser info:")
        pprint(user, compact=True)
        await asyncio.sleep(15)
        return user
    except Exception as e:
        print(f"Error while getting user information: {e}")
        return user
