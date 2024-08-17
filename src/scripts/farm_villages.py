import asyncio
from get_user_info import User


# Attack one village
async def attack_village(page, current_village_id: int, target_village_id: int) -> None:
    try:
        await page.goto(
            f"https://en141.tribalwars.net/game.php?village={current_village_id}&screen=place&target={target_village_id}"
        )

        # Select all troops
        # selectAllTroopsButton = await page.wait_for_selector("a[id='selectAllUnits']")
        # await selectAllTroopsButton.click()

        # Select template
        selectSpearsButton = await page.wait_for_selector("a.troop_template_selector")
        await selectSpearsButton.click()

        # Attack the target village
        attackButton = await page.wait_for_selector("input[id='target_attack']")
        await attackButton.click()

        # Send the attack
        sendAttackButton = await page.wait_for_selector(
            "input[id='troop_confirm_submit']"
        )
        await sendAttackButton.click()
        return
    except Exception as e:
        print(f"Error while attacking the village: {e}")
        return


# Farm all the villages
async def farm_villages(page, user: User) -> None:
    try:
        # Get user information
        last_attack_barbarian_id = user.get("last_attack_barbarian_id")
        barbarian_ids = user.get("barbarian_ids")
        current_village_id = user.get("current_village_id", None)
        villages = user.get("villages", [])
        current_village = next(
            (village for village in villages if village["id"] == current_village_id),
            None,
        )
        inactive_troops = current_village.get("inactive_troops", {})
        inactive_spears = inactive_troops.get("spears", 0)

        # Find the next barbarian village to attack
        if last_attack_barbarian_id in barbarian_ids:
            last_index = barbarian_ids.index(
                last_attack_barbarian_id
            )  # Get the last index
            next_index = (last_index + 1) % len(barbarian_ids)  # Get the next index
            next_attack_barbarian_id = barbarian_ids[next_index]
        else:
            # If the last attack village is not in the list, attack the first village
            next_attack_barbarian_id = barbarian_ids[0]

        await asyncio.sleep(5)

        print(f"\nInactive troops are {inactive_troops}")

        # Check if enough troops are available to attack the village
        if inactive_spears >= 20:
            print(f"\nNext village to attack is: {next_attack_barbarian_id}")
            user["last_attack_barbarian_id"] = next_attack_barbarian_id  # Update the last attack barbarian
            await attack_village(page, current_village_id, next_attack_barbarian_id)
        else:
            print(
                f"\nNot enough troops to attack the village: {next_attack_barbarian_id}"
            )

        return
    except Exception as e:
        print(f"Error while farming the villages: {e}")
        return
