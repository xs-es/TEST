from setuptools import setup, find_packages

setup(
    name="ez_git",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "PyGithub==2.6.1",
        "python-dotenv==1.0.0",
        "PyQt6==6.6.1",
        "gitpython==3.1.41",
    ],
    python_requires=">=3.8",
) 