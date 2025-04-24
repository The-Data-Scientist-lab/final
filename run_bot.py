import os
import sys
import asyncio
from bot import client
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

async def main():
    try:
        logger.info("Starting the bot...")
        await client.start()
        logger.info("Bot started successfully!")
        await client.run_until_disconnected()
    except Exception as e:
        logger.error(f"Error occurred: {str(e)}")
        # Wait for 5 seconds before restarting
        await asyncio.sleep(5)
        # Restart the script
        os.execv(sys.executable, ['python'] + sys.argv)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Bot stopped by user")
    except Exception as e:
        logger.error(f"Fatal error: {str(e)}")
        # Wait for 5 seconds before restarting
        asyncio.run(asyncio.sleep(5))
        # Restart the script
        os.execv(sys.executable, ['python'] + sys.argv) 