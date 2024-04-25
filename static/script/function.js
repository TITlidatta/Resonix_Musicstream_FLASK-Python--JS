
function getp(a)
{
  var x = a.getAttribute("pid");
  fetch('/playp/'+x, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json', 
      'Authorization': 'Bearer your-access-token', 
    },
    redirect: 'follow'
  }).then(response => {
    if (response.ok) {
      return response.json(); 
    } else {
      console.error('Failed to log in');
    }
  })
  .then(data => {
      window.location.href = data.redirect_url; 
  })
  .catch(error => {
    console.error('Error during login:', error);
  });
}

function addp(tagg) {
          
  var divv = document.createElement("div");
  var sect = tagg.getAttribute("sec");
  divv.id="overlay";
  divv.style.display = "none";  
  document.body.appendChild(divv);
  var form = document.createElement("form");
  form.classList.add("row", "gy-2", "gx-3", "align-items-center");
  form.id ="formnow";

  
  var fields = [
    { id: "autoSizingInput1", placeholder: "Name" , name : "Name"},
  ];
  
  fields.forEach(function (field) {
    var row = document.createElement("div");
    row.classList.add("row");
    row.style.paddingBottom = "10px";

    var col = document.createElement("div");
    col.classList.add("col-auto");

    var label = document.createElement("label");
    label.classList.add("visually-hidden");
    label.htmlFor = field.id;
    label.textContent = field.placeholder;

    var input = document.createElement("input");
    input.type = "text";
    input.classList.add("form-control");
    input.id = field.id;
    input.placeholder = field.placeholder;
    input.name = field.name;

    col.appendChild(label);
    col.appendChild(input);
    row.appendChild(col);
    form.appendChild(row);
  });

  
  var submitRow = document.createElement("div");
  submitRow.classList.add("row");
  submitRow.style.paddingLeft = "140px";

  var submitCol = document.createElement("div");
  submitCol.classList.add("col-auto");

  var submitButton = document.createElement("button");
  submitButton.type = "submit";
  submitButton.classList.add("btn", "btn-primary", "btn-sm");
  submitButton.textContent = "Submit";
  submitButton.addEventListener("click", function () {
    subc(idx);
});

  submitCol.appendChild(submitButton);
  submitRow.appendChild(submitCol);
  form.appendChild(submitRow);
  divv.appendChild(form);
  var c =document.getElementById("overlay");
  c.style.display ="flex";

  
}

function subc(idx)
        {
          event.preventDefault();
          var ndata= new FormData(document.getElementById("formnow"));
          var namep= ndata.get('Name');
          console.log(namep)
          var adding='http://127.0.0.1:5000/addpl/'+idx+"/"+namep ;
          fetch( adding, {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
              'Authorization': 'Bearer your-access-token',
            },
            redirect: 'manual'
          }).then(response => {
          
            if (response.ok) {
                console.log('Request sent successfully');
                alert('Added it');
  
            } else {
                console.error('Failed to send request:', response.statusText);
            }
        })
        .catch(error => {
            console.error('Error sending request:', error);
        });

        var formc= document.getElementById("overlay");
        formc.remove();
        showp(namep);
        }
   
        function showp(pp)
        {
          console.log(pp)
          var x=document.getElementById("listpp");
          var listItem = document.createElement("li");
          listItem.setAttribute("class", "list-group-item");
          listItem.style.backgroundColor = "rgba(255, 255, 255, 0.54)";
          listItem.style.borderRadius = "8px";
          listItem.style.marginBottom = "5px";
          listItem.setAttribute("pid", 7);
          listItem.onclick = function() {
              getp(this);
          };
          listItem.innerHTML = "<b>" +pp+ "</b>";
          x.appendChild(listItem);
        }

        function createDivWithSelectOptions(elem) {
            
            var div = document.createElement("div");
            div.id="clear";
            div.classList.add("select-options-div");
            var ulx = document.createElement("ul");
            var ul = document.getElementById("listpp");
            var sog=elem.id;

            // Check if ul exists
            if (ul) {
              // Get all the li elements inside the ul
              var liElements = ul.querySelectorAll("li");
              var names = [];
              liElements.forEach(function(li) {
                names.push(li.textContent);
              });
            }
            
            for( var i=0; i< names.length ; i++)
            {
              var li1 = document.createElement("li");
              var pl=names[i];
              li1.textContent = names[i];
              (function(pl, sog) {
                li1.addEventListener("click", function() {
                    addtop(pl, sog);
                });
            })(pl, sog);
        
              ulx.appendChild(li1);
            }
            div.appendChild(ulx);
            document.body.appendChild(div);
            var referenceElement = elem;

            // Calculate position relative to the reference element
            var rect = referenceElement.getBoundingClientRect();
            div.style.top = (rect.top + window.scrollY + referenceElement.offsetHeight) + 'px';
            div.style.left = (rect.left + window.scrollX) + 'px';
        }
        
    function addtop(xp,xs)
    {
      console.log(xp,xs);
      var adding='http://127.0.0.1:5000/addtopl/'+xp+"/"+xs ;
          fetch( adding, {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
              'Authorization': 'Bearer your-access-token',
            },
            redirect: 'manual'
          }).then(response => {
          
            if (response.ok) {
                console.log('Request sent successfully');
                alert('Done');
  
            } else {
                console.error('Failed to send request:', response.statusText);
            }
        })
        .catch(error => {
            console.error('Error sending request:', error);
        });

      var xc=document.getElementById("clear");
      xc.remove();
    }



