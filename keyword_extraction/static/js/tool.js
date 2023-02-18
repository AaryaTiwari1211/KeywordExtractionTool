var textinput = document.getElementById('textinput')

var heading = document.getElementById('inputheading')
var textbtn = document.getElementById('textbtn')
var urlbtn = document.getElementById('urlbtn')
var webbtn = document.getElementById('webbtn')

textbtn.onclick = () => {
    textinput.innerHTML = '<textarea class="form-control" id="exampleFormControlTextarea1" placeholder="Enter text" name="text-input" rows="7"></textarea>'
    heading.innerHTML = 'INPUT TEXT HERE'
}
urlbtn.onclick = () => {
    textinput.innerHTML = '<input class="form-control" type="text" placeholder="Enter URL" name="url-input">'
    heading.innerHTML = 'INPUT URL HERE'
}
webbtn.onclick = () => {
    textinput.innerHTML = '<input type="file" class="form-control-file" id="exampleFormControlFile1" name="file-input" placeholder="Attach File">'
    heading.innerHTML = 'INPUT FILE HERE'
}

var analysis_btn = document.getElementById('analysis-btn')
var algo_btn = document.getElementById('algo-btn')
var word_cloud_btn = document.getElementById('word-cloud-btn')

var analysis_heading = document.getElementById('analysis-heading')
var analysis_content = document.getElementById('analysis-content')


analysis_btn.onclick = () => {
    analysis_heading.innerHTML = 'ANALYSIS'
}
