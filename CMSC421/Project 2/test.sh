#!/usr/bin/bash
chmod a+x initial.py
cp initial.py initial
chmod a+x initial
echo './initial'
./initial
./initial
./initial
./initial
./initial

chmod a+x mutate.py
cp mutate.py mutate
chmod a+x mutate
echo './mutate ["*", ["+", ["e", "x"], ["sin", 100]], ["cos", ["-", 400, "x"]]]'
./mutate '["*", ["+", ["e", "x"], ["sin", 100]], ["cos", ["-", 400, "x"]]]'
./mutate '["*", ["+", ["e", "x"], ["sin", 100]], ["cos", ["-", 400, "x"]]]'
./mutate '["*", ["+", ["e", "x"], ["sin", 100]], ["cos", ["-", 400, "x"]]]'
./mutate '["*", ["+", ["e", "x"], ["sin", 100]], ["cos", ["-", 400, "x"]]]'
./mutate '["*", ["+", ["e", "x"], ["sin", 100]], ["cos", ["-", 400, "x"]]]'
echo './mutate ["+", 3, ["-", 2, ["*", 1, "x"]]]'
./mutate '["+", 3, ["-", 2, ["*", 1, "x"]]]'
./mutate '["+", 3, ["-", 2, ["*", 1, "x"]]]'
./mutate '["+", 3, ["-", 2, ["*", 1, "x"]]]'
./mutate '["+", 3, ["-", 2, ["*", 1, "x"]]]'
./mutate '["+", 3, ["-", 2, ["*", 1, "x"]]]'

chmod a+x crossover.py
cp crossover.py crossover
chmod a+x crossover
echo './crossover ["+", 3, ["-", 2, ["*", 1, "x"]]] ["e", ["cos", ["sin", x]]]'
./crossover '["+", 3, ["-", 2, ["*", 1, "x"]]]' '["e", ["cos", ["sin", "x"]]]'
./crossover '["+", 3, ["-", 2, ["*", 1, "x"]]]' '["e", ["cos", ["sin", "x"]]]'
./crossover '["+", 3, ["-", 2, ["*", 1, "x"]]]' '["e", ["cos", ["sin", "x"]]]'
./crossover '["+", 3, ["-", 2, ["*", 1, "x"]]]' '["e", ["cos", ["sin", "x"]]]'
./crossover '["+", 3, ["-", 2, ["*", 1, "x"]]]' '["e", ["cos", ["sin", "x"]]]'

chmod a+x error.py
cp error.py error
chmod a+x error
echo './error line.json ["+", "x", 1]'
./error line.json '["+", "x", 1]'