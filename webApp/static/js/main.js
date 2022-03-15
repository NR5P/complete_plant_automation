
window.onload = getAllComponents;
let oldResponseCycle;
let oldResponseTimed;

/* query api every second to refresh components list on main page*/
let interval = setInterval(getAllComponents, 2000);

/* get all components and put them on the main screen */
function getAllComponents() {
    getAllTimedIrrigation(getAllCycleIrrigation);
}

function getAllCycleIrrigation() {
    const xhr = new XMLHttpRequest();
    xhr.open('GET', '/api/getallcycleirrigation', true);
    xhr.onload = function() {
        let output = "";
        if (this.status === 200) {
            const response = JSON.parse(this.responseText);
            if (this.responseText !== oldResponseCycle)
            {
                oldResponseCycle = this.responseText;
                response.forEach(element => {
                    output += `<button class="u-full-width accordian">${element.name}</button>
                            <div class="accordian-content" id="element-id-${element.id}">
                                ${returnComponentSettings("cycleirrigation", element)}
                            </div>`;
                });
                document.getElementById("list-all-components").innerHTML = output;
                setUpAccordian();
            }
        }
    }
    xhr.send();
}
   
function getAllTimedIrrigation(callback) {
    const xhr = new XMLHttpRequest();
    xhr.open('GET', '/api/getalltimedirrigation', true);
    xhr.onload = function() {
        let output = "";
        if (this.status === 200) {
            const response = JSON.parse(this.responseText);
            if (this.responseText !== oldResponseTimed)
            {
                oldResponseTimed = this.responseText;
                response.forEach(element => {
                    output += `<button class="u-full-width accordian">${element.name}</button>
                            <div class="accordian-content" id="element-id-${element.id}">
                                ${returnComponentSettings("timedirrigation", element)}
                            </div>`;
                });
                document.getElementById("list-all-components").innerHTML = output;
                setUpAccordian();
            }
            callback();
        }
    }
    xhr.send();
}
 
////////////////////////////////////////////////////////////////////////////////////////////

/* this is to hide and unhide accordians onclick in the main menu */
let accordians = document.getElementsByClassName("accordian");

function setUpAccordian() {
    for (let i = 0; i < accordians.length; i++)
        {
            accordians[i].onclick = function() {
                let content = this.nextElementSibling;

                if (content.style.maxHeight)
                {
                    content.style.maxHeight = null; // accordian is open, close it
                } else {
                    content.style.maxHeight = content.scrollHeight + "px"; // accordian is closed, open it
            }
        }
    }
}

//////////////////////////////////////////////////////////////////////////////////////////

/* 
converts the isoformat time stored in json to a readable time output later will make this 
dynamic for either 24 or 12 hour formats
*/
function convertFromIsoToTime(isoFormat){
    //const time = new Date(isoFormat);
    //return time.prototype.getHours() + " : " + time.prototype.getMinutes;
    return isoFormat;
}

//////////////////////////////////////////////////////////////////////////////////////////

/* takes component and returns the settings of the element depending on the componenet type */
function returnComponentSettings(type, element) {
    let output = "";
    switch (type) {
        case "cycleirrigation" :
            output += `
                    <div>
                       <div class="row">
                        <label class="u-pull-left one-third column">Name</label>
                        <h4 class="u-pull-right two-thirds column">${element.name}</h4>
                       </div>
                       <div class="row">
                        <label class="u-pull-left one-third column">description</label>
                        <h4 class="u-pull-right two-thirds column">${element.description}</h4>
                       </div>
                       <div class="row">
                        <label class="u-pull-left one-third column">Pin</label>
                        <h4 class="u-pull-right two-thirds column">${element.pin}</h4>
                       </div>
                       <div class="row">
                        <label class="u-pull-left one-third column">On or Off</label>
                        <h4 class="u-pull-right two-thirds column">
                            ${element.on ? "ON" : "OFF"}
                        </h4>
                       </div>
                       <div class="row">
                        <label class="u-pull-left one-third column">Current State</label>
                        <h4 class="u-pull-right two-thirds column">
                            ${element.currentstate ? "Currently Running" : "Currently Off"}
                        </h4>
                       </div>
                       <div class="row">
                        <label class="u-pull-left one-third column">Cycle On Time</label>
                        <h4 class="u-pull-right two-thirds column">${element.cycleOnMinutes}:${element.cycleOnSeconds}</h4> 
                       </div>
                       <div class="row">
                        <label class="u-pull-left one-third column">Cycle Off Time</label>
                        <h4 class="u-pull-right two-thirds column">${element.cycleOffMinutes}:${element.cycleOffSeconds}</h4> 
                       </div>`

                    element.blackouttimes.forEach(time => {
                        output += `
                            <div class="time-block">
                                <div class="row">
                                    <label class="u-pull-left one-third column">Blackout Start Time</label>
                                    <h4 class="u-pull-right two-thirds column">${convertFromIsoToTime(time.blackoutStart)}</h4> 
                                </div>
                                <div class="row">
                                    <label class="u-pull-left one-third column">Blackout Stop Time</label>
                                    <h4 class="u-pull-right two-thirds column">${convertFromIsoToTime(time.blackoutStop)}</h4> 
                                </div>
                            </div>
                        `
                    })                       

                    output+=`
                       <div class="row">
                        <button class="u-full-width edit-btn">Edit</button>
                       </div>
                       <div class="row">
                        <button id="delete-btn" class="u-full-width delete-btn">Delete</button>
                       </div>
                    </div>
                       `
            return output;
        
        case "timedirrigation" :  
            return output;

        default:
            return "there was a problem here";
    }
}

///////////////////////////////DROPDOWN BUTTON FOR ADDING COMPONENTS//////////////////////////////\
function dropDownAddList() {
    document.getElementById("myDropdown").classList.toggle("show");
}

window.onclick = function(event) {
    if (!event.target.matches('.dropbtn')) {
        var dropdowns = document.getElementsByClassName("dropdown-content");
        var i;
        for (i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
                if (openDropdown.classList.contains('show')) {
                    openDropdown.classList.remove('show');
                }
        }
    }
} 