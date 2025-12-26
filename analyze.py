#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
微博热搜爬虫 - 数据分析入口
Weibo Hot Search Crawler - Data Analysis Entry Point
"""

from weibo_hot_analyzor.analyze import (
    init_processing_submodule,
    load_data,
    deduplicate_data,
    analyze_data
)
import sys
import argparse

if __name__ == "__main__":
    # 解析命令行参数
    parser = argparse.ArgumentParser(
        description='微博数据分析工具 / Weibo Data Analysis Tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例 / Examples:
  python analyze.py --dedup         # 去重数据
  python analyze.py --help          # 查看帮助
        """
    )
    
    parser.add_argument('--dedup', action='store_true', 
                       help='去重原始数据并保存为 data_deduped.csv')
    
    args = parser.parse_args()
    
    print("=" * 50)
    print("微博数据分析 - 自动启动程序")
    print("Weibo Data Analysis - Auto Launcher")
    print("=" * 50 + "\n")
    
    # 初始化submodule
    init_processing_submodule()
    
    # 根据命令行参数执行不同的操作
    if args.dedup:
        print()
        df = load_data()
        print()
        deduplicate_data(df)
    else:
        print("\n⚠️  请指定操作参数")
        print("⚠️  Please specify an operation parameter")
        print("\n可用的操作 / Available operations:")
        print("  --dedup          去重数据 (Deduplicate data)")
        print("\n使用 --help 查看更多帮助 / Use --help for more information")
