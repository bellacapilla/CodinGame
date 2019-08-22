/*
Author: Isabella Navarro
Solution proposed with Set instead of Array to sort horses
and avoid duplicatesd values.

Problem:
Casablanca’s hippodrome is organizing a new type of horse racing: duals. During a dual, only two horses will 
participate in the race. In order for the race to be interesting, it is necessary to try to select two horses with similar strength.

Write a program which, using a given number of strengths, identifies the two closest strengths and shows their difference with an 
integer (≥ 0).
*/

// Input
const N = parseInt(readline());

let difference = 0; // Initializes a variable for the calculated difference.
let allStrength = new Set(); // Initializes a new Set.

for (let i = 0; i < N; i++) { // Loops through the input lines
    const pi = parseInt(readline()); // Parse input line int
    
    if (!allStrength.has(pi)) { // Checks if pi is not yet in Set
        allStrength.add(pi);    // Add pi to Set
        
        for (let elem of allStrength) { // Loop through elements and calculate differences
            let tempVal = Math.abs(pi - elem);
            if (difference === 0 || (tempVal < difference && tempVal !== 0)) {
                 difference = tempVal; // Updates difference value
            }
        }
    } 
}

// Output
console.log(difference);  
