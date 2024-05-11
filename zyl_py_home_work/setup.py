from setuptools import setup, find_packages

setup(
    name='pythonHomework',
    version='0.1.0',
    author='Junxi Den',
    author_email='weimanbeihou@outlook.com',
    description='pythonHomework',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/1125wei/pythonHomework',
    packages=find_packages(),
    install_requires=[
        # 依赖列表
    ],
    classifiers=[
        # 开发状态
        'Development Status :: 3 - Alpha',
        # 目标用户
        'Intended Audience :: Developers',
        # 许可证（比如MIT License）
        'License :: OSI Approved :: MIT License',
        # 兼容的Python版本
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.6',
)
