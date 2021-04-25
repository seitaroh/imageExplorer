# imageExplorer

## 1 ローカルでの起動手順


### 1.1 依存ライブラリのインストール手順
Pythonの依存ライブラリをPipenvを使ってインストールする

ルートディレクトリで次のコマンドを実行する
```shell
$ pipenv install
```

仮想環境に入る
```shell
$ pipenv shell
```
### 1.2データベースの作成
データベースはsqliteを使用

データベースにスキーマをインストールする．ルートディレクトリで次のコマンドを実行する
```shell
$ python manage.py makemigrations imageExplorer
$ python manage.py migrate
```

### 1.3 環境変数の設定
環境変数を設定する．ルートディレクトリに'.env'ファイルを作成する

例
```python
SECRET_KEY = "sample)&y0m0sxp@#kg73y6%8s(uu!*247p2@sgrh%&s*4#xqovgm41n"
```

### 1.4 サーバの立ち上げ
ルートディレクトリで次のコマンドを実行する

```shell
$ python manage.py runserver
```