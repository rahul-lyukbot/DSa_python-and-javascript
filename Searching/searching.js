let arr = [10, 20, 30, 40, 50, 60];

function bSearch(arr, x) {
  if (arr.length === 1) {
    return 1;
  }
  let low = 0;
  let high = arr.length - 1;

  while (low < high) {
    let mid = Math.floor((low + high) / 2);

    if (arr[mid] === x) {
      return mid;
    } else if (arr[mid - 1] > x) {
      low = mid + 1;
    } else high = mid - 1;
  }
  return -1;
}

console.log(bSearch(arr, 50));
