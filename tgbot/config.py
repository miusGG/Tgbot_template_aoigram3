from dataclasses import dataclass
import json
from typing import List, Dict


@dataclass
class TgBot:
    token: str
    admins_ids: List[int]

    @staticmethod
    def from_json(config: json):
        with open(config, 'r') as f:
            cfg = json.load(f)
        main_config = cfg['main']
        token = main_config['BOT_TOKEN']
        admin_ids = main_config['ADMINS']
        return TgBot(token=token, admins_ids=admin_ids)


@dataclass
class Config:
    tg_bot: TgBot


def load_config(path):
    """
    :param path: .\cfg.json
    :return: 1 dataclass
    tg_bot:
        token
        admins_ids
    """
    return Config(
        tg_bot=TgBot.from_json(path)
    )
