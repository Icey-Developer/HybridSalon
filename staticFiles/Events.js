let QueryArr = ["first", "eq(1)", "last"];


$(document).ready(function () {
    //Get Query Attributes//Index Tab Index.No
    console.log("Query Document loaded")
    node = document.querySelectorAll("fieldset");
    Tab = document.querySelectorAll("li");

    let QueryArr = ["first", "eq(1)", "last"];

    //Setting all forms to fieldset to invisible
    $("fieldset").hide()
    $("fieldset:first").show()
    //Setting Step1 Button to invisible
    document.getElementById("Step2").style.display = "none"

    //Listening for a Button event using Class
    var basicTimeline = anime.timeline({
      autoplay: false
    });
    
    var pathEls = $(".check");
    for (var i = 0; i < pathEls.length; i++) {
      var pathEl = pathEls[i];
      var offset = anime.setDashoffset(pathEl);
      pathEl.setAttribute("stroke-dashoffset", offset);
    }
    
    basicTimeline
    .add({
      targets: ".Proceed",
      duration: 20,
      easing: "linear",
      backgroundColor : "#ffffff"
    })
      .add({
        targets: ".calender",
        filter : "opacity(20%)"
      })
    .add({
        targets: ".Proceed",
        duration: 20,
        easing: "linear",
        width: "50%",
        backgroundColor : "#a3ffb7",
        rotate: "-2deg",
        content: "Sent",
        display : "none"

    })
    .add({
    targets: ".text",
    duration: 20,
    easing: "linear",
    color : "#000000"
  })

    
    $(".Proceed").click(function() {
      basicTimeline.play();
      const xhr = new Booking("https://blb.onrender.com/Redirect:About")
      // Example usage
      
      const postData = _OXB8user;
      xhr.Run(postData);
    });
    
    $(".text").click(function() {
      basicTimeline.play();
    });

    $(".Next").click(function () {
      //End Of Section
      

      //Looping through All Query Tabs(<li>)
      $.each (Tab, function (t) {

        //Looping through Array of position
        $.each (QueryArr, function(x) {
          //Checking in x is less the the amount of queries in Tab(<li>)
          if (x < t+1) {
            //Code

            //Validating Input
            switch (t) {
                case 0:
                    Init({n : $("fieldset:"+QueryArr[t]).children("div").children("input:text")[1].value}, {e : $("fieldset:"+QueryArr[t]).children("div").children("input:text")[0].value}, {Tel : $("fieldset:"+QueryArr[t]).children("div").children("input:text")[2].value})
                    console.log(_OXB8user)
                    console.log(0)
                    break;
                case 1:
                    Coiffure({T : CoiffureArray[0]}, {l : CoiffureArray[1]}, {s : CoiffureArray[2]}, {e : CoiffureArray[3]})
                    console.log(_OXB8user)
                    console.log(1)
                    break;
            }
            console.log(t)
            console.log($("fieldset:"+QueryArr[t]).children("input:text")[0])
            
            //Animating fieldset using $("fieldset:"+Array(Datatype)[number])
            $("fieldset:"+QueryArr[t]).slideUp("slow", function() {
              $("fieldset:"+QueryArr[t+1]).slideDown("slow")
            })
          }
        })
  
        //Checking Tab class is active
        if (Tab[t].className == "active") {
          //Code
          //Activating the Tab using document.getElementById(id+(number)).classList.add(class)
          //Replacing in certain Tabs
          Tab[t].classList.remove("active");
          document.getElementById("idx"+(t)).classList.add("complete");
          document.getElementById("idx"+(t+1)).classList.add("active");
          ele = document.getElementById("Set"+(t+1))
  


          if (node[t].id == "idx1") {
            console.log("last")
            document.getElementById("idx"+(t)).classList.add("complete");
          }
          return false;
        }
      });
    });
    
    $("Submit").click(() => {

    })
    //Selector events

    
    //Instance Listener Events
    
   
  });

