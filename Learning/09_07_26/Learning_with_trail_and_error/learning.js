var x= 10;
let y = 3;
 console.log(x+y);

function Demo(){
    return 23;
}

console.log(Demo())
var x=0
function change_color(){
    if(x==0){
        document.getElementById("testing").style.color="red";
        x=1
    }else{
        document.getElementById("testing").style.color="blue";
        x=0
    }    
}

    i=0
    function myFunction() {
        i+=1
        document.getElementById("demo").innerHTML = "Paragraph changed."+i;
    }


    function writing1(){
        document.write("dlkvldb dv lbv bvhlb");
    }
    
    function writing2(){
        document.getElementById("writing").textContent = "hi i have changed";
    }
    function writing3(){
        document.getElementById("writing").innerHTML = "hi i have changed";
    }
    
    function writing4(){
        document.getElementById("writing").innerText = "hi i have changed";
    }

    function bealert(x){
        alert(x);
    }
    function Looping(){
        for (let i = 0; i < 5; i++) {
        text = "The number is " + i + "<br>";
        document.getElementById("loop").innerHTML=text;
        }
    }
    let name=""
    function handleSubmit(event){
        event.preventDefault();
        name = document.getElementById("name").value;
        // alert(name);
        display();
        
    }
    function display(){
        document.getElementById("display").innerHTML = name;
    }
