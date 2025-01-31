from setuptools import setup, find_packages

setup(name='asyncurl',
      version='0.2.0',
      url='https://github.com/hidden-function/asyncurl',
      license='MIT',
      author='Hidekuma',
      author_email='d.hidekuma@gmail.com',
      description='Asynchronous cURL Requests',
      packages=find_packages(exclude=['tests']),
      long_description=open('README.md').read(),
      long_description_content_type='text/markdown',
      zip_safe=False,
      keywords=['async', 'asynchronous', 'requests', 'cURL', 'curl', 'crawling'],
      install_requires=[
        'asyncio>=3.4.3',
        'requests>=2.22.0',
        'uvloop>=0.12.2'
      ],
      python_requires = '>=3.6',
      test_suite='tests')
