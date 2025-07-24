from setuptools import setup, find_packages

with open("README.md", "r", encoding="UTF-8") as readme:
    description = readme.read()
setup(
    name                            = "MySQLite",
    version                         = "0.1.0",
    author                          = "BX293A_PEN",
    description                     = "QUICを簡単に使えるようにするモジュール",
    long_description                = description,          # パッケージの詳細な説明 (通常はREADME.mdから読み込む)
    long_description_content_type   = "text/markdown",      # long_descriptionの形式
    url                             = "https://github.com/BX293APEN/MySQLite",
    packages                        = find_packages(),      # パッケージを見つける
    classifiers                     = [                     # パッケージの分類情報
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires                 = ">=3.6",              # 必須とするPythonのバージョン
    entry_points={                                          # コマンドラインツールとしてインストールする場合
        "console_scripts": [
            "MySQLite=MySQLite.MySQLite:main",
        ],
    },
)