#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
微博热搜爬虫 - 获取关键词入口
Weibo Hot Search Crawler - Fetch Keywords Entry Point
"""

from weibo_hot_analyzor.fetch_keywords import fetch_weibo_hot_keywords, save_keywords_to_txt

if __name__ == "__main__":
    keywords, update_time = fetch_weibo_hot_keywords()
    save_keywords_to_txt(keywords)
    print(f"已保存 {len(keywords)} 个热搜关键词到 files/keyword_list.txt\nSaved {len(keywords)} hot search keywords to files/keyword_list.txt")
    if update_time:
        print(f"更新时间: {update_time}\nUpdate time: {update_time}")
