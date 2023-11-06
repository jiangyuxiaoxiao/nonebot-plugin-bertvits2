"""
@Author: Kasugano Sora
@Github: https://github.com/jiangyuxiaoxiao
@Date: 2023/11/06-09:53
@Desc: 插件配置项
@Ver : 1.0.0
"""
from pydantic import BaseModel, validator


class Config(BaseModel):
    bertvits_host: str = "127.0.0.1"
    bertvits_port: int = 5000
    bertvits_auto_translate: bool = False
