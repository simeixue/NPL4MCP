# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/python-notebook-mcp/server.py
# module: server
# qname: server.process_cell_output
# lines: 216-265
def process_cell_output(output: Any) -> Dict:
    """Process a cell output and convert to a readable format."""
    if output.output_type == 'stream':
        return {
            'type': 'stream',
            'name': output.name,
            'text': output.text
        }
    elif output.output_type == 'execute_result':
        result = {
            'type': 'execute_result',
            'execution_count': output.execution_count,
            'data': {}
        }
        
        # Handle text/plain
        if 'text/plain' in output.data:
            result['data']['text/plain'] = output.data['text/plain']
        
        # Handle images
        if 'image/png' in output.data:
            image_data = output.data['image/png']
            result['data']['image/png'] = f"[Base64 encoded image: {len(image_data)} bytes]"
        
        return result
    elif output.output_type == 'display_data':
        result = {
            'type': 'display_data',
            'data': {}
        }
        
        # Handle text/plain
        if 'text/plain' in output.data:
            result['data']['text/plain'] = output.data['text/plain']
        
        # Handle images
        if 'image/png' in output.data:
            image_data = output.data['image/png']
            result['data']['image/png'] = f"[Base64 encoded image: {len(image_data)} bytes]"
        
        return result
    elif output.output_type == 'error':
        return {
            'type': 'error',
            'ename': output.ename,
            'evalue': output.evalue,
            'traceback': output.traceback
        }
    else:
        return {'type': output.output_type, 'data': str(output)}