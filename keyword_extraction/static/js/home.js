// Home page
var button = document.getElementById('viewmore')
var divelement = document.getElementById('showhide')
button.onclick = () => {
    if (divelement.style.display !== "none") 
    {
        divelement.style.display = "none";
        button.innerHTML = "View More"
        
    } 
    else 
    {
        divelement.style.display = "block";
        button.innerHTML = "View Less"
    }
    
}