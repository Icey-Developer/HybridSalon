$(document).ready(() => {
  
  const pack = []
  const isLeapYear = (year) => {
    return (
      (year % 4 === 0 && year % 100 !== 0 && year % 400 !== 0) ||
      (year % 100 === 0 && year % 400 === 0)
    );
  };
  const getFebDays = (year) => {
    return isLeapYear(year) ? 29 : 28;
  };
  let calendar = document.querySelector(".calendar");
  const month_names = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
  ];
  let month_picker = document.querySelector("#month-picker");
  const dayTextFormate = document.querySelector(".day-text-formate");
  const timeFormate = document.querySelector(".time-formate");
  const dateFormate = document.querySelector(".date-formate");

  month_picker.onclick = () => {
    month_list.classList.remove("hideonce");
    month_list.classList.remove("hide");
    month_list.classList.add("show");
    dayTextFormate.classList.remove("showtime");
    dayTextFormate.classList.add("hidetime");
    timeFormate.classList.remove("showtime");
    timeFormate.classList.add("hideTime");
    dateFormate.classList.remove("showtime");
    dateFormate.classList.add("hideTime");
  };

  

  const generateCalendar = (month, year) => {
    let calendar_days = document.querySelector(".calendar-days");
    calendar_days.innerHTML = "";
    let calendar_header_year = document.querySelector("#year");
    let days_of_month = [
      31,
      getFebDays(year),
      31,
      30,
      31,
      30,
      31,
      31,
      30,
      31,
      30,
      31,
    ];

    function Pack() {
      // Get the calendar days container
      let calendar_days = document.querySelector(".calendar-days");
  
      // If the clicked day is disabled or booked, return
      if (this.classList.contains('disabled') || this.classList.contains('booked')) {
          return false;
      }
  
      // Remove the "selected" class from all calendar days
      for (let child = 0; child < calendar_days.children.length; child++) {
          let day = calendar_days.children[child];
          day.classList.remove("selected");
      }
  
      // Add the "selected" class to the clicked day
      this.classList.add("selected");
  
      // Update the selected date in your data structure or variable
      let selectedDate = this.innerHTML + " " + document.querySelector("#month-picker").innerHTML + " " + currentDate.getFullYear();
      _OXB8user.D$T.Date = selectedDate;
      pack[0] = selectedDate;
      console.log(pack[0]);
  
      // Fetch unavailable times for the selected date
      Get_Unavailable("https://blb.onrender.com/Unavailable/Date")
      .then(res => {
          // Process the unavailable times
          function Get_Sep(text) {
              return text.split(" ");
          }
          for (let i = 0; i <= days_of_month[month] + first_day.getDay() - 1; i++) {
              if (i >= first_day.getDay()) {
                  let day = document.createElement("div");
                  day.innerHTML = i - first_day.getDay() + 1;
                  if (i - first_day.getDay() + 1 <= currentDate.getDate() && year === currentDate.getFullYear() && month === currentDate.getMonth()) {
                      day.classList.add("disabled");
                  }
                  for (let j in res) {
                      let D = Get_Sep(res[j]);
                      let dayValue = parseInt(D[0]);
                      let yearValue = parseInt(D[2]);
                      let m = new Date(`${D[1]} 1, ${yearValue}`);
                      let monthValue = m.getMonth() + 1;
                      if (monthValue === (currentDate.getMonth() + 1) && yearValue === currentDate.getFullYear()) {
                          if (dayValue === parseInt(day.innerHTML)) {
                              day.classList.add("booked");
                              console.log("booked");
                          }
                      }
                  }
                  day.addEventListener("click", Pack);
                  
              }
          }
      })
      .catch(error => {
          console.error("Error fetching unavailable times:", error);
      });
  }
  

    let currentDate = new Date();

    month_picker.innerHTML = month_names[month];

    calendar_header_year.innerHTML = year;

    let first_day = new Date(year, month);

    const times = Get_Unavailable("https://blb.onrender.com/Unavailable/Date").then((res) => {
      function Get_Sep(text) {
        let s = text.split(" ")
        return s
      }

      for (let i = 0; i <= days_of_month[month] + first_day.getDay() - 1; i++) {
        let day = document.createElement("div");
  
        if (i >= first_day.getDay()) {
          day.innerHTML = i - first_day.getDay() + 1;
          if (
              i - first_day.getDay() + 1 <= currentDate.getDate()&&
              year === currentDate.getFullYear()
              && month === currentDate.getMonth() 
  
            ) {day.classList.add("disabled");}
          
            
            for (j in res) {
              let D = Get_Sep(res[j]);
              console.log(D);
          
              // Parse extracted date components into integers
              let dayValue = parseInt(D[0]);
              let yearValue = parseInt(D[2]);
              let m = new Date(`${D[1]} 1, ${yearValue}`); // Use a specific year to ensure consistency
              let monthValue = m.getMonth() + 1; // Months in JavaScript are zero-based, so we add 1 to get the correct month number
          
              // Check if the extracted date matches the current month and year
              if (monthValue === (currentDate.getMonth() + 1) && yearValue === currentDate.getFullYear()) {
                  // Check if the extracted date matches the current day
                  if (dayValue == day.innerHTML) {
                      day.classList.add("booked");
                      console.log("booked");
                  }
              }
          }
          

  
        }
  
        day.addEventListener("click", Pack)
        calendar_days.appendChild(day);
      }
    })
 
  };

  let month_list = calendar.querySelector(".month-list");
  month_names.forEach((e, index) => {
    let month = document.createElement("div");
    month.innerHTML = `<div>${e}</div>`;

    month_list.append(month);
    month.onclick = () => {
      currentMonth.value = index;
      generateCalendar(currentMonth.value, currentYear.value);
      month_list.classList.replace("show", "hide");
      dayTextFormate.classList.remove("hideTime");
      dayTextFormate.classList.add("showtime");
      timeFormate.classList.remove("hideTime");
      timeFormate.classList.add("showtime");
      dateFormate.classList.remove("hideTime");
      dateFormate.classList.add("showtime");
    };
  });

  (function () {
    month_list.classList.add("hideonce");
  })();
  document.querySelector("#pre-year").onclick = () => {
    --currentYear.value;
    generateCalendar(currentMonth.value, currentYear.value);
  };
  document.querySelector("#next-year").onclick = () => {
    ++currentYear.value;
    generateCalendar(currentMonth.value, currentYear.value);
  };

  let currentDate = new Date();
  let currentMonth = { value: currentDate.getMonth() };
  let currentYear = { value: currentDate.getFullYear() };
  generateCalendar(currentMonth.value, currentYear.value);

  
});
