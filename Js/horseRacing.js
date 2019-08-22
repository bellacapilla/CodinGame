// Author: Isabella Navarro
// Solution proposed with Set instead of Array to sort horses
// and avoid duplicatesd values.


const N = parseInt(readline());

let difference = 0;
let allStrength = new Set();

for (let i = 0; i < N; i++) {
    const pi = parseInt(readline());
    
    if (!allStrength.has(pi)) {
        allStrength.add(pi);             
        
        for (let elem of allStrength) {
            let tempVal = Math.abs(pi - elem);
            if (difference === 0 || (tempVal < difference && tempVal !== 0)) {
                 difference = tempVal; 
            }
        }
    } 
}

console.log(difference);  
