from setuptools import setup, find_packages


setup(
    name="IrGateways",
    version='0.0.1',
    author="MohammadMahdi Arbabpouri",
    author_email="sardarcyberym@gmail.com",
    description="IrGateways for connect to iranian payment",
    long_description="IrGateways using for connect to iranian payment, for example: Zarinpal, Nextpay and more",
    packages=find_packages(),
    install_requires=["requests", "pydantic"],
    keywords=["python", "IrGateways", "IranianPayment"],
    classifiers=["Programming Language :: Python :: 3"]
)
