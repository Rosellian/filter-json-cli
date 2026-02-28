format:
\tblack src tests

lint:
\tflake8 src tests

test:
\tpytest -q

all: format lint test
