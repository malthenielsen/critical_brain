gcc_flags= -fopenmp -g -lm -pthread -O3 -Wall -Wextra -pedantic

EXE=IE_neuron

SRC=$(EXE).cpp

run: $(EXE)
	./$(EXE)
	python ./IE_analysis.py


$(EXE): $(SRC)
		g++ $(gcc_flags) $< -o $@

clean:
	rm -rf $(EXE)
	rm -rf results.bin
