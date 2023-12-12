from setuptools import find_packages, setup

setup(
    name='energy_forecasting',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    # entry_points = {
    #     'console_scripts': ['virtual_raphael=virtual_raphael.main:main'],
    # },
    version='0.1.0',
    description='modules for energy forecasting',
    author='Yu Chen (Leslie)',
    license='MIT',
)
