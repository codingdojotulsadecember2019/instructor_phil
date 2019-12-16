function multiply(x,y){
  console.log(x);
  console.log(y);
}
b = multiply(2,3);
console.log(b);

console.log('---------------------------------------------------------------------------------------------------------------------');

function multiply(x,y){
  return x*y;
}
b = multiply(2,3);
console.log(b);
console.log(multiply(5,2));

console.log('---------------------------------------------------------------------------------------------------------------------');

var x = [1,2,3,4,5,10];
for(var i=0; i<5; i++)
{
 i = i + 3; 
 console.log(i);
}

console.log('---------------------------------------------------------------------------------------------------------------------');

var x=15;
console.log(x);
function awesome(){
  var x=10;
  console.log(x);
}
console.log(x);
awesome();
console.log(x);

console.log('---------------------------------------------------------------------------------------------------------------------');

for(var i=0; i<15; i+=2){
 console.log(i);
}

console.log('---------------------------------------------------------------------------------------------------------------------');

for(var i=0; i<3; i++){
 for(var j=0; j<2; j++){
     console.log(i*j);
 }
}

console.log('---------------------------------------------------------------------------------------------------------------------');

function looping(x,y){
 for(var i=0; i<x; i++){
    for(var j=0; j<x; j++){
        console.log(i*j);
    } 
 }
}
z = looping(3,3);
console.log(z);

console.log('---------------------------------------------------------------------------------------------------------------------');

function looping(x,y){
 for(var i=0; i<x; i++){
    for(var j=0; j<y; j++){
       console.log(i*j);
    } 
 }
 return x*y;
}
z = looping(3,5);
console.log(z);
