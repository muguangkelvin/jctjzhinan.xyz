# SEO Profile 批量替换契约规范文件

本规范用于未来通过自动化工具或全局指令替换全站 SEO 关键词与导航系统。

## 替换步骤流程

1. 读取当前 `data/site_seo_profile.json` 与 `docs/site-seo-profile.json`。
2. 规范化输入的新关键词集合（核心词、辅助词、长尾词、Hero 词、Footer 词、导航标签）。
3. 校验旧 URL 映射关系，生成 301 重定向配置文件 `config/_default/redirects.json`，确保无 404 死链。
4. 重新渲染 Header 导航、Footer 动态关键词说明、Hero 标题与摘要。
5. 扫描历史公开 Markdown 文件，清理废弃黑名单词汇。
6. 执行全站 Hugo 构建与 `scripts/verify-site.py` 自动化检测。

## 必须保留的数据与规则
- 固定前四名商业推广顺序（全球云 1、飞猫云 2、暮光 3、微风 4）。
- 27+ 机场独立测评 URL 结构 (`/providers/{slug}/`)。
- 原始邀请链接（含 `code` 参数）及 `rel="sponsored nofollow noopener"` 属性。
- 参考博客黑名单隔离逻辑。
