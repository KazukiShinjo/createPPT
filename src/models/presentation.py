"""プレゼンテーションデータモデル定義"""

from typing import List
from dataclasses import dataclass


@dataclass
class Slide:
    """スライドデータの構造を定義"""
    title: str
    content: List[str]

    def validate(self) -> bool:
        """入力検証ルールに従う"""
        if not isinstance(self.title, str) or len(self.title) == 0 or len(self.title) > 80:
            return False
        if not isinstance(self.content, list) or len(self.content) > 10:
            return False
        for item in self.content:
            if not isinstance(item, str) or len(item) == 0 or len(item) > 100:
                return False
        return True


@dataclass
class Presentation:
    """プレゼンテーション全体の構造を定義"""
    title: str
    slides: List[Slide]

    def validate(self) -> bool:
        """入力検証ルールに従う"""
        if not isinstance(self.title, str) or len(self.title) == 0 or len(self.title) > 100:
            return False
        if not isinstance(self.slides, list) or len(self.slides) < 1 or len(self.slides) > 500:
            return False
        return all(slide.validate() for slide in self.slides)
