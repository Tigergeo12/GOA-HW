//1
const countriesAndCapitals = new Map();

countriesAndCapitals.set('France', 'Paris');
countriesAndCapitals.set('Japan', 'Tokyo');
countriesAndCapitals.set('Brazil', 'Brasilia');

console.log(countriesAndCapitals)

//2

if(countriesAndCapitals.has("Japan")){
    console.log("Japan is in the list !")
}

//3

const studentsMarks = new Map();
studentsMarks.set("Cotne", 85);
studentsMarks.set("Giorgi" , 62);
studentsMarks.set("Luka" , 100);

console.log(studentsMarks.get("Luka"))

//4

const keys = new Map ();
keys.set("key1");
keys.set("key2");
keys.set("key3");

for(let i=0;i<keys.length;i++);
console.log(keys.keys());

//5

const continents = new Map ();
continents.set("Europe", "Nature");
continents.set("Asia", "Culture");
continents.set("Africa", "Wildlife");
continents.delete("Africa");
console.log(continents)

//6

console.log(continents.size);

//7

continents.set("North america" , "USA");
continents.set("Europe" , "Pretty women");
console.log(continents);

//8

function isMapEmpty(map) {
    return map.size = 0;
}

//9

//????

//10

console.log(continents.clear()) //undefined
