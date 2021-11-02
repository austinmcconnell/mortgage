from setuptools import setup, find_packages

with open('README.md') as f:
    LONG_DESCRIPTION = f.read()

setup(
    name='mortgage',
    version='1.0.5',
    description='Mortgage Calculator',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='Austin McConnell',
    author_email='austin.s.mcconnell@gmail.com',
    url='https://github.com/austinmcconnell/mortgage',
    packages=find_packages(exclude=['docs', 'tests']),
    python_requires='>=3.5',
    install_requires=[],
    extras_require={
        'develop': ['bump2version>=1.0.1,<2.0.0',
                    'pre-commit>=2.15.0,<3.0.0',
                    'pytest>=6.2.5,<7.0.0',
                    'pytest-cov>=3.0.0,<4.0.0',
                    'recommonmark>=0.7.1,<1.0.0',
                    'sphinx>=4.2.0,<5.0.0',
                    'sphinx-autodoc-typehints>=1.12.0,<2.0.0',
                    'tox>=3.24.4,<4.0.0']
    },
    license='MIT license',
    zip_safe=False,
    keywords='mortgage',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    test_suite='tests'
)
