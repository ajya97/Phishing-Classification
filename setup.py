from setuptools import setup

setup(
    name="phishing",
    version="1.0",
    py_modules=["run"],
    entry_points={
        "console_scripts": [
            "run=run:main",
        ],
    },
)