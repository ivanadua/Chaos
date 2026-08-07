async function run() {

const theta1=document.getElementById("t1").value;
const theta2=document.getElementById("t2").value;
const theta3=document.getElementById("t3").value;

const response=await fetch("https://YOUR-RENDER-URL.onrender.com/simulate",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({
theta1,
theta2,
theta3
})

});

const blob=await response.blob();

document.getElementById("gif").src=URL.createObjectURL(blob);

}
