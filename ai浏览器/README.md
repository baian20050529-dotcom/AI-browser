# Camoufox AI 浏览器运行环境

本目录按 Camoufox Python 安装文档配置，使用独立 Python 虚拟环境和 Camoufox 浏览器运行时。

## 安装

```bash
cd /workspace/GOOD/ai浏览器
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
XDG_CACHE_HOME="$PWD/.camoufox/cache" .venv/bin/python -m camoufox fetch
```

## 运行示例

默认以无头模式打开空白页：

```bash
.venv/bin/python 浏览器示例.py
```

也可以传入网址：

```bash
.venv/bin/python 浏览器示例.py https://example.com
```

云环境为无头运行环境；浏览外部网站还需要该网址域名获准通过环境网络策略。

官方安装说明：<https://camoufox.com/python/installation/>
