from setuptools import setup

setup(
    name='SarsCov2_aminoAcid_App',
    version='1.0.0',
    packages=['sarsCov2Lib'],
    url='',
    license='MIT',
    author='Alexander Graf',
    author_email='graf@genzentrum.lmu.de',
    description='Sars-CoV-2 Amino Acid Extractor',
    include_package_data=True,
    install_requires=[
        'PyQt5==5.15'
    ],
    scripts=['bin/sarsCov2AminoAcidGrabber'],
    package_data={'': ['reference/*']}
)
