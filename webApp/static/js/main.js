
window.onload = getAllComponents;

/* query api every second to refresh components list on main page*/
let interval = setInterval(getAllComponents, 2000);

/* get all components and put them on the main screen */
function getAllComponents() {
    const xhr = new XMLHttpRequest();
    xhr.open('GET', '/api', true);
    xhr.onload = function() {
        let output = "";
        if (this.status === 200) {
            const response = JSON.parse(this.responseText);
            response.forEach(element => {
                output += `<button class="u-full-width accordian">${element.name}</button>
                           <div class="accordian-content">
                                <p>
                                    lorem  jdsiapofjsa jpsa jfdspf sspa
                                    jf dsopaf jds jdspoa jfidspa jfdspo fdspa
                                    jfdisoa pfdjsiap  ijdsopa fjdis jfdsap
                                </p>
                           </div>`;
            });
        }
        document.getElementById("list-all-components").innerHTML = output;
        setUpAccordian();
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
                    // accordian is open, close it
                    content.style.maxHeight = null;
                    interval = setInterval(getAllComponents, 2000);
                } else {
                    // accordian is closed, open it
                    clearInterval(interval);
                    content.style.maxHeight = content.scrollHeight + "px";
            }
        }
    }
}
//////////////////////////////////////////////////////////////////////////////////////////