# 第6回
## 五目並べゲーム(ex06/gomoku.py)
### 制作者一覧
- コード代表者：C0B21079 渋谷佳吾
- README.md作成・議論者：C0B21079 渋谷佳吾,C0B21123 永野一輝,C0B21039 郭軒邑,C0B21003 赤石涼太,C0B21053 唐澤昂希 
### ゲーム概要
- ex06/gomoku.pyを実行すると、700×700のスクリーンに碁盤が表示される。プレイヤーは交代制で黒と白の石を置く。
- 先に縦・横・斜めで連続5つ石を並べたプレイヤーの勝ちとなり、各プレイヤーの勝利条件に適したメッセージボックスが表示される。

### 操作方法
- 盤面上にクリックすることで自分の石を配置することができる。

### クリア条件
- 縦・横・斜めいずれかで自分の石を連続5つ配置することができれば勝利。

### Gobangクラスの説明
- class Gobangというクラスの中で具体的にはゲーム処理を行っている。
- create_canvasメソッド：ウィジェット作成・配置
- set_eventメソッド：イベント設定
- init_gobangメソッド：ゲーム初期化
- draw_diskメソッド：石の描画
- intersectionメソッド：キャンバス上の座標を交点の位置に変換
- clickメソッド：盤面がクリックされたときの処理
- placeメソッド：(x,y)の交点に色がcolorの石を置く
- countメソッド：(x,y)に色がcolorの意思を置いた場合の石の並び数をチェック
- show_resultメソッド：ゲーム終了時の結果を表示する

### ToDo
- 石を配置するまで制限時間を設けたかった。

### 参考文献
- だえうホームページ,[Python/tkinter]五目並べゲームの作り方,2022年11月15日参照,https://daeudaeu.com/tkinter-gobang/
