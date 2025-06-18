from fastmcp import Client
import asyncio

async def run_agent():
    # Connect to the correct endpoint - note the /mcp path
    async with Client("http://localhost:8000/mcp") as client:
        # Initialize and get tools
        tools = await client.list_tools()
        print(f"Available tools: {tools}")
        
        # Call the add tool
        result = await client.call_tool("add", {"a": 3, "b": 5})
        print(f"Add result: {result}")
        
        # Call the multiply tool  
        result2 = await client.call_tool("multiply", {"a": 4, "b": 6})
        print(f"Multiply result: {result2}")
        
        return result

if __name__ == "__main__":
    result = asyncio.run(run_agent())
    print(f"Final result: {result}")