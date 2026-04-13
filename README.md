# createPPT - PowerPoint自動生成アプリケーション

PythonでJSONデータからPowerPointスライド（.pptx）を自動生成するアプリケーションです。

## 🎯 プロジェクト概要

指定された入力データから、自動的に構造化されたスライドを作成します。テンプレート形式のJSONファイルに従うだけで、簡単に美しいPowerPointプレゼンテーションが生成できます。

## 🧱 プロジェクト構成

```
createPPT/
├── src/
│   ├── models/              # データモデル層
│   │   ├── presentation.py  # プレゼンテーション、スライドデータ構造
│   │   └── styles.py        # スタイル定義（カラー、フォント、サイズ）
│   ├── services/            # ビジネスロジック層
│   │   └── validator.py     # 入力検証ルール
│   ├── generators/          # PowerPoint生成エンジン
│   │   └── pptx_generator.py # PPTX生成ロジック
│   ├── utils/               # ユーティリティ層
│   │   └── common.py        # 共通処理（ログ、ディレクトリ管理）
│   └── main.py              # メインエントリーポイント
├── tests/
│   └── test_core.py         # ユニットテスト
├── example_input.json       # 入力データ例
├── .github/
│   └── copilot-instructions.md  # Copilot指示書
└── README.md
```

## ⚙️ 使用技術

- **Python 3.11以上**
- **python-pptx**: PowerPoint生成ライブラリ
- **typing**: 型ヒント
- **logging**: ログ機能

## 📊 入力データ形式

### JSON構造例

```json
{
  "title": "プレゼンタイトル",
  "slides": [
    {
      "title": "スライド1",
      "content": ["ポイント1", "ポイント2", "ポイント3"]
    },
    {
      "title": "スライド2",
      "content": ["項目A", "項目B"]
    }
  ]
}
```

### 入力検証ルール

| フィールド | ルール | 必須 |
|----------|--------|------|
| title (プレゼンテーション) | 1～100文字 | ✅ |
| slides | 1～500スライド | ✅ |
| title (スライド) | 1～80文字 | ✅ |
| content | 配列、最大10行、1行最大100文字 | ✅ |

## 🎨 見た目仕様

### カラーパレット

- **背景**: 白 (#FFFFFF)
- **本文テキスト**: ダークグレー (#333333)
- **見出し**: ダークブルー (#2E5090)
- **アクセント**: ライトブルー (#5B9BD5)

### フォント設定

- **見出し**: HGゴシックB（フォールバック: Calibri Bold）
- **本文**: 游ゴシック（フォールバック: Calibri）

### テキストサイズ（ポイント）

| 要素 | サイズ |
|------|--------|
| タイトルスライド題名 | 44pt |
| セクション見出し | 40pt |
| コンテンツスライドタイトル | 32pt |
| 本文（箇条書き） | 18pt |
| サブテキスト | 14pt |

## 🚀 使用方法

### インストール

```bash
pip install python-pptx
```

### 実行

```bash
python src/main.py <入力JSONパス> <出力PowerPointパス>
```

### 例

```bash
python src/main.py example_input.json output.pptx
```

## 🧪 テスト実行

```bash
python -m pytest tests/ -v
# または
python -m unittest discover tests/
```

## 🚨 エラーハンドリング

### 入力検証エラー

- **無効なJSON形式**: エラーメッセージ表示して処理中止
- **必須フィールド不足**: 不足フィールドを指摘して中止
- **文字数超過**: 警告を記録して短縮処理

### 生成エラー

- **PowerPoint生成失敗**: スタックトレースをログに記録
- **ファイル書き込みエラー**: ディスク容量・権限確認を促す

### ロギングレベル

- **ERROR**: 生成失敗時
- **WARNING**: 入力修正時
- **INFO**: 正常完了時（処理時間を記録）

## ⚡ パフォーマンス

- **推奨処理数**: 100～500スライド
- **目標処理時間**: 100スライドで5秒以内
- **メモリ効率**: ストリーミング処理による大規模対応を検討中

### 制限事項

- 1スライドあたりのテキスト量に上限あり（100文字×10行が目安）
- 画像挿入は現フェーズでは非対応（将来拡張予定）

## 📝 単一責任の原則

- **models/**: データ構造と検証ルール
- **services/**: ビジネスロジック（入力処理）
- **generators/**: PowerPoint生成エンジン
- **utils/**: 共通処理

## 🔄 将来の拡張予定

- 画像挿入機能
- テーマ・テンプレート選択
- 図表・グラフ挿入
- セクション管理機能
- エクスポート形式拡張（PDF、HTML等）

## 📄 ライセンス

MIT License

## 👨‍💻 開発情報

このプロジェクトはCopilot指示書に基づいて実装されています。詳細は [.github/copilot-instructions.md](.github/copilot-instructions.md) を参照してください。
