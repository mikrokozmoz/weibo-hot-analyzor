# 微博热搜分析工具 | *Weibo Hot Search Analyzer*

一个用于微博数据分析和处理的完整工具链。支持智能去重、分词统计、词云生成、以及AI驱动的摘要分析。（可选：支持数据合并功能）

*A complete toolkit for Weibo data analysis and processing. Supports smart deduplication, word frequency statistics, word cloud generation, and AI-driven summary analysis. (Optional: supports data merging functionality)*

---

## 项目简介 | *Project Overview*

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

## 功能特性 | *Features*

### 数据处理模块 | *Data Processing Module*

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

### AI 分析模块 | *AI Analysis Module*

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

## 快速上手 | *Quick Start*

### 1. 环境安装 | *Installation*

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

### 2. 数据预处理 | *Data Preprocessing*

使用 `utils` 模块处理 CSV 数据（去重、分词、词云等）。

*Use the `utils` module to process CSV data (deduplication, tokenization, word clouds, etc.).*

#### 2.1 配置处理参数 | *Configure Processing Parameters*

编辑 `utils/settings.py`，设置：
- `LOAD_POSTS_FOLDER_PATH`：包含 CSV 文件的文件夹路径
- 其他处理参数（去重阈值、词长度范围等）

*Edit `utils/settings.py` to set:*
- *`LOAD_POSTS_FOLDER_PATH`: Path to folder containing CSV files*
- *Other processing parameters (deduplication threshold, word length range, etc.)*

#### 2.2 执行数据处理 | *Execute Data Processing*

```bash
# 方式一：使用命令行参数
# Method 1: Using command-line arguments
python -m utils --load_files_from_folder --dedupe

# 方式二：在 Python 代码中调用
# Method 2: Call in Python code
from utils import data_processing

result = data_processing(
    load_files_from_folder=True,
    extract_topics=True,
    dedupe=True,
    tokenize=True,
    word_frequency=True,
    create_wordcloud=True
)

# 访问结果 / Access results
df = result['df']  # 处理后的 DataFrame
word_freq = result['word_freq_by_keyword']  # 词频字典
```

**支持的参数** | *Supported parameters*:
- `--load_files_from_folder`：从文件夹加载 CSV / Load CSV from folder
- `--extract_topics`：提取话题 / Extract topics
- `--dedupe`：去重处理 / Deduplication
- `--tokenize`：分词统计 / Word segmentation & frequency
- `--word_frequency`：生成词频表 / Generate frequency table
- `--create_wordcloud`：生成词云 / Generate word clouds

### 3. AI 驱动分析 | *AI-Driven Analysis*

使用 `analyzer` 模块进行 AI 分析和摘要生成。

*Use the `analyzer` module for AI analysis and summary generation.*

#### 3.1 配置 AI 参数 | *Configure AI Parameters*

编辑 `analyzer/settings.py`，设置：
- `API_KEY`：阿里云百炼 API Key（从 https://bailian.console.aliyun.com/ 获取）
- `MODEL_NAME`：选择模型（推荐 qwen-plus 或 qwen-max）
- `INPUT_FILE`：待分析的 CSV 文件路径
- 其他分析参数

