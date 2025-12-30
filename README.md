# 微博热搜分析工具 | Weibo Hot Search Analyzer

一个用于微博数据分析和处理的完整工具链。支持智能去重、分词统计、词云生成、以及AI驱动的摘要分析。（可选：支持数据合并功能）

A complete toolkit for Weibo data analysis and processing. Supports smart deduplication, word frequency statistics, word cloud generation, and AI-driven summary analysis. (Optional: supports data merging functionality)

---

## 项目简介 | Project Overview

本项目专注于微博数据的分析和处理，通过模块化的设计，用户可以灵活地：
- 使用 `utils` 模块进行数据预处理（去重、分词、词云生成等）
- 使用 `analyzer` 模块进行 AI 驱动的分析和摘要生成
- 自定义参数，一键执行完整的数据处理流程
- （可选）使用数据合并功能整合多个来源的数据

*This project focuses on analysis and processing of Weibo data. With a modular design, users can flexibly:*
- *Use the `utils` module for data preprocessing (deduplication, tokenization, word cloud generation, etc.)*
- *Use the `analyzer` module for AI-driven analysis and summary generation*
- *Customize parameters and execute the complete data processing pipeline with a single command*
- *(Optional) Use data merging functionality to consolidate data from multiple sources*

---

## 功能特性 | Features

### 数据处理模块 | Data Processing Module

- **灵活的数据加载** 📂：从文件夹直接加载 CSV 文件
- **智能去重** ✨：支持自定义相似度阈值的去重，保留最早发布的记录
- **话题提取** 🏷️：自动从微博中提取前三个话题
- **分词统计** 🔤：基于 jieba 的中文分词和词频统计
- **词云生成** ☁️：按关键词自动生成高质量词云图
- **参数集中管理** ⚙️：所有处理参数在 `utils/settings.py` 中配置

<br>

- *Flexible data loading from CSV files in a folder* 
- *Smart deduplication with custom similarity threshold* 
- *Automatic topic extraction from posts* 
- *Chinese word segmentation and frequency statistics based on jieba*
- *Auto-generate high-quality word clouds per keyword*
- *Centralized parameter management in `utils/settings.py`*

### AI 分析模块 | AI Analysis Module

- **两阶段分析** 🧠：第一阶段微观事实提取（逐关键词分析）+ 第二阶段宏观关联分析（全局事件关联）
- **知识库生成** 📚：自动生成背景知识库，支持下游应用
- **模型灵活配置** 🔧：支持多种阿里云百炼大模型（qwen-plus、qwen-max 等）
- **完善的错误处理** 🛡️：API 调用失败自动重试机制

<br>

- *Two-stage analysis (micro-fact extraction + macro-correlation analysis)*
- *Automatic knowledge base generation for downstream applications*
- *Flexible model configuration supporting multiple Alibaba Cloud models*
- *Robust error handling with automatic retry on API failures*

---

## 快速上手 | Quick Start

### 1. 环境安装 | Installation

```bash
# 克隆项目
# Clone the repository
git clone --recursive https://github.com/mikrokozmoz/weibo-hot-analyzer
cd weibo-hot-analyzer

# 创建虚拟环境（可选但推荐）
# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate

# 安装依赖
# Install dependencies
pip install -r requirements.txt
```

### 2. 数据预处理 | Data Preprocessing

使用 `utils` 模块处理 CSV 数据（去重、分词、词云等）。

Use the `utils` module to process CSV data (deduplication, tokenization, word clouds, etc.).

#### 2.1 配置处理参数 | Configure Processing Parameters

编辑 `utils/settings.py`，设置：
- `LOAD_POSTS_FOLDER_PATH`：包含 CSV 文件的文件夹路径
- 其他处理参数（去重阈值、词长度范围等）

Edit `utils/settings.py` to set:
- `LOAD_POSTS_FOLDER_PATH`: Path to folder containing CSV files
- Other processing parameters (deduplication threshold, word length range, etc.)

#### 2.2 执行数据处理 | Execute Data Processing

```bash
# 方式一：使用命令行参数
# Method 1: Using command-line arguments
python -m utils --load_files_from_folder --dedupe

# 方式二：在 Python 代码中调用
# Method 2: Call in Python code
from utils import data_processing

result = data_processing(
    load_files_from_folder=True,
    dedupe=True
)
```

**支持的参数** | *Supported parameters*:
- `--load_files_from_folder`：从文件夹加载 CSV / Load CSV from folder
- `--extract_topics`：提取话题 / Extract topics
- `--dedupe`：去重处理 / Deduplication
- `--tokenize`：分词统计 / Word segmentation & frequency
- `--word_frequency`：生成词频表 / Generate frequency table
- `--create_wordcloud`：生成词云 / Generate word clouds

### 3. AI 驱动分析 | AI-Driven Analysis

使用 `analyzer` 模块进行 AI 分析和摘要生成。

Use the `analyzer` module for AI analysis and summary generation.

#### 3.1 配置 AI 参数 | Configure AI Parameters

编辑 `analyzer/settings.py`，设置：
- `API_KEY`：阿里云百炼 API Key（从 https://bailian.console.aliyun.com/ 获取）
- `MODEL_NAME`：选择模型（推荐 qwen-plus 或 qwen-max）
- `INPUT_FILE`：待分析的 CSV 文件路径
- 其他分析参数

