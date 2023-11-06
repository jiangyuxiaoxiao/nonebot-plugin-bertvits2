<div align="center">

# nonebot-plugin-bertvits2

_✨ bertVits2 语音合成插件 ✨_
</div>

## 介绍

bertvits2的nonebot2插件，直接对接bertvits2项目的自带api。

## 安装

### 1. bertvits2安装

+ 下载`bertvits2`的[2.0.1 release](https://github.com/fishaudio/Bert-VITS2/releases/tag/2.0.1)（包括UI文件）
+ 环境安装
+ 运行`server_fastapi.py`，第一次运行默认退出，生成`config.yml`文件，并按文件说明对`server`属性进行配置
+ 运行`server_fastapi.py`

### 2. 插件安装

#### 2.1 使用 nb-cli 安装

`nb plugin install nonebot-plugin-bertvits2`

#### 2.2 使用pip安装

`pip install nonebot-plugin-bertvits2`

### 3.配置

本插件需要在 nonebot2 项目的`.env`文件中添加下表中的配置

|           配置项           | 必填 |        默认值         |                       说明                        |
|:-----------------------:|:--:|:------------------:|:-----------------------------------------------:|
|      bertvits_host      | 否  | "http://127.0.0.1" |                bertVits api的host                |
|      bertvits_port      | 否  |        5000        |                bertVits api的port                |
| bertvits_auto_translate | 否  |       false        | 是否使用bertVits的机翻，开启需要百度api，详见bertVits的config.yml |

## 使用

+ `语音人物列表` ： 查看当前bertvits2已加载模型人物
+ `刷新人物列表` ： 刷新当前bertvits2已加载模型人物
+ `xxx说xxxx`  ： bertVits语音合成，前为人物名，后为要说的话。
+ `xxx中文/日语/英语说xxxx` ：同上，指定目标语言