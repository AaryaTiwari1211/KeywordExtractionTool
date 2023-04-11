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

var topic_model = document.getElementById('topicmodel')
var heading = document.getElementById('heading')

var displayer = false


analysis_btn.onclick = () => {
    heading.innerHTML = 'Close Analysis'
}

algo_btn.onclick = () => {
    heading.innerHTML = 'View Algorithm'
}
word_cloud_btn.onclick = () => {
    if (!displayer) {
        heading.innerHTML = 'Word Cloud'
        topic_model.style.display = 'block'
        displayer = true
    }
    else{
        heading.innerHTML = 'Topic Model'
        topic_model.style.display = 'none'
        displayer = false
    }

}