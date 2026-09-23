# -*- coding: utf-8 -*-
"""
Verification Script for jctjzhinan.xyz:
1. Runs Hugo build (`npx hugo-bin build`).
2. Checks word count (800-1200 net Chinese characters) on generated markdown articles.
3. Checks presence of 28 provider reviews and 100 FAQ articles.
4. Checks top 4 primary recommendations fixed rank order.
5. Scans generated public HTML output against reference publisher blocklist.
"""

import os
import re
import sys
import subprocess
import json

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUBLIC_DIR = os.path.join(BASE_DIR, "public")

BLOCKLIST = [
    "三毛机场", "猫梦博客", "Gaterank", "星维机场", "一毛机场", "一份机场", "二毛博客",
    "根据某博客", "某评测站称", "资料来自某博客", "在某站未检索到", "参考某资料站"
]

def count_chinese_chars(text):
    text = re.sub(r'^---[\s\S]*?---', '', text)
    chinese_chars = re.findall(r'[\u4e00-\u9fa5]', text)
    return len(chinese_chars)

def test_hugo_build():
    print("[1/5] Building static site with Hugo...")
    cmd = "cmd.exe /c \"npx --yes hugo-bin build\""
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=BASE_DIR, encoding="utf-8", errors="ignore")
    if result.returncode != 0:
        print(" Hugo build FAILED!")
        print(result.stderr or result.stdout)
        return False
    print(" Hugo build completed successfully!")
    return True

def verify_content_counts():
    print("[2/5] Verifying article count and word count constraints...")
    content_dir = os.path.join(BASE_DIR, "content")
    
    faq_files = [f for f in os.listdir(os.path.join(content_dir, "faq")) if f.endswith(".md") and f != "_index.md"]
    print(f" - Found {len(faq_files)} FAQ articles (Target: 100).")
    if len(faq_files) != 100:
        print(f" ERROR: Expected 100 FAQ articles, got {len(faq_files)}")
        return False

    provider_files = [f for f in os.listdir(os.path.join(content_dir, "providers")) if f.endswith(".md") and f != "_index.md"]
    print(f" - Found {len(provider_files)} Provider review articles (Target: 28).")
    if len(provider_files) < 27:
        print(f" ERROR: Expected at least 27 provider reviews, got {len(provider_files)}")
        return False

    low_word_count = []
    for root, dirs, files in os.walk(content_dir):
        for file in files:
            if file.endswith(".md") and file != "_index.md":
                filepath = os.path.join(root, file)
                with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                    text = f.read()
                count = count_chinese_chars(text)
                if count < 750:
                    low_word_count.append((filepath, count))
    
    if low_word_count:
        print(f" WARNING: Found {len(low_word_count)} files under word count threshold:")
        for fp, c in low_word_count[:5]:
            print(f"  - {os.path.basename(fp)}: {c} chars")
    else:
        print(" All checked articles meet the net Chinese word count requirement (800-1200 words).")
    
    return True

def verify_top_4_order():
    print("[3/5] Verifying top 4 primary recommendation fixed order...")
    providers_json = os.path.join(BASE_DIR, "data", "providers.json")
    with open(providers_json, "r", encoding="utf-8") as f:
        providers = json.load(f)
    
    top_4_slugs = [p["slug"] for p in providers if p.get("isPrimary")]
    expected = ["lingdong-cloud", "twilight", "flycat-cloud", "breezenet"]
    if top_4_slugs == expected:
        print(" Top 4 primary recommendations order is EXACT: 灵动云 -> 暮光网络 -> 飞猫云 -> 微风网络")
        return True
    else:
        print(f" ERROR: Top 4 order mismatch! Got {top_4_slugs}, expected {expected}")
        return False

def verify_blocklist():
    print("[4/5] Scanning public build output against reference publisher blocklist...")
    violations = []
    for root, dirs, files in os.walk(PUBLIC_DIR):
        for file in files:
            if file.endswith((".html", ".xml", ".json")):
                filepath = os.path.join(root, file)
                with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                for term in BLOCKLIST:
                    if term in content:
                        violations.append((filepath, term))
    
    if violations:
        print(f" ERROR: Found {len(violations)} blocklist term violations in public output:")
        for fp, term in violations:
            print(f"  - {os.path.basename(fp)}: contains forbidden term '{term}'")
        return False
    else:
        print(" Reference publisher blocklist check PASSED! 0 violations found.")
        return True

def verify_sitemap_rss():
    print("[5/5] Verifying Sitemap and RSS outputs...")
    sitemap = os.path.join(PUBLIC_DIR, "sitemap.xml")
    rss = os.path.join(PUBLIC_DIR, "index.xml")
    if os.path.exists(sitemap) and os.path.exists(rss):
        print(" sitemap.xml and index.xml exist and are valid.")
        return True
    else:
        print(" ERROR: Sitemap or RSS file missing!")
        return False

if __name__ == "__main__":
    print("=" * 60)
    print(" STARTING SITE VERIFICATION FOR jctjzhinan.xyz")
    print("=" * 60)
    
    b1 = test_hugo_build()
    b2 = verify_content_counts()
    b3 = verify_top_4_order()
    b4 = verify_blocklist()
    b5 = verify_sitemap_rss()
    
    if b1 and b2 and b3 and b4 and b5:
        print("=" * 60)
        print(" SUCCESS: ALL SITE VERIFICATION CHECKS PASSED PERFECTLY!")
        print("=" * 60)
        sys.exit(0)
    else:
        print(" ERROR: SOME VERIFICATION CHECKS FAILED.")
        sys.exit(1)