*Edit `analyzer/settings.py` to set:*
- *`API_KEY`: Alibaba Cloud Bailian API Key (get from https://bailian.console.aliyun.com/)*
- *`MODEL_NAME`: Choose model (recommended qwen-plus or qwen-max)*
- *`INPUT_FILE`: Path to CSV file to analyze*
- *Other analysis parameters*

#### 3.2 运行分析 | *Run Analysis*

```bash
# 执行两阶段 AI 分析
python analyzer/summary.py

# 输出结果：
# Output results:
# - stage1_keyword_analysis.csv: 关键词微观分析 / Micro-analysis per keyword
# - stage2_correlation_analysis_report.md: 宏观关联报告 / Keyword-correlation report
# - final_context_knowledge_base.txt: 完整知识库 / Complete knowledge base
```

#### 3.3 测试打标效果 | *Test Labeling*

```bash
python -m analyzer.labeling_testing

# 输出：
# - labeling_test_results.csv: 打标测试结果
```

#### 3.4 批量推理 | *Batch Inference*

使用阿里云百炼的批量推理服务对大规模数据进行标注。

*Use Alibaba Cloud Bailian's batch inference service for large-scale labeling.*

**步骤 1: 生成批量推理请求 | *Step 1: Generate Batch Requests*

```bash
python -m analyzer.batch_generator

# 功能说明 / Features:
# - 读取 post_list.csv
# - 自动按 id 去重（保留第一条记录的正文）
# - 生成 batch_list.jsonl 请求文件
# - 使用 labeling_prompt.txt 作为 system prompt
#
# Output: analyzer/data/batch_list.jsonl
```

**步骤 2: 上传至百炼批量推理服务 | *Step 2: Upload to Alibaba Batch Service*

1. 访问 https://dashscope.aliyuncs.com （选择批量推理服务）
2. 上传 `batch_list.jsonl` 文件
3. 等待任务完成，获取结果 URL

*Visit https://dashscope.aliyuncs.com and use batch inference service*

**步骤 3: 下载并处理结果 | *Step 3: Download & Process Results*

```bash
# 在 analyzer/settings.py 中更新 RESULT_URL
# Update RESULT_URL in analyzer/settings.py

python -m analyzer.result_download_and_conversion

# 输出结果：
# 1. batch_results_raw.jsonl - 原始返回结果
# 2. batch_results_final.csv - 去重后的三列格式（id、content、label）
# 3. batch_results_final_expanded.csv - 标签展开版本（10列：id、content、validity、stance、emotion_category、emotion_subtype、target、mf_main、mf_direction、reasoning）
```

**关键特性 | *Key Features*

- ✅ **自动去重** | Automatic deduplication：与 batch_generator 一致的去重逻辑，避免重复标注
- ✅ **成本优化** | Cost optimization：不在请求体中存储原始正文，减少数据传输
- ✅ **完整追溯** | Full traceability：根据 custom_id 从原始数据恢复正文，保证数据完整性
- ✅ **标签拆解** | Label parsing：自动将 JSON label 拆解为单独列，支持后续分析

---

## 项目结构 | *Project Structure*

```
weibo-hot-analyzer/
├── analyzer/                          # AI 驱动分析模块 / AI Analysis Module
│   ├── __init__.py
│   ├── settings.py                   # AI 分析参数配置 / AI parameters
│   ├── summary.py                    # 两阶段分析脚本 / Two-stage analysis script
│   ├── labeling_testing.py           # 打标测试工具 / Labeling testing tool
│   ├── batch_generator.py            # 批量推理文件生成器 / Batch inference file generator (新 / New)
│   ├── result_download_and_conversion.py  # 批量推理结果处理 / Batch result processor (新 / New)
│   ├── download_sample_results.py    # 样本结果下载工具 / Sample results downloader (新 / New)
│   ├── data/                         # 数据目录 / Data directory
│   │   ├── batch_example.jsonl       # 批量推理示例文件 / Batch inference example
│   │   ├── batch_list.jsonl          # 生成的批量请求文件 / Generated batch requests
│   │   ├── batch_results_raw.jsonl   # 原始批量推理结果 / Raw batch results
│   │   ├── batch_results_final.csv   # 处理后的三列结果 / Processed three-column results
│   │   └── batch_results_final_expanded.csv  # 标签展开版本 / Expanded label version
│   └── prompts/                      # Prompt 模板文件 / Prompt templates
│       ├── sys_prompt.txt            # 系统 prompt / System prompt
│       ├── keyword_prompt.txt        # 关键词分析 prompt / Keyword analysis prompt
│       ├── correlation_prompt.txt    # 关联分析 prompt / Correlation analysis prompt
│       └── labeling_prompt.txt       # 打标 prompt / Labeling prompt
│
├── utils/                             # 数据处理模块 / Data Processing Module
│   ├── __init__.py
│   ├── __main__.py                   # 命令行接口 / CLI interface
│   ├── settings.py                   # 处理参数配置 / Processing parameters
│   └── data_processing.py            # 入口函数 / Entry function
│
├── processing/                        # Submodule: 数据处理库
│   └── post_analysis/
│       ├── __init__.py
│       ├── pre_processing.py         # 数据加载、去重、话题提取
│       └── corpus_analysis.py        # 分词、词频、词云     
│
├── requirements.txt                   # 项目依赖 / Dependencies
├── README.md                          # 项目说明（本文件）
└── .gitmodules                        # Submodule 配置
```

---

## 核心概念 | *Core Concepts*

### 去重相似度阈值 | *Deduplication Similarity Threshold*

去重过程中，相似度阈值控制去重的严格程度：

*The similarity threshold controls the strictness of deduplication:*

| 阈值范围 | 说明 | 建议场景 |
|---------|------|--------|
| 0.70-0.80 | 宽松去重，移除更多重复 | 需要高质量唯一内容的分析 |
| 0.80-0.90 | 平衡去重，推荐使用 | 一般数据分析 |
| 0.90-0.99 | 严格去重，移除较少重复 | 保留细微差异内容 |

<br>

| *Threshold* | *Description* | *Recommended Scenario* |
|---------|---------|--------|
| *0.70-0.80* | *Loose dedup, remove more* | *High-quality unique content analysis* |
| *0.80-0.90* | *Balanced dedup (recommended)* | *General data analysis* |
| *0.90-0.99* | *Strict dedup, remove fewer* | *Preserve subtle differences* |

### AI 模型选择 | *AI Model Selection*

支持的阿里云百炼模型：

*Supported Alibaba Cloud Bailian models:*

- **qwen-plus**：性价比高，适合大部分任务 / Cost-effective, suitable for most tasks
- **qwen-max**：逻辑能力强，适合复杂分析 / Stronger logic, suitable for complex analysis
- **qwen-turbo**：速度快，适合快速处理 / Fast speed, suitable for quick processing

---

## 详细模块说明 | *Module Documentation*

### 1. 数据处理模块 | *Data Processing Module (`utils`)*

#### 核心函数 | *Core Function*

**`data_processing()`** - 统一的数据处理入口函数 / Unified data processing entry function

#### 参数配置 | *Settings Configuration (`utils/settings.py`)*

**数据加载参数 | *Load Parameters***
- `LOAD_POSTS_FOLDER_PATH` - CSV 文件所在文件夹路径（必须指定）/ Folder path containing CSV files (required)
- `LOAD_POSTS_KEYWORD_COLUMN` - 新增列名称（默认：'关键词'）/ New column name (default: '关键词')

**话题提取参数 | *Topic Extraction Parameters***
- `EXTRACT_TOPICS_TOPICS_COLUMN` - 包含话题的列名（默认：'话题'）/ Column name containing topics
- `EXTRACT_TOPICS_ID_COLUMN` - 微博ID列名（默认：'id'）/ Post ID column name

**去重参数 | *Deduplication Parameters***
- `DEDUPE_KEYWORD_COL` - 用于分组的关键词列名（默认：'关键词'）/ Grouping column name
- `DEDUPE_TEXT_COL` - 用于判断重复的文本列（默认：'微博正文_cleaned'）/ Text column for similarity check
- `DEDUPE_TIME_COL` - 用于选择保留记录的时间列（默认：'发布时间'）/ Time column for record selection
- `DEDUPE_SUM_COLS` - 需要求和的数值列（默认：None，自动为 ['点赞数','评论数','转发数','互动总数']）/ Numeric columns to sum
- `DEDUPE_SIMILARITY_THRESHOLD` - 相似度阈值（默认：0.88）/ Similarity threshold (0-1)
- `DEDUPE_MIN_LEN_FOR_SIMILARITY` - 计算相似度的最小长度（默认：6）/ Minimum length for similarity calculation
- `DEDUPE_DEBUG` - 是否输出 debug 信息（默认：False）/ Enable debug output
- `DEDUPE_AUTO_CLEAN` - 自动清洗文本（默认：False）/ Auto-clean text if column doesn't exist

**分词参数 | *Tokenization Parameters***
- `TOKENIZE_TEXT_COLUMN` - 包含文本的列名（默认：'微博正文'）/ Column containing text
- `TOKENIZE_KEYWORD_COLUMN` - 包含关键词的列名（默认：'关键词'）/ Column containing keywords
- `TOKENIZE_WORD_LENGTH_RANGE` - 词长范围（默认：(2, 10)）/ Word length range (min, max)

**词频统计参数 | *Word Frequency Parameters***
- `WORD_FREQ_TOP_N` - 保留前 N 个词（默认：50）/ Keep top N words

**词云参数 | *Word Cloud Parameters***
- `WORDCLOUD_KEYWORD_COLUMN` - 关键词列名（默认：'关键词'）/ Keyword column name
- `WORDCLOUD_WORD_COLUMN` - 词列名（默认：'词'）/ Word column name
- `WORDCLOUD_FREQ_COLUMN` - 词频列名（默认：'词频'）/ Frequency column name
- `WORDCLOUD_TOP_N` - 每个关键词保留的词数（默认：30）/ Top N words per keyword
- `WORDCLOUD_FONT_PATH` - 字体文件路径 / Font path (for Chinese characters)
- `WORDCLOUD_COLORS_LIST` - 颜色列表 / Color list
- `WORDCLOUD_COLS` - 词云显示列数（默认：3）/ Number of columns
- `WORDCLOUD_FIGSIZE` - 图表尺寸（默认：(15, 12)）/ Figure size (width, height)
- `WORDCLOUD_PREFER_HORIZONTAL` - 优先水平布置词（默认：0.7）/ Prefer horizontal layout (0-1)
- `WORDCLOUD_RELATIVE_SCALING` - 词大小相对缩放（默认：0.5）/ Relative scaling (0-1)
- `WORDCLOUD_MIN_FONT_SIZE` - 最小字体大小（默认：10）/ Minimum font size
- `WORDCLOUD_SHOW` - 是否显示词云（默认：True）/ Display word clouds

---

### 2. AI 分析模块 | *AI Analysis Module (`analyzer`)*

#### 核心脚本 | *Core Scripts*

**`summary.py`** - 两阶段 AI 分析脚本 / Two-stage AI analysis script

运行方式 | Usage:
```bash
python analyzer/summary.py
```

**分析流程**：
1. **阶段一** - 关键词微观分析 / Stage 1 - Keyword fact extraction
   - 逐个关键词分析，提取核心事实和观点
   - *Per-keyword analysis to extract facts and key points*
   - 输出：`stage1_keyword_analysis.csv` / Output: CSV file with per-keyword analysis

2. **阶段二** - 宏观关联分析 / Stage 2 - Correlation analysis
   - 分析关键词之间的关联和逻辑关系
   - *Analyze correlations and logical relationships between keywords*
   - 输出：`stage2_correlation_analysis_report.md` / Output: Markdown report

3. **知识库生成** - 综合背景知识库 / Knowledge base - Synthesized background knowledge
   - 输出：`final_context_knowledge_base.txt` / Output: Knowledge base text file

**`labeling_testing.py`** - 打标测试工具 / Labeling testing tool

功能：测试打标效果，自动更新 prompt 中的背景知识

*Features: Test labeling effectiveness, auto-update background knowledge in prompts*

```bash
# 1. 更新背景知识 / Update background knowledge in prompt
python analyzer/labeling_testing.py update

# 2. 测试打标 / Test labeling effectiveness
python analyzer/labeling_testing.py test --n 20

# 3. 完整流程：更新 + 测试 / Complete workflow: update + test
python analyzer/labeling_testing.py update && python analyzer/labeling_testing.py test
```

配置参数参考 `analyzer/settings.py` 中的：
- `TEST_POST_LIST` - 用于打标的微博列表 CSV 文件
- `TEST_SAMPLE_SIZE` - 测试样本数（默认：20）
- `API_KEY`、`MODEL_NAME` 等 API 配置

*Configuration parameters in `analyzer/settings.py`:*
- *`TEST_POST_LIST` - CSV file with posts for labeling*
- *`TEST_SAMPLE_SIZE` - Number of samples to test (default: 20)*
- *`API_KEY`, `MODEL_NAME` and other API settings*

**`batch_generator.py`** - 批量推理文件生成器 / Batch inference file generator

用途：为阿里云百炼 API 的批量推理功能生成 JSONL 格式的请求文件

*Purpose: Generate JSONL request files for Alibaba Cloud Bailian batch inference API*

```bash
# 生成批量推理文件 / Generate batch inference file
python analyzer/batch_generator.py

# 或指定输入输出文件 / Or specify input/output files
python analyzer/batch_generator.py \
  --input analyzer/data/post_list.csv \
  --output analyzer/data/batch_generated.jsonl \
  --prompt analyzer/prompts/labeling_prompt.txt \
  --model qwen-plus
```

输出文件为 JSONL 格式，每行一个 JSON 请求对象，可直接上传至阿里云百炼批量推理 API。

*Output file in JSONL format (one JSON request per line), ready for Alibaba Cloud Bailian batch API.*

配置参数参考 `analyzer/settings.py` 中的：
- `TEST_POST_LIST` - 输入的微博列表 CSV 文件
- `MODEL_NAME` - 使用的模型
- 其他 API 配置

*Configuration parameters in `analyzer/settings.py`:*
- *`TEST_POST_LIST` - Input CSV file with posts*
- *`MODEL_NAME` - Model to use*
- *Other API settings*

#### 参数配置 | *Settings Configuration (`analyzer/settings.py`)*

**API 配置 | *API Configuration***
- `API_KEY` - 阿里云百炼 API Key（必须修改）/ Alibaba Cloud Bailian API Key (MUST MODIFY)
- `BASE_URL` - API 接入点（默认：`https://dashscope.aliyuncs.com/compatible-mode/v1`）/ API endpoint
- `MODEL_NAME` - 使用的模型（默认：'qwen-plus'）/ Model to use (default: qwen-plus)

**分析参数 | *Analysis Parameters***
- `TEMP_STAGE_1` - 阶段一温度参数（默认：0.3）/ Stage 1 temperature for deterministic results
- `TEMP_STAGE_2` - 阶段二温度参数（默认：0.5）/ Stage 2 temperature for balanced results
- `MAX_TEXT_LENGTH` - 单次请求最大文本长度（默认：25000）/ Max text per request (to control cost)
- `MAX_RETRIES` - API 调用失败重试次数（默认：3）/ Retry count on API failure

**文件路径 | *File Paths***
- `INPUT_FILE` - 待分析的数据文件（默认：'analyzer/data/context_posts.csv'）/ CSV file to analyze
- `PROMPT_DIR` - Prompt 文件夹（默认：'analyzer/prompts'）/ Prompt templates folder
  - `PROMPT_SYSTEM_FILE` - 系统 prompt / System prompt file
  - `PROMPT_STAGE1_FILE` - 阶段一 prompt / Stage 1 prompt file
  - `PROMPT_STAGE2_FILE` - 阶段二 prompt / Stage 2 prompt file
- `OUTPUT_STAGE1_CSV` - 阶段一输出（默认：'analyzer/data/stage1_keyword_analysis.csv'）
- `OUTPUT_STAGE2_MD` - 阶段二输出（默认：'analyzer/data/stage2_correlation_analysis_report.md'）
- `OUTPUT_FINAL_CONTEXT` - 知识库输出（默认：'analyzer/data/final_context_knowledge_base.txt'）

**打标测试参数 | *Labeling Test Parameters***
- `TEST_POST_LIST` - 用于打标的微博列表（默认：'analyzer/data/post_list.csv'）/ Post list for testing
- `TEST_SAMPLE_SIZE` - 测试样本数（默认：20）/ Number of samples to test

---

## 依赖项 | *Dependencies*

### 主要库 | *Main Libraries*

- **Python 3.8+**
- **pandas** - 数据处理 / Data processing
- **jieba** - 中文分词 / Chinese word segmentation
- **wordcloud** - 词云生成 / Word cloud generation
- **matplotlib** - 数据可视化 / Data visualization
- **openai** - OpenAI API 客户端（用于阿里云兼容接口）/ OpenAI client for Alibaba Cloud compatible API
- **requests** - HTTP 请求 / HTTP requests

### Submodule 依赖 | *Submodule Dependencies*

- **[weibo-posts-processing](https://github.com/mikrokozmoz/weibo-posts-processing)** - 微博数据处理库 / Weibo data processing library
  - 提供数据预处理、去重、分词、词云等核心功能
  - Provides core functionality for preprocessing, deduplication, tokenization, word clouds

---

## 常见问题 | *FAQ*

### Q: 如何获取阿里云百炼 API Key？

1. 访问 https://bailian.console.aliyun.com/
2. 注册或登录阿里云账号
3. 在控制台创建 API Key
4. 复制 API Key 到 `analyzer/settings.py` 的 `API_KEY` 字段

### *Q: How do I get Alibaba Cloud Bailian API Key?*

1. *Visit https://bailian.console.aliyun.com/*
2. *Register or login to Alibaba Cloud account*
3. *Create API Key in the console*
4. *Copy the API Key to `API_KEY` field in `analyzer/settings.py`*

---

## 许可证 | *License*

MIT License

---

## 相关项目 | *Related Projects*

- [weibo-posts-processing](https://github.com/mikrokozmoz/weibo-posts-processing) - 微博数据处理库 / Weibo data processing library
- [weibo-search](https://github.com/dataabc/weibo-search) - 微博爬虫框架 / Weibo crawler framework

---

## 贡献 | *Contributing*

欢迎提交 issue 或 pull request！

Contributions via issues or pull requests are welcome!
