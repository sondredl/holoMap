all:
	@if [ ! -d "build" ]; then mkdir build; fi
	cd build/ && cmake -G Ninja .. && ninja

setup:
	cp project/hooks/pre-commit .git/hooks/pre-commit
	chmod +x .git/hooks/pre-commit
