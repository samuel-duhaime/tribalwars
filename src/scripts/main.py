import asyncio
import os
import threading
from playwright.async_api import async_playwright
from .login import login
from .farm_villages import farm_villages
from .get_user_info import get_user_info

# from .construct_buildings import construct_buildings
# from .recruit_troops import recruit_troops


# Shared variable to signal the active script
active_script = None


async def research_weapons() -> None:
    try:
        print("Starting research_weapons...")
        await asyncio.sleep(10)
        print("Completed research_weapons.")
    except Exception as e:
        print(f"Error while researching weapons: {e}")


# Handle user input in a separate thread
def handle_input() -> None:
    global active_script
    while True:
        print(f"\nActive script: {active_script}")
        # Print the available commands
        scripts_commands = {
            "login": "Login",
            "start": "Start every script automatically",
            "exit": "Exit the scripts",
        }
        print(f"\nScripts commands are:\n")
        for command, description in scripts_commands.items():
            print(f"{command}: {description}")
        choice = input("\nEnter your choice: ")

        if choice == "login":
            active_script = "login"
        elif choice == "start":
            active_script = "start"
        elif choice == "exit":
            print("\nExiting scripts mode...")
            active_script = "exit"
            return
        else:
            print("\nInvalid choice. Please try again.")


# Main function
async def main() -> None:
    global active_script
    async with async_playwright() as p:
        # Define the user data directory path inside the project
        project_dir = os.path.dirname(os.path.abspath(__file__))
        user_data_dir = os.path.join(project_dir, "..", "..", "user_data")

        # Launch the browser with a persistent context
        browser = await p.chromium.launch_persistent_context(
            user_data_dir, headless=False
        )

        # Set the default timeout for the context
        browser.set_default_timeout(10000)

        # Open a new page
        page = await browser.new_page()

        # Start the input handling thread
        input_thread = threading.Thread(target=handle_input)
        input_thread.start()

        while True:
            if active_script == "login":
                print("Logging in...")
                await login(page)  # Login to Tribal Wars
                print("Logged in.")
                active_script = None
            elif active_script == "start":
                try:
                    user = await get_user_info(page)  # Get the user information
                    await farm_villages(page, user)  # Farm all the villages

                    # await research_weapons()
                except Exception as e:
                    print(f"Error in main loop: {e}")
            elif active_script == "exit":
                print("Exiting...")
                await browser.close()
                return


# Entry point
if __name__ == "__main__":
    loop = asyncio.get_event_loop()  # Get the event loop
    loop.run_until_complete(main())  # Run the main function until it completes
