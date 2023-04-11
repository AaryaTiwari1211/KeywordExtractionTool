var textinput = document.getElementById('textinput')

var left_heading = document.getElementById('inputheading')
var textbtn = document.getElementById('textbtn')
var urlbtn = document.getElementById('urlbtn')
var webbtn = document.getElementById('webbtn')

var image = document.getElementById('wordcloud')
var text = document.getElementById('text_data').value

var analysis_btn = document.getElementById('analysisbtn')
var algo_btn = document.getElementById('algobtn')
var word_cloud_btn = document.getElementById('wordcloudbtn')

var topic_model = document.getElementById('topic-model-content')
var heading = document.getElementById('heading')

const options = {
    "format": "png",
    "width": 1000,
    "height": 1000,
    "fontFamily": "sans-serif",
    "fontScale": 15,
    "scale": "linear",
    "text": text,
};

analysis_btn.onclick = () => {
    heading.innerHTML = 'Close Analysis'
}

algo_btn.onclick = () => {
    heading.innerHTML = 'View Algorithm'
}
word_cloud_btn.onclick = () => {
    heading.innerHTML = 'Word Cloud'
    topic_model.style.display = 'block'
}
