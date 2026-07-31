from setuptools import setup, find_packages

setup(
    name="phishing",
    version="1.0",
    packages=find_packages(),
    py_modules=["run"],
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "run=run:main",
        ],
    },
)