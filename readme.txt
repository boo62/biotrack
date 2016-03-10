# I suggest you install inside a virtual environment.

# Uncompress tar file
tar -zxvf biotrack-0.1.tar.gz
cd biotrack-0.1/

# To run tests before installing.
python setup.py test

# To install.
python setup.py install

# You can run the script modcomp on the example models provided.
cd tests/example_models/
modcomp <filename>
