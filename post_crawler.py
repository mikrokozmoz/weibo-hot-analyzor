#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
微博热搜爬虫 - 爬虫启动入口
Weibo Hot Search Crawler - Post Crawler Entry Point
"""

from weibo_hot_analyzor.post_crawler import (
    init_submodule,
    update_cookie,
    read_keywords,
    update_settings,
    run_crawler
)

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
