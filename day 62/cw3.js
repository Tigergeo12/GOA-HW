const arr = new Array("mercedes", "BMW", "audi", "porsche")
arr.push("Ferrar"); // adds Ferrari to the list
arr.pop(); //removes the last element of the liust "ferrari"
arr.unshift("Lamborghini" , "Maseratti");// adds an element to the start of the list
arr.shift(); //removes the first value in the list
console.log(arr.slice(1,3)) // returs selected elements in a new array doesnt change the original list
arr.splice(2,0, "Bugatti" , "Alfa Romeo") // select where you want to add by the first value then what you want to delete and then the values you are adding