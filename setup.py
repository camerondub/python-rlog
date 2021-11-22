from setuptools import find_packages, setup

setup(
    name="rlog",
    version="21.11.3",
    author="Cameron Wong",
    description="personal python logging configuration (console + rotating file log)",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=["python-decouple"],
)
