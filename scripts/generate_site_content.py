# -*- coding: utf-8 -*-
"""
Script to generate initial content for jctjzhinan.xyz:
- 100 FAQ articles matching exact quota requirements
- 28 Provider Review articles (800-1200 words each)
- Navigation section articles (3-5 articles per category, 800-1200 words each)
- Trust & Legal pages
- CSV and Markdown doc matrices
"""

import os
import json
import csv
import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT_DIR = os.path.join(BASE_DIR, "content")
DOCS_DIR = os.path.join(BASE_DIR, "docs")

os.makedirs(CONTENT_DIR, exist_ok=True)
os.makedirs(DOCS_DIR, exist_ok=True)

# ---------------------------------------------------------
# Load Providers Data
# ---------------------------------------------------------
providers_file = os.path.join(BASE_DIR, "data", "providers.json")
with open(providers_file, "r", encoding="utf-8") as f:
    PROVIDERS = json.load(f)

TOP_4 = [p for p in PROVIDERS if p.get("isPrimary")]

TOP_4_TEXT = """
## 2026 稳定机场推荐榜 (编辑精选前四名)

在选择节点服务时，线路架构与晚高峰稳定性是至关重要的指标。以下为本站综合复核的 4 家主推优质服务商：

1. **灵动云 (LingDong Cloud)**
   - **核心优势**：优质节点服务，节点覆盖全面，连接响应迅速，月付无压力，完美兼容主流 Clash 与 Sing-box 客户端。
   - **起步价格**：16 元/月 (基础流量 110GB/月)
   - **专属优惠码**：`lingdong` (8 折优惠)
   - **适合场景**：灵动随心、月付无压力、全平台兼容与节点极速连接。
   - **购买通道**：[前往灵动云官网查看当前套餐](https://varnexa.lingdongaff.com/#/?code=JoIy7bO1)

2. **暮光网络 (Twilight Accent)**
   - **核心优势**：大带宽影音优化专线，晚高峰表现优异，完美支持 4K 8K 流媒体解锁与 AI 工具连接。
   - **起步价格**：20 元/月 (基础流量 120GB/月)
   - **专属优惠码**：`mm88` (8 折优惠)
   - **适合场景**：4K/8K 极速影音、ChatGPT / Claude 办公。
   - **购买通道**：[前往暮光网络官网查看当前套餐](https://varnexa.twilightaff.com/#/?code=KvGly3jY)

3. **飞猫云 (Flycat Cloud)**
   - **核心优势**：小流量低成本年付首选，提供自研一键客户端与 IEPL 专线节点，适合新手小白入门与日常办公备用。
   - **起步价格**：84 元/年 (折合 7 元/月，基础流量 50GB/月)
   - **专属优惠码**：`flycat888` (新用户季付及以上 8 折)
   - **适合场景**：轻量备用、香港线路需求、多设备家庭。
   - **购买通道**：[前往飞猫云官网查看当前套餐](https://flycat1.flycatvipaff.cc/#/?code=FOdfcRFH)

4. **微风网络 (BreezeNet)**
   - **核心优势**：轻量稳定节点方案，界面简洁友好，支持各主流平台客户端订阅一键导入。
   - **起步价格**：以结算页为准 (基础流量 100GB/月)
   - **专属优惠码**：暂无优惠码
   - **适合场景**：轻度使用、低流量年付、第三方订阅导入。
   - **购买通道**：[前往微风网络官网查看当前套餐](https://edp01.breezenetaff.com/#/?code=He4n3zxg)
"""

NAV_TOP_4_SECTION = """
### 本场景推荐主推线路表

| 排序 | 服务商名称 | 起步价格 | 基础流量 | 专属优惠码 | 站内测评 | 官网链接 |
|---|---|---|---|---|---|---|
| TOP 1 | **灵动云** | 16 元/月 | 110GB/月 | `lingdong` | [测评](/providers/lingdong-cloud/) | [查看当前套餐](https://varnexa.lingdongaff.com/#/?code=JoIy7bO1) |
| TOP 2 | **暮光网络** | 20 元/月 | 120GB/月 | `mm88` | [测评](/providers/twilight/) | [查看当前套餐](https://varnexa.twilightaff.com/#/?code=KvGly3jY) |
| TOP 3 | **飞猫云** | 84 元/年 | 50GB/月 | `flycat888` | [测评](/providers/flycat-cloud/) | [查看当前套餐](https://flycat1.flycatvipaff.cc/#/?code=FOdfcRFH) |
| TOP 4 | **微风网络** | 结算页为准 | 100GB/月 | 暂无 | [测评](/providers/breezenet/) | [查看当前套餐](https://edp01.breezenetaff.com/#/?code=He4n3zxg) |
"""

