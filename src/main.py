"""メインエントリーポイント"""

import sys
import logging
import time
from pathlib import Path
from src.services.validator import InputValidator, ValidationError
from src.generators.pptx_generator import PresentationGenerator
from src.utils.common import setup_logging, ensure_output_directory


def main(json_input_path: str, output_pptx_path: str) -> int:
    """
    プレゼンテーション生成のメイン処理
    
    Args:
        json_input_path: 入力JSONファイルパス
        output_pptx_path: 出力PowerPointファイルパス
        
    Returns:
        終了コード（0: 成功, 1: エラー）
    """
    setup_logging("INFO")
    logger = logging.getLogger(__name__)

    try:
        start_time = time.time()
        logger.info(f"処理開始: {json_input_path} → {output_pptx_path}")

        # 入力ファイルの読み込み
        input_path = Path(json_input_path)
        if not input_path.exists():
            logger.error(f"入力ファイルが見つかりません: {json_input_path}")
            return 1

        with open(input_path, "r", encoding="utf-8") as f:
            json_data = f.read()

        # 検証
        logger.info("入力データを検証しています...")
        presentation = InputValidator.validate_from_json(json_data)

        # PowerPoint生成
        logger.info("PowerPointを生成しています...")
        ensure_output_directory(output_pptx_path)

        generator = PresentationGenerator()
        generator.generate(presentation, output_pptx_path)

        elapsed_time = time.time() - start_time
        logger.info(f"✅ 処理完了: {elapsed_time:.2f}秒")
        return 0

    except ValidationError as e:
        logger.error(f"検証エラー: {e}")
        return 1
    except IOError as e:
        logger.error(f"ファイルエラー: {e}")
        return 1
    except Exception as e:
        logger.error(f"予期しないエラー: {e}", exc_info=True)
        return 1


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("使用方法: python main.py <入力JSONパス> <出力PowerPointパス>")
        sys.exit(1)

    exit_code = main(sys.argv[1], sys.argv[2])
    sys.exit(exit_code)
