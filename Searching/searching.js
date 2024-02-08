let arr = [10, 20, 30, 40, 50, 60];
let targetValue = 50;

function bSearch(array, target) {
  if (arr.length === 1) {
    return 1;
  }
  let low = 0;
  let high = arr.length - 1;

  while (low <= high) {
    let mid = Math.floor((low + high) / 2);

    if (arr[mid] === targetValue) {
      return mid;
    } else if (arr[mid] < targetValue) {
      low = mid + 1;
    } else high = mid - 1;
  }
  return -1;
}

let result = bSearch(arr, targetValue);

if (result !== -1) {
  console.log(`target ${targetValue} is in given array at index ${result}`);
} else {
  console.log(`target ${targetValue} is not present in given array`);
}
