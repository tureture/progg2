#include <cstdlib>
// Person class 

class Person{
	public:
		Person(int);
		int get();
		int fib();
		void set(int);
	private:
		int n;
		int _fib(int);
	};
 
Person::Person(int in){
	n = in;
	}
 
int Person::get(){
	return n;
	}
 
void Person::set(int in){
	n = in;
	}

int Person::fib(){
	return _fib(n);
}

int Person::_fib(int in){
	if (in <= 1){
		return 0;
	} else {
		return _fib(in-1) + _fib(in-2);
	}
}



extern "C"{
	Person* Person_new(int n) {return new Person(n);}
	int Person_get(Person* person) {return person->get();}
	int Person_fib(Person* person) {return person->fib();}
	void Person_set(Person* person, int n) {person->set(n);}
	void Person_delete(Person* person){
		if (person){
			delete person;
			person = nullptr;
			}
		}
	}
