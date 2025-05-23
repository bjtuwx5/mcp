class MCP:
    def __init__(self):
        self.tools = []

    def tool(self):
        def decorator(func):
            # 调用 add_tool 方法将函数添加到工具列表中
            self.add_tool(func)
            return func
        return decorator

    def add_tool(self, func):
        self.tools.append(func)
        print(f"Tool {func.__name__} added.")


# 创建 MCP 实例
mcp = MCP()


@mcp.tool()
def my_tool():
    print("This is my tool.")


# 调用 my_tool
my_tool()

# 查看工具列表
print(mcp.tools)