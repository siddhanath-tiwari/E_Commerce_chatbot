from setuptools import find_packages, setup

setup(
    name="E_Commerce_chatbot",
    version="0.0.1",
    author="siddhanth-tiwari",
    author_email="pratimatiwari8299@gmail.com", 
    packages=find_packages(),
    install_requires=['langchain-astradb','langchain ','langchain-openai','datasets','pypdf','python-dotenv','flask']
)