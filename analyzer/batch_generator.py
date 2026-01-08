"""
批量生成百炼大模型推理任务 JSON 文件
Generate batch inference JSON file for Alibaba Qwen API
"""

import pandas as pd
import json
from . import settings


def generate_batch_file(post_list_file=None,
                       prompt_file='analyzer/prompts/labeling_prompt.txt',
                       output_file='analyzer/data/batch_generated.jsonl',
                       model_name=None):
    """
    从 post_list.csv 生成百炼批量推理 JSON 文件
    Generate batch inference JSON file from post_list.csv for Alibaba Qwen API
    
    参数 Parameters:
    - post_list_file: 输入的微博列表 CSV 文件（默认从 settings.py 读取）/ Input post list CSV file (defaults from settings.py)
    - prompt_file: 标注 prompt 文件路径 / Path to labeling prompt file
    - output_file: 输出的 JSONL 文件 / Output batch file path
    - model_name: 模型名称（默认从 settings.py 读取）/ Model name (defaults from settings.py)
    """
    
    if post_list_file is None:
        post_list_file = settings.TEST_POST_LIST
    if model_name is None:
        model_name = settings.MODEL_NAME
    
    try:
        # 读取 CSV 文件 / Read CSV file
        df = pd.read_csv(post_list_file, header=0)
        
        # 自动处理列名 / Auto-handle column names
        if len(df.columns) >= 2:
            id_col = df.columns[0]
            content_col = df.columns[1]
        else:
            raise ValueError("CSV 文件必须至少有两列 / CSV file must have at least 2 columns")
        
        # 读取 prompt 文件 / Read prompt file
        with open(prompt_file, 'r', encoding='utf-8') as f:
            system_prompt = f.read()
        
        # 生成批量推理文件 / Generate batch inference file
        with open(output_file, 'w', encoding='utf-8', newline='') as f:
            for idx, (_, row) in enumerate(df.iterrows(), 1):
                post_id = str(row[id_col])
                content = str(row[content_col])
                
                # 构建 API 请求体 / Build API request body
                request_body = {
                    "model": model_name,
                    "messages": [
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": f"请对以下微博进行打标：\n{content}"}
                    ]
                }
                
                # 构建完整请求对象 / Build complete request object
                request_obj = {
                    "custom_id": f"request-{idx}",
                    "method": "POST",
                    "url": "/v1/chat/completions",
                    "body": request_body
                }
                
                # 写入 JSONL 格式（每行一个 JSON）/ Write in JSONL format (one JSON per line)
                f.write(json.dumps(request_obj, ensure_ascii=False) + '\n')
        
        print(f"✓ 已生成 {len(df)} 条批量推理请求")
        print(f"✓ Generated {len(df)} batch inference requests")
        print(f"✓ 文件保存到 / File saved to: {output_file}")
        return True
    
    except Exception as e:
        print(f"✗ 生成失败 / Generation failed: {e}")
        print(f"✗ {e}")
        return False


if __name__ == '__main__':
    # 示例使用 / Example usage
    print("正在生成批量推理文件...")
    generate_batch_file()
