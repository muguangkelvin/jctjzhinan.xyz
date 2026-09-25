---
title: "Surge 高级规则分流与 TUN 模式排错手把手教程"
date: 2026-09-19T10:00:00+08:00
lastmod: 2026-09-19T10:00:00+08:00
slug: "surge-rules-guide"
categories: ["clients"]
tags: ["Surge 规则配置", "机场推荐", "配置教程"]
summary: "Mac 与 iOS 端顶级代理工具 Surge 进阶配置与语法说明。"
author: "JC指南编辑部"
---

## Surge 高级规则分流与 TUN 模式排错手把手教程

<div class="status-intro-box">
  <div class="status-badge-title">🍏 Apple 生态顶级代理工具 · 分流与 TUN 局域网共享</div>
  <p>Surge 是专为 Apple 生态（macOS / iOS / iPadOS）打造的高级网络调试与代理工具，官方并无原生 Android 版本。在多设备与跨平台场景中，通常由运行 Surge（开启“增强模式”即 TUN 虚拟网卡）的 Mac 充当全网网关，或通过配置代理共享服务为局域网内的 Android 设备提供分流支持。</p>
</div>

<figure class="article-image-box">
  <img src="/images/surge-proxy-diagram.png" alt="Surge 代理中转与分流工作原理示意图" loading="lazy">
  <figcaption>【Surge 代理中转与分流工作原理示意图】</figcaption>
</figure>

**Mac 与 iOS 端顶级代理工具 Surge 进阶配置与语法说明。** 在 2026 年的网络环境下，掌握【**Surge 规则配置**】的相关知识与配置技能，能够显著提升海外连接的平稳度与安全性。

<br>

### 一、 高级规则分流（Rule-based Routing）

Surge 的分流系统遵循从上至下优先匹配的原则。一旦某条规则命中，后续规则即刻终止。

#### 1. 核心分流规则语法与场景

- **域名匹配**：
  - `DOMAIN,example.com,Proxy`：精确匹配主域名。
  - `DOMAIN-SUFFIX,google.com,Proxy`：匹配所有以该域名结尾的子域（如 `mail.google.com`）。
  - `DOMAIN-KEYWORD,twitter,Proxy`：包含关键字即匹配。
- **IP 与 CIDR 匹配**：
  - `IP-CIDR,192.168.0.0/16,DIRECT,no-resolve`：局域网直连。*务必加上 `no-resolve`，避免 Surge 强制做 DNS 反查触发延迟。*
  - `GEOIP,CN,DIRECT`：中国大陆 IP 直连。
- **应用进程匹配（macOS 专属）**：
  - `PROCESS-NAME,Telegram,Proxy`：针对特定应用进程分流。
- **最终兜底匹配**：
  - `FINAL,DIRECT` 或 `FINAL,Proxy,dns-failed`：末尾兜底规则。

#### 2. 外部规则集（Rule-Set）管理

为避免主配置文件过于臃肿，推荐引入外部规则集：

```ini
[Rule]
# 引用远程规则集
RULE-SET,https://raw.githubusercontent.com/.../Telegram.list,Proxy
RULE-SET,https://raw.githubusercontent.com/.../Reject.list,REJECT
RULE-SET,SYSTEM,DIRECT

# 兜底
FINAL,Proxy
```

<br>

### 二、 TUN 增强模式与全平台（Android）接入

Surge 的“增强模式 (Enhanced Mode)”基于虚拟网卡（TUN）工作，能够接管系统内所有不主动遵循系统代理设置的流量（如终端命令行、UDP 游戏流量、虚拟机等）。

#### 1. macOS 开启 Enhanced Mode (TUN)
- 接管本机的全部网络协议栈与 UDP 流量。
- 点击菜单栏 Surge 图标，进入偏好设置。
- 打开 **Enhanced Mode（增强模式）** 开关。
- 首次开启需安装特权辅助进程（*Privileged Helper*），输入 macOS 开机密码授权。

#### 2. 开启局域网共享 (Allow Wi-Fi Access)
- 允许 Android 等同一局域网设备接入 Surge。
- 在 Surge 设置中勾选 **Allow Wi-Fi Access（允许局域网连接）**。
- 记下 Surge 监听的 HTTP 代理端口（默认 `6152`）与 SOCKS5 端口（默认 `6153`）。
- 查看 Mac 当前的局域网 IP（例如 `192.168.1.100`）。

#### 3. Android 终端网络配置
- 让 Android 流量经由 Surge 规则分流。
- 将 Android 手机与 Mac 连接至同一个 Wi-Fi。
- 打开 Android 的“WLAN 设置”，长按当前连接的 Wi-Fi -> **修改网络**。
- 将代理设置为 **手动**，主机名填写 Mac IP（`192.168.1.100`），端口填 `6152`。
- 保存后，Android 设备的所有 Web 流量将统一由 Mac 上的 Surge 进行规则分流与去广告。

<br>

### 三、 TUN 模式常见故障排错（Troubleshooting）

| 故障现象 | 根源排查 | 解决方案 |
|:---|:---|:---|
| **开启增强模式后全网断网** | DNS 冲突或虚拟网卡 IP 冲突 | 检查 `[General]` 下 `tun-excluded-routes`，确保未将默认网关路由死循环；将 `dns-server` 调整为 `223.5.5.5, 119.29.29.29`。 |
| **特定应用连接超时** | 该应用采用私有协议或绕过了假 IP | 在 Surge 配置的 `[General]` 中，在 `skip-proxy` 或 `tun-excluded-routes` 填入该应用的 IP 段或域名。 |
| **DNS 污染 / 泄露** | 未开启 Fake-IP 模式导致本地提早解析 | 开启 `enhanced-mode-by-rule = false` 并设置 `dns-follow-system = false`，强制由远程节点解析域名。 |
| **Android 连接共享后无网络** | macOS 防火墙拦截入站连接 | 前往 macOS“系统设置 - 网络 - 防火墙”，将 Surge 设置为“允许传入连接”，或关闭局域网防火墙隔离测试。 |

---


### 深入解析：为什么选择稳定的 Surge 规则配置 对于网络体验至关重要？

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


---


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


---

### 选购与配置步骤总结

1. **确定需求**：根据你的主要场景（影音、AI 办公、社交或备用）选择合适的套餐。
2. **校验优惠**：在结算页面填入对应独家优惠码，锁定折扣。
3. **导入配置**：使用 Clash Verge Rev、Sing-box 或 Shadowrocket 导入订阅并开启 TUN / 规则分流。
