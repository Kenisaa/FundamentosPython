

let n1 = 0;
let n2 = 1;
let n = 0; 

console.log(n1);
console.log(n2);
while (n < 10) {
    let suma = n1 + n2;
    console.log(suma);
    
    n1 = n2;
    n2 = suma;

    n += 1
}