/**
 * Quicksort impplementation in ts
 * Time complexity: Linear Logarithmic O(n Log n)
 * Space complexity: O(Log n)
 */

let unsorted = [64, 34, 25, 12, 22, 11, 90, 5];

function partition(ls: number[], low: number, high: number): number {
  let pivot = ls[high];
  let i = low - 1;

  for (let j = low; j < high; j++) {
    if (ls[j] < ls[high]) {
      i += 1;
      let tmp = ls[j];
      ls[j] = ls[i];
      ls[i] = tmp;
    }
  }
  let tmp = ls[i + 1];
  ls[i + 1] = ls[high];
  ls[high] = tmp;

  return i + 1;
}

function quicksort(ls: number[], low: number = 0, _high?: number) {
  let high = _high;
  if (!high) high = ls.length - 1;

  if (low < high) {
    let pivot_index = partition(ls, low, high);

    quicksort(ls, low, pivot_index - 1);
    quicksort(ls, pivot_index + 1, high);
  }

  return ls;
}

console.log(quicksort(unsorted));