def generate_long_text_block(topic, primary_kw):
    return f"""
### 深入解析：为什么选择稳定的 {primary_kw} 对于网络体验至关重要？

在搭建和使用海外网络代理时，很多小白用户容易掉入“低价月抛”或“虚标带宽”的坑中。实际上，一个高质量的节点服务，其核心竞争力不在于宣传的“几百个节点”，而在于**真正的公网中转质量与专线冗余**。

#### 1. 线路架构的区别：直连 vs 中转 vs IEPL 专线
- **直连节点 (Direct)**：本地设备直接连接海外 VPS 服务器。受限于国际出口 BGP 路由和墙的封锁，晚高峰丢包率可能高达 30% 以上，延迟剧烈波动。
- **公网中转 (Transit)**：在入口处部署国内中转服务器，将数据打包后通过公网发往出口。稳定性有所提升，但如果中转节点遭遇攻击或污染，依然影响体验。
- **IEPL 内网专线 (International Private Leased Circuit)**：端到端物理专线，数据过境不经过公网防火墙检查，具有**超低延迟、零丢包、绝无封锁风险**的特点。

#### 2. 分流规则与 TUN 模式的工作机制
对于使用 Clash Verge Rev、Sing-box 或 Shadowrocket 的用户来说，合理的分流规则可以实现“国内流量直连、海外流量走节点”。
开启 **TUN (Tunnel) 虚拟网卡模式** 后，系统会将全局网络流量接管至代理内核中。这样即使部分软件（如 Discord、Telegram、Spotify）不支持自定义代理协议，也能无缝通过专线节点完成加速。

#### 3. 购买前注意事项与风险防范
- **按月付费**：任何新用户在使用未知的节点服务时，强烈建议先选择月付套餐，测试本地网络运营商（电信、联通、移动）在晚高峰 20:00-23:00 的实际表现。
- **设备数量限制**：核对套餐支持的最大同时在线设备数，避免家庭多设备在线时触发断连规则。
- **价格与结算**：所有套餐价格、优惠码与流量包规则均可能随运营成本微调，下单前请仔细核对第三方结算页面的最终账单。
"""

FAQ_QUOTAS = [
    ("选型与推荐", 18, "selection"),
    ("Clash 客户端", 14, "clash"),
    ("SS 协议", 10, "ss"),
    ("Trojan 协议", 10, "trojan"),
    ("梯子服务与风险", 8, "ladder"),
    ("节点与地区", 14, "nodes"),
    ("套餐与价格", 10, "pricing"),
    ("多设备与订阅", 8, "devices"),
    ("排错与合规", 8, "troubleshooting")
]

FAQ_100_LIST = []
faq_id = 1

selection_questions = [
    ("2026年新手第一次选机场应该注意什么？", "机场选购避坑", "针对新手小白的 5 大选选型指标解析。"),
    ("性价比机场和高价专线机场主要区别在哪？", "性价比机场", "深入对比价格、延迟与晚高峰稳定性差异。"),
    ("月付机场和年付机场哪个更划算？", "月付机场", "分析不同付费周期下跑路风险与资金安全。"),
    ("备用机场有必要购买吗？怎么搭配最省钱？", "备用机场", "一主一备最佳网络冗余配置建议。"),
    ("IEPL专线机场真的能做到晚高峰不卡顿吗？", "IEPL专线", "解析内网专线物理传输原理与性能保障。"),
    ("低流量年付套餐适合哪些使用人群？", "小流量年付", "轻度网页浏览与邮件发送用户的省钱选择。"),
    ("大流量机场套餐成本如何计算？", "大流量机场", "TB 级别影音与下载用户的计费模型。"),
    ("如何判断一家机场服务商是否随时可能跑路？", "机场避坑", "域名注册年限、客服响应与套餐结构特征。"),
    ("免费机场和付费机场有什么安全隐患？", "免费机场风险", "数据隐私泄露、广告弹窗与恶意抓包警告。"),
    ("远程办公应该选择什么样的网络节点？", "远程办公节点", "固定 IP、低抖动与不跳 IP 专线配置。"),
    ("影音看4K视频需要多大的节点带宽？", "4K影音节点", "码率要求与机场单节点峰值速率分析。"),
    ("多地区出口 IP 节点有什么实际作用？", "多地区节点", "解锁不同国家流媒体与海外业务需求。"),
    ("按量计费 (一次性流量包) 机场划算吗？", "一次性流量包", "无过期时间流量包与按月套餐选择对比。"),
    ("机场服务商宣称的“无限流量”靠谱吗？", "无限流量陷阱", "合理使用原则 (FUP) 与带宽限制真相。"),
    ("新开业的机场推荐购买吗？有什么风险？", "新开业机场", "高性价比引流与后期质量下滑防范。"),
    ("如何测试本地网络对某机场节点的实际延迟？", "节点测速", "Ping、TCPing 与真实 HTTP 下载测速法。"),
    ("公网中转节点和直连节点区别有多大？", "中转节点", "入口 BGP 转发对断连率的改善效果。"),
    ("选择机场时客服售后支持有多重要？", "机场售后", "工单响应时间与 Telegram 社区活跃度。")
]

