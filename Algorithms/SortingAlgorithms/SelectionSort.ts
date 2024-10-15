/**
 * Selection Sort implementation
 * Time Complexity : Quadratic O(n^2)
 * Space Complexity : Constant O(1)
 */

let unsorted_list = [64, 34, 25, 12, 22, 11, 90, 5];

function selectionSort(arr: number[]): number[] {
  let n = arr.length;

  if (n <= 1) return arr;

  for (let i = 0; i < n; i++) {
    let min_index = i;

    for (let j = i + 1; j < n; j++) {
      if (arr[min_index] > arr[j]) min_index = j;
    }
    let tmp = arr[i];
    arr[i] = arr[min_index];
    arr[min_index] = tmp;
  }

  return arr;
}
console.log(selectionSort(unsorted_list));
