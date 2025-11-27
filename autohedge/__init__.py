# Load environment variables before any imports
from dotenv import load_dotenv
load_dotenv()

from autohedge.main import AutoHedge

__all__ = ["AutoHedge"]
