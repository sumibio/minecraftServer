# 概要
請求金額情報をdiscordに送信します。

以下の記事を参考にServerless Frameworkでデプロイできるようにしています。
https://dev.classmethod.jp/articles/notify-slack-aws-billing/

# 開発環境
nodejsで動作するServerless Frameworkを使用して開発しています。
yarnで必要なパッケージをインストールすることができます。

```bash
$ yarn install
```

# デプロイ
ディレクトリを移動してスクリプトを実行することでデプロイが可能です。
デプロイにはshell/env/に.envが必要です。

```text
slell
└── env
    ├── prd
    └── dev
       └── .env　各環境変数を`key=value`形式で記載
```

デプロイ

```bash
$ bash deploy_prd.sh
```

アンデプロイ

```bash
$ bash remove_prd.sh
```