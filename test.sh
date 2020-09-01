FILES=inputs/*
OUTPUT_DIR=outputs/
EXPECTED_OUTPUT_DIR=expectedOutputs/

for f in $FILES
do
	echo "Flattening $f"
	python3 jsonflattener.py $OUTPUT_DIR $f
	cmp -s $OUTPUT_DIR$(basename $f) $EXPECTED_OUTPUT_DIR$(basename $f) || echo "TEST $f FAILED"

done
