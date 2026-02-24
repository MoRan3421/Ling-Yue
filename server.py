from flask import Flask, jsonify, request

app = Flask(__name__)

# ======================
# 数据（示例）
# ======================

HEROES = [
    {"id": 1, "name": "凌霄剑尊", "role": "战士", "hp": 3200, "atk": 180},
    {"id": 2, "name": "月璃仙姬", "role": "法师", "hp": 2400, "atk": 260},
]

GEARS = [
    {"id": 1, "name": "灵刃", "atk": 60},
    {"id": 2, "name": "玄甲", "hp": 800},
]

RUNES = [
    {"id": 1, "name": "天灵", "atk": 12},
    {"id": 2, "name": "护元", "hp": 150},
]

PLAYER = {
    "rank": 2,        # 筑基
    "stars": 3,
    "points": 0
}

RANKS = [
    "凡人","炼体","筑基","金丹",
    "元婴","化神","合体","渡劫",
    "灵尊","灵王","灵皇","天道","至高·灵约"
]

# ======================
# API
# ======================

@app.route("/api/heroes")
def heroes():
    return jsonify(HEROES)

@app.route("/api/gears")
def gears():
    return jsonify(GEARS)

@app.route("/api/runes")
def runes():
    return jsonify(RUNES)

@app.route("/api/rank")
def rank():
    return jsonify({
        "name": RANKS[PLAYER["rank"]],
        "rank": PLAYER["rank"],
        "stars": PLAYER["stars"],
        "points": PLAYER["points"]
    })

@app.route("/api/match_result", methods=["POST"])
def match_result():
    data = request.json
    win = data.get("win", False)

    if PLAYER["rank"] < 4:  # 低端（星）
        PLAYER["stars"] += 1 if win else -1
        if PLAYER["stars"] >= 5:
            PLAYER["rank"] += 1
            PLAYER["stars"] = 0

    elif PLAYER["rank"] < 9:  # 中段（星+分）
        if win:
            PLAYER["stars"] += 1
            PLAYER["points"] += 20
        else:
            PLAYER["points"] -= 10

    else:  # 高端（分）
        PLAYER["points"] += 25 if win else -20

    PLAYER["stars"] = max(0, PLAYER["stars"])
    PLAYER["points"] = max(0, PLAYER["points"])

    return jsonify({"ok": True})

app.run(host="0.0.0.0", port=5000)