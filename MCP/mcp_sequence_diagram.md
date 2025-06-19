# MCP Server-Client Interaction Flow

This diagram shows the sequence of interactions between the MCP client, server, and AI agent when processing the math question "(3 + 5) x 12?".

```mermaid
sequenceDiagram
    participant User
    participant AI_Agent as AI Agent
    participant MCP_Client as MCP Client
    participant MCP_Server as MCP Server (math_server2.py)
    participant Add_Tool as Add Tool
    participant Multiply_Tool as Multiply Tool

    User->>AI_Agent: "what's (3 + 5) x 12?"
    
    Note over AI_Agent: AI analyzes question and plans tool usage
    
    AI_Agent->>MCP_Client: Request available tools
    MCP_Client->>MCP_Server: list_tools()
    MCP_Server-->>MCP_Client: [add, multiply] tools
    MCP_Client-->>AI_Agent: Available tools response
    
    Note over AI_Agent: AI decides to use add first, then multiply
    
    AI_Agent->>MCP_Client: call_tool("add", {a: 3, b: 5})
    MCP_Client->>MCP_Server: Tool call: add(3, 5)
    MCP_Server->>Add_Tool: Execute add(3, 5)
    Add_Tool-->>MCP_Server: Return: 8
    MCP_Server-->>MCP_Client: ToolMessage(content='8')
    MCP_Client-->>AI_Agent: Tool result: 8
    
    AI_Agent->>MCP_Client: call_tool("multiply", {a: 8, b: 12})
    MCP_Client->>MCP_Server: Tool call: multiply(8, 12)
    MCP_Server->>Multiply_Tool: Execute multiply(8, 12)
    Multiply_Tool-->>MCP_Server: Return: 96
    MCP_Server-->>MCP_Client: ToolMessage(content='96')
    MCP_Client-->>AI_Agent: Tool result: 96
    
    Note over AI_Agent: AI formats final response
    
    AI_Agent-->>User: "The result of (3 + 5) × 12 is 96."

    rect rgb(240, 248, 255)
        Note over User, Multiply_Tool: Key Components from sample_output.txt:
        Note over User, Multiply_Tool: • HumanMessage: Original question
        Note over User, Multiply_Tool: • AIMessage with tool_calls: Planning phase
        Note over User, Multiply_Tool: • ToolMessage(8): First calculation result  
        Note over User, Multiply_Tool: • ToolMessage(96): Second calculation result
        Note over User, Multiply_Tool: • Final AIMessage: Formatted answer
    end
```

## Flow Explanation

1. **User Query**: User asks a compound math question
2. **Tool Discovery**: AI agent discovers available math tools via MCP
3. **Sequential Execution**: 
   - First: `add(3, 5)` → returns `8`
   - Second: `multiply(8, 12)` → returns `96`
4. **Response Formation**: AI formats the final answer with proper mathematical notation

## Message Types in sample_output.txt

- **HumanMessage**: The original user question
- **AIMessage (with tool_calls)**: AI's plan to use specific tools
- **ToolMessage**: Results from each tool execution
- **Final AIMessage**: The formatted response to the user

The MCP server enables the AI to break down complex mathematical expressions into sequential tool calls, demonstrating proper order of operations.
