from numpy.distutils.core import setup

package_data = {
    'Gahdf5': [
        'gahdf5/*',
        'tests/*',
    ]
}

setup(
    name='Gahdf5',
    python_requires='>=3.7',
    version="0.1",
    packages=['gahdf5'],
    package_data=package_data,
    scripts=['bin/convert_to_hdf5', 'bin/without_parttype', 'bin/inside_hdf5'],
    description="Do something",
    author="Vinicius Lourival Bilck",
    author_email="bilck.vinicius1998@gmail.com",
    url='https://github.com/ViniBilck/Gahdf5',
    platform='Linux',
    license="MIT License",
    classifiers=['Programming Language :: Python :: 3.7'],
)
