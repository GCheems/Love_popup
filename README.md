# Love Popup（浪漫弹窗）

一个使用 Tkinter 制作的“浪漫弹窗”小应用：在屏幕上随机铺满带情话与表情的置顶小窗，支持一键启动/关闭与快捷键操作，适合表白、整活或制造小惊喜。

## 功能特点
- 一键启动 / 一键关闭 / 退出程序
- 快捷键：空格启动，Esc 关闭全部
- 弹窗顶置、自动网格排布并带轻微抖动，铺满更自然
- 语句与表情随机组合，可自定义内容
- 控制最大弹窗数量，滚动替换，稳定不积压

## 环境要求
- Windows（附带 `run.bat` / `run.vbs` 免黑框启动脚本）
- Python 3（Windows 官方安装包通常自带 Tkinter）
- 其他平台可直接用 `python love_popup.py` 运行主程序

## 快速开始
- 双击运行：`run.bat`（内部调用 `run.vbs`，优先使用 `pyw/pythonw` 无控制台启动）
- 或命令行运行：
  ```bash
  python love_popup.py
  ```
- 若提示“未找到 Python”，请先安装 Python 3 并勾选“Add to PATH”。

## 使用说明
- 按钮：
  - `一键启动` 开始铺满
  - `一键关闭` 关闭全部
  - `退出程序` 关闭应用
- 快捷键：
  - 空格 启动
  - `Esc` 关闭全部
- 点击任意弹窗任意位置也会快速关闭全部。

## 自定义配置
配置位于 `love_popup.py` 顶部常量，按需调整：

```python
POPUP_W = 240      # 每个弹窗宽度
POPUP_H = 120      # 每个弹窗高度
SPAWN_DELAY = 400  # 弹窗出现速度（毫秒）
JITTER = 8         # 弹窗位置随机抖动像素

BG_COLORS = [
    "SystemButtonFace"  # 使用系统默认配色，接近标准对话框
]
TEXT_COLOR = "#202020"

EMOJIS = ["❤️", "💖", "💘", "💗", "💞", "💓", "✨", "🌙", "⭐", "🌟", "🌸", "🌷", "🫶", "🎀"]
PHRASES = [
    "世界很暗，但你发着光。",
    "月色与雪色之间，你是第三种绝色。",
    # ...更多短句可自行增删
]
```

行为逻辑：
- 根据屏幕宽高计算网格位置，随机打散显示顺序
- 超过最大数量时销毁最早弹窗，保持总量稳定

## 常见问题
- 双击无反应 / 无弹窗：请确认已安装 Python 3，并可在命令行执行 `python --version` 或 `py -3 --version`。
- Linux / macOS：没有 `run.bat`/`run.vbs`，直接 `python love_popup.py` 即可（窗口外观受平台主题影响）。
- 字体 / Emoji 显示：取决于系统字体支持，必要时调整 `PHRASES` / `EMOJIS`。

## 可选：打包为可执行文件（Windows）
使用 PyInstaller 打包方便分发：

```bash
pip install pyinstaller
pyinstaller --noconsole --onefile love_popup.py
# 可加图标
# pyinstaller --noconsole --onefile --icon heart.ico love_popup.py
```

生成的可执行文件位于 `dist/` 目录。

## 文件说明
- `love_popup.py`：主程序（Tkinter UI + 弹窗逻辑）
- `run.bat`：Windows 批处理启动入口（调用 VBS，避免黑框）
- `run.vbs`：优先使用 `pyw/pythonw` 无控制台启动

---
若需要英文版 README、加入截图/动图或添加发行版打包脚本，请告诉我～

