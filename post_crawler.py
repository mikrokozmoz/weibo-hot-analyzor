#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
后爬虫程序：自动初始化submodule、读取关键词、修改配置、运行爬虫
Post-crawler program: Auto initialize submodule, read keywords, modify config, run crawler
"""

import subprocess
import os
import sys
import re

def init_submodule():
    """自动初始化submodule（如果还未初始化）"""
    crawler_path = 'weibo-search'
    
    if not os.path.exists(os.path.join(crawler_path, '.git')):
        print("📥 初始化爬虫模块...")
        print("📥 Initializing crawler module...")
        try:
            subprocess.run(['git', 'submodule', 'update', '--init', '--recursive'], check=True)
            print("✅ 爬虫模块初始化成功")
            print("✅ Crawler module initialized successfully")
        except Exception as e:
            print(f"❌ 初始化失败: {e}")
            print(f"❌ Initialization failed: {e}")
            sys.exit(1)
    else:
        print("✅ 爬虫模块已就绪")
        print("✅ Crawler module is ready")

def read_keywords():
    """读取keyword_list.txt中的关键词"""
    keyword_file = 'files/keyword_list.txt'
    try:
        with open(keyword_file, 'r', encoding='utf-8') as f:
            keywords = [line.strip() for line in f if line.strip()]
        if keywords:
            print(f"📖 读取到 {len(keywords)} 个关键词: {keywords}")
            print(f"📖 Read {len(keywords)} keywords: {keywords}")
            return keywords
        else:
            print(f"⚠️  {keyword_file} 为空")
            print(f"⚠️  {keyword_file} is empty")
            return []
    except FileNotFoundError:
        print(f"❌ 找不到文件: {keyword_file}")
        print(f"❌ File not found: {keyword_file}")
        sys.exit(1)

def update_settings(keywords):
    """更新weibo-search的settings.py中的KEYWORD_LIST"""
    settings_path = 'weibo-search/weibo/settings.py'
    
    if not os.path.exists(settings_path):
        print(f"❌ 找不到: {settings_path}")
        print(f"❌ Not found: {settings_path}")
        sys.exit(1)
    
    try:
        with open(settings_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 用正则表达式替换KEYWORD_LIST的值
        # 格式: KEYWORD_LIST = [...] 或 KEYWORD_LIST = 'xxx.txt'
        keywords_str = repr(keywords)  # 转为Python字符串格式
        new_content = re.sub(
            r"KEYWORD_LIST\s*=\s*.*(?=\n)",
            f"KEYWORD_LIST = {keywords_str}",
            content
        )
        
        with open(settings_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"✏️  已更新 {settings_path} 中的 KEYWORD_LIST")
        print(f"✏️  Updated KEYWORD_LIST in {settings_path}")
    except Exception as e:
        print(f"❌ 更新设置失败: {e}")
        print(f"❌ Failed to update settings: {e}")
        sys.exit(1)

def update_cookie():
    """更新爬虫的Cookie"""
    settings_path = 'weibo-search/weibo/settings.py'
    
    print("\n" + "=" * 50)
    print("🍪 Cookie 配置")
    print("🍪 Cookie Configuration")
    print("=" * 50)
    print("请输入你的微博Cookie（从浏览器开发者工具中复制）")
    print("Please enter your Weibo Cookie (copy from browser developer tools)")
    print("按 Enter 使用默认值 / Press Enter to use default value")
    
    cookie_input = input("Cookie: ").strip()
    
    if cookie_input:
        try:
            with open(settings_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 替换cookie值
            new_content = re.sub(
                r"'cookie':\s*'[^']*'",
                f"'cookie': '{cookie_input}'",
                content
            )
            
            with open(settings_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print("✅ Cookie 已更新")
            print("✅ Cookie updated")
        except Exception as e:
            print(f"❌ 更新Cookie失败: {e}")
            print(f"❌ Failed to update cookie: {e}")
            sys.exit(1)
    else:
        print("⏭️  使用默认值")
        print("⏭️  Using default value")

def run_crawler():
    """运行爬虫，支持断点续传"""
    print("\n🚀 启动爬虫...")
    print("\n🚀 Starting crawler...")
    try:
        os.chdir('weibo-search')
        # 使用scrapy爬虫，支持JOBDIR实现断点续传
        subprocess.run([
            'scrapy', 'crawl', 'search', 
            '-s', 'JOBDIR=crawls/search'
        ], check=True)
        os.chdir('..')
        print("\n✅ 爬虫完成！")
        print("\n✅ Crawler completed!")
    except Exception as e:
        print(f"❌ 爬虫运行失败: {e}")
        print(f"❌ Crawler execution failed: {e}")
        os.chdir('..')
        sys.exit(1)

if __name__ == "__main__":
    print("=" * 50)
    print("微博热搜爬虫 - 自动启动程序")
    print("Weibo Trending Crawler - Auto Launcher")
    print("=" * 50)
    
    init_submodule()
    update_cookie()  # 先更新Cookie
    keywords = read_keywords()
    
    if keywords:
        update_settings(keywords)
        run_crawler()
    else:
        print("⚠️  没有关键词，退出程序")
        print("⚠️  No keywords found, exiting program")
