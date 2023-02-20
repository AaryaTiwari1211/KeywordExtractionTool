var textinput = document.getElementById('textinput')

var left_heading = document.getElementById('inputheading')
var textbtn = document.getElementById('textbtn')
var urlbtn = document.getElementById('urlbtn')
var webbtn = document.getElementById('webbtn')

textbtn.onclick = () => {
    textinput.innerHTML = '<textarea class="form-control" id="exampleFormControlTextarea1" placeholder="Enter text" name="text-input" rows="7"></textarea>'
    left_heading.innerHTML = 'INPUT TEXT HERE'
}
urlbtn.onclick = () => {
    textinput.innerHTML = '<input class="form-control" type="text" placeholder="Enter URL" name="url-input">'
    left_heading.innerHTML = 'INPUT URL HERE'
}
webbtn.onclick = () => {
    textinput.innerHTML = '<input type="file" class="form-control-file" id="exampleFormControlFile1" name="file-input" placeholder="Attach File">'
    left_heading.innerHTML = 'INPUT FILE HERE'
}

var analysis_btn = document.getElementById('analysisbtn')
var algo_btn = document.getElementById('algobtn')
var word_cloud_btn = document.getElementById('wordcloudbtn')

var right_heading = document.getElementById('analysisheading')
var right_content = document.getElementById('analysiscontent')

right_heading.style.display = 'none'

var content2 = document.getElementById('algo')
content2.style.display = 'none'

var content1 = document.getElementById('analysis')
content1.style.display = 'none'
var content3 = document.getElementById('word-cloud-img')
content3.style.display = 'none'

var displayer1 = false;
var displayer2 = false;
var displayer3 = false;

var btn1head = document.getElementById('btnname1')
var btn2head = document.getElementById('btnname2')
var btn3head = document.getElementById('btnname3')


analysis_btn.onclick = () => {
    if(!displayer1)
    {
        btn1head.innerHTML = 'Close Analysis'
        console.log("Heading changed to ANALYSIS")
        console.log("Content changed to ANALYSIS")
        right_heading.innerHTML = 'ANALYSIS';
        content1.style.display = 'block'
        displayer1 = !displayer1
    }
    else
    {
        btn1head.innerHTML = 'Generate Complete Analysis'
        content1.style.display = 'none'
        displayer1 = !displayer1
    }
}
algo_btn.onclick = () => {
    if(!displayer2)
    {
        btn2head.innerHTML = 'Close Algorithm'
        console.log("Heading changed to ALGORITHM USED")
        console.log("Content changed to ALGORITHM")
        right_heading.innerHTML = 'ALGORITHM USED';
        content2.style.display = 'block'
        displayer2 = !displayer2
    }
    else
    {
        btn2head.innerHTML = 'View Algorithm'
        content2.style.display = 'none'
        displayer2 = !displayer2
    }
}
word_cloud_btn.onclick = () => {

    if(!displayer3)
    {
        btn3head.innerHTML = 'Close Topic Model'
        console.log("Heading changed to TOPIC MODEL")
        console.log("Content changed to TOPIC MODEL")
        right_heading.innerHTML = 'TOPIC MODEL';
        content3.style.display = 'block'
        displayer3 = !displayer3
    }
    else
    {
        btn3head.innerHTML = 'Generate Topic Model'
        content3.style.display = 'none'
        displayer3 = !displayer3
    }
}
