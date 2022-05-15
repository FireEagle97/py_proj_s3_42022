//initialize all event listener
window.addEventListener('DOMContentLoaded',init);

function init(){
    handleReview()
    handleStarSelect()
    handleSelect()
}

function handleReview() {

    let one = document.getElementById('first')
    let two = document.getElementById('second')
    let three = document.getElementById('third')
    let four = document.getElementById('fourth')
    let five = document.getElementById('fifth')
    let form = document.querySelector('.rate-form')
    let confirmBox = document.getElementById('confirm-box')
    let csrf = document.getElementsByName('csrfmiddlewaretoken')

    let rate_arr = [one,two,three,four,five]
    rate_arr.forEach(item=> item.addEventListener('mouseover', (event)=>{
        handleSelect(event.target.id)
}))
    rate_arr.forEach(item=> item.addEventListener('click', (event)=>{
        let val = event.target.id
        form.addEventListener('submit', e=>{
            e.preventDefault()
            let id = e.target.id
            console.log('id:' +id)
            let num_val = getNumericValue(val)
            console.log('stars' +num_val)
        })
    }
))


}

let handleStarSelect = (size) => {
    let form = document.querySelector('.rate-form')
    let children = form.children
    for (let i=0; i< children.length;i++) {
        if(i <= size){
            children[i].classList.add('checked')
        } else {
            children[i].classList.remove('checked')
        }
    }
}

let handleSelect = (selection) => {
    switch (selection){
        case 'first': {
            handleStarSelect(1)
            return
        }
        case 'second': {
            handleStarSelect(2)
            return
        }
        case 'third': {
            handleStarSelect(3)
            return
        }
        case 'forth':{
            handleStarSelect(4)
            return
        }
        case 'fifth':{
            handleStarSelect(5)
            return
        }
    }
}

let getNumericValue = (stringValue) =>{
    let numericValue;
    if (stringValue === 'first'){
        numericValue = 1
    }
    else if (stringValue === 'second'){
        numericValue = 2
    }
    else if (stringValue === 'third'){
        numericValue = 3
    }
    else if (stringValue === 'fourth'){
        numericValue = 4
    }
    else {
        numericValue = 5
    }
    return numericValue

}
