# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/python-notebook-mcp/server.py
# module: server
# qname: server.notebook_to_dict
# lines: 126-174
def notebook_to_dict(nb) -> Dict:
    """Convert notebook object to a safe dictionary representation."""
    result = {
        "cells": [],
        "metadata": dict(nb.metadata),
        "nbformat": nb.nbformat,
        "nbformat_minor": nb.nbformat_minor
    }
    
    for cell in nb.cells:
        cell_dict = {
            "cell_type": cell.cell_type,
            "source": cell.source,
            "metadata": dict(cell.metadata)
        }
        
        if cell.cell_type == 'code':
            cell_dict["execution_count"] = cell.execution_count
            cell_dict["outputs"] = []
            
            if hasattr(cell, 'outputs'):
                for output in cell.outputs:
                    output_dict = {"output_type": output.output_type}
                    
                    if output.output_type == 'stream':
                        output_dict["name"] = output.name
                        output_dict["text"] = output.text
                    elif output.output_type in ('execute_result', 'display_data'):
                        output_dict["data"] = {}
                        if hasattr(output, 'data'):
                            for key, value in output.data.items():
                                if key == 'image/png':
                                    output_dict["data"][key] = f"[Base64 encoded image: {len(value)} bytes]"
                                else:
                                    output_dict["data"][key] = value
                        if hasattr(output, 'metadata'):
                            output_dict["metadata"] = dict(output.metadata)
                        if hasattr(output, 'execution_count') and output.output_type == 'execute_result':
                            output_dict["execution_count"] = output.execution_count
                    elif output.output_type == 'error':
                        output_dict["ename"] = output.ename
                        output_dict["evalue"] = output.evalue
                        output_dict["traceback"] = output.traceback
                    
                    cell_dict["outputs"].append(output_dict)
        
        result["cells"].append(cell_dict)
    
    return result