function func(v,idx)
{
var ssid=v.getAttribute("att");
fetch('/addCluster/'+idx+"/"+ssid, {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json', 
    'Authorization': 'Bearer your-access-token', 
  },
  redirect: 'manual'
}).then(response => {
  if (response.ok) {
  } else {
    console.log("could not track");
  }
})
.catch(error => {
  console.error('Error during login:', error);
});
}


function Remove(r,str)
{
    var z=r.getAttribute("setr");
    fetch('/remo/'+z+"/"+str, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json', 
          'Authorization': 'Bearer your-access-token', 
        },
        redirect: 'follow'
      }).then(response => {
        if (response.ok) {
            alert('Removed');
        } else {
          console.error('Failed to log in');
        }
      })
      .then(data => {
          window.location.href = data.redirect_url; 
      })
      .catch(error => {
        console.error('Error during login:', error);
      });
}

function func1()
{
  event.preventDefault();
  ndata= new FormData(document.getElementById("loginform"));
  fetch('/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json', 
          'Authorization': 'Bearer your-access-token', 
        },
        body: JSON.stringify(Object.fromEntries(ndata.entries())),
        redirect: 'follow'
      }).then(response => {
        if (response.ok) {
          return response.json(); 
        } else {
          console.error('Failed to log in');
        }
      })
      .then(data => {
          window.location.href = data.redirect_url; 
      })
      .catch(error => {
        console.error('Error during login:', error);
      });
}


function addAA(nm,id)
{
  var divv = document.createElement("div");
    divv.id="overlay";
    divv.style.display = "none";  
    document.body.appendChild(divv);
    var form = document.createElement("form");
    form.classList.add("row", "gy-2", "gx-3", "align-items-center");
    form.id ="formnow";

    var fields = [
    { id: "autoSizingInput1", placeholder: "Name", name: "Name" },
    { id: "autoSizingInput2", placeholder: "Lyrics", name: "lyrics" },
    { id: "autoSizingInput3", placeholder: "Genre", name: "Genre" },
    { id: "mp3FileInput", type: "file", name: "song", accept: ".mp3" }, // Input for MP3 file
    { id: "autoSizingInput4", placeholder: "Poster", name: "poster" }
];

    fields.forEach(function(field) {
      var row = document.createElement("div");
      row.classList.add("row");
      row.style.paddingBottom = "10px";
  
      var col = document.createElement("div");
      col.classList.add("col-auto");
  
      var label = document.createElement("label");
      label.classList.add("visually-hidden");
      label.htmlFor = field.id;
      label.textContent = field.placeholder;
  
      var input;
      if (field.type === "file") {
          input = document.createElement("input");
          input.type = "file";
          input.accept = field.accept; // Set the accept attribute for file type
          
      } else {
          input = document.createElement("input");
          input.type = "text";
          input.placeholder = field.placeholder;
      }
      input.classList.add("form-control");
      input.id = field.id;
      input.name = field.name;
  
      col.appendChild(label);
      col.appendChild(input);
      row.appendChild(col);
      form.appendChild(row);
  });
  

    
    var submitRow = document.createElement("div");
    submitRow.classList.add("row");
    submitRow.style.paddingLeft = "140px";

    var submitCol = document.createElement("div");
    submitCol.classList.add("col-auto");

    var submitButton = document.createElement("button");
    submitButton.type = "submit";
    submitButton.classList.add("btn", "btn-primary", "btn-sm");
    submitButton.textContent = "Submit";
    submitButton.addEventListener("click", function () {
      subc(nm,id);
  });

    submitCol.appendChild(submitButton);
    submitRow.appendChild(submitCol);
    form.appendChild(submitRow);
    divv.appendChild(form);
    var c =document.getElementById("overlay");
    c.style.display ="flex";
}


