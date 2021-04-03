person(marcus, pompej).
person(marcus, tallinn).
person(joe, pompej).

born_year(marcus, 40).
born_year(bob, 1999).
born_year(joe, 2005).

male(marcus).
male(bob).
male(joe).

mortal(male).

vulcane_in_pompej(79).
current_year(2019).

not_alive(Person):-
    mortal(Person).

not_alive(Person):-
	person(Person, pompej), 
	current_year(Current_Year),
	vulcane_in_pompej(Vulcane), 
	Current_Year > Vulcane.
	
not_alive(Person):-
	born_year(Person, Born),
    current_year(Current_Year), 
	Vanus is Current_Year - Born, 
	Vanus > 150.