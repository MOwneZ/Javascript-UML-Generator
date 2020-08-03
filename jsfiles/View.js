class View {
  static BLANK () {
    return ''
  }
  static SPACE () {
    return '&nbsp;'
  }
  static SPACES(n){
    let result = ''
    for (let i = 0; i <n; i+= 1){
      result += View.SPACE()
    }
    return result
  }
  static TAB () {
    return '&nbsp;&nbsp;&nbsp;&nbsp;'
  }
  static NEWLINE () {
    return '<br>'
  }
  static clr () {
    document.body.style.fontFamily = 'Courier New'
    document.body.innerHTML = ''
  }
  static out (newText) {
    document.body.innerHTML += newText
  }
  static add (newText) {
    document.body.innerHTML += '<br>' + newText
  }
  static centre (original, targetSize=8) {
    let result = original
    let size = result.length
    while (size < targetSize){
      if (result.length % 2){
        result += View.SPACE()
      }
      else {
        result = View.SPACE() + result 
      }
      size += 1
    }
    return result
  }
  
  static padRight (original, targetSize=7) {
    let result = '' + original
    let size = result.length
    while (size < targetSize){
      result += View.SPACE()
      size += 1
    }
    return result
  }
}