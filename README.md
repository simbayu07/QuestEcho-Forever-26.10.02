# QuestEcho 1.9.4 — Forever compatibility snapshot (2026-10-02)

本仓库的 `QuestEcho/` 已同步为实际安装并修复后的 **QuestEcho 1.9.4**，用于 WoW Forever 1.60.1 / build 70170 / Interface 16001（项目编号 18）。保留原仓库历史；之前远端标记为 1.9.4 的标签实际仍包含 1.7.0 源码，本次提交以目录内 TOC 及文件校验清单为准。

## 本次兼容修复

- 现代 Forever / Era 不再进入旧版 1.12 的全局帧回调兼容层，修复 `OnUpdate` 丢失 `elapsed` 等参数引起的连续报错。
- Forever 同时识别旧项目编号 1 和新编号 18；使用现代声音句柄及停止路径，避免启用旧聊天框改写。
- `Bindings.xml` 从普通 TOC 加载清单移除，保留文件及全部快捷键，交由客户端的绑定加载机制读取。

详细范围、来源及复用补丁的方式见 [兼容修复说明](docs/COMPATIBILITY.md)。15 个插件文件的 SHA-256 见 [快照清单](docs/installed-snapshot.json)。

## 安装

将本仓库的 **`QuestEcho/` 子目录**复制到目标客户端的 `Interface/AddOns/` 下，随后在游戏中执行 `/reload`。仓库根目录、`docs/` 和 `tools/` 不属于插件安装内容。

语音数据包仍须单独安装；本仓库没有包含 `QuestEchoData`、`QuestEchoData-zhCN`、任何用户保存配置或个人采集数据。`QuestEchoSilence.wav` 是原插件自带的 60 字节静音资源，保留供其兼容逻辑使用。

## 作者与版权

上游作者为 Leysure，项目地址为 [LeySure/QuestEcho-Forever](https://github.com/LeySure/QuestEcho-Forever)。所有原始版权声明原样保留；本仓库不授予上游代码新的开源许可。`Core.lua` 中的专有版权声明仍适用。

以下保留原仓库介绍；其中旧版本下载链接属于历史说明，不代表本次快照版本。

---

# QuestEcho

**Bring your quests and conversations to life with immersive voiceovers!**

[![Release](https://img.shields.io/github/v/release/LeySure/QuestEcho-Forever?label=Release)](https://github.com/LeySure/QuestEcho-Forever/releases)
[![WoW Clients](https://img.shields.io/badge/WoW-Retail%20%7C%20Classic%20%7C%20Forever-orange)](https://github.com/LeySure/QuestEcho-Forever/releases)
[![Ko-fi](https://img.shields.io/badge/Support%20on-Ko--fi-FF5E5B?logo=kofi)](https://ko-fi.com/leysure/tip)

QuestEcho is a lightweight World of Warcraft addon that automatically plays voice lines when you interact with NPCs or handle quests. Designed to enhance role-playing immersion without altering core gameplay.

---
![QuestEcho](https://github.com/LeySure/QuestEcho-Forever/blob/main/Screenshot/QuestEcho.png?raw=true)
## Features

- **Auto-Play Voiceovers:** Triggers voice lines seamlessly on quest acceptance, quest completion, and NPC gossip interactions.
- **Cross-Client Support:** Fully compatible with WoW Retail, Classic Era, Forever, Vallina（Turtle 1.12）、 WLK 3.3.5a（Warmane） clients.
- **Lightweight & Efficient:** Minimal performance impact, ensuring a smooth gameplay experience.
- **Custom Commands:** Use `/qe` to easily toggle settings or manage the addon in-game.

---

## Important: Audio Data Packs Required

**QuestEcho is a player framework only and does NOT include any audio files.**

Due to the large file size (1GB+), the voice packs are distributed via GitHub Releases instead of CurseForge. You must download and install the corresponding Data Pack separately from the links below.

### Available Downloads (v1.7.0)

| File | Description | Size |
|------|-------------|------|
| `QuestEcho.zip` | Core addon (required) | <5MB |
| `QuestEchoData.zip` | English Voice Pack | >1GB |
| `QuestEchoData-zhCN.zip` | Chinese Voice Pack (中文语音包) | >1GB |

Download all files from: **[GitHub latest Releases](https://github.com/LeySure/QuestEcho-Forever/releases/tag/1.9.0)**

Multiple data packs can be installed simultaneously without conflicts.

---

## Installation

1. Download the **Core Addon** and your desired **Voice Pack(s)** from the [Releases page](https://github.com/LeySure/QuestEcho-Forever/releases/tag/1.7.0).
2. Extract the folders into your WoW `Interface/AddOns` directory.
3. Ensure all addons are enabled on your character selection screen.
4. Launch the game and enjoy immersive voiceovers!

---

## Commands

| Command | Description |
|---------|-------------|
| `/qe` | Open settings panel |
| `/qe toggle` | Enable/disable voiceovers |
| `/qe help` | Show all available commands |

---

## Compatibility

| Client | Supported |
|--------|-----------|
| Retail | √ |
| Classic Era | √ |
| Forever | √ |

---

## Support & Feedback

If QuestEcho helped enhance your adventure, consider supporting the development!

[![Ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/leysure/tip)

Found a bug or have a feature request? Please [open an issue](https://github.com/LeySure/QuestEcho-Forever/issues) on GitHub.

---

## 中文说明

**QuestEcho** 是一款为魔兽世界打造的沉浸式配音插件，可在接取任务、完成任务和与 NPC 对话时自动播放语音。

### 重要提示

- 核心插件不包含任何语音文件，需单独下载语音包。
- 因语音包体积过大，请从上方 **GitHub Releases** 页面下载。
- 支持同时安装中英文语音包，互不冲突。
- 兼容正式服、怀旧服和无限服（Forever）。

### 安装步骤

1. 从 [Releases 页面](https://github.com/LeySure/QuestEcho-Forever/releases/tag/1.7.0) 下载核心插件和所需语音包。
2. 将文件夹解压到游戏的 `Interface/AddOns` 目录。
3. 在角色选择界面确保所有插件已启用。
4. 进入游戏，使用 `/qe` 命令进行设置。
