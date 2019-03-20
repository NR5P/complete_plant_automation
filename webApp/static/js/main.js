
window.onload = getAllComponents;

/* query api every second to refresh components list on main page*/
setInterval(() => {
    getAllComponents()
}, 2000);

/* get all components and put them on the main screen */
function getAllComponents() {
    const xhr = new XMLHttpRequest();
    xhr.open('GET', '/api', true);
    xhr.onload = function() {
        let output = "";
        if (this.status === 200) {
            const response = JSON.parse(this.responseText);
            response.forEach(element => {
                output += `<button class="u-full-width">${element.name}</button>`;
            });
        }
        document.getElementById("list-all-components").innerHTML = output;
    }
    xhr.send();
}
