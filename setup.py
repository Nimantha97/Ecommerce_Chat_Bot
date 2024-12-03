from setuptools import find_packages, setup

setup(
    name="Ecommercebot",
    version="0.0.1",
    author="nimantha",
    author_email="nimantha.nimanthagayan0309@gmail.com",
    packages=find_packages(),
    install_requires=['langchain-astradb','langchain ','langchain-openai','datasets','pypdf','python-dotenv','flask']
)
