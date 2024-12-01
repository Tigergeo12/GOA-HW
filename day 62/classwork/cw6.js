function manualIndexOf(array, element) {
    for (let i = 0; i < array.length; i++) {
        if (array[i] = element) {
            return i; 
        }
    }
    return -1; 
}


const fruits = ['apple', 'banana', 'cherry', 'date'];
console.log(manualIndexOf(fruits, 'cherry')); 
console.log(manualIndexOf(fruits, 'grape'));  