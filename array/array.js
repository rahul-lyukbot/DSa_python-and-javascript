const arr = [1, 8, 40, 3, 12];
const arr2 = [1, 2, 3, 4, 8];

// Q - 1 Find largest element in a array in one traversal
function largetElement(arr) {
  // setting current element
  let currentEle = 0;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] > currentEle) {
      currentEle = arr[i];
    }
  }

  return currentEle;
}

// console.log(larget_element([1, 8, 40, 3, 12]));

// Q - 2 Check if the given array is sorted in increasing order or not
function isSorted(arr) {
  let currentEle = arr[0];
  for (let i = 1; i < arr.length; i++) {
    if (currentEle < arr[i]) {
      currentEle = arr[i];
    } else {
      return false;
    }
  }
  return true;
}

// console.log(isSorted(arr2));

// Q - 3 Rverse a given array
function reverseArray(arr) {
  let new_arr = [];
  for (let i = arr.length - 1; i >= 0; i--) {
    new_arr.push(arr[i]);
  }
  return new_arr;
}

// console.log(reverseArray(arr));

// Q - 4 Move all zero to the end of the array and non zero to the begining to the array without changin their order
function moveZeroToEnd(arr) {
  let count = 0;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] !== 0) {
      [arr[i], arr[count]] = [arr[count], arr[i]];
      count++;
    }
  }
  return arr;
}

// console.log(moveZeroToEnd([1, 2, 0, 7, 0, 9]));

// Q - 5 Rotate a given array to the left by 1

function rotateArray(arr) {
  if (arr.length <= 1) {
    return arr;
  }
  let first_element = arr[0];
  for (let i = 1; i < arr.length; i++) {
    arr[i - 1] = arr[i];
  }
  arr[arr.length - 1] = first_element;
  return arr;
}

console.log(rotateArray([1, 2, 3, 4]));
