from setuptools import setup, find_packages

setup(
    name='MOOCsCubeX', 
    version='0.1',  
    packages=find_packages(), 
    install_requires=[ 
      'matplotlib==3.8.0',
      'networkx==3.4.2',
      'node2vec==0.5.0',
      'scikit-learn==1.5.2',
      'six==1.16.0',
      'sklearn-pandas==2.2.0',
      'tqdm==4.66.6'
    ],
    python_requires='>=3.6',  # Phiên bản Python tối thiểu
)
