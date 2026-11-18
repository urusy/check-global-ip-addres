# グローバルIPを確認するスクリプト
グローバルIPを取得して、前回から変更があればSlackへ通知する。

過去分は履歴ファイルへ追記する。

## Setup
Python 3.10以上が必要（requests 2.33.0 / urllib3 2.8.0 の要件）。

`config.json`の`slack.url`を通知したいSlackのチャンネル用に変更する。

