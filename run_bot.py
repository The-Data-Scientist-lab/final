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
        sys.exit(1)

if __name__ == '__main__':
    try:
        # Use uvloop if available for better performance
        try:
            import uvloop
            uvloop.install()
        except ImportError:
            pass
            
        # Run the bot
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Bot stopped by user")
    except Exception as e:
        logger.error(f"Fatal error: {str(e)}")
        sys.exit(1) 