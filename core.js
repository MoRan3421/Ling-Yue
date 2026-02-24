
/* ========= 全站语言 + 主题系统 ========= */

const LANG = {
  zh:{
    homeTitle:"🌌 欢迎来到《灵约》",
    homeDesc:"动漫修仙风格的 5V5 MOBA 竞技游戏<br>踏入灵曜峡谷，召唤强力英雄，展开智慧与操作的对决",
    coreTitle:"🎮 核心玩法",
    heroSystem:"英雄系统",
    heroes:"⚔️ 英雄",
    heroDesc:"25+ 修行英雄<br>难度 · 契合度 · 修为熟练度",
     heroesTitle: "⚔️ 英雄殿堂",
    heroesCount: "当前英雄数量：23 位",
    role: {
      warrior: "战士",
      mage: "法师",
      assassin: "刺客",
      support: "辅助",
      tank: "坦克"
    },
    difficulty: "难度 {stars}",
    mastery: "修为：{value}",
    synergy: "契合度：{value}",
    power: "版本强度：{value}",
    lingxiao:"凌霄剑尊", yueli:"月璃仙姬", xuanying:"玄影", linglu:"灵鹿医者",
    equipSystem:"装备系统",
    gearRune:"🛡 英雄装备与符文",
    gearDesc:"查看装备推荐与符文搭配<br>强化英雄实力",
    seasonTag:"S1 赛季",
    rankTitle:"🏆 修行排位",
    rankDesc:"加星机制 · 表现结算<br>高段位积分制",
    highMatch:"高端对局",
    supremeTitle:"👑 灵尊试炼",
    supremeDesc:"积分累计<br>巅峰强者排行榜",
    recordTag: "战绩",
    recordTitle: "📊 战绩",
    recordDesc: "对局数据 · 英雄表现<br>成长分析",
    platformTitle:"🌍 全平台支持",
    pc:"🖥️ PC",
    pcDesc:"Windows / 云端启动",
    mobile:"📱 Mobile",
    mobileDesc:"Google Play · App Store",
    console:"🎮 主机",
    consoleDesc:"Xbox · Nintendo Switch",
    vr:"🥽 VR",
    vrDesc:"沉浸式观战 / 剧情体验",
    stream:"☁️ Stream",
    streamDesc:"无需下载 · 低配畅玩",
    newsTitle:"📢 游戏资讯",
    noticeTag:"S1",
    noticeTitle:"📜 公告",
    noticeDesc:"初灵启源赛季<br>平衡与更新说明",
    eventTitle:"🎉 活动",
    eventDesc:"限时玩法 · 奖励领取",
    testTag:"体验服",
    testTitle:"🧪 体验服",
    testDesc:"新英雄 · 新机制<br>抢先试玩",
    settingTitle: "⚙️ 设置",
    settingDesc: "语言 · 主题颜色<br>显示与操作",
    moreTitle:"🌟 更多内容",
    communityTag:"玩家互动",
    communityTitle:"💬 社区",
    communityDesc:"玩家讨论 · 攻略分享<br>英雄心得与版本理解",
    officialTag:"世界观",
    officialTitle:"🏢 官方",
    officialDesc:"灵约世界设定<br>阵营 · 势力 · 修行体系",
    footerText:"© 灵约 LingYue · S1 初灵启源<br>公平竞技 · 防外挂系统 · 多端互通",
    title:"⚙️ 游戏设置",
    subtitle:"语言 · 主题 · 显示",
    langTitle:"🌐 语言",
    themeTitle:"🎨 主题颜色",
    tipTitle:"ℹ️ 提示",
    tipText:"所有设置会自动保存，刷新仍然生效。",
    blue:"💙灵约蓝",
    green:"💚青灵绿",
    pink:"💗樱花粉",
    purple:"💜星辉紫"

  },
  en:{
    homeTitle:"🌌 Welcome to LingYue",
    homeDesc:"Anime cultivation 5V5 MOBA<br>Enter the Spirit Canyon and battle with strategy and skill",
    coreTitle:"🎮 Core Gameplay",
    heroSystem:"Hero System",
    heroes:"⚔️ Heroes",
    heroDesc:"25+ Heroes<br>Difficulty · Synergy · Mastery",
    heroesTitle: "⚔️ Hall of Heroes",
    heroesCount: "Current Heroes: 23",
    role: {
      warrior: "Warrior",
      mage: "Mage",
      assassin: "Assassin",
      support: "Support",
      tank: "Tank",
    },

    difficulty: "Difficulty {stars}",
    mastery: "Mastery: {value}",
    synergy: "Synergy: {value}",
    power: "Tier: {value}",
   lingxiao:"LingXiao", yueli:"YueLi", xuanying:"XuanYing", linglu:"LingLu",
  equipSystem:"Equipment System",
    gearRune:"🛡 Equipment & Runes",
    gearDesc:"Build recommendations and rune setup<br>Enhance your power",
    seasonTag:"S1 Season",
    rankTitle:"🏆 Ranked Matches",
    rankDesc:"Star system · Performance scoring<br>High tier points",
    highMatch:"High-Level Matches",
    supremeTitle:"👑 Supreme Trials",
    supremeDesc:"Accumulated points<br>Leaderboard for top players",
    recordTag: "Record",
    recordTitle: "📊 Record",
    recordDesc: "Match data · Hero performance<br>Growth analysis",
    platformTitle:"🌍 Cross Platform",
    pc:"🖥️ PC",
    pcDesc:"Windows / Cloud Launch",
    mobile:"📱 Mobile",
    mobileDesc:"Google Play · App Store",
    console:"🎮 Console",
    consoleDesc:"Xbox · Nintendo Switch",
    vr:"🥽 VR",
    vrDesc:"Immersive spectating / Story mode",
    stream:"☁️ Stream",
    streamDesc:"No download · Low-end friendly",
    newsTitle:"📢 News",
    noticeTag:"S1",
    noticeTitle:"📜 Notice",
    noticeDesc:"Season 1 balance & update notes",
    eventTitle:"🎉 Event",
    eventDesc:"Limited-time gameplay · Rewards",
    testTag:"Test Server",
    testTitle:"🧪 Test Server",
    testDesc:"New heroes · New mechanics<br>Try early",
    settingTitle: "⚙️ Settings",
    settingDesc: "Language · Theme Color<br>Display & Controls",
    moreTitle:"🌟 More Content",
    communityTag:"Community",
    communityTitle:"💬 Community",
    communityDesc:"Player discussions · Guides<br>Hero strategies & meta",
    officialTag:"Lore",
    officialTitle:"🏢 Official",
    officialDesc:"LingYue world lore<br>Factions · Powers · Cultivation system",
    footerText:"© LingYue · Season 1<br>Fair Competition · Anti-cheat · Cross-play",
    title:"⚙️ Settings",
    subtitle:"Language · Theme · Display",
    langTitle:"🌐 Language",
    themeTitle:"🎨 Theme Color",
    tipTitle:"ℹ️ Notice",
    tipText:"All settings are saved automatically.",
    blue:"💙 LingYue Blue",
    green:"💚 Spirit Green",
    pink:"💗 Sakura Pink",
    purple:"💜 Starlight Purple",
  },

  jp:{
    homeTitle:"🌌 霊契へようこそ",
    homeDesc:"アニメ修行系 5V5 MOBA<br>霊曜峡谷に入り、戦略と操作で勝利を掴め",
    coreTitle:"🎮 コアゲームプレイ",
    heroSystem:"ヒーローシステム",
    heroes:"⚔️ ヒーロー",
    heroDesc:"25人以上のヒーロー<br>難易度 · 相性 · 熟練度",
    heroesTitle: "⚔️ 英雄殿堂",
    heroesCount: "現在の英雄数：25 人",
    role: {
      warrior: "戦士",
      mage: "法師",
      assassin: "刺客",
      support: "補助",
      tank: "タンク",
    },
    difficulty: "難易度 {stars}",
    mastery: "修行度：{value}",
    synergy: "相性：{value}",
    power: "評価：{value}",
    lingxiao:"凌霄剣尊", yueli:"月璃仙姫", xuanying:"玄影", linglu:"霊鹿医者",
    equipSystem:"装備システム",
    gearRune:"🛡 装備とルーン",
    gearDesc:"ビルドとルーン構成<br>戦闘力を強化",
    seasonTag:"S1 シーズン",
    rankTitle:"🏆 ランクマッチ",
    rankDesc:"スターシステム · パフォーマンススコア<br>ハイティアポイント",
    highMatch:"ハイレベルマッチ",
    supremeTitle:"👑 至高試練",
    supremeDesc:"ポイント累計<br>トッププレイヤーのランキング",
    recordTag: "戦績",
    recordTitle: "📊 戦績",
    recordDesc: "対戦データ · ヒーローの活躍<br>成長分析",
    platformTitle:"🌍 マルチプラットフォーム",
    pc:"🖥️ PC",
    pcDesc:"Windows / クラウド起動",
    mobile:"📱 モバイル",
    mobileDesc:"Google Play · App Store",
    console:"🎮 コンソール",
    consoleDesc:"Xbox · Nintendo Switch",
    vr:"🥽 VR",
    vrDesc:"没入型観戦 / ストーリーモード",
    stream:"☁️ ストリーム",
    streamDesc:"ダウンロード不要 · 低スペック対応",
    newsTitle:"📢 お知らせ",
    noticeTag:"S1",
    noticeTitle:"📜 お知らせ",
    noticeDesc:"シーズン1 バランス & 更新内容",
    eventTitle:"🎉 イベント",
    eventDesc:"期間限定プレイ · 報酬",
    testTag:"テストサーバー",
    testTitle:"🧪 テストサーバー",
    testDesc:"新ヒーロー · 新メカニクス<br>先行体験",
    settingTitle: "⚙️ 設定",
    settingDesc: "言語 · テーマカラー<br>表示と操作",
    moreTitle:"🌟 その他",
    communityTag:"コミュニティ",
    communityTitle:"💬 コミュニティ",
    communityDesc:"プレイヤーの議論 · ガイド<br>ヒーロー戦略とメタ",
    officialTag:"ロア",
    officialTitle:"🏢 公式",
    officialDesc:"霊契ワールドロア<br>派閥 · 力 · 修行システム",
    footerText:"© 霊契 · シーズン1<br>公平対戦 · アンチチート · クロスプレイ",
    title:"⚙️ 設定",
    subtitle:"言語 · テーマ · 表示",
    langTitle:"🌐 言語",
    themeTitle:"🎨 テーマカラー",
    tipTitle:"ℹ️ ヒント",
    tipText:"設定は自動的に保存されます。",
    blue:"💙 霊契ブルー",
    green:"💚 スピリットグリーン",
    pink:"💗 サクラピンク",
    purple:"💜 スターライトパープル",
  }
};

