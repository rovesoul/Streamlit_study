# Streamlit Study

> 一个 Python 初学者学习 Streamlit 的代码仓库，通过小项目快速上手 Web 开发。

## 已学内容

| 文件 | 内容 |
|------|------|
| `hellowpage.py` | Streamlit 基础：创建第一个页面，虚拟环境配置 |
| `dataShow1.py` | 基础组件：DataFrame 展示、折线图、柱状图、地图、滑块、文本输入、选择框、进度条、布局、Radio 单选框 |

## 快速开始

```bash
# 克隆仓库
git clone https://github.com/rovesoul/Streamlit_study.git
cd Streamlit_study

# 创建虚拟环境（推荐）
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
# .venv\Scripts\activate     # Windows PowerShell
# .venv\Scripts\activate.bat # Windows CMD

# 安装依赖
pip install streamlit pandas numpy

# 运行示例
streamlit run hellowpage.py
streamlit run dataShow1.py
```

## 未来学习规划(也就是目前没学，未来可能会去学，也可能改变计划)

### 第一阶段：核心概念（必学）

| 主题 | 说明 |
|------|------|
| **Session State** | 跨请求保持变量，理解 Streamlit 的状态管理机制，是做复杂交互的基石 |
| **Callbacks** | 配合 Session State 实现精细的状态控制，如表单提交、按钮点击后的处理逻辑 |
| **st.form & st.form_submit_button** | 批量提交输入，避免每次输入都触发重新运行，大幅改善用户体验 |
| **st.cache_data / st.cache_resource** | 缓存数据或资源（模型加载等），避免重复计算，提升性能 |

### 第二阶段：常用功能（推荐）

| 主题 | 说明 |
|------|------|
| **多页面应用（Multi-page）** | 通过 `pages/` 目录组织多个页面，构建完整的应用 |
| **聊天组件** `st.chat_message` / `st.chat_input` | 构建 LLM 对话应用，大模型时代必备 |
| **文件上传下载** `st.file_uploader` / `st.download_button` | 上传数据文件、导出结果 |
| **列布局进阶** `st.columns` / `st.tabs` / `st.expander` | 灵活组织页面结构，提升可读性 |
| **侧边栏深度使用** | 构建配置面板、导航菜单 |

### 第三阶段：部署与生产（进阶）

| 主题 | 说明 |
|------|------|
| **Streamlit Cloud 部署** | 免费托管，一键发布自己的应用 |
| **Secrets 管理** `st.secrets` | 安全存储 API Key 等敏感信息 |
| **自定义样式** | 隐藏默认元素、注入 CSS，打造品牌风格 |
| **第三方组件** | `streamlit-option-menu`、`streamlit-extras` 等扩展生态 |
| **与 LLM 集成** | 结合 LangChain / FastAPI 构建 AI 应用后端 |

## 参考资料

- 官方文档：https://docs.streamlit.io/
- 官方 API 参考：https://docs.streamlit.io/develop/api-reference
- 官方高级概念：https://docs.streamlit.io/get-started/fundamentals/advanced-concepts
- Gallery 示例：https://streamlit.io/gallery
