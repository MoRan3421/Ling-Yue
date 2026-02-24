# config.py
SCREEN_W, SCREEN_H = 1280, 720
FPS = 60

# 13 段位
RANKS = [
    "凡人", "炼体", "筑基", "金丹",
    "元婴", "化神", "合体",
    "大乘", "渡劫",
    "灵尊", "灵王", "灵皇",
    "天道"
]

# 分层
LOW_END = range(0, 4)      # 低端：纯星
MID_END = range(4, 9)      # 中段：星 + 积分
HIGH_END = range(9, 13)    # 高端：纯积分

MAX_STARS = 5