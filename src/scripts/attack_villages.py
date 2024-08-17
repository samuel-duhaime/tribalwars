# Recruit some troops
# async def recruit_troop(page, number_of_troops):
#     try:
#         recruitButton = await page.wait_for_selector("input[id^='spear_']")
#         print(f"\nRecruiting {number_of_troops} troop(s)...")
#         await recruitButton.focus()
#         await page.keyboard.type(str(number_of_troops))
#         await page.keyboard.press("Enter")
#     except Exception as e:
#         print(f"\nError while recruiting the troop: {e}")


# Attack all the villages
async def attack_villages(page):
    try:
        await page.goto(
            "https://en141.tribalwars.net/game.php?village=47430&screen=place&target=46773"
        )

        while True:
            # Dictionary to store attack commands
            attack_commands = {
                "attack": "Attack one village",
                "exit": "Exit attack villages",
            }

            # Print the building commands
            print(f"\nAttack commands are:\n")
            for command, description in attack_commands.items():
                print(f"{command}: {description}")

            # Ask the user for the recruits troop choice
            choice = input("\nEnter your choice: ")
            if choice == "attack":
                # Select all troops
                selectAllTroopsButton = await page.wait_for_selector(
                    "a[id='selectAllUnits']"
                )
                await selectAllTroopsButton.click()

                # Attack the target village
                attackButton = await page.wait_for_selector("input[id='target_attack']")
                await attackButton.click()

                # Send the attack
                sendAttackButton = await page.wait_for_selector("input[id='troop_confirm_submit']")
                await sendAttackButton.click()
            elif choice == "exit":  # Escape key
                print("\nExiting attack village...")
                break
            else:
                print("\nInvalid choice. Please try again.")
    except Exception as e:
        print(f"Error while attacking the villages: {e}")
