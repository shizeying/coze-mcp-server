# MCP Coze Server

A MCP server implementation for Coze API

## Installation

Install the package with all dependencies:
```bash
pip install mcp-coze-server
```

Or install from source:
```bash
git clone https://github.com/shizeying/coze-mcp-server.git
cd coze-mcp-server
pip install -r requirements.txt
pip install -e .
```

## Usage

1. 设置环境变量：

```bash
export COZE_API_TOKEN="your_api_token"
export COZE_API_BASE="https://api.coze.cn"  # 或其他API地址
```

2. 运行服务器：

```bash
python -m coze_mcp_server
```

## Configuration

Support the following configuration methods:

1. Environment variables:
   - COZE_API_TOKEN
   - COZE_API_BASE

2. Command line arguments:
   - --coze-api-token
   - --coze-api-base

## Development

1. Clone the repository:

```bash
git clone https://github.com/shizeying/coze-mcp-server.git
```

2. Install dependencies:

```bash
pip install -r requirements.txt
pip install -e .
```

## License

This project is licensed under the MIT License - see the LICENSE file for details. 