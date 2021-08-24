// remove duplicates from an array
array = [1, 2, 2, 3, 4, 5, 4]
newArray = []

len = array.length

for (i = 0; i < len; i++){
  if (newArray.indexOf(array[i]) === -1){
  newArray.push(array[i])
  }
}
console.log(newArray)
