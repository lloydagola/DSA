/**
 * bubble sort in typescript
 * space complexity : constant O(1)
 * time complexity  : quadratic O(n^2)
 */

const unsortedArray: number[] = [64, 34, 25, 12, 22, 11, 90, 5];

function bubbleSort(arr: number[] = [], order: string = "ascending"): number[] {
  const n = arr.length;

  for (let i = 0; i < n - 1; i++) {
    for (let j = 0; j < n - 1 - i; j++) {
      if (
        (order === "descending" && arr[j] < arr[j + 1]) ||
        (order === "ascending" && arr[j] > arr[j + 1])
      ) {
        [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]]; // Swap elements
      }
    }
  }

  return arr;
}

console.log(bubbleSort(unsortedArray));
