function smaller(nums) {
    let newArray = [];
    for(let i = 0; i < nums.length; i++) {
        let count = 0; 
        for(let n = i + 1; n < nums.length; n++) {
            if(nums[n] < nums[i]) { 
                count = count + 1;
            }
        }
        newArray.push(count); 
    }
    
    return newArray; 
}