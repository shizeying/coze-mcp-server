from setuptools import setup, find_packages

setup(
    name="mcp-coze-server",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "cozepy @ git+https://github.com/shizeying/coze-py.git@v0.13.1.post1",
        "mcp>=1.6.0",
        "pydantic>=2.0.0",
    ],
    python_requires=">=3.11",
) 