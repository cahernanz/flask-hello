from setuptools import (
    find_packages,
    setup,
)

setup(
    name='flask_hello',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            'flask_hello=flask_hello.app:main',
        ]
    },
)
