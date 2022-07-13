install:
	@pip install -r requirements.txt

test:
	@pytest -x tests/

run:
	python3 main.py