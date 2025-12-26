#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
微博热搜爬虫 - 合并结果入口
Weibo Hot Search Crawler - Merge Results Entry Point
"""

from weibo_hot_analyzor.merge_results import merge_crawler_results

if __name__ == "__main__":
    print("=" * 50)
    print("合并爬虫结果")
    print("Merge Crawler Results")
    print("=" * 50 + "\n")
    
    merge_crawler_results()
