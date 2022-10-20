console.log("Running JS file");

// Review of stuff from Web Fundamentals
function changeColor(element) {
    element.style.backgroundColor = "red";
}

function changeBack(element) {
    element.style.backgroundColor = "white";
}

function searchIMDB(e) {
    e.preventDefault(); // Stop the page from refreshing itself and stopping the default behavior of sending a form
    var searchForm = document.getElementById("searchForm");
    var searchFormInstance = new FormData(searchForm);
    // console.log(searchFormInstance.get("title"));
    fetch("http://localhost:5000/search", { method: 'POST', body: searchFormInstance})
        .then( response => response.json() ) // Grabbing an HTML response and then grabbing JSON data
        .then( data => {
            // Showing first result ONLY
            var searchResultsDiv = document.getElementById("search_results");
            searchResultsDiv.innerText = ""; // Cleared the DIV out first
            // Title
            var titleTag = document.createElement("p");
            titleTag.innerText = "Title: " + data.results[0]["title"];
            // ID
            var idTag = document.createElement("p");
            idTag.innerText = "ID: " + data.results[0]["id"];
            // Image
            var imgTag = document.createElement("img");
            imgTag.src = data.results[0]["image"];
            // Add to HTML
            searchResultsDiv.appendChild(titleTag);
            searchResultsDiv.appendChild(idTag);
            searchResultsDiv.appendChild(imgTag);
            
            console.log(data); // Show data (for debugging)
        })
}