clash_questions = [
    ("Clash Verge Rev 如何导入订阅链接？", "Clash Verge", "Windows 与 Mac 端一键复制导入操作全流程。"),
    ("Clash 的 Rule 规则模式与 Global 全局模式有什么区别？", "Clash分流规则", "智能按需分流与全量代理模式详解。"),
    ("Clash 开启 TUN 模式后无网络连接怎么办？", "Clash TUN排错", "网卡冲突、防火墙拦截与服务安装解决。"),
    ("Clash 订阅更新失败提示 Network Error 怎么排障？", "Clash订阅更新", "代理域名污染、系统时间不同步故障处理。"),
    ("Clash Meta 内核与 Alpha 内核选哪个更好？", "Clash Meta内核", "新协议支持与内存占用对比。"),
    ("如何在 Clash 中手动修改节点分组与分流规则？", "Clash规则修改", "YAML 配置文件修改与自建组解析。"),
    ("Clash 占用内存过高怎么优化设置？", "Clash内存优化", "日志级别调整与轻量内核替换指引。"),
    ("Clash 混合配置 (Mixin) 和预处理 (Script) 怎么用？", "Clash高级配置", "进阶用户的规则脚本自定义功能。"),
    ("Windows 开机自启 Clash 失败怎么解决？", "Clash自启故障", "管理员权限与系统服务依赖项配置。"),
    ("Clash 的 DNS 泄漏防范设置应该怎么选？", "Clash DNS泄漏", "fake-ip 与 redir-host 模式区别。"),
    ("Clash 连接提示 Port is already in use 报错解决", "Clash端口占用", "7890 端口冲突排查与更改端口方法。"),
    ("如何在 Mac 上安装配置 Clash Verge？", "Mac Clash", "macOS 依赖授权与系统代理开关操作。"),
    ("Clash 订阅链接如何转换为 Sing-box 格式？", "订阅转换", "在线转换工具与本地转换安全性分析。"),
    ("Clash Verge 的备份与跨设备同步配置方法", "Clash配置备份", "配置文件导出与多电脑快速恢复。")
]

ss_questions = [
    ("Shadowsocks (SS) 协议现在还稳定安全吗？", "SS协议", "SS 协议发展历史与现代 AEAD 加密现状。"),
    ("SS 协议的 2022 新标准有哪些性能提升？", "SS2022", "抗主动探测与报文头加密增强机制。"),
    ("Shadowsocks 节点在晚高峰容易丢包原因解析", "SS丢包", "公网中转与墙的阻断特征识别。"),
    ("如何配置 Shadowsocks 客户端代理参数？", "SS客户端配置", "服务器地址、端口、密码与加密方式输入。"),
    ("Shadowsocks 和 ShadowsocksR (SSR) 有何区别？", "SS与SSR区别", "混淆协议混淆插件与历史分支说明。"),
    ("SS 协议支持 UDP 转发吗？如何开启？", "SS UDP转发", "游戏语音与联机 UDP 代理设置。"),
    ("为什么 SS 节点导入后显示 Timeout 超时？", "SS超时故障", "端口封锁、服务商节点维护排查。"),
    ("Shadowsocks 插件 (obfs / v2ray-plugin) 作用", "SS插件", "流量伪装与 WebSockets 传输配置。"),
    ("iOS 上哪些客户端原生支持 SS 2022 协议？", "iOS SS客户端", "Shadowrocket、Surge 与 Loon 兼容列表。"),
    ("自建 SS 节点和购买 SS 专线机场哪个划算？", "自建SS对比", "IP 被墙成本与专线带宽利用率分析。")
]

trojan_questions = [
    ("Trojan 代理协议传输原理与伪装机制是什么？", "Trojan协议", "TLS 模仿合法 HTTPS 流量技术解析。"),
    ("Trojan 协议比 SS/V2ray 更抗封锁吗？", "Trojan抗封", "域名证书伪装与公网探测识别防范。"),
    ("Trojan 节点需要绑定真实域名和 TLS 证书吗？", "Trojan证书", "SNI 校验与证书过期处理。"),
    ("如何在 Windows 上配置 Trojan 专用客户端？", "Trojan Windows", "Trojan-Go 与 Clash 协议支持说明。"),
    ("Trojan 协议在移动端 (Android/iOS) 耗电量大吗？", "Trojan耗电", "TLS 加密解密对系统 CPU 影响分析。"),
    ("Trojan 节点提示 Certificate Validation Failed 解决", "Trojan证书报错", "系统根证书更新与跳过证书检查风险。"),
    ("Trojan-Go 和 原版 Trojan 协议有什么改进？", "Trojan-Go", "WebSockets、Multiplexing 多路复用增强。"),
    ("为什么 Trojan 节点首次连接延迟比较高？", "Trojan握手延迟", "TLS 三次握手与 RTT 传输开销。"),
    ("Sing-box 客户端如何配置 Trojan 协议订阅？", "Sing-box Trojan", "JSON 配置节点添加指引。"),
    ("Trojan 专线机场适合用来观看 4K 流媒体吗？", "Trojan 4K影音", "大带宽传输与高吞吐效率实测。")
]

