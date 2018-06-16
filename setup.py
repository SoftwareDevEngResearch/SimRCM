try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

setup(
    name='simrcm',
    version='0.1.0',
    description='Simulation of Rapid Compression Machine',
    author='Diba Behnoudfar',
    author_email='dbehnoud@gmail.com',
    url='http://github.com/dbehnoud',
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
    ],
    license='BSD-3-Clause',
    python_requires='>=3',
    zip_safe=False,
    packages=['simrcm', 'simrcm.tests'],
    # or find automatically:
    package=find_packages(),
    package_dir={
        'simrcm': 'simrcm',
        'simrcm.tests': 'simrcm/tests',
        },
    include_package_data=True,

    
)




