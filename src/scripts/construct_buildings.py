# Construct a building
async def construct_building(page, building_name):
    try:
        # Wait for the construct button to be visible and click it
        constructButton = await page.wait_for_selector(
            f"[id^='main_buildlink_{building_name}_'].btn-build"
        )
        await constructButton.click()
        print(f"Constructing {building_name} building...")
    except Exception as e:
        print(f"Error while constructing the building {building_name}: {e}")


# Construct the buildings
async def construct_buildings(page):
    try:
        await page.goto(
            "https://en141.tribalwars.net/game.php?village=47430&screen=main"
        )

        while True:
            # Dictionary to store building commands
            building_commands = {
                "main": "Headquarters",
                "barrack": "Barracks",
                "smithy": "Smithy",
                "market": "Market",
                "wood": "Timber camp",
                "clay": "Clay pit",
                "iron": "Iron mine",
                "farm": "Farm",
                "storage": "Warehouse",
                "hide": "Hiding place",
                "wall": "Wall",
                "finish": "Finish construction",
                "exit": "Exit construct buildings",
            }

            # Print the building commands
            print(f"\nConstruct commands are:\n")
            for command, description in building_commands.items():
                print(f"{command}: {description}")

            # Ask the user for the building choice
            choice = input("\nEnter your choice: ")
            if choice == "main":
                await construct_building(page, "main")
            elif choice == "barrack":
                await construct_building(page, "barracks")
            elif choice == "smithy":
                await construct_building(page, "smith")
            elif choice == "market":
                await construct_building(page, "market")
            elif choice == "wood":
                await construct_building(page, "wood")
            elif choice == "clay":
                await construct_building(page, "stone")
            elif choice == "iron":
                await construct_building(page, "iron")
            elif choice == "farm":
                await construct_building(page, "farm")
            elif choice == "storage":
                await construct_building(page, "storage")
            elif choice == "finish":
                # Finish the construction when under 3 minutes left
                finishButton = await page.wait_for_selector(".btn-instant-free")
                print("Finishing the construction...")
                await finishButton.click()
            elif choice == "exit":  # Escape key
                print("Exiting construct buildings...")
                break
            else:
                print("Invalid choice. Please try again.")
    except Exception as e:
        print(f"Error while constructing the buildings: {e}")