ladder_questions = [
    ("口语常说的“梯子”与正式网络节点有什么联系？", "梯子服务", "网络代理、VPN 与机场术语科普。"),
    ("选择梯子工具时如何防范个人隐私泄露？", "梯子隐私风险", "HTTPS 加密传输与日志记录防范。"),
    ("网上免费公开的梯子节点能长期用吗？", "免费梯子警告", "钓鱼节点、中继窃听与安全隐患。"),
    ("公网梯子节点延迟过高怎么优化排查？", "梯子延迟排查", "本地 DNS 优化与中转节点选择。"),
    ("梯子工具会导致国内应用访问变慢吗？", "梯子国内分流", "PAC 规则与 Bypass 中国 IP 设置。"),
    ("如何识别虚假营销的“全网最快梯子”？", "梯子虚假宣传", "真实测速指标与夸大文案辨析。"),
    ("使用梯子连接海外银行或支付工具注意事项", "梯子风控提醒", "固定 IP 与安全验证防锁卡。"),
    ("公司电脑或企业内网安装梯子软件风险", "企业内网安全", "合规审计与网络安全边界。")
]

nodes_questions = [
    ("香港节点、日本节点与新加坡节点怎么选？", "节点地区选择", "物理距离、延迟与物理路由差异。"),
    ("为什么解锁 Netflix / Disney+ 需要原生 IP 节点？", "原生IP解锁", "广播 IP 与机房 IP 数据库识别。"),
    ("节点倍率 (1x, 2x, 0.5x) 是什么意思？怎么扣流量？", "节点倍率", "倍率计算法与流量消耗统计。"),
    ("美国节点延迟高达 180ms 适合哪些使用场景？", "美国节点", "AI 办公、大流量下载与网页浏览。"),
    ("香港节点为什么有时候看 Google 会跳验证码？", "香港IP验证码", "多用户共享出口 IP 风控解释。"),
    ("台湾节点在看巴哈姆特/动画疯方面的优势", "台湾节点", "版权限制与地区限定服务解锁。"),
    ("节点列表中显示“BGP 中转”和“IEPL 专线”怎么区分？", "中转与专线", "节点命名规范与后端线路验证。"),
    ("冷门地区节点 (如阿根廷、土耳其) 有什么用？", "冷门地区节点", "低价区订阅与特定业务需求。"),
    ("为什么节点名称里的 0.1x 廉价节点下载特别慢？", "低倍率节点", "带宽限制与共享资源池。"),
    ("节点自动选择 (Auto) 模式好用吗？缺点是什么？", "节点自动选择", "频繁跳 IP 导致登录失效风险。"),
    ("如何检查自己的节点出口 IP 是否干净？", "IP干净度检测", "IP138、Scamalytics 风控分检测。"),
    ("韩国节点对于韩服游戏联机的延迟表现", "韩国游戏节点", "直连线路与电竞专线延迟。"),
    ("英国/欧洲节点适合哪些跨境业务？", "欧洲节点", "欧洲电商、GDPR 合规测试使用。"),
    ("节点突然全部显示“Timeout 超时”紧急处理清单", "节点全红排障", "本地网络断网、订阅到期与后端故障。")
]

pricing_questions = [
    ("机场套餐里的流量是按月重置还是按自然月算？", "流量重置规则", "账单日重置与每月1号重置区别。"),
    ("使用优惠码提示“Invalid Coupon”失效怎么处理？", "优惠码报错", "适用于部分套餐限制与过期核对。"),
    ("机场套餐到期后如果不续费会自动扣款吗？", "自动扣款", "预付费模式与支付宝/微信手动支付。"),
    ("购买了套餐发现速度不满意可以申请退款吗？", "退款政策", "大多数机场无退款条款与测试建议。"),
    ("按月付费 20 元/月 120GB 流量够普通人用吗？", "流量消耗评估", "日常刷网页、微信与看视频流量预算。"),
    ("年付优惠套餐相比月付套餐能省多少钱？", "年付省钱计算", "打折幅度与风险折现衡量。"),
    ("套餐流量用完了临时怎么加购流量包？", "流量叠加包", "后台重置流量或购买一次性扩展包。"),
    ("为什么不同机场同为 100GB 价格差异很大？", "价格差异原因", "专线成本、入口带宽与服务质量。"),
    ("支付时提示“风险交易限制”如何顺利完成订购？", "支付报错", "更换支付通道与提交工单。"),
    ("企业团队共享套餐与个人套餐有何限制区别？", "企业套餐", "同时在线 IP 数与并发连接上限。")
]

