#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 导入正则表达式和网络请求库
# Import regex and requests libraries
import re
import requests

# 获取微博热搜关键词列表
# Fetch Weibo hot search keywords list
def fetch_weibo_hot_keywords():
    # 微博热搜榜README的原始链接
    # Raw link to Weibo trending hot search README
    url = "https://raw.githubusercontent.com/justjavac/weibo-trending-hot-search/master/README.md"
    resp = requests.get(url)
    resp.encoding = 'utf-8'
    text = resp.text
    # 找到"今日热门搜索"下的所有内容（包括更新时间和关键词）
    # Find all content under "Today's Hot Searches" (including update time and keywords)
    pattern = r"## 今日热门搜索\n([\s\S]+?)(?:\n## |\Z)"
    match = re.search(pattern, text)
    if not match:
        # 如果没有找到对应段落则报错
        # Raise error if the section is not found
        raise ValueError("未找到今日热门搜索段落\nCould not find the section for today's hot searches.")
    section = match.group(1)
    # 提取更新时间
    # Extract update time
    update_time = None
    update_match = re.search(r"<!--.*?([A-Za-z]{3} \w{3} \d{2} \d{4} [\d:]+) GMT\+0800.*?-->", section)
    if update_match:
        update_time = update_match.group(1)
    # 跳过注释和空行，提取关键词
    # Skip comments and blank lines, extract keywords
    lines = section.strip().split('\n')
    keywords = []
    for line in lines:
        line = line.strip()
        if not line or line.startswith('<!--'):
            continue
        # 匹配形如 1. [关键词](链接) 的行
        # Match lines like: 1. [keyword](link)
        m = re.match(r"\d+\. \[(.+?)\]", line)
        if m:
            kw = m.group(1)
            # 给关键词前后加#号
            # Add # to the beginning and end of the keyword
            keywords.append(f"#{kw}#")
    return keywords, update_time

# 将关键词保存到txt文件
# Save keywords to a txt file
def save_keywords_to_txt(keywords, filename="files/keyword_list.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        for kw in keywords:
            # 每个关键词单独一行写入
            # Write each keyword on a separate line
            f.write(kw + "\n")

# 主程序入口
# Main program entry
if __name__ == "__main__":
    keywords, update_time = fetch_weibo_hot_keywords()
    save_keywords_to_txt(keywords)
    # 打印保存结果和更新时间
    # Print save result and update time
    print(f"已保存 {len(keywords)} 个热搜关键词到 files/keyword_list.txt\nSaved {len(keywords)} hot search keywords to files/keyword_list.txt")
    if update_time:
        print(f"更新时间: {update_time}\nUpdate time: {update_time}")
