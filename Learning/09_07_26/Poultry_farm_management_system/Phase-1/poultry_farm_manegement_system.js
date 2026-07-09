class Bird{
    constructor(Id,Breed="",G="U",Purpose="",Parents=[,],DOB="",Approx_age=0,catagory=""){
        this.Id=Id;
        this.Breed=Breed;
        this.G=G
        this.Purpose=Purpose
        this.Parents=Parents
        this.DOB=DOB
        this.Approx_age=Approx_age
        this.catagory=catagory
    }
    getData(){
        return [this.Id,this.Breed,this.G,this.Purpose,this.Parents,this.DOB,this.Approx_age,this.catagory];
    }
}

let Birds = [];
let table=document.getElementById("OP_table")

function Open_Add_new_form(){
    document.getElementById("Add_new_form").style.display="block";
}
function add_data(){
    let newRow = table.insertRow(table.rows.length);
    

}
function handleSubmit(event){
    let form = document.getElementById("form");
    event.preventDefault()
    let id = document.getElementById("id").value;
    let breed = document.getElementById("breed").value;
    let gender = document.getElementById("gender").value;
    let purpose = document.getElementById("purpose").value;
    let parentid_1 = document.getElementById("parentid_1").value;
    let parentid_2 = document.getElementById("parentid_2").value;
    let dob = document.getElementById("dob").value;
    let age = document.getElementById("age").value;
    let catagory = document.getElementById("catagory").value;
    let parentid=[parentid_1,parentid_2]
    Birds.push(new Bird(id,breed,gender,purpose,parentid,dob,age,catagory));
    add_data()
    alert("Your new bird had been added sucessfully");
    document.getElementById("Add_new_form").style.display="none";
    form.reset();
}

function View_Birds(){
    document.getElementById("View_Birds").innerHTML = Birds[0].getData();
    
}
