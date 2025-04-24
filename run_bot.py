import asyncio
import logging
import os
from aiohttp import web
from bot import client

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
        await client.start()
        logger.info("Bot started successfully")
        return client
    except Exception as e:
        logger.error(f"Error in bot: {e}")
        raise

async def main():
    # Start bot first
    bot = await start_bot()
    
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
    
    try:
        # Run both bot and web server
        await asyncio.gather(
            bot.run_until_disconnected(),
            asyncio.sleep(float('inf'))  # Keep the web server running
        )
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