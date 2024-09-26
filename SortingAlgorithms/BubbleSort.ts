/**
 * bubble sort in typescript
 * space complexity : constant O(1)
 * time complexity  : quadratic O(n^2)
 */

const unsortedArray: number[] = [64, 34, 25, 12, 22, 11, 90, 5];

function bubbleSort(myArray: number[]): number[] {
  const n = myArray.length;
  let swapped: boolean;

  for (let i = 0; i < n - 1; i++) {
    swapped = false;
    for (let j = 0; j < n - i - 1; j++) {
      if (myArray[j] > myArray[j + 1]) {
        [myArray[j], myArray[j + 1]] = [myArray[j + 1], myArray[j]];
        swapped = true;
      }
    }
    if (!swapped) {
      break;
    }
  }

  return myArray;
}

const myArray: number[] = [7, 3, 9, 12, 11];
const sortedArray = bubbleSort(myArray);
console.log("Sorted array:", sortedArray);
