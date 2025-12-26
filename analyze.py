#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
数据分析主程序：自动初始化processing submodule，加载合并数据，进行分析
Data analysis main program: Auto initialize processing submodule, load merged data, perform analysis
"""

import subprocess
import os
import sys
import argparse
import pandas as pd

def init_processing_submodule():
    """自动初始化processing submodule（如果还未初始化）"""
    processing_path = 'processing'
    
    if not os.path.exists(os.path.join(processing_path, '.git')):
        print("📥 初始化数据处理模块...")
        print("📥 Initializing data processing module...")
        try:
            subprocess.run(['git', 'submodule', 'update', '--init', '--recursive'], check=True)
            print("✅ 数据处理模块初始化成功")
            print("✅ Data processing module initialized successfully")
        except Exception as e:
            print(f"❌ 初始化失败: {e}")
            print(f"❌ Initialization failed: {e}")
            sys.exit(1)
    else:
        print("✅ 数据处理模块已就绪")
        print("✅ Data processing module is ready")

def load_data():
    """加载合并后的原始数据"""
    data_path = 'files/data_raw.csv'
    
    if not os.path.exists(data_path):
        print(f"❌ 找不到数据文件: {data_path}")
        print(f"❌ Data file not found: {data_path}")
        print("⚠️  请先运行 merge_results.py 来合并爬虫结果")
        print("⚠️  Please run merge_results.py first to merge crawler results")
        sys.exit(1)
    
    try:
        import pandas as pd
        df = pd.read_csv(data_path, encoding='utf-8')
        print(f"✅ 已加载数据: {data_path}")
        print(f"✅ Data loaded: {data_path}")
        print(f"📊 数据规模: {len(df)} 行, {len(df.columns)} 列")
        print(f"📊 Data shape: {len(df)} rows, {len(df.columns)} columns")
        return df
    except Exception as e:
        print(f"❌ 加载数据失败: {e}")
        print(f"❌ Failed to load data: {e}")
        sys.exit(1)

def deduplicate_data(df):
    """去重数据"""
    try:
        from processing.post_analysis import pre_processing
        
        print("\n" + "=" * 50)
        print("开始去重数据...")
        print("Starting data deduplication...")
        print("=" * 50)
        
        # 获取相似度阈值
        print("\n🎚️  设置相似度阈值 / Set similarity threshold")
        print("=" * 50)
        print("相似度阈值说明:")
        print("Similarity threshold explanation:")
        print("  - 阈值越高，去重越严格（只有极其相似的才会被去重）")
        print("    Higher threshold = stricter dedup (only very similar posts removed)")
        print("  - 阈值越低，去重越宽松（相似程度较低的也会被去重）")
        print("    Lower threshold = looser dedup (more posts removed)")
        print("  - 推荐范围: 0.75 - 0.95")
        print("    Recommended range: 0.75 - 0.95")
        print("  - 默认值: 0.88")
        print("    Default value: 0.88")
        print("\n💡 使用默认值: 直接按回车键 (Enter)")
        print("💡 Use default value: Just press Enter")
        print("=" * 50)
        
        while True:
            try:
                threshold_input = input("\n请输入相似度阈值 (0-1) / Enter similarity threshold (0-1) [默认 0.88]: ").strip()
                
                # 如果为空，使用默认值
                if not threshold_input:
                    similarity_threshold = 0.88
                    print(f"✅ 使用默认值: {similarity_threshold}")
                    print(f"✅ Using default value: {similarity_threshold}")
                    break
                
                # 尝试转换为浮点数
                similarity_threshold = float(threshold_input)
                
                # 检查是否在0到1之间
                if 0 <= similarity_threshold <= 1:
                    print(f"✅ 已设置阈值: {similarity_threshold}")
                    print(f"✅ Threshold set: {similarity_threshold}")
                    break
                else:
                    print("❌ 输入错误，请输入0到1之间的数值")
                    print("❌ Invalid input, please enter a value between 0 and 1")
            except ValueError:
                print("❌ 输入错误，请输入有效的数值")
                print("❌ Invalid input, please enter a valid number")
        
        # 调用dedupe_posts函数
        df_deduped = pre_processing.dedupe_posts(df, similarity_threshold=similarity_threshold)
        
        # 保存去重后的数据
        output_dir = 'files'
        os.makedirs(output_dir, exist_ok=True)  # 确保files目录存在
        output_path = os.path.join(output_dir, 'data_deduped.csv')
        df_deduped.to_csv(output_path, index=False, encoding='utf-8')
        
        print(f"\n✅ 去重完成!")
        print(f"✅ Deduplication completed!")
        print(f"📊 原始数据: {len(df)} 行")
        print(f"📊 Original data: {len(df)} rows")
        print(f"📊 去重后: {len(df_deduped)} 行 (移除 {len(df) - len(df_deduped)} 条重复)")
        print(f"📊 After dedup: {len(df_deduped)} rows (removed {len(df) - len(df_deduped)} duplicates)")
        print(f"📁 已保存到: {output_path}")
        print(f"📁 Saved to: {output_path}")
        
        return df_deduped
    except Exception as e:
        print(f"❌ 去重失败: {e}")
        print(f"❌ Deduplication failed: {e}")
        sys.exit(1)

def analyze_data(df):
    """
    使用processing模块进行数据分析
    
    目前支持的功能：
    - 文本预处理（清洗、分词等）
    - 语料分析（词频统计、词云等）
    """
    try:
        # 导入processing模块
        from processing.post_analysis import pre_processing, corpus_analysis
        
        print("\n" + "=" * 50)
        print("开始数据分析...")
        print("Starting data analysis...")
        print("=" * 50)
        
        # 这里可以根据需要调用processing模块中的各个函数
        # 例如：
        # df['cleaned_text'] = df['内容'].apply(corpus_analysis.clean_text)
        # freq_stats = corpus_analysis.word_frequency_analysis(df['cleaned_text'])
        
        print("\n💡 可用的处理函数：")
        print("💡 Available processing functions:")
        print("  - corpus_analysis.clean_text() - 文本清洗")
        print("  - corpus_analysis.word_segmentation() - 分词")
        print("  - corpus_analysis.word_frequency_analysis() - 词频分析")
        print("  - pre_processing.load_posts_from_folder() - 加载文件夹中的CSV文件")
        
        return df
    except ImportError as e:
        print(f"❌ 导入processing模块失败: {e}")
        print(f"❌ Failed to import processing module: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ 数据分析失败: {e}")
        print(f"❌ Data analysis failed: {e}")
        sys.exit(1)

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
