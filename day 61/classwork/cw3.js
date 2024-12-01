function Car (name, model) {

    this.name = name
    this.model = model


    this.printInfo = function () {
        console.log(this.name, this.model)
    }

}



const car1 = new Car("Mercedes", "e63");
const car2 = new Car("BMW" , "E38");
const car3 = new Car("Audi", "RSQ8")
