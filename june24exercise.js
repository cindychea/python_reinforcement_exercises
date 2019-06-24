// In some countries of the former Soviet Union there was a belief about lucky tickets. 
// A transport ticket of any sort was believed to possess luck if sum of digits on the left half of its number was equal to the sum of digits on the right half. 
// Here are examples of such numbers:
// 003111 # 3 = 1 + 1 + 1
// 813372 # 8 + 1 + 3 = 3 + 7 + 2
// 17935 # 1 + 7 = 3 + 5
// 56328116
// Your task is to write a method luckCheck(str), which returns true if argument is string decimal representation of a lucky ticket number, or false for all other numbers. 
// It should handle errors for empty strings or strings which don't represent a decimal number

function luckCheck(str) {
    if (str === '' || str < 0) {
        console.log('Error, please insert a valid string.')
    } else {
        var upper = Math.ceil(str.length / 2)
        var lower = Math.floor(str.length / 2)
        var leftHalf = str.slice(0, lower)
        var rightHalf = str.slice(upper)
        if (sumOfString(leftHalf) === sumOfString(rightHalf)) {
            console.log(true)
        } else {
            console.log(false)
        }

    }
}

function sumOfString(str) {
    let i = function(x) {return parseInt(x, 10)}
    return str.split('').map(i).reduce((a, b) => a + b)
}

luckCheck('003111')
luckCheck('813372')
luckCheck('913371')
luckCheck('17935')
luckCheck('56328116')
luckCheck('')
luckCheck('-003111')