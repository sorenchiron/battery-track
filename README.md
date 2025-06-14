
<img src="imgs/bg-design.jpg" style="width:100%"/>

# Battery-track
电池电量跟踪与记录，耗电极低，exe免安装点击运行。数据全可导出，不申请权限，无任何广告或云控嗅探。

# 使用方法

下载exe程序，直接双击即可开始记录

# 功能特性
1. 记录存放为“今日日期.csv”
1. 可随时关闭、中断，不影响记录正确性。
1. 可自动继续记录。
1. 支持命令行详细设置自定义参数、频率
1. 文件记录了 `时间、电量百分比、预计续航秒`（系统预测值）

exe与py程序的命令行相同，命令行调用方法如下：

Usage: battery-track.py [OPTIONS]

```bash

╭─ Options ──────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --logfile                                TEXT   [default: battery-today.csv]                               │
│ --interval                               FLOAT  [default: 60]                                              │
│ --forcenew              --no-forcenew           [default: no-forcenew]                                     │
│ --install-completion                            Install completion for the current shell.                  │
│ --show-completion                               Show completion for the current shell, to copy it or       │
│                                                 customize the installation.                                │
│ --help                                          Show this message and exit.                                │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```