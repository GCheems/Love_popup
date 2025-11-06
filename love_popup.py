import tkinter as tk
from tkinter import ttk
import random

# 配置：可按需微调
POPUP_W = 240         # 每个弹窗宽度
POPUP_H = 120         # 每个弹窗高度
SPAWN_DELAY = 400     # 弹窗出现速度（毫秒）
JITTER = 8            # 弹窗位置随机抖动像素

BG_COLORS = [
    "SystemButtonFace"  # 使用系统默认配色，接近标准对话框
]
TEXT_COLOR = "#202020"

EMOJIS = ["❤️", "💖", "💘", "💗", "💞", "💓", "✨", "🌙", "⭐", "🌟", "🌸", "🌷", "🫶", "🎀"]

PHRASES = [
    "世界很暗，但你发着光。",
    "月色与雪色之间，你是第三种绝色。",
    "我喜欢三月的风，六月的雨，不落的太阳，还有最好的你。",
    "你是人间理想，也是心动本身。",
    "山海海不及你眉眼半分。",
    "我见众生皆草木，唯你是青山。",
    "你来时，风起云涌；你笑时，星河倾倒。",
    "我的宇宙为你藏有温柔千万缕。",
    "情话很长，我长话短说：我喜欢你。",
    "想把宇宙的温柔，撒满你的人间。",
    "你一出现，风都甜了。",
    "我与春风皆过客，你携秋水揽星河。",
    "你是我不变的答案。",
    "你是落日弥漫的橘，也是天边最温柔的光。",
    "假如爱有天意，那一定是你。",
    "你是我心中唯一的灯塔。",
    "你是我生命中的奇迹，是我心中永远的光。",
    "我爱你，要在一起一辈子。",
    "你在哪里我想你了。",

]


class LovePopupApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("浪漫弹窗启动器")
        self.root.resizable(False, False)

        self.running = False
        self.jobs = []
        self.popups = []
        self.positions = []
        self.max_popups = None

        # UI
        frm = tk.Frame(self.root, padx=16, pady=16)
        frm.pack(fill="both", expand=True)

        self.start_btn = tk.Button(frm, text="一键启动", width=12, height=2, command=self.start)
        self.start_btn.grid(row=0, column=0, padx=6, pady=6)

        self.stop_btn = tk.Button(frm, text="一键关闭", width=12, height=2, command=self.close_all)
        self.stop_btn.grid(row=0, column=1, padx=6, pady=6)

        self.quit_btn = tk.Button(frm, text="退出程序", width=12, height=2, command=self.quit)
        self.quit_btn.grid(row=0, column=2, padx=6, pady=6)

        self.status = tk.Label(frm, text="提示：空格=启动，Esc=关闭全部", fg="#666")
        self.status.grid(row=1, column=0, columnspan=3, pady=(8, 0))

        # 快捷键
        self.root.bind("<Escape>", lambda e: self.close_all())
        self.root.bind("<space>",  lambda e: (not self.running) and self.start())

        # 初始位置与大小
        self.root.geometry("420x130+80+80")

    def compute_positions(self):
        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()
        cols = max(1, sw // POPUP_W)
        rows = max(1, sh // POPUP_H)

        # 居中铺满
        x0 = (sw - cols * POPUP_W) // 2
        y0 = (sh - rows * POPUP_H) // 2

        positions = []
        for r in range(rows):
            for c in range(cols):
                x = x0 + c * POPUP_W + random.randint(-JITTER, JITTER)
                y = y0 + r * POPUP_H + random.randint(-JITTER, JITTER)
                x = max(0, min(x, sw - POPUP_W))
                y = max(0, min(y, sh - POPUP_H))
                positions.append((x, y))

        random.shuffle(positions)  # 打散顺序，更有铺开的感觉
        self.positions = positions
        self.max_popups = len(positions)

    def start(self):
        if self.running:
            return
        self.running = True
        self.start_btn.config(state="disabled")
        self.status.config(text="铺满中… Esc可随时关闭全部")
        self.compute_positions()
        self.schedule_next()

    def schedule_next(self):
        if not self.running:
            return
        if not self.positions:
            # 位置用尽则重新生成，持续弹出
            self.compute_positions()
        x, y = self.positions.pop()
        self.create_popup(x, y)
        job = self.root.after(SPAWN_DELAY, self.schedule_next)
        self.jobs.append(job)

    def create_popup(self, x, y):
        # 控制弹窗数量以保持稳定：超出则移除最早的一个
        if self.max_popups and len(self.popups) >= self.max_popups:
            try:
                old = self.popups.pop(0)
                old.destroy()
            except Exception:
                pass

        top = tk.Toplevel(self.root)
        top.title("温馨提示")
        top.attributes("-topmost", True)
        top.resizable(False, False)
        top.geometry(f"{POPUP_W}x{POPUP_H}+{x}+{y}")

        bg = random.choice(BG_COLORS)
        top.configure(bg=bg)

        # 内容：使用 ttk，贴近系统标准弹窗风格
        frm = ttk.Frame(top, padding=16)
        frm.pack(fill="both", expand=True)

        msg = random.choice(PHRASES)
        e1 = random.choice(EMOJIS)
        e2 = random.choice(EMOJIS)
        text = f"{e1} {msg} {e2}"
        lbl = ttk.Label(frm, text=text, wraplength=POPUP_W - 40, justify="center")
        lbl.pack(expand=True)

        btn = ttk.Button(frm, text="好的", command=self.close_all)
        btn.pack(pady=(6, 0))

        # 点击任一弹窗任意位置也可快速关闭全部
        top.bind("<Button-1>", lambda e: self.close_all())

        self.popups.append(top)

    def close_all(self):
        self.running = False
        # 取消后续任务
        for job in self.jobs:
            try:
                self.root.after_cancel(job)
            except Exception:
                pass
        self.jobs.clear()
        # 关闭所有弹窗
        for w in self.popups:
            try:
                w.destroy()
            except Exception:
                pass
        self.popups.clear()
        self.start_btn.config(state="normal")
        self.status.config(text="已关闭全部。空格=启动，Esc=关闭全部")

    def quit(self):
        self.close_all()
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = LovePopupApp(root)
    root.mainloop()
