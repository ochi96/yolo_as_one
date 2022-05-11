from setuptools import setup, find_packages


setup(
    name='yolo_as_one',
    version='0.2',
    license='MIT',
    author="Bramwel Ochieng",
    author_email='lol@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/ochi96/yolo_as_one',
    keywords='yolo installation inferencing'
    # install_requires=[
    #       'scikit-learn',
    #   ]
)