function subc(nm,id) 
{
  event.preventDefault();
  
  var formData = new FormData();
  var name = document.getElementById("autoSizingInput1").value;
  var lyrics = document.getElementById("autoSizingInput2").value;
  var genre = document.getElementById("autoSizingInput3").value;
  var poster = document.getElementById("autoSizingInput4").value;
  
  var mp3FileInput = document.getElementById("mp3FileInput");
  var mp3File = mp3FileInput.files[0]; 
  
  var reader = new FileReader();
  reader.onload = function(event) {
      var blob = new Blob([event.target.result], { type: mp3File.type });
      formData.append('song', blob, mp3File.name);
      
      formData.append('Name', name);
      formData.append('Lyrics', lyrics);
      formData.append('Genre', genre);
      formData.append('Poster', poster);
      
      console.log(formData.get('song'));
      var adding = 'http://127.0.0.1:5000/addAA/' + nm + "/" + id;
      fetch(adding, {
          method: 'POST',
          body: formData
      }).then(response => {
          if (response.ok) {
              console.log('Request sent successfully');
              alert('Added it , PLEASE RELOAD ');
          } else {
              console.error('Failed to send request:', response.statusText);
          }
      }).catch(error => {
          console.error('Error sending request:', error);
      });
  };
  reader.readAsArrayBuffer(mp3File);
  var x= document.getElementById("overlay");
  x.remove();
}

