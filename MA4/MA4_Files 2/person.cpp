#include <cstdlib>
// Person class 

class Person{
	public:
		Person(int);
		int get();
		int fibc(int);
		void set(int);
	private:
		int age;
	};
 
Person::Person(int n){
	age = n;
	}
 
int Person::get(){
	return age;
	}
 
void Person::set(int n){
	age = n;
	}

int Person::fibc(int n){
	if (n <= 1){
		return 0;
	} else {
		return fibc(n-1) + fibc(n-2);
	}
}



extern "C"{
	Person* Person_new(int n) {return new Person(n);}
	int Person_get(Person* person) {return person->get();}
	int Person_fibc(Person* person, int n) {return person->fibc(n);}
	void Person_set(Person* person, int n) {person->set(n);}
	void Person_delete(Person* person){
		if (person){
			delete person;
			person = nullptr;
			}
		}
	}
