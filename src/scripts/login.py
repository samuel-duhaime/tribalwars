import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# TODO: Fix the login function
# Login to Tribal Wars
async def login(page):
    try:
        # Navigate to the Tribal Wars login page
        await page.goto("https://www.tribalwars.net/")

        # Fill in the username and password
        username = os.getenv("TW_USERNAME")
        password = os.getenv("TW_PASSWORD")
        await page.fill('input[name="username"]', username)
        await page.fill('input[name="password"]', password)

        # Press the login button
        await page.click('a.btn-login')
        print("Logged in successfully")
    except Exception as e:
        print(f"Error while logging in: {e}")
    finally:
        return