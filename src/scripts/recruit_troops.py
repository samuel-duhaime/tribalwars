from playwright.async_api import Page

# Recruit some troops
async def recruit_troop(page: Page, number_of_troops: int) -> None:
    try:
        recruitButton = await page.wait_for_selector("input[id^='spear_']")
        print(f"\nRecruiting {number_of_troops} troop(s)...")
        await recruitButton.focus()
        await page.keyboard.type(str(number_of_troops))
        await page.keyboard.press("Enter")
        return
    except Exception as e:
        print(f"\nError while recruiting the troop: {e}")
        return


# Recruit all the troops
async def recruit_troops(page):
    try:
        await page.goto(
            "https://en141.tribalwars.net/game.php?village=47430&screen=train"
        )

        while True:
            # Dictionary to store train commands
            recruit_commands = {
                "spear": "Train spear fighters",
                "exit": "Exit recruit troops",
            }

            # Print the building commands
            print(f"\nRecruit commands are:\n")
            for command, description in recruit_commands.items():
                print(f"{command}: {description}")

            # Ask the user for the recruits troop choice
            choice = input("\nEnter your choice: ")
            if choice == "spear":
                number_of_troops = input("Enter the number of troops to recruit: ")
                if number_of_troops.isdigit() and int(number_of_troops) > 0:
                    await recruit_troop(page, int(number_of_troops))
            elif choice == "exit":  # Escape key
                print("\nExiting recruit troops...")
                break
            else:
                print("\nInvalid choice. Please try again.")
    except Exception as e:
        print(f"Error while training the troops: {e}")
