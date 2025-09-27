import json, dataclasses
import pickle
import pandas as pd
import os
import ast
import numpy as np
from enum import Enum
from pathlib import Path
from typing import Any

try:
    from pydantic import BaseModel  # pydantic v2/v1 都可
except Exception:  # 没装也不影响
    class BaseModel:  # type: ignore
        pass
class FileUtil:
    def _to_jsonable(obj: Any):
        if isinstance(obj, BaseModel):
            # pydantic v2/v1 统一处理
            dump = getattr(obj, "model_dump", None) or getattr(obj, "dict", None)
            return dump() if dump else str(obj)
        if dataclasses.is_dataclass(obj):
            return dataclasses.asdict(obj)
        if isinstance(obj, (set, tuple)):
            return list(obj)
        if isinstance(obj, Path):
            return str(obj)
        if isinstance(obj, Enum):
            return obj.value
        if isinstance(obj, bytes):
            return obj.decode("utf-8", "ignore")
        # 兜底交给 str，避免再次抛 TypeError
        try:
            json.dumps(obj)
            return obj
        except TypeError:
            return str(obj)

    def save_data(data: Any, path: str, indent: int = 2, ensure_ascii: bool = False):
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=indent, ensure_ascii=ensure_ascii, default=FileUtil._to_jsonable)

    
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