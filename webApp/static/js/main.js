
window.onload = getAllComponents;
let oldResponse;

/* query api every second to refresh components list on main page*/
let interval = setInterval(getAllComponents, 2000);

/* get all components and put them on the main screen */
function getAllComponents() {
    const xhr = new XMLHttpRequest();
    xhr.open('GET', '/api', true);
    xhr.onload = function() {
        let output = "";
        if (this.status === 200) {
            //TODO break this up!!!!!!!!. have response as a top variable and make another function to check if the file is different than the old response, if it is then update, if not don't update.
            const response = JSON.parse(this.responseText);
            if (this.responseText !== oldResponse)
            {
                oldResponse = this.responseText;
                response.forEach(element => {
                    output += `<button class="u-full-width accordian">${element.name}</button>
                            <div class="accordian-content">
                                ${returnComponentSettings(element)}
                            </div>`;
                });
                document.getElementById("list-all-components").innerHTML = output;
                setUpAccordian();
            }
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
    return "";
}

//////////////////////////////////////////////////////////////////////////////////////////

/* takes component and returns the settings of the element depending on the componenet type */
function returnComponentSettings(element) {
    let output = "";
    switch (element.componentType) {
        case "cycleirrigation" :
            output += `
                       <div class="row">
                        <button class="u-pull-left one-third column">Change Name</button>
                        <h4 class="u-pull-right two-thirds column">${element.name}</h4>
                       </div>
                       <div class="row">
                        <button class="u-pull-left one-third column">Change Notes</button>
                        <p class="u-pull-right two-thirds column">${element.notes}</p>
                       </div>
                       <div class="row">
                        <button class="u-pull-left one-third column">Change Pin</button>
                        <h4 class="u-pull-right two-thirds column">${element.pin}</h4>
                       </div>
                       <div class="row">
                        <button class="u-pull-left one-third column">On or Off</button>
                        <h4 class="u-pull-right two-thirds column">
                            ${element.on ? "ON" : "OFF"}
                        </h4>
                       </div>
                       <div class="row">
                        <button class="u-pull-left one-third column">Change Pin</button>
                        <h4 class="u-pull-right two-thirds column">
                            ${element.currentstate ? "Currently Running" : "Currently Off"}
                        </h4>
                       </div>
                       <div class="row">
                        <button class="u-pull-left one-third column">Cycle On Time</button>
                        <h4 class="u-pull-right two-thirds column">${element.cycleOnMinutes}:${element.cycleOnSeconds}</h4> 
                       </div>
                       <div class="row">
                        <button class="u-pull-left one-third column">Cycle Off Time</button>
                        <h4 class="u-pull-right two-thirds column">${element.cycleOffMinutes}:${element.cycleOffSeconds}</h4> 
                       </div>
                       <div class="row">
                        <button class="u-pull-left one-third column">Blackout Start Time</button>
                        <h4 class="u-pull-right two-thirds column">${convertFromIsoToTime(element.blackoutStartTime)}</h4> 
                       </div>
                       <div class="row">
                        <button class="u-pull-left one-third column">Blackout Stop Time</button>
                        <h4 class="u-pull-right two-thirds column">${convertFromIsoToTime(element.blackoutStopTime)}</h4> 
                       </div>
                       <div class="row">
                        <button class="u-full-width">Test</button>
                       </div>
                       `
            return output;
        
        case "timedirrigation" :  

            return output;
        
        case "fan" : 

            return output;

        case "light" : 

            return output;

        case "heater" : 
        
            return output;

        case "humidifier" : 

            return output;
    
        default:
            return "there was a problem here";
    }
}

///////////////////////////////DROPDOWN BUTTON FOR ADDING COMPONENTS//////////////////////////////\
function dropDownAddList() {
    document.getElementById("addNewDropDown").classList.toggle("show");
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