from setuptools import setup
import purepyhive


setup(
    name="purepyhive",
    version=purepyhive.__version__,
    description="Pure Sasl Transport Thrift Transport for PyHive",
    url="https://github.com/devinstevenson/pure-pyhive",
    packages=['purepyhive'],
    install_requires=['pyhive', 'thrift', 'pure-sasl'],
    
)
