from fastmcp import FastMCP

mcp = FastMCP("Math")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b

if __name__ == "__main__":
    print("Starting Math MCP server...")
    print("Server will be available at http://localhost:8000/mcp")
    mcp.run(transport="streamable-http", host="localhost", port=8000)