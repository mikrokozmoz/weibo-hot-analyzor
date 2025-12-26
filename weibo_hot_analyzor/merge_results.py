#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
合并爬虫结果：将所有话题的CSV文件合并成一个总的CSV文件
Merge crawler results: Combine all topic CSV files into one master CSV file
"""

import os
import sys
import pandas as pd
from pathlib import Path

def merge_crawler_results():
    """合并爬虫结果文件"""
    results_dir = 'weibo-search/结果文件'
    output_dir = 'files'
    
    # 检查结果目录是否存在
    if not os.path.exists(results_dir):
        print(f"❌ 找不到结果目录: {results_dir}")
        print(f"❌ Results directory not found: {results_dir}")
        sys.exit(1)
    
    # 获取所有子文件夹
    folders = [f for f in os.listdir(results_dir) 
               if os.path.isdir(os.path.join(results_dir, f))]
    
    if not folders:
        print(f"⚠️  结果目录为空")
        print(f"⚠️  Results directory is empty")
        sys.exit(1)
    
    print(f"📁 找到 {len(folders)} 个结果文件夹")
    print(f"📁 Found {len(folders)} result folders\n")
    
    dfs = []
    
    for folder in folders:
        # 只删除前后的%23，保留中间的%23（防止数字开头或含有%23的话题被截断）
        keyword = folder.lstrip('%23').rstrip('%23')
        
        # CSV文件路径
        csv_path = os.path.join(results_dir, folder, f"{folder}.csv")
        
        if not os.path.exists(csv_path):
            print(f"⚠️  找不到CSV文件: {csv_path}")
            print(f"⚠️  CSV file not found: {csv_path}")
            continue
        
        try:
            # 读取CSV文件
            df = pd.read_csv(csv_path, encoding='utf-8')
            
            # 添加关键词列
            df['关键词'] = keyword
            
            dfs.append(df)
            print(f"✅ 已读取: {keyword}")
            print(f"✅ Loaded: {keyword} ({len(df)} rows)")
        except Exception as e:
            print(f"❌ 读取失败: {csv_path}")
            print(f"❌ Failed to read: {csv_path} - {e}")
    
    if not dfs:
        print("❌ 没有成功读取任何CSV文件")
        print("❌ No CSV files were successfully read")
        sys.exit(1)
    
    # 合并所有数据框
    print("\n🔗 合并数据中...")
    print("🔗 Merging data...")
    merged_df = pd.concat(dfs, ignore_index=True)
    
    # 保存为CSV
    output_path = os.path.join(output_dir, 'data_raw.csv')
    os.makedirs(output_dir, exist_ok=True)
    
    try:
        merged_df.to_csv(output_path, index=False, encoding='utf-8')
        print(f"\n✅ 数据已保存: {output_path}")
        print(f"✅ Data saved: {output_path}")
        print(f"📊 总共 {len(merged_df)} 条数据，{len(merged_df.columns)} 列")
        print(f"📊 Total {len(merged_df)} rows, {len(merged_df.columns)} columns")
    except Exception as e:
        print(f"❌ 保存失败: {e}")
        print(f"❌ Failed to save: {e}")
        sys.exit(1)

if __name__ == "__main__":
    print("=" * 50)
    print("合并爬虫结果")
    print("Merge Crawler Results")
    print("=" * 50 + "\n")
    
    merge_crawler_results()
