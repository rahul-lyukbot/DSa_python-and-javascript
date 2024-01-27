// Q - 1 Find largest element in a array in one traversal
function larget_element(arr) {
  // setting current element
  let currentEle = 0;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] > currentEle) {
      currentEle = arr[i];
    }
  }

  return currentEle;
}

console.log(larget_element([1, 8, 40, 3, 12]));
