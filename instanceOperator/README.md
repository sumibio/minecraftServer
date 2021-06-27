# 概要
EC2インスタンスの起動停止を行う関数処理全般です。

### handler/ec2_operator
API GatewayをトリガーにEC2の起動停止を行います。

### handler/set_route53_record.py
EC2が起動/停止した際にRoute53のレコード削除追加を行います。

### handler/notification_for_discord.py
discordへのメッセージ通知を行います。

# 開発環境
nodejsで動作するServerless Frameworkを使用して開発しています。
yarnで必要なパッケージをインストールすることができます。

```bash
$ yarn install
```

# デプロイ
ディレクトリを移動してスクリプトを実行することでデプロイが可能です。
デプロイにはshell/env/に3つのファイルが必要になります。

```text
slell
└── env
    ├── prd
    └── dev
       ├── domainname.txt　取得したドメイン名を記載 e.g. example.com
       ├── hostzoneid.txt　route53で作成したホストゾーンIDを記載
       ├── webhookurl.txt　通知送信先のURLを記載
       └── instanceid.txt　EC2インスタンスのIDを記載
```

デプロイ

```bash
$ bash deploy_prd.sh
```

アンデプロイ

```bash
$ bash remove_prd.sh
```