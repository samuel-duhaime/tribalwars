# Scripts for Tribalwars

To run this script, you need to start Google Chrome with remote debugging enabled.
```bash
google-chrome --remote-debugging-port=9222
```

Then you can run the script with the following command:
```bash
poetry run python -m src.scripts.main
```

To check the types of the script, you can run the following command:
```bash
poetry run mypy src/scripts
```