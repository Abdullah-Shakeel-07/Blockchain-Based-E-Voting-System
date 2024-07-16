
function checkData()
{
    try{
    let fname=document.getElementById("fname").value
    let lname=document.getElementById("lname").value
    let cnic=document.getElementById("CNIC").value
    let Vote=document.querySelector('input[name="fav_language"]:checked').value
    var dt = {}
    dt['sendData'] = { "fname": fname, "lname": lname, "cnic": cnic, "Vote": Vote }

    fetch('http://127.0.0.1:8000/SendInformation', { method: 'POST', mode: 'no-cors', body: JSON.stringify(dt) })
    .then(response => response.json())
    .then(json => {
        if(json==1)
        {
            alert("Your Vote was successfully casted to " + Vote)
        }
        else if(json==0)
        {
            alert("Your Vote was unsuccessfull")
        }
        else
        {
            if(json['state'])
                alert("Your Vote was successfully casted to " + Vote)



                document.getElementById("inpform").remove();


                divdata=document.getElementById("addmoreinfo");
                
                divdata.appendChild(document.createElement('br'))
                voter1=document.createElement("h1");
                voter1.className="text-slate-200 text-3xl font-bold";
                voter1.innerHTML="Abdullah: " + String(json['Abdullah']);
                divdata.appendChild(voter1);
    
                divdata.appendChild(document.createElement('br'))
                voter1=document.createElement("h1");
                voter1.className="text-slate-200 text-3xl font-bold";
                voter1.innerHTML="Haris: " + String(json['Haris']);
                divdata.appendChild(voter1);
    
                divdata.appendChild(document.createElement('br'))
                divdata.appendChild(document.createElement('br'))
                

                if(json['Haris']==json['Abdullah'])
                {
                    voter1=document.createElement("h1");
                    voter1.className="text-slate-200 text-3xl font-bold";
                    voter1.innerHTML="Draw";
                    divdata.appendChild(voter1);
                }

                else if(json['Haris']>json['Abdullah'])
                {
                    voter1=document.createElement("h1");
                    voter1.className="text-slate-200 text-3xl font-bold";
                    voter1.innerHTML="Haris Won The Election";
                    divdata.appendChild(voter1);
                }
                else 
                {
                    
                    voter1=document.createElement("h1");
                    voter1.className="text-slate-200 text-3xl font-bold";
                    voter1.innerHTML="Abdullah Won The Election";
                    divdata.appendChild(voter1);
                }
            
        }
    })
    document.getElementById("fname").value="";
    document.getElementById("lname").value="";
    document.getElementById("CNIC").value="";
    
    var temp = document.getElementsByName("fav_language");
        for(var i=0;i<temp.length;i++)
            temp[i].checked = false;    

}
    catch
    {
        alert("Select all required fields");
    }


            // clearing data fields
    
}