var textinput = document.getElementById('textinput')
var urlinput = document.getElementById('urlinput')
// var docinput = document.getElementById('docinput')

var left_heading = document.getElementById('inputheading')
var textbtn = document.getElementById('textbtn')
var urlbtn = document.getElementById('urlbtn')
// var docbtn = document.getElementById('docbtn')

var image = document.getElementById('wordcloud')

var analysis_btn = document.getElementById('analysisbtn')
var algo_btn = document.getElementById('algobtn')
var word_cloud_btn = document.getElementById('wordcloudbtn')

var topic_model = document.getElementById('topicmodel')
var graph = document.getElementById('generated-graph')
var heading = document.getElementById('heading')

var word_cloud_displayer = false
var url_displayer = false
var analysis_displayer = false
var text_displayer = true


textbtn.onclick = () => {
    if (!text_displayer) {
        left_heading.innerHTML = 'Text Input'
        textinput.style.display = 'block'
        urlinput.style.display = 'none'
        text_displayer = true
        url_displayer = false
    }
}
urlbtn.onclick = () => {
    if (!url_displayer) {
        left_heading.innerHTML = 'URL Input'
        urlinput.style.display = 'block'
        textinput.style.display = 'none'
        url_displayer = true
        text_displayer = false
    }
}
// docbtn.onclick = () => {
//     if (!displayer3) {
//         left_heading.innerHTML = 'Document Input'
//         docinput.style.display = 'block'
//         textinput.style.display = 'none'
//         urlinput.style.display = 'none'
//         displayer3 = true
//         displayer1 = false
//         displayer2 = false
//     }
// }


analysis_btn.onclick = () => {
    if (!analysis_displayer) {
        heading.innerHTML = 'Analysis'
        graph.style.display = 'block'
        analysis_displayer = true
    }
    else {
        heading.innerHTML = 'Topic Model'
        graph.style.display = 'none'
        analysis_displayer = false
    }
}

algo_btn.onclick = () => {
    heading.innerHTML = 'View Algorithm'
}
word_cloud_btn.onclick = () => {
    if (!word_cloud_displayer) {
        heading.innerHTML = 'Word Cloud'
        topic_model.style.display = 'block'
        word_cloud_displayer = true
    }
    else {
        heading.innerHTML = 'Topic Model'
        topic_model.style.display = 'none'
        word_cloud_displayer = false
    }

}