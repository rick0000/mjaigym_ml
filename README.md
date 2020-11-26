# mjaigym_ml
## 概要
日本麻雀ライブラリ[mjaigym](https://github.com/rick0000/mjaigym)を使って教師あり学習、強化学習を行うサンプルです。  
本サンプルでは5種類の行動(打牌、リーチ、チー、ポン、カン)を予測する機械学習モデルを作成します。

学習の結果は mlflow Tracking で記録しており、実験結果の比較が容易にできます。


## 機能
1. 教師あり学習
    * 特徴量抽出機能  
        牌譜から特徴量を計算しファイルに保存します。

    * 教師あり学習機能  
        保存した特徴量をもとに機械学習モデルの学習を行います。

2. 強化学習
    * 強化学習機能  
        自己対戦を行い生成した牌譜をもとに機械学習モデルの学習を行います。

3. 評価
    * 一致度評価機能  
        牌譜の内容と機械学習モデルの予測の一致度を計算します。

    * 強さ評価機能  
        対戦を行い機械学習モデルの強さの評価を行います。

4. その他
    * オンライン対戦機能  
        学習した機械学習モデルでオンライン対戦を行います。
    

## 使用方法
* 教師あり学習

```
# 学習用特徴量抽出
python feature_extract.py \
    --mjson_dir <学習用mjson牌譜ファイルのフォルダ> \
    --feature_dir <特徴量出力フォルダ> \
    --extract_config <特徴量抽出コンフィグファイルのパス>

# テスト用用特徴量抽出
python feature_extract.py \
    --mjson_dir <テスト用mjson牌譜ファイルのフォルダ> \
    --feature_dir <特徴量出力フォルダ> \
    --game_num <解析するファイル数上限> \
    --extract_config <特徴量抽出コンフィグファイルのパス>

# 学習
python supervised_train.py \
    --train_feature_dir <学習用特徴量フォルダ> \
    --test_train_dir <テスト用特徴量フォルダ> \
    --model_config <モデル構成コンフィグファイルのパス> \
    --train_config <学習用パラメータコンフィグファイルのパス> \
    --output_dir <モデルファイルを保存するディレクトリのパス> \
    --model_type <学習するモデルの種類(dahai, reach, pon, chi, kan)> \
    --model_dir <[option]既存モデルファイルが保存されているディレクトリのパス>
    
# 精度評価
python evaluate_accuracy.py \
    --extract_config <特徴量抽出コンフィグファイルのパス> \
    --model_config <モデル構成コンフィグファイルのパス> \
    --model_type <評価するモデルの種類(dahai, reach, pon, chi, kan)> \
    --model_dir <[option]既存モデルファイルが保存されているディレクトリのパス>

# 対戦評価
python evaluate_battle.py \
    --extract_config <特徴量抽出コンフィグファイルのパス>\
    --model_config <モデル構成コンフィグファイルのパス>\
    --model_dir <既存モデルファイルが保存されているディレクトリのパス>
```

* 強化学習
```
python reinforcement_train.py \
    --model_config <モデル構成コンフィグファイルのパス> \
    --train_config <学習用パラメータコンフィグファイルのパス> \
    --output_dir <モデルファイルを保存するディレクトリのパス> \

```


# 
データ保存形式
* ラベルデータ＆メタデータ:csv
* 特徴量:numpy.array