function edit(p)
{
  var aaid=p.getAttribute("aid");
  console.log(typeof(aaid));
  aaid=parseInt(aaid);
  console.log(typeof(aaid));
  fetch('/Albuma/'+aaid, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json', 
      'Authorization': 'Bearer your-access-token', 
    },
    redirect: 'follow'
  }).then(response => {
    if (response.ok) {
      return response.json(); 
    } else {
      console.error('Failed to log in');
    }
  })
  .then(data => {
      window.location.href = data.redirect_url; 
  })
  .catch(error => {
    console.error('Error during login:', error);
  });
}
function adds(sss,nam)
{
var divv = document.createElement("div");
    divv.id="overlay";
    divv.style.display = "none";  
    document.body.appendChild(divv);
    var form = document.createElement("form");
    form.classList.add("row", "gy-2", "gx-3", "align-items-center");
    form.id ="formnow";

    var fields = [
    { id: "autoSizingInput1", placeholder: "Name", name: "Name" },
    { id: "autoSizingInput2", placeholder: "Lyrics", name: "lyrics" },
    { id: "autoSizingInput3", placeholder: "Genre", name: "Genre" },
    { id: "mp3FileInput", type: "file", name: "song", accept: ".mp3" }, // Input for MP3 file
    { id: "autoSizingInput4", placeholder: "Poster", name: "poster" }
];

    fields.forEach(function(field) {
      var row = document.createElement("div");
      row.classList.add("row");
      row.style.paddingBottom = "10px";
  
      var col = document.createElement("div");
      col.classList.add("col-auto");
  
      var label = document.createElement("label");
      label.classList.add("visually-hidden");
      label.htmlFor = field.id;
      label.textContent = field.placeholder;
  
      var input;
      if (field.type === "file") {
          input = document.createElement("input");
          input.type = "file";
          input.accept = field.accept; // Set the accept attribute for file type
          
      } else {
          input = document.createElement("input");
          input.type = "text";
          input.placeholder = field.placeholder;
      }
      input.classList.add("form-control");
      input.id = field.id;
      input.name = field.name;
  
      col.appendChild(label);
      col.appendChild(input);
      row.appendChild(col);
      form.appendChild(row);
  });
  

    
    var submitRow = document.createElement("div");
    submitRow.classList.add("row");
    submitRow.style.paddingLeft = "140px";

    var submitCol = document.createElement("div");
    submitCol.classList.add("col-auto");

    var submitButton = document.createElement("button");
    submitButton.type = "submit";
    submitButton.classList.add("btn", "btn-primary", "btn-sm");
    submitButton.textContent = "Submit";
    submitButton.addEventListener("click", function () {
      subc(nam);
  });

    submitCol.appendChild(submitButton);
    submitRow.appendChild(submitCol);
    form.appendChild(submitRow);
    divv.appendChild(form);
    var c =document.getElementById("overlay");
    c.style.display ="flex";
}
    function subc(nam) {
      event.preventDefault();
      
      var formData = new FormData();
      var name = document.getElementById("autoSizingInput1").value;
      var lyrics = document.getElementById("autoSizingInput2").value;
      var genre = document.getElementById("autoSizingInput3").value;
      var poster = document.getElementById("autoSizingInput4").value;
      
      var mp3FileInput = document.getElementById("mp3FileInput");
      var mp3File = mp3FileInput.files[0]; 
      
      var reader = new FileReader();
      reader.onload = function(event) {
          var blob = new Blob([event.target.result], { type: mp3File.type });
          formData.append('song', blob, mp3File.name);
          
          formData.append('Name', name);
          formData.append('Lyrics', lyrics);
          formData.append('Genre', genre);
          formData.append('Poster', poster);
          
          console.log(formData.get('song'));
          var adding = 'http://127.0.0.1:5000/addsl/' + nam;
          fetch(adding, {
              method: 'POST',
              body: formData
          }).then(response => {
              if (response.ok) {
                  console.log('Request sent successfully');
                  alert('Added it');
              } else {
                  console.error('Failed to send request:', response.statusText);
              }
          }).catch(error => {
              console.error('Error sending request:', error);
          });
      };
      reader.readAsArrayBuffer(mp3File);
      var x= document.getElementById("overlay");
      x.remove();
  }
    
  function addA(sss,nam)
{
var divv = document.createElement("div");
    divv.id="overlay";
    divv.style.display = "none";  
    document.body.appendChild(divv);
    var form = document.createElement("form");
    form.classList.add("row", "gy-2", "gx-3", "align-items-center");
    form.id ="formnow";
    form.style.height="185px";
    var fields = [
    { id: "autoSizingInput1", placeholder: "Name", name: "Name" },
    { id: "autoSizingInput3", placeholder: "Genre", name: "Genre" },
];

    fields.forEach(function(field) {
      var row = document.createElement("div");
      row.classList.add("row");
      row.style.paddingBottom = "10px";
  
      var col = document.createElement("div");
      col.classList.add("col-auto");
  
      var label = document.createElement("label");
      label.classList.add("visually-hidden");
      label.htmlFor = field.id;
      label.textContent = field.placeholder;
  
      var input;
      input = document.createElement("input");
      input.type = "text";
      input.placeholder = field.placeholder;
      input.classList.add("form-control");
      input.id = field.id;
      input.name = field.name;
      col.appendChild(label);
      col.appendChild(input);
      row.appendChild(col);
      form.appendChild(row);
  });
  

    
    var submitRow = document.createElement("div");
    submitRow.classList.add("row");
    submitRow.style.paddingLeft = "140px";

    var submitCol = document.createElement("div");
    submitCol.classList.add("col-auto");

    var submitButton = document.createElement("button");
    submitButton.type = "submit";
    submitButton.classList.add("btn", "btn-primary", "btn-sm");
    submitButton.textContent = "Submit";
    submitButton.addEventListener("click", function () {
      subcx(nam);
  });

    submitCol.appendChild(submitButton);
    submitRow.appendChild(submitCol);
    form.appendChild(submitRow);
    divv.appendChild(form);
    var c =document.getElementById("overlay");
    c.style.display ="flex";
}
function subcx(nam) {
  event.preventDefault();
  
  var formData = new FormData();
  var name = document.getElementById("autoSizingInput1").value;
  var genre = document.getElementById("autoSizingInput3").value;
  formData.append('Name', name);
  formData.append('Genre', genre);

  var adding = 'http://127.0.0.1:5000/addsA/' + nam;
      fetch(adding, {
          method: 'POST',
          body: formData
      }).then(response => {
          if (response.ok) {
              console.log('Request sent successfully');
              alert('Added it, PLEASE RELOAD');
          } else {
              console.error('Failed to send request:', response.statusText);
          }
      }).catch(error => {
          console.error('Error sending request:', error);
      });

  var x= document.getElementById("overlay");
  x.remove();
}