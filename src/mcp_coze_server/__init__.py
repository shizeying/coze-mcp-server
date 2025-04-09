"""
MCP server implementation for Coze API
"""

import asyncio

from .server import CozeServer
from .__main__ import main

def main():
    asyncio.run(mcp.run_stdio_async())

if __name__ == "__main__":
    main()

__version__ = "0.1.3"
__all__ = ["CozeServer", "main"] 