from ..features.buildings.buildings import Buildings

# Simple main function
def main():
    Buildings(47430).save()
    # Buildings(47430).upgrade("Headquarters")
    # Buildings(47430).construct("Headquarters")
    Buildings(47430).get()


# Entry point
if __name__ == "__main__":
    main()  # Run the main function
