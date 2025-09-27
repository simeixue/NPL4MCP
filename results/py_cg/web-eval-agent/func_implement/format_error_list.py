# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/web-eval-agent/webEvalAgent/src/tool_handlers.py
# module: webEvalAgent.src.tool_handlers
# qname: webEvalAgent.src.tool_handlers.format_agent_result.format_error_list
# lines: 226-260
    def format_error_list(items, item_formatter):
        """Format a list of error items with character limit.
        
        Args:
            items: List of error items to format
            item_formatter: Function that takes (index, item) and returns a formatted string
            
        Returns:
            str: Formatted error list with potential truncation
        """
        if not items:
            return " No items found.\n"
            
        result = f" ({len(items)} items)\n"
        
        # Combine all items with line breaks
        all_items_text = ""
        for i, item in enumerate(items):
            item_line = item_formatter(i, item)
            all_items_text += item_line
            
        # Truncate if necessary and add indicator
        if len(all_items_text) > MAX_ERROR_OUTPUT_CHARS:
            truncated_text = all_items_text[:MAX_ERROR_OUTPUT_CHARS]
            # Try to end at a newline if possible
            last_newline = truncated_text.rfind('\n')
            if last_newline > MAX_ERROR_OUTPUT_CHARS * 0.9:  # Only if we're not losing too much
                truncated_text = truncated_text[:last_newline+1]
                
            result += truncated_text
            result += f"  ... [Output truncated, {len(all_items_text) - len(truncated_text)} more characters not shown]\n"
        else:
            result += all_items_text
            
        return result