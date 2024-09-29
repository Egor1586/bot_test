import asyncio
import logging

import bot_modules as bm

async def main():
    bm.dp.include_router(bm.router)
    await bm.dp.start_polling(bm.bot)
    
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')