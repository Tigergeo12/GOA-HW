class person {
    constructor(age, gender){
        this.age = age
        this.gender = gender
    }

    get concatenation(){
        return this.concatenate()
    }

    concatenate(){
        return this.gender + ' ' + this.age + ' years old'
    }
}

const actress = new person(22, 'male')
console.log(actress.concatenation)






class animals {
    constructor(name){
        this.name = name
    }
    makeSound(sound){
        this.sound = sound
        return sound
    }
}

class dog extends animals {
    constructor(name){
        super(name)
    }
}

const Dog = new dog('rexi')

console.log(Dog.makeSound('bark'))
