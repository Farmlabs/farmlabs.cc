Farmlabs.cc Open Knowledge Platform
===================================

Quickstart
----------

Create a python3 virtualenv and activate it:

    python3 -m virtualenv -p python3 venv
    . ./venv/bin/activate

Install dependencies:

    pip install -r requirements.txt

Create the development database:

    cd app
    python3 models.py

Start the API server:

    python server.py

Now you can start having fun (hint: the frontend files are in `templates` :). If you're feeling uninspired, just go over [the issues on our Github repo](https://github.com/Farmlabs/farmlabs.cc/issues) and see if you find something you'd like to hack on.

The project is still in its early days, so nothing is set in stone.
