# 概要
EC2インスタンスの起動停止を行うAWS Lambdaを利用したアプリケーションです。

* ElasticIPへの課金を回避する為、インスタンスの停止起動の際に都度Route53のレコードを更新します。
* インスタンスの状態変化をDiscordへ通知します。

## Pythonスクリプト

* handler/ec2_operator
API GatewayをトリガーにEC2の起動停止を行います。

* handler/set_route53_record.py
EC2が起動/停止した際にRoute53のレコード削除追加を行います。

* handler/notification_for_discord.py
discordへのメッセージ通知を行います。

## デプロイ
nodejsで動作するServerless Frameworkを使用して開発しています。
Serverless Frameworkをインストール後、下記のコマンドで必要なパッケージを取得してください。

```bash
$ yarn install
```

`.env`に必要な環境変数を記載してください

```text
slell
└── env
    ├── prd
    └── dev
       └── .env　各環境変数を`key=value`形式で記載
```

必要な変数
* avatar_url
Discordに通知する際に表示するアイコン（URLで指定）

* webhook_url
Discord通知用のwebhookURL

* domain_name
Route53に登録しているドメイン名

* hostedzone_id
Route53に登録しているドメインのホストゾーンid

* instance_id
停止起動を行う対象インスタンスid

上記設定が完了したら、下記のシェルスクリプトでデプロイ可能です。

```bash
$ bash deploy_prd.sh
```
