import sys
import os
import asyncio

# 👇 Добавляем путь к корню проекта в sys.path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from bot.main import main

if __name__ == "__main__":
    asyncio.run(main())
