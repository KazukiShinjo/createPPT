"""スタイル定義（見た目仕様）"""

from dataclasses import dataclass
from typing import Tuple


@dataclass
class ColorPalette:
    """カラーパレット定義"""
    base: str = "#FFFFFF"           # スライド背景
    text: str = "#333333"           # 本文テキスト
    heading: str = "#2E5090"        # 見出し
    accent: str = "#5B9BD5"         # アクセント、箇条書き記号


@dataclass
class FontSettings:
    """フォント設定"""
    heading_font: str = "HGゴシックB"     # 見出し用フォント（フォールバック: Calibri Bold）
    body_font: str = "游ゴシック"        # 本文用フォント（フォールバック: Calibri）


@dataclass
class TextSize:
    """テキストサイズ定義（ポイント）"""
    title_slide: int = 44      # タイトルスライドの題名
    section_heading: int = 40  # セクション見出し
    slide_title: int = 32      # コンテンツスライドタイトル
    body: int = 18             # 本文（箇条書き）
    subtext: int = 14          # サブテキスト


@dataclass
class LayoutMargins:
    """レイアウト・マージン定義（インチ）"""
    horizontal: float = 0.5         # 左右マージン
    vertical: float = 0.5           # 上下マージン
    indent_level1: float = 0.5      # 箇条書き1段目インデント
    indent_level2: float = 1.0      # 箇条書き2段目インデント
    line_spacing: float = 1.15      # 行間


class Styles:
    """スタイル設定の統合クラス"""
    colors = ColorPalette()
    fonts = FontSettings()
    sizes = TextSize()
    margins = LayoutMargins()
