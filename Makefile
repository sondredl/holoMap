all:
	mkdir build
	cd build
	cmake ..
	cmake --build .

setup:
	cp project/hooks/pre-commit .git/hooks/pre-commit
	chmod +x .git/hooks/pre-commit
