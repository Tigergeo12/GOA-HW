function findLongest(array) {
    if (array.length === 0) {
      return "Empty array"
    }
  
    let max = array[0];
    for (let i of array) {
      if (i > max) {
        max = i;
      }
    }
    return max;
  }