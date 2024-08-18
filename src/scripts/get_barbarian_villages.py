from typing import List
from playwright.async_api import Page

# Get the barbarian villages ids
async def get_barbarian_villages(page: Page) -> List[int]:
    try:
        # Get the barbarian villages
        await page.goto(
            "https://www.twstats.com/en141/index.php?page=village_locator&stage=4&source=village&village_coords=332|546&searchstring=&tribe_id=0&filter=abandoned"
        )

        # Get all the links with href containing "index.php?page=village&id="
        links_elements = await page.query_selector_all('a[href*="index.php?page=village&id="]')
        links = await page.evaluate('(elements) => elements.map(element => element.href)', links_elements)
        # TODO: Filter my own villages with a variable
        filtered_links = [link for link in links if "id=47430" not in link] 
        # Extract the last 5 numbers from each link
        village_ids = [int(link.split("id=")[-1][-5:]) for link in filtered_links]
        return village_ids
    except Exception as e:
        print(f"Error while getting barbarian villages: {e}")
        return []
