"""
@Author: Kasugano Sora
@Github: https://github.com/jiangyuxiaoxiao
@Date: 2023/11/06-09:47
@Desc:
@Ver : 1.0.0
"""
import re

from nonebot.plugin import PluginMetadata
from nonebot import get_driver
from nonebot.adapters.onebot.v11 import MessageEvent, MessageSegment
from nonebot import on_regex, on_command

from .config import Config
from .api import get_speakers, auto_translate

__plugin_meta__ = PluginMetadata(
    name="nonebot-plugin-bertvits2",
    description="bertvits2语音合成插件",
    usage="语音人物列表: 查看当前已加载语音人物"
          "刷新人物列表: 从bertvits重新获取已加载人物"
          "xxx说xxxx / xxx中文/日语/英语说xxxx: 语音合成",
    type="application",
    homepage="https://github.com/jiangyuxiaoxiao/nonebot-plugin-bertvits2",
    config=Config,
    supported_adapters={"~onebot.v11"},

)

plugin_config = Config.parse_obj(get_driver().config)

get_list = on_command("语音人物列表", priority=100)
refresh_list = on_command("刷新人物列表", priority=100)
speak = on_regex(pattern="#?.+说", priority=100, block=False)
speakers = None


@get_list.handle()
async def _(event: MessageEvent):
    global speakers
    if speakers is None:
        speakers = await get_speakers()
    spkList = speakers.keys()
    await get_list.send("当前已加载的bertVits2模型人物: \n"
                        f"{' '.join(spkList)}")


@refresh_list.handle()
async def _(event: MessageEvent):
    global speakers
    speakers = await get_speakers()
    spkList = speakers.keys()
    await get_list.send("刷新成功，当前已加载的bertVits2模型人物: \n"
                        f"{' '.join(spkList)}")


@speak.handle()
async def _(event: MessageEvent):
    global speakers
    if speakers is None:
        speakers = await get_speakers()
    language = None
    msg = event.message.extract_plain_text()
    text = msg.split("说", maxsplit=1)[1]
    if text == "":
        return
    msg = re.match(pattern=r"#?.+说", string=msg)
    if msg is None:
        return
    name = msg.group().split("说")[0].lstrip("#").strip()
    if name.endswith("中文"):
        language = "ZH"
        name = name.rstrip("中文")
    if name.endswith("日语"):
        language = "JP"
        name = name.rstrip("日语")
    if name.endswith("英语"):
        language = "EN"
        name = name.rstrip("英语")
    if name not in speakers.keys():
        return

    speaker = speakers[name]
    audio = await speaker.speak(text=text, language=language, autoTranslate=auto_translate)
    await speak.send(MessageSegment.record(audio))
