import asyncio
import logging
import os
from aiohttp import web
from bot import bot

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

async def health_check(request):
    return web.Response(text="OK")

async def start_bot():
    try:
        await bot.start()
        logger.info("Bot started successfully")
        await bot.run_until_disconnected()
    except Exception as e:
        logger.error(f"Error in bot: {e}")
        raise

async def main():
    # Create web application
    app = web.Application()
    app.router.add_get('/health', health_check)
    
    # Get port from environment variable or use default
    port = int(os.environ.get('PORT', 8080))
    
    # Start web server
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()
    logger.info(f"Web server started on port {port}")
    
    # Start bot in the background
    bot_task = asyncio.create_task(start_bot())
    
    try:
        # Keep the server running
        while True:
            await asyncio.sleep(3600)  # Sleep for 1 hour
    except asyncio.CancelledError:
        logger.info("Shutting down...")
        await bot.disconnect()
        await runner.cleanup()
    except Exception as e:
        logger.error(f"Fatal error: {e}")
        await bot.disconnect()
        await runner.cleanup()
        raise

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Bot stopped by user")
    except Exception as e:
        logger.error(f"Fatal error: {e}")
        raise 