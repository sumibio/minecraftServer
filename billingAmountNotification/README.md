# 概要
請求金額情報をdiscordに送信します。

以下の記事を参考に構築。
https://dev.classmethod.jp/articles/notify-slack-aws-billing/

さらにServerless Frameworkでデプロイ可能にしています。

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

上記設定が完了したら、下記のシェルスクリプトでデプロイ可能です。

```bash
$ bash deploy_prd.sh
```
