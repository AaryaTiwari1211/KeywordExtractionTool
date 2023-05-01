var textinput = document.getElementById('textinput')
var urlinput = document.getElementById('urlinput')
var fileinput = document.getElementById('fileinput')

var left_heading = document.getElementById('inputheading')

var textbtn = document.getElementById('textbtn')
var urlbtn = document.getElementById('urlbtn')
var filebtn = document.getElementById('filebtn')

var image = document.getElementById('wordcloud')

var analysis_btn = document.getElementById('analysisbtn')
var algo_btn = document.getElementById('algobtn')
var word_cloud_btn = document.getElementById('wordcloudbtn')

var topic_model = document.getElementById('topicmodel')
var graph = document.getElementById('generated-graph')
var algorithm = document.getElementById('algorithm')
var heading = document.getElementById('heading')

var word_cloud_displayer = false
var analysis_displayer = false
var algorithm_displayer = false

var text_displayer = true
var file_displayer = false
var url_displayer = false

textbtn.onclick = () => {
    if (!text_displayer) {
        left_heading.innerHTML = 'Text Input'
        textinput.style.display = 'block'
        urlinput.style.display = 'none'
        fileinput.style.display = 'none'
        text_displayer = true
        url_displayer = false
        file_displayer = false
    }
}
urlbtn.onclick = () => {
    if (!url_displayer) {
        left_heading.innerHTML = 'URL Input'
        urlinput.style.display = 'block'
        textinput.style.display = 'none'
        fileinput.style.display = 'none'
        url_displayer = true
        text_displayer = false
        file_displayer = false
    }
}
filebtn.onclick = () => {
    if (!file_displayer) {
        left_heading.innerHTML = 'TXT File Input'
        fileinput.style.display = 'block'
        textinput.style.display = 'none'
        urlinput.style.display = 'none'
        url_displayer = false
        text_displayer = false
        file_displayer = true
    }
}


analysis_btn.onclick = () => {
    window.location.href = "http://127.0.0.1:8000/graphs/"
}
algo_btn.onclick = () => {
    window.location.href = "http://127.0.0.1:8000/algorithm/"
}

word_cloud_btn.onclick = () => {
    if (!word_cloud_displayer) {
        topic_model.style.display = 'block'
        word_cloud_displayer = true
    }
    else {
        topic_model.style.display = 'none'
        word_cloud_displayer = false
    }

}