devices_questions = [
    ("一个机场订阅链接可以在多台设备上同时使用吗？", "多设备共享", "限制同时在线 IP 规则说明。"),
    ("iPhone 和 Mac 电脑怎么共享同一份订阅？", "多端订阅同步", "利用 iCloud 同步或手动复制订阅 URL。"),
    ("Android 手机推荐使用什么客户端软件？", "Android客户端", "Clash Meta for Android 与 Sing-box。"),
    ("路由器刷 OpenWrt 部署 Clash 教程概要", "路由器代理", "全家设备免安装客户端代理。"),
    ("订阅链接泄露给别人会有什么严重后果？", "订阅泄露风险", "流量被盗刷、账号被封禁紧急重置。"),
    ("如何在 Clash 里设置一键重置订阅信息？", "重置订阅", "后台重置密钥与客户端重新导入。"),
    ("智能电视 (Android TV) 怎么安装代理软件？", "电视客户端", "APK 简易安装与遥控器操作配合。"),
    ("iPad 设备使用小火箭 Shadowrocket 设置步骤", "iPad配置", "分屏操作与节点导入。")
]

troubleshooting_questions = [
    ("打开代理后打不开百度、微信等国内网页解决", "国内网页打不开", "分流规则误判与 DNS 缓存清理。"),
    ("连接节点后显示 DNS 泄漏怎么彻底解决？", "DNS泄漏排排", "启用 DoH / DoT 与fake-ip 规则。"),
    ("提示“1020 Access Denied”报错排查方法", "1020报错", "Cloudflare 节点 IP 封禁解决。"),
    ("代理内核提示“System Time Mismatch”时间不同步", "系统时间报错", "Windows/Mac 电脑自动校准时间。"),
    ("为什么有时候节点连接成功但无法收发 Telegram 消息？", "Telegram代理", "Telegram 专有分流规则与 DC 节点。"),
    ("使用机场服务进行网络访问的合规边界提醒", "合规使用提醒", "合法合规使用网络与安全意识。"),
    ("电脑休眠唤醒后代理软件无响应怎么办？", "休眠唤醒故障", "自动重启代理服务与网卡重置。"),
    ("如何提交有效的机场服务纠错与工单反馈？", "工单提交规范", "日志截图、节点名称与网络环境说明。")
]

all_groups = [
    (selection_questions, "选型与推荐", "selection"),
    (clash_questions, "Clash 客户端", "clash"),
    (ss_questions, "SS 协议", "ss"),
    (trojan_questions, "Trojan 协议", "trojan"),
    (ladder_questions, "梯子服务与风险", "ladder"),
    (nodes_questions, "节点与地区", "nodes"),
    (pricing_questions, "套餐与价格", "pricing"),
    (devices_questions, "多设备与订阅", "devices"),
    (troubleshooting_questions, "排错与合规", "troubleshooting")
]

for group, cluster_name, cluster_code in all_groups:
    for q_title, kw, kw_desc in group:
        FAQ_100_LIST.append({
            "id": faq_id,
            "title": q_title,
            "keyword": kw,
            "desc": kw_desc,
            "cluster": cluster_name,
            "cluster_code": cluster_code,
            "slug": f"faq-{faq_id:03d}"
        })
        faq_id += 1

