# MCP Coze Server

一个基于MCP（Model Control Protocol）的Coze API服务器实现。

## 功能特性

- 支持Coze API的完整功能
- 集成MCP协议
- 支持异步操作
- 支持工作流和机器人管理

## 安装

从GitHub Packages安装：

```bash
pip install mcp-coze-server
```

## 使用方法

1. 设置环境变量：

```bash
export COZE_API_TOKEN="your_api_token"
export COZE_API_BASE="https://api.coze.cn"  # 或其他API地址
```

2. 运行服务器：

```bash
python -m coze_mcp_server
```

## 配置

支持以下配置方式：

1. 环境变量：
   - COZE_API_TOKEN
   - COZE_API_BASE

2. 命令行参数：
   - --coze-api-token
   - --coze-api-base

## 开发

1. 克隆仓库：

```bash
git clone https://github.com/shizeying/coze-mcp-server.git
```

2. 安装依赖：

```bash
pip install -e .
```

## 许可证

MIT License 