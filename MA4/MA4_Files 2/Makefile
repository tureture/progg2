# Makefile for MA4
all:
	g++ -std=c++11 -c -fPIC person.cpp -o person.o
	g++ -std=c++11 -shared -o libperson.so  person.o	
clean:
	rm -fr *.o *.so __pycache__