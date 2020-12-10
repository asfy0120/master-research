from slackbot.bot import listen_to
from slackbot.bot import respond_to
from slackbot.bot import default_reply
import slackbot_settings
import datetime
import time
import re
from filereadwrite import FileReadWrite


@respond_to(r'^(.*)$',flags=re.DOTALL)
def comment_log(message,text):
    # 書き込みクラスのインスタンスを生成
    f = FileReadWrite()

    # 現在時刻の取得
    # now = datetime.datetime.now()
    now = time.time()
    # 時刻を文字列に変換する
    # str_now = now.strftime("%Y/%m/%d %H:%M:%S")

    # 出力情報(入力テキスト，UNIX時間)
    if '\n' in text:
        output = "%s,%s,%s\n" % (text.split()[0],text.split()[1], now)
    else:
        output = "%s,%s\n" % (text, now)

    #デバッグ用
    message.reply(text)

    # ファイルにデータを書き込む
    result = f.file_write("test.csv", output)
    # 書き込みに失敗した場合は応答する。それ以外は無応答
    if result == 'ng':
        message.reply("書き込みに失敗しました")

@listen_to(r'^(.*)$',flags=re.DOTALL)
def comment_log(message,text):
    # 書き込みクラスのインスタンスを生成
    f = FileReadWrite()

    # 現在時刻の取得
    # now = datetime.datetime.now()
    now = time.time()
    # 時刻を文字列に変換する
    # str_now = now.strftime("%Y/%m/%d %H:%M:%S")

    # 出力情報(入力テキスト，UNIX時間)
    if '\n' in text:
        output = "%s,%s,%s\n" % (text.split()[0],text.split()[1], now)
    else:
        output = "%s,%s\n" % (text, now)

    #デバッグ用
    message.reply(text)

    # ファイルにデータを書き込む
    result = f.file_write("test.csv", output)
    # 書き込みに失敗した場合は応答する。それ以外は無応答
    if result == 'ng':
        message.reply("書き込みに失敗しました")

@default_reply
def my_default_handler(message):
    # デフォルトリプライをsendに変更する
    message.send(slackbot_settings.DEFAULT_REPLY)
