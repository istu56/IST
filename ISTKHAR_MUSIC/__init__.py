# __init__.py
import asyncio
import logging as pylogging

# Logger setup
LOGGER = pylogging.getLogger("ISTKHAR_MUSIC")
LOGGER.setLevel(pylogging.INFO)
console = pylogging.StreamHandler()
formatter = pylogging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
console.setFormatter(formatter)
LOGGER.addHandler(console)

LOGGER_ID = -1001234567890  # apna log chat ID

# Optional functions
try:
    from .core.dir import update_dirs
    update_dirs()
    LOGGER.info("Directories updated.")
except ImportError:
    LOGGER.warning("update_dirs function not found, skipping.")
except Exception as e:
    LOGGER.error(f"Error updating dirs: {e}")

try:
    from .core.git import check_git
    check_git()
    LOGGER.info("Git client found.")
except ImportError:
    LOGGER.warning("check_git function not found, skipping.")
except Exception as e:
    LOGGER.error(f"Error in git check: {e}")

try:
    from .misc import load_database
    load_database()
    LOGGER.info("Database loaded.")
except ImportError:
    LOGGER.warning("load_database function not found, skipping.")
except Exception as e:
    LOGGER.error(f"Error loading database: {e}")

def start_userbots():
    try:
        from .userbot import start as run_userbots
        asyncio.run(run_userbots(log_chat_id=LOGGER_ID))
    except ImportError:
        LOGGER.error("run_userbots function not found.")
    except Exception as e:
        LOGGER.error(f"Error running userbots: {e}")

start_userbots()