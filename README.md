# rinsukicounter

`@rinsuki@imastodon.net` で一日一回、前日に何回`(凛|りん)`と書いたかを数えるbotです。

ここではimastodon.net決め打ちになっているのでまずないかとは思いますが、Mastodon 2.0からのsnowflakeに依存しているためsnowflakeじゃない箪笥だと動きません。

## how to run

1. `pip install -r requirements.txt`
2. 環境変数 `ACCESS_TOKEN` にscopeが `read write` なアクセストークンをぶっこんで `python main.py`