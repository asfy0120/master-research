import codecs

class FileReadWrite:
    # ファイルを読み込むメソッド
    def file_read(self, path):
        try:
            # ファイルを開く
            target_file = codecs.open(path, "r", "utf_8")
            # ファイルを読み込む
            text = target_file.read()
            target_file.close()
        except:
            # エラーが出た時の例外処理
            text = "ng"

        return text

    # ファイルを書き込むメソッド
    def file_write(self, path, text):
        try:
            target_file = codecs.open(path, "a", "utf_8")
            target_file.write(text)
            result = "ok"
            target_file.close()
        except:
            # エラーが出た時の例外処理
            result = "ng"
        return result

# クラスのテストコード(ファイル書き込み)
# def main():
#     c = FileReadWrite()
#     answer =  c.file_write("./test1.txt", "かきくけこn")
#     print(answer)

if __name__ == "__main__":
    main()
