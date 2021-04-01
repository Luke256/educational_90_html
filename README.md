# 「競プロ典型 90 問」問題まとめ
これは、[@e869120](https://twitter.com/e869120)さんの「競プロ典型 90 問」の問題・入出力例・解説(折り畳み)をひとまとめにしたhtmlを生成するプログラムです。


## このリポジトリについて
- Pythonが使用可能な環境であれば動作します(subprocess,osをインポート)。
- [UIkit](https://getuikit.com)をcssに使用しています。


## 使用方法
1. このリポジトリをクローン
2. クローンしたリポジトリに移動し、[「競プロ典型 90 問」のGitHubリポジトリ](https://github.com/E869120/kyopro_educational_90)をクローン  
以下のようなディレクトリ構造になります
```
.
├── kyopro_educational_90/
│   ├── README.md
│   ├── editorial
│   ├── problem
│   ├── problem-txt
│   ├── sample
│   └── sol
├── tasks/
├── uikit-3.6.5/
│   ├── css
│   └── js
├── README.md
├── index.html
├── template.html
└── update.py
```

3. 以下のコマンドを実行します
```
python update.py
```
4. そうすると、`tasks`ディレクトリ直下に公開されている問題の問題・入出力例・解説(折り畳み)がひとまとめにされたhtmlファイルが生成されます



## その他
なにか、ご質問・ご意見等ありましたら[@Luke02561](https://twitter.com/luke02561)へお問い合わせください(@ツイートをしていただくと見つかりやすいです)。