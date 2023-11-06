"""
@Author: Kasugano Sora
@Github: https://github.com/jiangyuxiaoxiao
@Date: 2023/11/06-10:04
@Desc: 
@Ver : 1.0.0
"""
import aiohttp

from .config import Config
from nonebot import get_driver

plugin_config = Config.parse_obj(get_driver().config)

host = plugin_config.bertvits_host
port = plugin_config.bertvits_port
auto_translate = plugin_config.bertvits_auto_translate


class speaker:
    def __init__(self, name: str, model_id: int, speaker_id: int, language: str):
        self.name = name
        self.model_id = model_id
        self.speaker_id = speaker_id
        self.language = language

    async def speak(self, text: str, language: str = None, autoTranslate: bool = True) -> bytes | None:
        url = f"{host}:{port}/voice"
        params = {
            "text": text,
            "model_id": self.model_id,
            "speaker_id": self.speaker_id,
            "language": language if language is not None else self.language,
            "auto_translate": autoTranslate
        }
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url, params=params) as response:
                if response.status == 200:
                    response = await response.read()
                    return response
        return None


async def get_speakers() -> dict[str, speaker]:
    result: dict[str, speaker] = dict()
    url = f"{host}:{port}/models/info"
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url) as response:
            models: dict[str, any] = await response.json()
            for model_id, model in models.items():
                for spk in model["spk2id"].keys():
                    if spk not in result.keys():
                        result[spk] = speaker(
                            name=spk,
                            model_id=int(model_id),
                            speaker_id=model["spk2id"][spk],
                            language=model["language"]
                        )
    return result


