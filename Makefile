all:
	#build

setup:
	cp project/hooks/pre-commit .git/hooks/pre-commit
	chmod +x .git/hooks/pre-commit
