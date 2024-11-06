// Base class: Animal
class Animal {
    constructor(name) {
        this.name = name;
    }

    speak() {
        console.log(`${this.name} makes a noise.`);
    }
}

// Child class: Mammal
class Mammal extends Animal {
    constructor(name, furColor) {
        super(name); // Call the constructor of the parent class (Animal)
        this.furColor = furColor;
    }

    speak() {
        console.log(`${this.name} makes a mammal noise.`);
    }
}

// Child class: Dog
class Dog extends Mammal {
    constructor(name, furColor, breed) {
        super(name, furColor); // Call the constructor of the parent class (Mammal)
        this.breed = breed;
    }

    speak() {
        console.log(`${this.name} barks.`);
    }
}

