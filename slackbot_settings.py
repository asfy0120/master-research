# ライブラリのインポート
import os

# 環境変数に定義しておく
#API_TOKEN = os.environ['xoxb-1557439170853-1553948204502-9loblhgfz3JAgtyT3NjqbeV9']
API_TOKEN ="xoxb-1557439170853-1553948204502-9loblhgfz3JAgtyT3NjqbeV9"

# デフォルトの応答
DEFAULT_REPLY = "すみません。よくわかりません"

PLUGINS = [
            'slackbot.plugins',
            # 'botmodules.conversation',
            'botmodules.memo',
            # ここにカンマ区切りでプラグインを追加していくことで拡張できます。
]
