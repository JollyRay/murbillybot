import asyncio
import logging
import sys

from main.setupbot import setup_bot


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(setup_bot())