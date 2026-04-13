"""共通ユーティリティ関数"""

import logging
import sys
from pathlib import Path


def setup_logging(log_level: str = "INFO") -> None:
    """
    ログ設定
    
    Args:
        log_level: ログレベル ("DEBUG", "INFO", "WARNING", "ERROR")
    """
    logging.basicConfig(
        level=getattr(logging, log_level),
        format="[%(asctime)s] %(levelname)s - %(name)s - %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout),
        ]
    )


def ensure_output_directory(output_path: str) -> None:
    """
    出力先ディレクトリが存在することを確認し、なければ作成
    
    Args:
        output_path: 出力ファイルパス
    """
    output_dir = Path(output_path).parent
    output_dir.mkdir(parents=True, exist_ok=True)