// =======================
// 当前语言
// =======================
let currentLang = localStorage.getItem("lang") || "zh";

const heroes = [
  {key:"lingxiao", role:"warrior", stars:3, mastery:78, synergy:86, power:"A"},
  {key:"yueli", role:"mage", stars:2, mastery:64, synergy:72, power:"S"},
  {key:"xuanying", role:"assassin", stars:4, mastery:81, synergy:90, power:"S+"},
  {key:"linglu", role:"support", stars:1, mastery:55, synergy:68, power:"A"},
  {key:"huangyue", role:"tank", stars:2, mastery:70, synergy:75, power:"A"},
  {key:"chiyanzun", role:"warrior", stars:3, mastery:82, synergy:88, power:"A"},
  {key:"xingxuan", role:"mage", stars:2, mastery:60, synergy:70, power:"B"},
  {key:"yeyan", role:"assassin", stars:4, mastery:90, synergy:93, power:"S+"},
  {key:"qingluo", role:"support", stars:1, mastery:50, synergy:65, power:"A"},
  {key:"xuanjia", role:"tank", stars:2, mastery:72, synergy:80, power:"A"},
  {key:"fengpo", role:"warrior", stars:3, mastery:76, synergy:82, power:"A"},
  {key:"xueyin", role:"mage", stars:2, mastery:63, synergy:71, power:"A"},
  {key:"wuying", role:"assassin", stars:4, mastery:88, synergy:91, power:"S"},
  {key:"lingyuan", role:"support", stars:1, mastery:52, synergy:67, power:"A"},
  {key:"yankui", role:"tank", stars:2, mastery:74, synergy:83, power:"A"},
  {key:"yanming", role:"warrior", stars:3, mastery:80, synergy:85, power:"S"},
  {key:"xingxi", role:"mage", stars:2, mastery:66, synergy:73, power:"A"},
  {key:"jinye", role:"assassin", stars:4, mastery:92, synergy:94, power:"S+"},
  {key:"yaoling", role:"support", stars:1, mastery:54, synergy:69, power:"A"},
  {key:"shanyue", role:"tank", stars:2, mastery:76, synergy:84, power:"A"},
  {key:"leiheng", role:"warrior", stars:3, mastery:79, synergy:87, power:"A"},
  {key:"huanshu", role:"mage", stars:2, mastery:65, synergy:74, power:"A"},
  {key:"youren", role:"assassin", stars:4, mastery:91, synergy:92, power:"S"},
  {key:"lingze", role:"support", stars:1, mastery:56, synergy:70, power:"A"},
  {key:"juyan", role:"tank", stars:2, mastery:78, synergy:86, power:"A"},
];

