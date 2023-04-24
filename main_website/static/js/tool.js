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
var heading = document.getElementById('heading')

var displayer = false

var displayer1 = true
var displayer2 = false
// var displayer3 = false



textbtn.onclick = () => {
    if (!displayer1) {
        left_heading.innerHTML = 'Text Input'
        textinput.style.display = 'block'
        urlinput.style.display = 'none'
        // docinput.style.display = 'none'
        displayer1 = true
        displayer2 = false
        // displayer3 = false
    }
}
urlbtn.onclick = () => {
    if (!displayer2) {
        left_heading.innerHTML = 'URL Input'
        urlinput.style.display = 'block'
        textinput.style.display = 'none'
        // docinput.style.display = 'none'
        displayer2 = true
        displayer1 = false
        // displayer3 = false
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
    heading.innerHTML = 'Analysis'
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
    else {
        heading.innerHTML = 'Topic Model'
        topic_model.style.display = 'none'
        displayer = false
    }

}