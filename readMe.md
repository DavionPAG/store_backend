# Python Server Setup

- install dependecies
python -m pip install flask pymongo flask-pymongo
python -m pip install "pymongo[srv]"

- create virtual environment
python -m venv venv

- activate the virtual environment
    - mac:
    source venv/bin/activate

    - win:
    venv\Scripts\activate

- run the project
python server.py