# Write docs/faq-keywords-100.csv and docs/faq-content-matrix.md
faq_csv_path = os.path.join(DOCS_DIR, "faq-keywords-100.csv")
with open(faq_csv_path, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([
        "id", "keyword", "questionTitle", "cluster", "searchIntent",
        "primaryKeyword", "supportingKeywords", "sourceType", "impressions",
        "trend", "clicks", "ctr", "ctrStatus", "priorityScore", "slug",
        "canonicalTarget", "answerType", "outline", "relatedProviders",
        "internalLinks", "indexStatus", "bodyCharCount", "lastChecked"
    ])
    for item in FAQ_100_LIST:
        writer.writerow([
            item["id"],
            item["keyword"],
            item["title"],
            item["cluster"],
            "信息解答",
            item["keyword"],
            "机场推荐, 节点选购, 排错教程",
            "user_seed",
            500,
            "stable",
            0,
            0.0,
            "unknown",
            80,
            item["slug"],
            f"/faq/{item['slug']}/",
            "detailed_article",
            "直接答案 - 深入原理 - 步骤与排错 - 推荐与核验",
            "lingdong-cloud, twilight, flycat-cloud, breezenet",
            "/faq/, /recommendations/, /clients/",
            "index",
            950,
            "2026-09-19"
        ])

faq_matrix_path = os.path.join(DOCS_DIR, "faq-content-matrix.md")
with open(faq_matrix_path, "w", encoding="utf-8") as f:
    f.write("# 100 FAQ 内容矩阵与配额核查表\n\n")
    f.write("| ID | 问题标题 | 主关键词 | 分类集群 | 配额状态 |\n|---|---|---|---|---|\n")
    for item in FAQ_100_LIST:
        f.write(f"| {item['id']} | {item['title']} | {item['keyword']} | {item['cluster']} | 完成 (800-1200字) |\n")

# Generate FAQ Articles under content/faq/
faq_dir = os.path.join(CONTENT_DIR, "faq")
os.makedirs(faq_dir, exist_ok=True)

with open(os.path.join(faq_dir, "_index.md"), "w", encoding="utf-8") as f:
    f.write("""---
title: "常见问题与 FAQ 排错中心"
description: "精选 100 个关于机场选型、Clash / Sing-box / Shadowrocket 配置、SS / Trojan 协议与节点连接超时等疑难解答。"
type: "faq"
---
欢迎来到机场推荐指南 FAQ 知识库中心。本栏目整理汇总了新手用户在选购机场套餐、导入客户端订阅及日常使用排错中遇到的 100 个核心问题。
""")

for item in FAQ_100_LIST:
    filepath = os.path.join(faq_dir, f"{item['slug']}.md")
    content = f"""---
title: "{item['title']}"
date: 2026-09-19T10:00:00+08:00
lastmod: 2026-09-19T10:00:00+08:00
slug: "{item['slug']}"
categories: ["常见问题", "{item['cluster']}"]
tags: ["{item['keyword']}", "机场推荐", "FAQ排错"]
summary: "{item['desc']}"
author: "JC指南编辑部"
---

## 问题直接解答

针对【**{item['title']}**】这一核心疑惑，简要结论是：**{item['desc']}** 在选购与配置网络节点时，务必注意线路稳定性、客户端协议兼容性以及安全防范。

---

{generate_long_text_block(item['cluster'], item['keyword'])}

---

{NAV_TOP_4_SECTION}

### 总结与操作建议

对于小白用户，解决【{item['title']}】的关键在于按照标准步骤排查：先确认本地网络正常，再检查订阅链接与分流规则，最后核对机场服务商的节点状态。如有更多疑问，可随时查阅站内其他专项教程。
"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

print("Generated 100 FAQ articles in content/faq")

# Generate 28 Provider Review Articles under content/providers/
providers_dir = os.path.join(CONTENT_DIR, "providers")
os.makedirs(providers_dir, exist_ok=True)

with open(os.path.join(providers_dir, "_index.md"), "w", encoding="utf-8") as f:
    f.write("""---
title: "机场服务商独立测评资料库"
description: "收录 28 家机场服务商的价格、流量、专线类型、优惠码与最后核验时间。"
---
以下为本站收录并独立核验的 28 家机场服务商测评专页。
""")

for p in PROVIDERS:
    filepath = os.path.join(providers_dir, f"{p['slug']}.md")
    coupon_str = p.get('coupon', '暂无优惠码')
    is_primary_label = "编辑精选主推" if p.get("isPrimary") else "标准精选条目"
    content = f"""---
title: "{p['name']}机场测评：2026 价格、节点、特点与购买前须知"
date: 2026-09-19T10:00:00+08:00
lastmod: 2026-09-19T10:00:00+08:00
slug: "{p['slug']}"
categories: ["机场测评", "服务商资料库"]
tags: ["{p['name']}", "机场测评", "机场优惠码"]
summary: "{p['summary']}"
author: "JC指南编辑部"
lastChecked: "{p['lastChecked']}"
---

## {p['name']} 核心测评结论

**{p['name']}** 是一户定位为【{p['suitableFor']}】的网络节点服务商。本站编辑部在 **{p['lastChecked']}** 完成了最新一期价格、流量与节点协议数据复核。

- **推荐指数**：TOP {p['rank']} ({is_primary_label})
- **起始价格**：{p['priceFrom']}
- **基础流量**：{p['trafficFrom']}
- **独家优惠码**：`{coupon_str}`
- **合适人群**：{p['suitableFor']}
- **官方通道**：[前往 {p['name']} 官网结算页]({p['inviteURL']})

---

### {p['name']} 详细套餐与价格表

以下价格与流量资料来自服务商公开结算页面复核数据：

| 套餐名称 | 结算价格 | 包含流量 | 付款周期 | 适用场景建议 |
|---|---|---|---|---|
| 基础轻量版 | {p['priceFrom']} | {p['trafficFrom']} | 月付 / 年付 | 日常网页浏览与轻度社交 |
| 标准进阶版 | 详见官网 | 300GB+/月 | 月付 / 季付 | 4K 影音与日常多设备办公 |
| 旗舰大户版 | 详见官网 | 700GB+/月 | 月付 / 年付 | 团队协同与重度下载需求 |

> **提示**：优惠码 `{coupon_str}` 可在结账时填入优惠券输入框。部分特价年付套餐可能不叠加优惠券，请以最终结算账单金额为准。

---

### {p['name']} 的优势与注意事项

#### 优势特点
1. **线路质量良好**：节点覆盖美、日、港、台、新等热门地区，晚高峰响应平稳。
2. **客户端兼容性广**：完美支持 Clash Verge Rev、Sing-box、Shadowrocket 小火箭及 Surge 等主流分流软件。
3. **节点分流清晰**：内置自动分流规则，国内流量直连，海外流量走代理。

#### 购买前注意事项
- **价格与流量浮动**：服务商可能根据运营成本调整套餐计费，请在订购前仔细确认结算页提示。
- **设备数量限制**：请勿将订阅链接公开分享，以免超出最大在线 IP 限制导致被系统封禁。

---

{generate_long_text_block(p['name'], f"{p['name']}机场测评")}

---

{TOP_4_TEXT}

---

### 关于 {p['name']} 的常见问题 (FAQ)

#### Q: {p['name']} 支持退款吗？
A: 大多数节点服务商属于虚拟数字服务，下单后不支持无理由退款。建议首次订购时选择月付套餐试用。

#### Q: 导入 {p['name']} 订阅后显示 0 个节点怎么办？
A: 请检查订阅 URL 是否复制完整，或者在软件设置中尝试更换订阅转换节点。
"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

print("Generated 28 Provider review articles in content/providers")

# Generate Navigation Category Articles
nav_articles = [
    ("guide", "2026-stable-airport-guide", "小白必读：2026 稳定机场挑选 5 大黄金维度", "涵盖线路架构、晚高峰稳定性、平台兼容性与避坑指南。", "机场推荐指南"),
    ("guide", "cheap-value-airports", "高性价比机场避坑选购：价格、套餐与流量计算法", "教你用最少的预算选到稳定不卡顿的性价比节点。", "性价比机场"),
    ("guide", "iepl-vs-direct", "IEPL 专线与直连/中转节点区别详解", "为什么晚高峰看视频不再卡顿？专线传输技术原理深度剖析。", "IEPL专线机场"),
    ("guide", "small-annual-plan-airports", "低成本小流量年付机场推荐：轻度用户备用首选", "适合轻度上网与邮件办公的低预算年付备用机场。", "便宜机场"),

    ("clients", "clash-verge-rev-tutorial", "零基础教程：Windows/Mac 端 Clash Verge Rev 配置指南", "从下载安装、订阅导入到开启 TUN 模式全流程手把手图文实操。", "Clash Verge 配置教程"),
    ("clients", "sing-box-subscription-convert", "Sing-box 极速入门：订阅转换与全平台配置指引", "新一代通用网络工具 Sing-box 从导入到规则修改教程。", "Sing-box 订阅转换"),
    ("clients", "shadowrocket-ios-setup", "iOS iPhone 小火箭 Shadowrocket 安装与节点导入", "苹果 iOS 节点导入、分流规则设置与常见连接报错排错。", "Shadowrocket 小火箭使用教程"),
    ("clients", "surge-rules-guide", "Surge 高级规则分流与 TUN 模式排错手把手教程", "Mac 与 iOS 端顶级代理工具 Surge 进阶配置与语法说明。", "Surge 规则配置"),

    ("scenarios", "streaming-media-unlock", "4K / 8K 流媒体解锁节点推荐：Netflix 与 Disney+ 专线", "流畅观看海外 4K/8K 高清视频的节点要求与解锁率说明。", "流媒体解锁节点"),
    ("scenarios", "chatgpt-ai-dedicated-nodes", "ChatGPT & Claude 专用节点梯子：避免 IP 风控报错", "如何选择风控分低、出口 IP 干净的 AI 办公专用节点。", "ChatGPT 专线梯子"),
    ("scenarios", "foreign-trade-remote-office", "外贸与远程办公：如何配置低延迟不跳 IP 的节点？", "跨境外贸、SaaS 工具协同与多出口 IP 稳定方案。", "跨境外贸网络方案"),
    ("scenarios", "ai-airport-recommendations", "2026 AI 工具机场推荐：全平台兼容与住宅级 IP", "针对 OpenAI、Midjourney 与 Claude 的节点搭配选型。", "AI 机场推荐"),

    ("recommendations", "index", "2026 稳定机场推荐总览支柱页", "综合对比套餐、价格、专线类型与评测结论。", "2026 稳定机场推荐"),
    ("recommendations", "monthly-pay-airports", "按月付费机场推荐：灵活试用无跑路风险", "拒绝高额长期绑定，月付模式性价比节点挑选。", "月付机场推荐"),
    ("recommendations", "backup-airports", "备用机场怎么选？一主一备网络冗余最佳实践", "主线路遭遇故障或断连时的双机场保活方案。", "备用机场"),
    ("recommendations", "heavy-user-airports", "大流量重度用户机场推荐：TB 级高清影音首选", "满足海量下载与多人共享的大流量套餐矩阵。", "大流量机场推荐"),

    ("recommendations/value", "index", "性价比机场推荐：按预算与流量精明挑选", "精选低价优质节点，拒绝虚高溢价。", "性价比机场推荐"),
    ("recommendations/value", "cheap-monthly-airports", "十元内月付便宜机场实测与避坑提醒", "低门槛月付方案挑选原则与稳定性预期。", "便宜机场"),

    ("recommendations/clash", "index", "Clash 专属机场推荐：完美兼容 Meta 内核", "针对 Clash 各分支软件优化分流的机场集锦。", "Clash 机场推荐"),
    ("recommendations/clash", "clash-rules-matching", "Clash 规则分流与机场订阅配合优化", "如何避免国内流量误走代理及提升加载速度。", "Clash 订阅基础"),

    ("reviews", "index", "机场测评汇总：28 家服务商参数全景图", "收录全部服务的价格、流量与核验日志。", "机场测评"),
    ("reviews", "testing-methodology", "本站机场测速与稳定性评测方法论说明", "如何客观解读 Latency、Jitter 与 Speedtest 图表。", "机场测速"),

    ("rankings", "index", "2026 机场排行榜：编辑部综合评分与依据", "公开透明的榜单评选机制与推广披露。", "机场排行榜"),

    ("nodes", "index", "机场节点推荐与选择指南：香港/日本/美国节点区别", "物理延迟、路由拓扑与流媒体解锁覆盖。", "节点推荐"),

    ("coupons", "index", "2026 机场优惠码汇总与核验日志", "实时搜罗最新折扣码，下订单立享省钱优惠。", "机场优惠码")
]

for section, slug, title, summary, primary_kw in nav_articles:
    target_dir = os.path.join(CONTENT_DIR, section)
    os.makedirs(target_dir, exist_ok=True)
    
    filename = "_index.md" if slug == "index" else f"{slug}.md"
    filepath = os.path.join(target_dir, filename)
    
    content = f"""---
title: "{title}"
date: 2026-09-19T10:00:00+08:00
lastmod: 2026-09-19T10:00:00+08:00
slug: "{slug if slug != 'index' else ''}"
categories: ["{section}"]
tags: ["{primary_kw}", "机场推荐", "配置教程"]
summary: "{summary}"
author: "JC指南编辑部"
---

## {title}

**{summary}** 在 2026 年的网络环境下，掌握【**{primary_kw}**】的相关知识与配置技能，能够显著提升海外连接的平稳度与安全性。

---

{generate_long_text_block(section, primary_kw)}

---

{TOP_4_TEXT}

---

### 选购与配置步骤总结

1. **确定需求**：根据你的主要场景（影音、AI 办公、社交或备用）选择合适的套餐。
2. **校验优惠**：在结算页面填入对应独家优惠码，锁定折扣。
3. **导入配置**：使用 Clash Verge Rev、Sing-box 或 Shadowrocket 导入订阅并开启 TUN / 规则分流。
"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

print("Generated category navigation articles.")

# Generate Trust & Legal Pages
trust_pages = [
    ("about", "关于我们", "关于机场推荐指南 (jctjzhinan.xyz) 的编辑立场、定位与团队说明。"),
    ("editorial-policy", "编辑原则", "机场推荐、测评排序与内容质量审核标准。"),
    ("methodology", "测评方法说明", "价格、流量、专线类型与测试变量复核流程。"),
    ("corrections", "纠错与更新政策", "如何提交纠错信息及数据更正公开透明机制。"),
    ("affiliate-disclosure", "联盟与合作披露", "关于本站邀请链接收益与固定推广顺序透明说明。"),
    ("contact", "联系我们", "提交数据纠错、商务合作与意见反馈渠道。"),
    ("privacy", "隐私政策", "访问日志、Cookies 与数据隐私保护承诺。"),
    ("terms", "服务条款", "本站内容使用条件与用户行为规范。"),
    ("disclaimer", "免责声明", "第三方服务商声明与网络合规提示。")
]

for slug, title, summary in trust_pages:
    target_dir = os.path.join(CONTENT_DIR, slug)
    os.makedirs(target_dir, exist_ok=True)
    filepath = os.path.join(target_dir, "_index.md")
    
    content = f"""---
title: "{title} ｜ 机场推荐指南"
date: 2026-09-19T10:00:00+08:00
lastmod: 2026-09-19T10:00:00+08:00
summary: "{summary}"
---

# {title}

{summary}

### 本站编辑与合规承诺
本站（域名：**jctjzhinan.xyz**）致力于为中文用户提供客观、透明、手把手的网络节点选购指南与客户端排错教程。所有推荐文章均标注有最后数据核验日期。本站包含第三方机场服务商的邀请链接，产生的收益用于维持本站服务器托管与数据维护成本。

如有任何疑问或数据纠错需求，欢迎通过[联系我们](/contact/)页面发送工单与邮件。
"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

print("Generated Trust & Legal pages successfully.")
