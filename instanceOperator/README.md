# 概要
特定IDのEC2インスタンスの起動をトリガーにRoute53のレコードを書き換えます。

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
       └── instansid.txt　EC2インスタンスのIDを記載
```

デプロイ

```bash
$ bash deploy_prd.sh
```

アンデプロイ

```bash
$ bash remove_prd.sh
```