"""入力データバリデーション"""

import json
import logging
from typing import Dict, Any
from src.models.presentation import Presentation, Slide


logger = logging.getLogger(__name__)


class ValidationError(Exception):
    """バリデーションエラー"""
    pass


class InputValidator:
    """入力データの検証を行う"""

    @staticmethod
    def validate_json(data: str) -> Dict[str, Any]:
        """
        JSON形式の検証
        
        Args:
            data: JSON文字列
            
        Returns:
            パース済みの辞書
            
        Raises:
            ValidationError: 無効なJSON形式の場合
        """
        try:
            return json.loads(data)
        except json.JSONDecodeError as e:
            logger.error(f"無効なJSON形式: {e}")
            raise ValidationError(f"無効なJSON形式です: {e}")

    @staticmethod
    def validate_presentation_dict(data: Dict[str, Any]) -> Presentation:
        """
        プレゼンテーション辞書の検証と変換
        
        Args:
            data: プレゼンテーションデータの辞書
            
        Returns:
            Presentationオブジェクト
            
        Raises:
            ValidationError: 必須フィールド不足または値が不正な場合
        """
        # 必須フィールドの確認
        if "title" not in data:
            logger.error("必須フィールド不足: 'title'")
            raise ValidationError("必須フィールド 'title' がありません")

        if "slides" not in data:
            logger.error("必須フィールド不足: 'slides'")
            raise ValidationError("必須フィールド 'slides' がありません")

        # スライドデータの変換
        try:
            slides = [
                Slide(title=slide.get("title", ""), content=slide.get("content", []))
                for slide in data["slides"]
            ]
            presentation = Presentation(title=data["title"], slides=slides)
        except (KeyError, TypeError) as e:
            logger.error(f"スライドデータの形式が不正です: {e}")
            raise ValidationError(f"スライドデータの形式が不正です: {e}")

        # 検証の実行
        if not presentation.validate():
            logger.error("プレゼンテーションデータが検証ルールに違反しています")
            raise ValidationError("プレゼンテーションデータが検証ルールに違反しています")

        logger.info(f"検証成功: タイトル='{presentation.title}', スライド数={len(presentation.slides)}")
        return presentation

    @staticmethod
    def validate_from_json(json_data: str) -> Presentation:
        """
        JSON文字列からプレゼンテーションを検証・生成
        
        Args:
            json_data: JSON形式のプレゼンテーションデータ
            
        Returns:
            Presentationオブジェクト
            
        Raises:
            ValidationError: 検証に失敗した場合
        """
        data_dict = InputValidator.validate_json(json_data)
        return InputValidator.validate_presentation_dict(data_dict)
