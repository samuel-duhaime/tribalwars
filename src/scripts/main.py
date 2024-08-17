import asyncio
import os
from playwright.async_api import async_playwright
from login import login
from construct_buildings import construct_buildings
from recruit_troops import recruit_troops
from attack_villages import attack_villages

# To run this script, you need to start Google Chrome with remote debugging enabled.
# google-chrome --remote-debugging-port=9222

# TODO: Get the user information
async def get_user_info():
    while True:
        try:
            print("Getting user information... every 10 seconds")
            await asyncio.sleep(10)
        except Exception as e:
            print(f"Error while getting user information: {e}")
            break


# Main function
async def main():
    async with async_playwright() as p:
        # Define the user data directory path inside the project
        project_dir = os.path.dirname(os.path.abspath(__file__))
        user_data_dir = os.path.join(project_dir, "..", "..", "user_data")

        # Launch the browser with a persistent context
        browser = await p.chromium.launch_persistent_context(
            user_data_dir, headless=False
        )

        # Open a new page
        page = await browser.new_page()

        # Loop automatically
        # loop = asyncio.get_event_loop()
        # loop.run_until_complete(get_user_info())
        # loop.run_forever()

        while True:
            # Dictionary to store building commands
            scripts_commands = {
                "login": "Login",
                "info": "Get user information",
                "construct": "Construct buildings",
                "recruit": "Recruit troops",
                "attack": "Attack villages",
                "exit": "Exit the scripts",
            }
            print(f"\nScripts commands are:\n")
            for command, description in scripts_commands.items():
                print(f"{command}: {description}")
            choice = input("\nEnter your choice: ")

            if choice == "login":
                # Login to Tribal Wars
                await login(page)
            elif choice == "info":
                # Get the user information
                await get_user_info()
            elif choice == "construct":
                # Construct the buildings
                await construct_buildings(page)
            elif choice == "recruit":
                # Recruit all the troops
                await recruit_troops(page)
            elif choice == "attack":
                # Attack all the villages
                await attack_villages(page)
            elif choice == "exit":  # Escape key
                print("Exiting scripts mode...")
                await browser.close()
                break
            else:
                print("Invalid choice. Please try again.")


# Entry point
if __name__ == "__main__":
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(get_user_info())
    # loop.run_forever()
    asyncio.run(main())
