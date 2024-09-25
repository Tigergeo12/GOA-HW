function uniqueInOrder(sequence){
  const result = []; //listi sadac davamatebt unikalur elementebs
  let lastItem = undefined; 
  
  for(let i = 0; i < sequence.length; i++){
    if(sequence[i] != lastItem){
      result.push(sequence[i]);
      lastItem = sequence[i]
    }
  }
  // tu saiteracio cvladis indexi != wina indexze myop elements vushvebt unikaluri elemnetebius siashi
  return result; //vabrunebt 
}

function uniqueInOrder(iterable){
    let result = [];
    for (let i = 0; i < iterable.length; i++) {
      if (iterable[i-1] === undefined || iterable[i-1] !== iterable[i]) { //|| igivea rac OR pitonshi
        result.push(iterable[i]);
      }
    }
    return result;
  }