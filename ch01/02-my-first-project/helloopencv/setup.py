from setuptools import setup

setup(
    name='helloopencv',
    version='0.1',
    py_modules=["helloopencv"],
    license='MIT',
    description='An example python opencv project',
    long_description=open('README.rst').read(),
    install_requires=['numpy', 'opencv-contrib-python'],
    url='https://github.com/Lawrence-Krukrubo/Exploring_Python_openCV4.git',
    author='Lawrence Krukrubo',
    author_email='sisokels@gmail.com'
)