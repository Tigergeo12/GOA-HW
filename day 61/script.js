const me = {
    // Properties of me
    name: "luka", // string for my name
    age: 15, // integer/number for my age
    weight: 98, 
    gender: "male", // string property for the person's gender
    handsome_jacked: true, // boolean property (initially set to true (always will be true))
    // Method/function of the object
    func: function() {
        // Log a greeting message to the console using the person's name
        console.log("Hello, I am " + this.name);//this is something you can use to call for any key value in a object without needing to find it.
    }
}

me.name = "giorgi" // changing a value of a key
delete me.age //deleting a key and value