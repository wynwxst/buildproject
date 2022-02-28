python -m pip install --upgrade build
python -m pip install --upgrade twine
python -m build
python3 -m twine upload --repository pypi dist/*