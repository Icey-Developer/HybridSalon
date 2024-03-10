CoiffureArray = []
//SECTION - Details Events
$(document).ready(() => {

})

//SECTION - Hairstyle Events
$(document).ready(() => {
    //REVIEW - Style Type
    $("#Style").ready(function () {
        const data = Get_key("https://icey-developer.github.io/SyncApi/Set.json").then(jsx => {
          $.each(jsx, function (i) {
            const opt = document.createElement("option")
            opt.value = jsx[i]
            document.getElementById("lstyle").appendChild(opt)
            
          })
        })
      });
    $("#Style").change(function () {
        document.getElementById("Extra-Display").innerHTML = ""
        CoiffureArray[0] = this.value
        const data = Get_Coiffure("https://icey-developer.github.io/SyncApi/Set.json").then(jsx => {
          Div = document.getElementById('selectors')
          const selector = document.createElement("input")
          
          setTimeout(() => {
            
            selector.setAttribute("list" , "length")
            selector.id = "Length"
            selector.autocomplete = "off"
            selector.className = "Form-Selection"
            selector.placeholder = "Select Length"
            
               
          Div.appendChild(selector)
          $("#Length").fadeOut(1); $("#Length").slideDown(200); 
          InstanceEvent()
          
          }, 500);
  
          selector.setAttribute("list" , $('#length').id)
          $.each(jsx, function (x) {
            Opt = document.getElementById("Style")
            if (Opt.value == Object.values(jsx[x])[0]) {
              console.log()
              console.log('match')
              const Obj = Object.values(Object.keys(jsx[x]))
              $.each(Obj, function(size) {
                const Option = document.createElement("option")
                Option.value = Obj[size]
                document.getElementById("length").appendChild(Option) 
                if (document.getElementById("Option-Display").children.length > 0) {
                  document.getElementById("Option-Display").innerHTML = " "
                }
  
              })
            }
          })
          $.each(Div.children, function(i) {
            if (i > 1) {
              Div.children[1].remove()
              InstanceEvent()
            }
          })
          
  
        })
     
      })
    //REVIEW - Style Length
    function InstanceEvent() {
        $("#Length").off("change");
        
        $("#Length").on("change", async () => {
          console.log("ready")
          document.getElementById("Extra-Display").innerHTML = " "
          CoiffureArray[1] = document.getElementById("Length").value
          const data = await Get_Coiffure("https://icey-developer.github.io/SyncApi/Set.json");
      
          const length = document.getElementById("Length");
  
          if (document.getElementById("Option-Display").children.length > 0) {
            document.getElementById("Option-Display").innerHTML = " ";
          }
      
          $.each(data, function (index, item) {
            const optValue = Object.values(item)[0];
      
            if (Opt.value == optValue) {
              console.log('match');
      
              const objValues = Object.values(item);
              $.each(objValues, function (sizeIndex) {
                const price = objValues[sizeIndex];
      
                if (length.value == price[0]) {
                  const tsx = price[1];
                  const extra = price[2];
                  console.log("Match2");
      
                  // Set Size
                  $.each(tsx, function (i, sizeValue) {
                    console.log(sizeValue);
      
                    const content = document.createElement("div");
                    const Radio = document.createElement("div");
                    const context = document.createElement("p");
                    const val = document.createElement("h5");
                    
                    //Radio Properties
                    content.className = "Option";
                    content.id = "Content";
                    context.innerHTML = price[0];
                    val.innerHTML = sizeValue;
      
                    content.appendChild(context);content.appendChild(val);content.appendChild(Radio)
                    
                    document.getElementById("Option-Display").appendChild(content);
  
                    content.addEventListener("click", OptInstance, true)
                    
                  });
      
                  // Set Extra
                  return false; // This will exit the loop after processing the current item
                }
      
                return true; // Continue the loop
              });
            }
          
          return true;});
        
        
        
        
        
        
        
        
        
        
        
        });
      } 
    function OptInstance() {

      
        //Elements
        const [indexStr, length, Element] = [this.children[1], document.getElementById("Length"), this.children[0]]
        CoiffureArray[2] = indexStr.innerHTML
        if (document.getElementById("Extra-Display").children.length > 0) {
          document.getElementById("Extra-Display").innerHTML = " "
        }
        //API Extract
        const data = Get_Coiffure("https://icey-developer.github.io/SyncApi/Set.json").then(jsx => {
          console.log(CoiffureArray)
          $.each(jsx, function (index, item) {
            const optValue = Object.values(item)[0];
      
            if (Opt.value == optValue) {
              
      
              const objValues = Object.values(item);
              $.each(objValues, function (sizeIndex) {
                const price = objValues[sizeIndex];
      
                if (length.value == price[0]) {
                  const tsx = price[1]; const extra = price[2]; const ArrIndex = price[1].indexOf(indexStr.innerHTML) + 1
                  
                  //Get Array Value with Array i
                  const EIndex = extra[ArrIndex - 1]
                  console.log(EIndex)
  
                  //Inquire Into The Element Value
                  if (Element.innerHTML.includes("knotless") || Element.innerHTML.includes("Curl")) {
                    console.log(Element.innerHTML.includes("knotless"))
  
                    // Success then Inquire Into The Array Value
                    for (let i = 0; i < extra.length; i++) {
                      //? Iterating through function
                      CreateElement(extra[i])
                    }
                  } 
  
                  document.getElementById("Step2").style.display = "block"
                  CreateElement(EIndex)
                  // Clearing Element 
  
  
                  // This will exit the loop after processing the current item
                  return false; 
                }
      
                return true; // Continue the loop
              });
            }
          
          return true;});
          
  
  
  
        })
      }
    function SetXtra() {
        const Xtra = this.children[0]
        CoiffureArray[3] = Xtra.innerHTML
        console.log(CoiffureArray)
      }
    const CreateElement = (Index) => {
        const [content, Heading, E$Display, Radio] = [document.createElement("div"), document.createElement("h5"), document.getElementById("Extra-Display"), document.createElement("div")]
  
        content.className = "Xtra"; content.id = "Extra"
        Heading.innerHTML = Index;
        content.appendChild(Heading);content.appendChild(Radio); E$Display.appendChild(content)
        content.addEventListener("click", SetXtra, true)
      }})

//SECTION - Date
$(document).ready(() => {
  // - Time
  TimeRange = document.querySelector(".C5")

  // - Request Data
  time = Get_Time("http://10.0.0.148:5000/Get/Available-time").then((res) => {

    TimeRange.children[1].children[0].innerHTML = res[0]

    TimeRange.children[0].addEventListener('click', function onClick() {
      console.log(TimeRange.children[0].children[0].innerHTML);
      _OXB8user.D$T.Time = TimeRange.children[0].children[0].innerHTML
  
    })
  
    TimeRange.children[1].children[0].innerHTML = res[1]

    TimeRange.children[1].addEventListener('click', function onClick() {
      console.log(TimeRange.children[1].children[0].innerHTML);
      _OXB8user.D$T.Time = TimeRange.children[1].children[0].innerHTML
    })




  })

  

})
