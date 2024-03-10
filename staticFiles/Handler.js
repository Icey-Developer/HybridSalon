//SECTION - Object Declaring
let _OXB8user = { 
  details: { n: "", e: "", Tel: "" }, 
  Coiffure: { T: "", l: "", s: "", e: "" },
  D$T: { Date: "", Time: "" } 
  };
let [data, regEx] = [[], /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/]

//SECTION - Inquire of Contingent Information

const Init = async (...args) => {
  $.each(args, function (type) {
    $.each(_OXB8user.details, function (key) {
      if (Object.keys(args[type]).toString() == "e") {
        if (regEx.test(Object.values(args[type]).toString())) {
          _OXB8user.details[Object.keys(args[type]).toString()] = Object.values(args[type]).toString();
        }

      }
      _OXB8user.details[Object.keys(args[type]).toString()] = Object.values(args[type]).toString();
    });
  });
};
const Coiffure = async (...args) => {
  $.each(args, function (type) {
    $.each(_OXB8user.Coiffure, function (key) {
      if (Object.keys(args[type]).toString() == "e") {
      }
      _OXB8user.Coiffure[Object.keys(args[type]).toString()] = Object.values(args[type]).toString();
    });
  });
};
const Yield = async (...args) => {
  $.each(args, function (type) {
    $.each(_OXB8user.Coiffure, function (key) {
      if (Object.keys(args[type]).toString() == "e") {
      }
      _OXB8user.Coiffure[Object.keys(args[type]).toString()] = Object.values(args[type]).toString();
    });
  });
};
//SECTION - API Requests
const Get_Time = async (url) => {
  try {
    const req = await fetch(url); // Fetch JSON data from the URL
    const jsonData = await req.json(); // Parse the JSON data
    const times = []; // Initialize an array to store extracted times
    for (const key in jsonData) {
      if (Object.hasOwnProperty.call(jsonData, key)) {
        // Extract time data from each JSON object and push it into the times array
        times.push(jsonData[key]);
      }
    }
    return times; // Return the array of times
  } catch (error) {
    console.error("Error occurred while fetching or parsing data:", error);
    return []; // Return an empty array in case of an error
  }
};

const Get_Unavailable = async url => {
  const req = await fetch(url).catch(function (err) {console.log(err)});
  const jsx = await req.json();

  return jsx;
}
const Get_key = async url => {
  const req = await fetch(url);
  const jsx = await req.json();
  let key = [];
  $.each(jsx, function (i) {
    key.push(Object.values(jsx[i])[0])[0];
  });
  return key;
};
const Get_Coiffure = async url => {
  const req = await fetch(url);
  const jsx = await req.json();
  const coiffure = [];
  $.each(jsx, function (i) {
    coiffure.push(jsx[i] /*Object.values(jsx[i])[0]*/);
    return;

  });

  return coiffure;
};
const Get_Econ = async url => {
  const req = await fetch(url);
  const jsx = await req.json();
  
  return jsx
}

// SECTION -Https Requests (METHOD=[POST, GET])
class Booking {
  constructor() {
    this.xhr = new XMLHttpRequest();
  }
  Post(data) {
    $.post("/Redirect:About",
    JSON.stringify(data),
    function(data, status) {
      $("fieldset:last").slideUp("slow", function() {

      })
      console.log(data, status);
    },
    )
  }
  Get() {
    this.xhr.open('GET', 'https://blb.onrender.com/Redirect:About');
    this.xhr.send();

    this.xhr.onreadystatechange = () => {
      if (this.xhr.readyState === 4) {
        if (this.xhr.status === 200) {
          console.log('GET response:', this.xhr.responseText);
          window.location.href = this.xhr.responseURL
        } else {
          console.error('GET request failed.');
        }
      }
    };
  }
  Run(data) {
    this.Post(data);
    setTimeout(() => {
      this.Get();
    }, 7000)
  }
}

// SECTION - Data Handling Classes
class create {
  constructor() {
  }

  Section(SubSection, Col_Type_A, Col_Type_B) {

  }

  Style() {
    const api = Get_Econ("https://blb.onrender.com/api/show").then(jsx => {
      $.each(jsx, function (item, index) {
        const [Sect, h2, Main] = [document.createElement("section"), document.createElement("h2"), document.querySelector(".Braids")]
        h2.innerHTML = item
        Sect.appendChild(h2)
        Sect.innerHTML += "<br><br>";
        
        Main.appendChild(Sect)
        
        //console.log(item)
        $.each(index, function(x) {
          const j = index[x]
          const [C1, C2, H4, Primary, Secondary] = [document.createElement("div"), document.createElement("div"), document.createElement("h4"), document.createElement("div"), document.createElement("div"),]
          const Prim_List = j[1]
          const Secon_List = j[2]
          H4.innerHTML = j[0]

          C1.appendChild(C2);C2.appendChild(H4)
          C2.appendChild(Primary); C2.appendChild(Secondary); Sect.appendChild(C1);

          $.each(Prim_List, function(i) {
            const A = document.createElement("h4")
            A.innerHTML = Prim_List[i]
            Primary.appendChild(A)
          })

          $.each(Secon_List, function(i) {
            const B = document.createElement("h4")
            B.innerHTML = Secon_List[i]
            Secondary.appendChild(B)
          })

          
          


        })

      return true});
    
    })
  }



}

document.addEventListener("loadeddata", new create().Style())