/* ========= 新增：读取嵌套语言（关键修复） ========= */
function getLangValue(obj, path){
  return path.split(".").reduce((o,k)=>o && o[k], obj);
}



/* ========= 新增：读取嵌套语言（关键修复） ========= */
function getLangValue(obj, path){
  return path.split(".").reduce((o,k)=>o && o[k], obj);
}

/* ========= 渲染英雄卡片 ========= */
function renderHeroes(lang=currentLang){
  const wrap = document.getElementById("heroes");
  if(!wrap) return;
  wrap.innerHTML="";
  heroes.forEach(h=>{
    const div = document.createElement("div");
    div.className="hero";
    div.innerHTML = `
      <h3>${LANG[lang][h.key] || h.key}</h3>
      <div class="role">${LANG[lang].role[h.role]}</div>
      <div class="info">
        ${LANG[lang].difficulty.replace("{stars}","★".repeat(h.stars))}<br>
        ${LANG[lang].mastery.replace("{value}",h.mastery)} · ${LANG[lang].synergy.replace("{value}",h.synergy)}<br>
        ${LANG[lang].power.replace("{value}",h.power)}
      </div>
    `;
    div.onclick = ()=>showDetail(h, lang);
    wrap.appendChild(div);
  });
}

function showDetail(h, lang=currentLang){
  const dName = document.getElementById("d-name");
  const dInfo = document.getElementById("d-info");
  if(!dName||!dInfo) return;
  dName.innerText = LANG[lang][h.key] || h.key;
  dInfo.innerText = `
职业：${LANG[lang].role[h.role]}
${LANG[lang].difficulty.replace("{stars}","★".repeat(h.stars))}
${LANG[lang].mastery.replace("{value}",h.mastery)}
${LANG[lang].synergy.replace("{value}",h.synergy)}
${LANG[lang].power.replace("{value}",h.power)}
  `;
}

