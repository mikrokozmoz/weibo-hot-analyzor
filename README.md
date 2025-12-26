# 微博热搜分析工具 | Weibo Hot Search Analyzer

一个用于爬取微博实时热搜话题、合并结果数据、进行数据分析和处理的完整工具链。

*A complete toolkit for crawling Weibo real-time trending topics, merging result data, and performing data analysis and processing.*

> 🔗 **基础爬虫库** | **Base Crawler Library**  
> 本项目基于 [weibo-search](https://github.com/dataabc/weibo-search) 项目，并使用了经过修改的fork版本 [weibo-search (fork)](https://github.com/mikrokozmoz/weibo-search) 作为爬虫引擎。
> 
> *This project is based on the [weibo-search](https://github.com/dataabc/weibo-search) project, and uses a modified fork version [weibo-search (fork)](https://github.com/mikrokozmoz/weibo-search) as the crawler engine.*

## 项目简介 | Project Overview

本项目将微博热搜话题爬取、数据聚合、数据清洗和分析整合为一个自动化工作流。通过简单的命令行脚本，用户可以快速获取微博热搜数据并进行深入分析。

*This project integrates Weibo trending topic crawling, data aggregation, data cleaning, and analysis into an automated workflow. Through simple command-line scripts, users can quickly obtain Weibo trending data and perform in-depth analysis.*

## 功能特性 | Features

- **简单配置** ⚙️：支持输入Cookie
- **智能合并** 📊：自动合并所有话题的爬虫结果为统一数据集
- **数据去重** ✨：支持自定义相似度阈值的智能去重

<br>

- **Easy Configuration** ⚙️: *Support for entering Cookie and custom keyword lists*
- **Smart Merging** 📊: *Automatically merge crawler results from all topics into a unified dataset*
- **Data Deduplication** ✨: *Support smart deduplication with custom similarity threshold*


## 快速上手 | Quick Start

### 1. 安装和环境配置 | Installation & Setup

```bash
# 克隆项目
# Clone the project
git clone https://github.com/mikrokozmoz/weibo-hot-analyzor
cd weibo-hot-analyzor

# 安装依赖（一键安装）
# Install all dependencies at once
pip install -r requirements.txt
```

### 2. 获取热搜关键词 | Fetch Keywords

```bash
# 自动获取微博当日热搜话题，保存到 files/keyword_list.txt
# Automatically fetch Weibo trending topics and save to files/keyword_list.txt
python -m weibo_hot_analyzor.fetch_keywords
```

**数据源** | *Data Source*：  
本脚本从 [justjavac/weibo-trending-hot-search](https://github.com/justjavac/weibo-trending-hot-search) 项目获取每日更新的微博热搜数据，该项目每小时自动更新一次微博热搜排行榜。

*This script fetches daily updated Weibo trending data from the [justjavac/weibo-trending-hot-search](https://github.com/justjavac/weibo-trending-hot-search) project, which automatically updates the Weibo trending list every hour.*

### 3. 启动爬虫爬取数据 | Start Crawler

```bash
# 启动爬虫脚本
# Start the crawler script
python -m weibo_hot_analyzor.post_crawler

# 按提示输入你的微博Cookie（从浏览器开发者工具获取）
# Enter your Weibo Cookie as prompted (obtain from browser developer tools)
```

**注意** | *Note*：
- 爬虫会在 `weibo-search/结果文件/` 目录下为每个关键词创建文件夹
- 支持断点续传：如果爬虫中途中断，重新运行会继续从断点开始

<br>

- *The crawler will create a folder for each keyword in `weibo-search/结果文件/`*
- *Supports breakpoint resume: if the crawler is interrupted, re-running will continue from the breakpoint*

### 4. 合并爬虫结果 | Merge Results

```bash
# 将所有话题的CSV文件合并成一个，自动添加"关键词"列
# Merge all topic CSV files into one, automatically add "keyword" column
python -m weibo_hot_analyzor.merge_results
```

输出文件：`files/data_raw.csv`  
*Output file: `files/data_raw.csv`*

### 5. 数据去重 | Deduplication

```bash
# 启动数据去重脚本
# Start data deduplication script
python -m weibo_hot_analyzor.analyze --dedup

# 按提示输入相似度阈值（0-1）
# 推荐值: 0.75-0.95，默认值: 0.88
# Enter similarity threshold (0-1) as prompted
# Recommended: 0.75-0.95, Default: 0.88
```

输出文件：`files/data_deduped.csv`  
*Output file: `files/data_deduped.csv`*

## 关键词说明 | Configuration Details

### 相似度阈值 | Similarity Threshold

在去重过程中，相似度阈值控制去重的严格程度：

*During deduplication, the similarity threshold controls the strictness of deduplication:*

| 阈值范围 | 说明 | 建议场景 |
|---------|------|--------|
| 0.70-0.80 | 宽松去重，移除更多重复 | 需要高质量唯一内容的分析 |
| 0.80-0.90 | 平衡去重，推荐使用 | 一般数据分析 |
| 0.90-0.99 | 严格去重，移除较少重复 | 保留细微差异内容 |

| Threshold Range | Description | Recommended Scenario |
|---------|------|--------|
| 0.70-0.80 | Loose dedup, remove more duplicates | Analysis requiring high-quality unique content |
| 0.80-0.90 | Balanced dedup, recommended | General data analysis |
| 0.90-0.99 | Strict dedup, remove fewer duplicates | Preserve subtle differences in content |

## 依赖项 | Dependencies

### 主要库 | Main Libraries

- **Python 3.7+**
- **pandas** - 数据处理 / Data processing
- **scrapy** - 网络爬虫框架 / Web scraping framework
- **jieba** - 中文分词 / Chinese word segmentation
- **wordcloud** - 词云生成 / Word cloud generation
- **matplotlib** - 数据可视化 / Data visualization
- **requests** - HTTP请求 / HTTP requests

### Submodule依赖 | Submodule Dependencies

本项目集成了两个重要的submodule：

*This project integrates two important submodules:*

- **[weibo-search](https://github.com/mikrokozmoz/weibo-search)** - 微博爬虫框架 / Weibo crawler framework
- **[weibo-posts-processing](https://github.com/mikrokozmoz/weibo-posts-processing)** - 微博数据处理库 / Weibo data processing library

Submodule会在脚本首次运行时自动初始化，无需手动操作。

*Submodules will be automatically initialized when the script runs for the first time, no manual operation required.*

## 文件说明 | File Descriptions

| 模块 | 说明 | 使用场景 |
|------|------|--------|
| `weibo_hot_analyzor.fetch_keywords` | 获取微博实时热搜话题 | 定期更新关键词列表 |
| `weibo_hot_analyzor.post_crawler` | 爬虫启动脚本，自动初始化weibo-search模块 | 日常爬取数据 |
| `weibo_hot_analyzor.merge_results` | 合并爬虫结果为统一数据集 | 爬虫完成后处理结果 |
| `weibo_hot_analyzor.analyze` | 数据分析脚本，支持去重等操作 | 数据清洗和初步分析 |

| Module | Description | Use Case |
|------|------|--------|
| `weibo_hot_analyzor.fetch_keywords` | Fetch Weibo real-time trending topics | Regularly update keyword list |
| `weibo_hot_analyzor.post_crawler` | Crawler startup script, auto-initialize weibo-search module | Daily data crawling |
| `weibo_hot_analyzor.merge_results` | Merge crawler results into unified dataset | Process results after crawling |
| `weibo_hot_analyzor.analyze` | Data analysis script, support deduplication operations | Data cleaning and initial analysis |

## 工作流程 | Workflow

```
┌──────────────────────────────────────────────────────────────────────┐
│ 1. python -m weibo_hot_analyzor.fetch_keywords - 获取热搜关键词      │
│    Get trending keywords from Weibo                                  │
└────────────────────┬─────────────────────────────────────────────────┘
                     │
                     ▼
┌──────────────────────────────────────────────────────────────────────┐
│ 2. python -m weibo_hot_analyzor.post_crawler - 爬取数据              │
│    Crawl data with custom Cookie and similarity threshold            │
└────────────────────┬─────────────────────────────────────────────────┘
                     │
                     ▼
┌──────────────────────────────────────────────────────────────────────┐
│ 3. python -m weibo_hot_analyzor.merge_results - 合并结果             │
│    Merge all topic results into data_raw.csv                         │
└────────────────────┬─────────────────────────────────────────────────┘
                     │
                     ▼
┌──────────────────────────────────────────────────────────────────────┐
│ 4. python -m weibo_hot_analyzor.analyze --dedup - 数据去重           │
│    Deduplicate data with custom threshold                            │
└──────────────────────────────────────────────────────────────────────┘
```

## 常见问题 | FAQ

**Q: 我需要输入Cookie吗？**  
*Q: Do I need to enter a Cookie?*

A: 是的，需要从浏览器获取微博的Cookie，以便爬虫能正常访问。步骤：
1. 打开 weibo.com，登录你的账号
2. 按 F12 打开开发者工具
3. 在 Network 标签中找任意请求，复制 Request Headers 中的 Cookie 值
4. 运行爬虫时，会弹出提示输入Cookie，粘贴即可

**Cookie 会被保存吗？**  
*Will the Cookie be saved?*

A: 会的！第一次输入Cookie后，程序会自动将其保存到 `weibo-search/weibo/settings.py` 中。之后每次运行爬虫时：
- 如果直接按 Enter（不输入任何内容），会自动使用上次保存的Cookie
- 如果需要更换Cookie，重新输入新的Cookie即可，会自动覆盖旧值

*Yes! After entering the Cookie for the first time, the program will automatically save it to `weibo-search/weibo/settings.py`. Each subsequent crawler run:*
- *If you just press Enter (without entering anything), it will automatically use the previously saved Cookie*
- *If you need to change the Cookie, simply enter a new one, which will automatically replace the old value*

**A: Yes, you need to obtain Weibo's Cookie from your browser for the crawler to access normally. Steps:*
1. *Open weibo.com and log in*
2. *Press F12 to open developer tools*
3. *In the Network tab, find any request and copy the Cookie value from Request Headers*
4. *When running the crawler, a prompt will appear to enter the Cookie, just paste it*

## 许可证 | License

MIT License

## 贡献 | Contributing

欢迎提交 issue 或 pull request！

*Contributions are welcome via issues or pull requests!*

## 相关项目 | Related Projects

- [weibo-search](https://github.com/mikrokozmoz/weibo-search) - 微博爬虫框架
- [weibo-posts-processing](https://github.com/mikrokozmoz/weibo-posts-processing) - 微博数据处理库
- [weibo-trending-hot-search](https://github.com/justjavac/weibo-trending-hot-search) - 微博热搜总结
