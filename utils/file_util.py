import json
import pickle
import pandas as pd
import os
import ast
import numpy as np

class FileUtil:
    # 写入data
    def save_data(data, path,indent=None, ensure_ascii=False):
        with open(path, 'w', encoding='utf-8') as file:
            if type(data) is not str:
                data = json.dumps(data,indent=indent, ensure_ascii=ensure_ascii)
            file.write(data)

    
    # 读取data
    def load_data(path, silent=False):
        if not os.path.exists(path):
            if silent:
                return None
            raise FileNotFoundError(f"[load_data] File not found: {path}")

        with open(path, 'r', encoding='utf-8') as file:
            content = file.read()
            try:
                return json.loads(content)  # 尝试当作 JSON 解析
            except json.JSONDecodeError:
                return content  # 不是 JSON 就原样返回字符串