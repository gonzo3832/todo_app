# Flaskアプリの作り方　ToDoアプリ編
忘備録としてざっくりまとめる
0. appの構成案を考える
ToDoアプリなので、必要な要件は以下の通り
- ToDoの入力ホーム(create)
- ToDoリストの一覧画面(read)
- 登録したToDoの編集機能(update)
- 完了したToDoの削除機能(delete)

1. appを分割する粒度を決める
今回はToDoアプリ自体を最小単位とする

2. ディレクトリ構成を考える
使用するappは一つだけなので、分割もくそもない。
保守性を考えて機能分割する癖をつけたいので、以下のようなディレクトリ構成を考える

〜ディレクトリ図〜

ToDoアプリをユーザー登録して使えるようにしたい！とかなったら、authorization appを追加し、
リンクをテンプレートに貼れば良い。
こうやって機能拡張していくイメージ。

3. app.pyにcreate_app関数を作る
書くこと：
- flask app のインスタンス化（親app）
- 子appのviews.pyのimport
- register_blueprintメソッドで、機能分割したappと子appを結びつける

その後、.envファイルにcreate_appまでのpathを書いておく

4. (子app)/views.pyでBlueprintを使ってアプリをインスタンス化
5. (子app)/views.pyにエンドポイントを書いてく
一旦最初のエンドポイントができた時点で走らせてみて、エラーチェックするとよい、と思う