Edit `analyzer/settings.py` to set:
- `API_KEY`: Alibaba Cloud Bailian API Key (get from https://bailian.console.aliyun.com/)
- `MODEL_NAME`: Choose model (recommended qwen-plus or qwen-max)
- `INPUT_FILE`: Path to CSV file to analyze
- Other analysis parameters

#### 3.2 运行分析 | Run Analysis

```bash
# 执行两阶段 AI 分析
# Run two-stage AI analysis
python -m analyzer

# 输出结果：
# Output results:
# - stage1_keyword_analysis.csv: 关键词微观分析 / Micro-analysis per keyword
# - stage2_correlation_analysis_report.md: 宏观关联报告 / Keyword-correlation report
# - final_context_knowledge_base.txt: 完整知识库 / Complete knowledge base
```

---

## 项目结构 | Project Structure

```
weibo-hot-analyzer/
├── analyzer/                          # AI 驱动分析模块 / AI Analysis Module
│   ├── settings.py                   # AI 分析参数配置 / AI parameters
│   ├── summary.py                    # 两阶段分析脚本 / Two-stage analysis script
│   ├── prompts/                      # Prompt 模板文件 / Prompt templates
│   │   ├── sys_prompt                # 系统 prompt
│   │   ├── keyword_prompt            # 关键词分析 prompt
│   │   └── correlation_prompt        # 关联分析 prompt
│   └── __init__.py
│
├── utils/                             # 数据处理模块 / Data Processing Module
│   ├── settings.py                   # 处理参数配置 / Processing parameters
│   ├── data_processing.py            # 入口函数 / Entry function
│   ├── __main__.py                   # 命令行接口 / CLI interface
│   └── __init__.py
│
├── processing/                        # Submodule: 数据处理库
│   └── post_analysis/
│       ├── pre_processing.py         # 数据加载、去重、话题提取
│       ├── corpus_analysis.py        # 分词、词频、词云
│       └── __init__.py
│
├── files/                             # 数据文件目录 / Data files directory
├── requirements.txt                   # 项目依赖 / Dependencies
├── README.md                          # 项目说明（本文件）
└── .gitmodules                        # Submodule 配置
```

---

## 核心概念 | Core Concepts

### 去重相似度阈值 | Deduplication Similarity Threshold

去重过程中，相似度阈值控制去重的严格程度：

The similarity threshold controls the strictness of deduplication:

| 阈值范围 | 说明 | 建议场景 |
|---------|------|--------|
| 0.70-0.80 | 宽松去重，移除更多重复 | 需要高质量唯一内容的分析 |
| 0.80-0.90 | 平衡去重，推荐使用 | 一般数据分析 |
| 0.90-0.99 | 严格去重，移除较少重复 | 保留细微差异内容 |

| Threshold | Description | Recommended Scenario |
|---------|---------|--------|
| 0.70-0.80 | Loose dedup, remove more | High-quality unique content analysis |
| 0.80-0.90 | Balanced dedup (recommended) | General data analysis |
| 0.90-0.99 | Strict dedup, remove fewer | Preserve subtle differences |

### AI 模型选择 | AI Model Selection

支持的阿里云百炼模型：

Supported Alibaba Cloud Bailian models:

- **qwen-plus**：性价比高，适合大部分任务 / Cost-effective, suitable for most tasks
- **qwen-max**：逻辑能力强，适合复杂分析 / Stronger logic, suitable for complex analysis
- **qwen-turbo**：速度快，适合快速处理 / Fast speed, suitable for quick processing

---

## 依赖项 | Dependencies

### 主要库 | Main Libraries

- **Python 3.8+**
- **pandas** - 数据处理 / Data processing
- **jieba** - 中文分词 / Chinese word segmentation
- **wordcloud** - 词云生成 / Word cloud generation
- **matplotlib** - 数据可视化 / Data visualization
- **openai** - OpenAI API 客户端（用于阿里云兼容接口）/ OpenAI client for Alibaba Cloud compatible API
- **requests** - HTTP 请求 / HTTP requests

### Submodule 依赖 | Submodule Dependencies

- **[weibo-posts-processing](https://github.com/mikrokozmoz/weibo-posts-processing)** - 微博数据处理库 / Weibo data processing library
  - 提供数据预处理、去重、分词、词云等核心功能
  - Provides core functionality for preprocessing, deduplication, tokenization, word clouds

---

## 常见问题 | FAQ

### Q: 如何获取阿里云百炼 API Key？

A: 
1. 访问 https://bailian.console.aliyun.com/
2. 注册或登录阿里云账号
3. 在控制台创建 API Key
4. 复制 API Key 到 `analyzer/settings.py` 的 `API_KEY` 字段

### Q: How do I get Alibaba Cloud Bailian API Key?

A:
1. Visit https://bailian.console.aliyun.com/
2. Register or login to Alibaba Cloud account
3. Create API Key in the console
4. Copy the API Key to `API_KEY` field in `analyzer/settings.py`

---

## 许可证 | License

MIT License

---

## 相关项目 | Related Projects

- [weibo-posts-processing](https://github.com/mikrokozmoz/weibo-posts-processing) - 微博数据处理库 / Weibo data processing library
- [weibo-search](https://github.com/dataabc/weibo-search) - 微博爬虫框架 / Weibo crawler framework

---

## 贡献 | Contributing

欢迎提交 issue 或 pull request！

Contributions via issues or pull requests are welcome!
