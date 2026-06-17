## 4K-IPTV-M3U

基于组播源的省级直播列表仓库，按省份自动生成 `m3u/txt` 文件，并在 README 中展示可直接使用的加速下载链接。

### 相关播放器项目

- 纯直播 APP: [lemonTV](https://github.com/jia070310/lemonTV)
- 影视+直播集合版: [lomenTV-VDS](https://github.com/jia070310/lomenTV-VDS)
- Windows 直播播放器: [lemonIPTV-windows](https://github.com/jia070310/lemonIPTV-windows)

![预览图](https://github.com/jia070310/4K-IPTV-M3U/blob/main/tv.png)

### 仓库内容

- `rtp/b.py`: 组播源抓取与生成主脚本（支持电信/移动/联通多源提取）
- `m3u/`: 自动生成的 M3U 文件
- `txt/`: 自动生成的 TXT 文件
- `.github/workflows/`: 定时任务与自动更新流程

### 更新机制

- 定时任务执行后自动更新 `m3u`、`txt`
- 同步自动重写 README 文件列表（含“最近更新时间”）
- 下载链接统一使用 `gh-proxy` 加速前缀

### 本地运行

```bash
pip install -r requirements.txt
python rtp/b.py
```

## 加速下载说明

以下下载链接均已添加 `gh-proxy` 加速前缀，可直接使用。  
GitHub README 不支持可执行脚本，`onclick` 复制按钮会失效，因此改为“可复制直链”文本（手动复制即可）。

---

## M3U 文件列表

<table style="width:100%; table-layout:auto;">
<colgroup>
<col style="width: 220px;" />
<col style="width: 120px;" />
<col style="width: 170px;" />
<col />
</colgroup>
<thead>
<tr>
<th style="white-space:nowrap;">文件名</th>
<th style="white-space:nowrap;">加速链接</th>
<th style="white-space:nowrap;">最近更新时间</th>
<th style="white-space:nowrap;">可复制直链</th>
</tr>
</thead>
<tbody>
<tr><td style="white-space:nowrap;">上海电信.m3u</td><td style="white-space:nowrap;"><a href="https://gh-proxy.org/https://raw.githubusercontent.com/jia070310/4K-IPTV-M3U/main/m3u/%E4%B8%8A%E6%B5%B7%E7%94%B5%E4%BF%A1.m3u">下载链接</a></td><td style="white-space:nowrap;">2026-06-17 22:51:43</td><td><code>https://gh-proxy.org/https://raw.githubusercontent.com/jia070310/4K-IPTV-M3U/main/m3u/%E4%B8%8A%E6%B5%B7%E7%94%B5%E4%BF%A1.m3u</code></td></tr>
<tr><td style="white-space:nowrap;">内蒙古联通.m3u</td><td style="white-space:nowrap;"><a href="https://gh-proxy.org/https://raw.githubusercontent.com/jia070310/4K-IPTV-M3U/main/m3u/%E5%86%85%E8%92%99%E5%8F%A4%E8%81%94%E9%80%9A.m3u">下载链接</a></td><td style="white-space:nowrap;">2026-06-17 22:51:43</td><td><code>https://gh-proxy.org/https://raw.githubusercontent.com/jia070310/4K-IPTV-M3U/main/m3u/%E5%86%85%E8%92%99%E5%8F%A4%E8%81%94%E9%80%9A.m3u</code></td></tr>
<tr><td style="white-space:nowrap;">四川电信.m3u</td><td style="white-space:nowrap;"><a href="https://gh-proxy.org/https://raw.githubusercontent.com/jia070310/4K-IPTV-M3U/main/m3u/%E5%9B%9B%E5%B7%9D%E7%94%B5%E4%BF%A1.m3u">下载链接</a></td><td style="white-space:nowrap;">2026-06-17 22:51:43</td><td><code>https://gh-proxy.org/https://raw.githubusercontent.com/jia070310/4K-IPTV-M3U/main/m3u/%E5%9B%9B%E5%B7%9D%E7%94%B5%E4%BF%A1.m3u</code></td></tr>
<tr><td style="white-space:nowrap;">四川电信1.m3u</td><td style="white-space:nowrap;"><a href="https://gh-proxy.org/https://raw.githubusercontent.com/jia070310/4K-IPTV-M3U/main/m3u/%E5%9B%9B%E5%B7%9D%E7%94%B5%E4%BF%A11.m3u">下载链接</a></td><td style="white-space:nowrap;">2026-06-17 22:51:43</td><td><code>https://gh-proxy.org/https://raw.githubusercontent.com/jia070310/4K-IPTV-M3U/main/m3u/%E5%9B%9B%E5%B7%9D%E7%94%B5%E4%BF%A11.m3u</code></td></tr>
<tr><td style="white-space:nowrap;">山东联通.m3u</td><td style="white-space:nowrap;"><a href="https://gh-proxy.org/https://raw.githubusercontent.com/jia070310/4K-IPTV-M3U/main/m3u/%E5%B1%B1%E4%B8%9C%E8%81%94%E9%80%9A.m3u">下载链接</a></td><td style="white-space:nowrap;">2026-06-17 22:51:43</td><td><code>https://gh-proxy.org/https://raw.githubusercontent.com/jia070310/4K-IPTV-M3U/main/m3u/%E5%B1%B1%E4%B8%9C%E8%81%94%E9%80%9A.m3u</code></td></tr>
<tr><td style="white-space:nowrap;">山西联通.m3u</td><td style="white-space:nowrap;"><a href="https://gh-proxy.org/https://raw.githubusercontent.com/jia070310/4K-IPTV-M3U/main/m3u/%E5%B1%B1%E8%A5%BF%E8%81%94%E9%80%9A.m3u">下载链接</a></td><td style="white-space:nowrap;">2026-06-17 22:51:43</td><td><code>https://gh-proxy.org/https://raw.githubusercontent.com/jia070310/4K-IPTV-M3U/main/m3u/%E5%B1%B1%E8%A5%BF%E8%81%94%E9%80%9A.m3u</code></td></tr>
<tr><td style="white-space:nowrap;">山西联通1.m3u</td><td style="white-space:nowrap;"><a href="https://gh-proxy.org/https://raw.githubusercontent.com/jia070310/4K-IPTV-M3U/main/m3u/%E5%B1%B1%E8%A5%BF%E8%81%94%E9%80%9A1.m3u">下载链接</a></td><td style="white-space:nowrap;">2026-06-17 22:51:43</td><td><code>https://gh-proxy.org/https://raw.githubusercontent.com/jia070310/4K-IPTV-M3U/main/m3u/%E5%B1%B1%E8%A5%BF%E8%81%94%E9%80%9A1.m3u</code></td></tr>
<tr><td style="white-space:nowrap;">广东电信.m3u</td><td style="white-space:nowrap;"><a href="https://gh-proxy.org/https://raw.githubusercontent.com/jia070310/4K-IPTV-M3U/main/m3u/%E5%B9%BF%E4%B8%9C%E7%94%B5%E4%BF%A1.m3u">下载链接</a></td><td style="white-space:nowrap;">2026-06-17 22:51:43</td><td><code>https://gh-proxy.org/https://raw.githubusercontent.com/jia070310/4K-IPTV-M3U/main/m3u/%E5%B9%BF%E4%B8%9C%E7%94%B5%E4%BF%A1.m3u</code></td></tr>
<tr><td style="white-space:nowrap;">贵州电信.m3u</td><td style="white-space:nowrap;"><a href="https://gh-proxy.org/https://raw.githubusercontent.com/jia070310/4K-IPTV-M3U/main/m3u/%E8%B4%B5%E5%B7%9E%E7%94%B5%E4%BF%A1.m3u">下载链接</a></td><td style="white-space:nowrap;">2026-06-17 22:51:43</td><td><code>https://gh-proxy.org/https://raw.githubusercontent.com/jia070310/4K-IPTV-M3U/main/m3u/%E8%B4%B5%E5%B7%9E%E7%94%B5%E4%BF%A1.m3u</code></td></tr>
<tr><td style="white-space:nowrap;">辽宁联通.m3u</td><td style="white-space:nowrap;"><a href="https://gh-proxy.org/https://raw.githubusercontent.com/jia070310/4K-IPTV-M3U/main/m3u/%E8%BE%BD%E5%AE%81%E8%81%94%E9%80%9A.m3u">下载链接</a></td><td style="white-space:nowrap;">2026-06-17 22:51:43</td><td><code>https://gh-proxy.org/https://raw.githubusercontent.com/jia070310/4K-IPTV-M3U/main/m3u/%E8%BE%BD%E5%AE%81%E8%81%94%E9%80%9A.m3u</code></td></tr>
</tbody>
</table>
## TXT 文件列表

<table style="width:100%; table-layout:auto;">
<colgroup>
<col style="width: 220px;" />
<col style="width: 120px;" />
<col style="width: 170px;" />
<col />
</colgroup>
<thead>
<tr>
<th style="white-space:nowrap;">文件名</th>
<th style="white-space:nowrap;">加速链接</th>
<th style="white-space:nowrap;">最近更新时间</th>
<th style="white-space:nowrap;">可复制直链</th>
</tr>
</thead>
<tbody>
<tr><td style="white-space:nowrap;">上海电信.txt</td><td style="white-space:nowrap;"><a href="https://gh-proxy.org/https://raw.githubusercontent.com/jia070310/4K-IPTV-M3U/main/txt/%E4%B8%8A%E6%B5%B7%E7%94%B5%E4%BF%A1.txt">下载链接</a></td><td style="white-space:nowrap;">2026-06-17 22:51:43</td><td><code>https://gh-proxy.org/https://raw.githubusercontent.com/jia070310/4K-IPTV-M3U/main/txt/%E4%B8%8A%E6%B5%B7%E7%94%B5%E4%BF%A1.txt</code></td></tr>
<tr><td style="white-space:nowrap;">内蒙古联通.txt</td><td style="white-space:nowrap;"><a href="https://gh-proxy.org/https://raw.githubusercontent.com/jia070310/4K-IPTV-M3U/main/txt/%E5%86%85%E8%92%99%E5%8F%A4%E8%81%94%E9%80%9A.txt">下载链接</a></td><td style="white-space:nowrap;">2026-06-17 22:51:43</td><td><code>https://gh-proxy.org/https://raw.githubusercontent.com/jia070310/4K-IPTV-M3U/main/txt/%E5%86%85%E8%92%99%E5%8F%A4%E8%81%94%E9%80%9A.txt</code></td></tr>
<tr><td style="white-space:nowrap;">四川电信.txt</td><td style="white-space:nowrap;"><a href="https://gh-proxy.org/https://raw.githubusercontent.com/jia070310/4K-IPTV-M3U/main/txt/%E5%9B%9B%E5%B7%9D%E7%94%B5%E4%BF%A1.txt">下载链接</a></td><td style="white-space:nowrap;">2026-06-17 22:51:43</td><td><code>https://gh-proxy.org/https://raw.githubusercontent.com/jia070310/4K-IPTV-M3U/main/txt/%E5%9B%9B%E5%B7%9D%E7%94%B5%E4%BF%A1.txt</code></td></tr>
<tr><td style="white-space:nowrap;">四川电信1.txt</td><td style="white-space:nowrap;"><a href="https://gh-proxy.org/https://raw.githubusercontent.com/jia070310/4K-IPTV-M3U/main/txt/%E5%9B%9B%E5%B7%9D%E7%94%B5%E4%BF%A11.txt">下载链接</a></td><td style="white-space:nowrap;">2026-06-17 22:51:43</td><td><code>https://gh-proxy.org/https://raw.githubusercontent.com/jia070310/4K-IPTV-M3U/main/txt/%E5%9B%9B%E5%B7%9D%E7%94%B5%E4%BF%A11.txt</code></td></tr>
<tr><td style="white-space:nowrap;">山东联通.txt</td><td style="white-space:nowrap;"><a href="https://gh-proxy.org/https://raw.githubusercontent.com/jia070310/4K-IPTV-M3U/main/txt/%E5%B1%B1%E4%B8%9C%E8%81%94%E9%80%9A.txt">下载链接</a></td><td style="white-space:nowrap;">2026-06-17 22:51:43</td><td><code>https://gh-proxy.org/https://raw.githubusercontent.com/jia070310/4K-IPTV-M3U/main/txt/%E5%B1%B1%E4%B8%9C%E8%81%94%E9%80%9A.txt</code></td></tr>
<tr><td style="white-space:nowrap;">山西联通.txt</td><td style="white-space:nowrap;"><a href="https://gh-proxy.org/https://raw.githubusercontent.com/jia070310/4K-IPTV-M3U/main/txt/%E5%B1%B1%E8%A5%BF%E8%81%94%E9%80%9A.txt">下载链接</a></td><td style="white-space:nowrap;">2026-06-17 22:51:43</td><td><code>https://gh-proxy.org/https://raw.githubusercontent.com/jia070310/4K-IPTV-M3U/main/txt/%E5%B1%B1%E8%A5%BF%E8%81%94%E9%80%9A.txt</code></td></tr>
<tr><td style="white-space:nowrap;">山西联通1.txt</td><td style="white-space:nowrap;"><a href="https://gh-proxy.org/https://raw.githubusercontent.com/jia070310/4K-IPTV-M3U/main/txt/%E5%B1%B1%E8%A5%BF%E8%81%94%E9%80%9A1.txt">下载链接</a></td><td style="white-space:nowrap;">2026-06-17 22:51:43</td><td><code>https://gh-proxy.org/https://raw.githubusercontent.com/jia070310/4K-IPTV-M3U/main/txt/%E5%B1%B1%E8%A5%BF%E8%81%94%E9%80%9A1.txt</code></td></tr>
<tr><td style="white-space:nowrap;">广东电信.txt</td><td style="white-space:nowrap;"><a href="https://gh-proxy.org/https://raw.githubusercontent.com/jia070310/4K-IPTV-M3U/main/txt/%E5%B9%BF%E4%B8%9C%E7%94%B5%E4%BF%A1.txt">下载链接</a></td><td style="white-space:nowrap;">2026-06-17 22:51:43</td><td><code>https://gh-proxy.org/https://raw.githubusercontent.com/jia070310/4K-IPTV-M3U/main/txt/%E5%B9%BF%E4%B8%9C%E7%94%B5%E4%BF%A1.txt</code></td></tr>
<tr><td style="white-space:nowrap;">贵州电信.txt</td><td style="white-space:nowrap;"><a href="https://gh-proxy.org/https://raw.githubusercontent.com/jia070310/4K-IPTV-M3U/main/txt/%E8%B4%B5%E5%B7%9E%E7%94%B5%E4%BF%A1.txt">下载链接</a></td><td style="white-space:nowrap;">2026-06-17 22:51:43</td><td><code>https://gh-proxy.org/https://raw.githubusercontent.com/jia070310/4K-IPTV-M3U/main/txt/%E8%B4%B5%E5%B7%9E%E7%94%B5%E4%BF%A1.txt</code></td></tr>
<tr><td style="white-space:nowrap;">辽宁联通.txt</td><td style="white-space:nowrap;"><a href="https://gh-proxy.org/https://raw.githubusercontent.com/jia070310/4K-IPTV-M3U/main/txt/%E8%BE%BD%E5%AE%81%E8%81%94%E9%80%9A.txt">下载链接</a></td><td style="white-space:nowrap;">2026-06-17 22:51:43</td><td><code>https://gh-proxy.org/https://raw.githubusercontent.com/jia070310/4K-IPTV-M3U/main/txt/%E8%BE%BD%E5%AE%81%E8%81%94%E9%80%9A.txt</code></td></tr>
</tbody>
</table>
---

## 免责声明

- 本仓库中的频道地址来源于网络公开信息抓取与整理，仅供技术学习、测试与研究使用。
- 本仓库不存储、不制作任何视频内容，不提供任何视听节目传播服务。
- 链接可用性与内容合法性由源站提供方负责，可能随时失效或变更。
- 使用者应遵守所在地法律法规及相关版权要求，因使用本仓库内容产生的风险与责任由使用者自行承担。