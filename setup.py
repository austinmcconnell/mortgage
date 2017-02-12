from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = [
    'python-dateutil >=2.5.0, < 3.0'
]

test_requirements = [
    'pytest >=3.0.5, <4.0',
    'coverage >=4.3, <5.0',
    'bumpversion >=0.5.3, < 1.0'
]

setup(
    name='mortgage',
    version='1.0.0',
    description='Mortgage Calculator',
    long_description=readme,
    author='Austin McConnell',
    author_email='austin.s.mcconnell@gmail.com',
    url='https://github.com/austinmcconnell/mortgage',
    packages=find_packages(),
    install_requires=requirements,
    license='MIT license',
    zip_safe=False,
    keywords='mortgage',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
