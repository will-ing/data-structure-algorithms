# Shift an Array
<!-- Short summary or background information -->
We need to be able to insert numbers in the middle of an array

## Challenge
<!-- Description of the challenge -->
Write a function called insertShiftArray which takes in an array and the value to be added. Without utilizing any of the built-in methods available to your language, return an array with the new value added at the middle index.

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
using slices to break the array in two parts and then concatenate them together with the integer in the middle. Big O was O(n).

## Solution
<!-- Embedded whiteboard image -->
![image](../assets/shiftWhiteboard.png)