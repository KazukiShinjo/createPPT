"""プレゼンテーション生成テスト"""

import unittest
import json
import tempfile
from pathlib import Path
from src.models.presentation import Presentation, Slide
from src.services.validator import InputValidator, ValidationError
from src.generators.pptx_generator import PresentationGenerator


class TestModels(unittest.TestCase):
    """モデルのテスト"""

    def test_slide_validate_valid(self):
        """有効なスライドの検証"""
        slide = Slide(title="テスト", content=["ポイント1", "ポイント2"])
        self.assertTrue(slide.validate())

    def test_slide_validate_invalid_title_empty(self):
        """タイトルが空のスライドは無効"""
        slide = Slide(title="", content=["ポイント"])
        self.assertFalse(slide.validate())

    def test_slide_validate_invalid_title_too_long(self):
        """タイトルが長すぎるスライドは無効"""
        slide = Slide(title="a" * 81, content=["ポイント"])
        self.assertFalse(slide.validate())

    def test_slide_validate_invalid_content_too_many_items(self):
        """コンテンツアイテムが多すぎるスライドは無効"""
        slide = Slide(title="テスト", content=[f"ポイント{i}" for i in range(11)])
        self.assertFalse(slide.validate())

    def test_presentation_validate_valid(self):
        """有効なプレゼンテーションの検証"""
        slides = [Slide(title="スライド1", content=["ポイント1"])]
        presentation = Presentation(title="テストプレゼン", slides=slides)
        self.assertTrue(presentation.validate())

    def test_presentation_validate_invalid_title_empty(self):
        """タイトルが空のプレゼンテーションは無効"""
        slides = [Slide(title="スライド1", content=["ポイント1"])]
        presentation = Presentation(title="", slides=slides)
        self.assertFalse(presentation.validate())

    def test_presentation_validate_invalid_no_slides(self):
        """スライドがないプレゼンテーションは無効"""
        presentation = Presentation(title="テスト", slides=[])
        self.assertFalse(presentation.validate())


class TestValidator(unittest.TestCase):
    """バリデーターのテスト"""

    def test_validate_json_valid(self):
        """有効なJSON形式の検証"""
        json_str = '{"title": "テスト", "slides": [{"title": "スライド1", "content": ["ポイント1"]}]}'
        result = InputValidator.validate_json(json_str)
        self.assertEqual(result["title"], "テスト")

    def test_validate_json_invalid(self):
        """無効なJSON形式の検証"""
        json_str = '{"title": "テスト"'  # 不正なJSON
        with self.assertRaises(ValidationError):
            InputValidator.validate_json(json_str)

    def test_validate_presentation_dict_missing_title(self):
        """必須フィールド 'title' が不足している場合"""
        data = {"slides": []}
        with self.assertRaises(ValidationError):
            InputValidator.validate_presentation_dict(data)

    def test_validate_presentation_dict_missing_slides(self):
        """必須フィールド 'slides' が不足している場合"""
        data = {"title": "テスト"}
        with self.assertRaises(ValidationError):
            InputValidator.validate_presentation_dict(data)


class TestGenerator(unittest.TestCase):
    """ジェネレーターのテスト"""

    def test_generate_pptx(self):
        """PowerPointファイル生成テスト"""
        with tempfile.TemporaryDirectory() as tmpdir:
            output_path = Path(tmpdir) / "test.pptx"

            slides = [
                Slide(title="スライド1", content=["ポイント1", "ポイント2"]),
                Slide(title="スライド2", content=["ポイント3"]),
            ]
            presentation = Presentation(title="テストプレゼン", slides=slides)

            generator = PresentationGenerator()
            generator.generate(presentation, str(output_path))

            # ファイルが生成されたことを確認
            self.assertTrue(output_path.exists())
            self.assertGreater(output_path.stat().st_size, 0)


if __name__ == "__main__":
    unittest.main()
