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
		int fibn(int);
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
	return fibn(n);
}

int Person::fibn(int in){
	if (in <= 1){
		return (in);
	} else {
		return (fibn(in-1) + fibn(in-2));
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