function closeDetail(){
  document.getElementById("detail").style.display="none";
}

/* ========= 全站语言（修复点） ========= */
function applyLang(lang){
  if(!LANG[lang]) return;

  document.querySelectorAll("[data-i18n]").forEach(el=>{
    const key = el.dataset.i18n;
    const value = getLangValue(LANG[lang], key);
    if(value) el.innerHTML = value;
  });

  localStorage.setItem("lang",lang);
  currentLang = lang;
  renderHeroes(lang);
}

/* ========= 页面初始化 ========= */
document.addEventListener("DOMContentLoaded", function(){
  const savedLang = localStorage.getItem("lang")||"zh";
  const savedTheme = localStorage.getItem("theme")||"#7b8cff";

  applyLang(savedLang);
  document.documentElement.style.setProperty('--primary', savedTheme);

  const langSelect = document.getElementById("langSelect");
  if(langSelect){
    langSelect.value = savedLang;
    langSelect.addEventListener("change",function(){
      applyLang(this.value);
    });
  }

  document.querySelectorAll("[data-color]").forEach(btn=>{
    btn.addEventListener("click",function(){
      const color=this.dataset.color;
      document.documentElement.style.setProperty('--primary',color);
      localStorage.setItem("theme",color);
    });
  });
});
function closeDetail(){
  document.getElementById("detail").style.display="none";
}

/* ========= 应用语言 ========= */
function applyLang(lang){
  document.querySelectorAll("[data-i18n]").forEach(el=>{
    const val=getLangValue(LANG[lang],el.dataset.i18n);
    if(val) el.innerHTML=val;
  });
  currentLang=lang;
  localStorage.setItem("lang",lang);
  renderHeroes(lang);
}

/* ========= 初始化 ========= */
document.addEventListener("DOMContentLoaded",()=>{
  const sel=document.getElementById("langSelect");
  sel.value=currentLang;
  sel.onchange=e=>applyLang(e.target.value);
  applyLang(currentLang);
});


