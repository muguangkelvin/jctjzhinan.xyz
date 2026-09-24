---
title: "测评方法说明"
description: "JC指南 (jctjzhinan.xyz) 的节点性能测试、流媒体解锁能力及多变量控制复核标准。"
date: 2026-09-19T10:00:00+08:00
lastmod: 2026-09-24T18:00:00+08:00
summary: "JC指南 (jctjzhinan.xyz) 的节点性能测试、流媒体解锁能力及多变量控制复核标准。"
---

<div class="status-intro-box">
  <div class="status-badge-title">📊 量化指标 · 变量控制 · 定期轮巡</div>
  <p>为了让用户在选购机场服务时有据可依，JC指南 (jctjzhinan.xyz) 建立了一套标准化的节点测试与评测复核体系。</p>
</div>

<br>

## 📈 1. 核心测试指标与权重

| 测试维度 | 权重 | 测试方法与判定标准 |
|:---|:---|:---|
| **晚高峰稳定性** | 40% | 每日 20:00 - 23:00 集中抽查，记录丢包率（<1% 为优）、ICMP/TCP 延迟波动。 |
| **流媒体与 AI 解锁** | 25% | 自动脚本与人工测试 Netflix 4K、Disney+、YouTube 及 OpenAI/ChatGPT 节点风控 IP 解锁率。 |
| **价格与月付门槛** | 20% | 优先评估是否提供低门槛月付、优惠码力度及流量套餐真实折算单价。 |
| **客户端兼容度** | 15% | 验证 YAML/JSON 格式订阅在 Clash Verge Rev、Sing-box、Shadowrocket 上的导入无错率。 |

<br>

## 🔬 2. 测试环境与变量控制

- 🌐 **本地网络环境**：覆盖国内三大运营商（中国电信、中国联通、中国移动）千兆宽带与 5G 移动网络。
- 💻 **客户端测试组**：Windows 11 (Clash Verge Rev TUN 模式)、macOS (Sing-box)、iOS (Shadowrocket) 与 Android (Clash Meta)。
- 🔄 **数据核验周期**：主推榜单每周轮巡复核，全量 28 家服务商每月更新评测日志。
