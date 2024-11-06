class Animal { // main class 
    constructor(name, age, type) {
        this.name = name;
        this.age = age;
        this.type = type;
    }

    displayAnimal() {
        console.log(this.name);
        console.log(this.age);
        console.log(this.type);
    }
}
// Inherited class Dog
class Dog extends Animal {
    constructor(name, age, breed) {
        super(name, age, "mammal"); // called the constructor from the parent function so we dont have to write the constructor again
        this.breed = breed; 
    }

    displayDog() {
        this.displayAnimal(); 
        console.log(this.breed);
    }
}
// Inherited class Cat
class Cat extends Animal {
    constructor(name, age, color) {
        super(name, age, "mammal"); 
        this.color = color; 
    }

    displayCat() {
        this.displayAnimal(); 
        console.log(this.color);
    }
}