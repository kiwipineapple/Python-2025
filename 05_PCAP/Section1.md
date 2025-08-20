**truc()**  Return the truncated integer parts of different numbers  
`print(math.trunc(2.77))`     
**result: 2**

**factorial(x)** Returns the factorial of desired number.  
`math.factorial(3)`  
**result: 6  (3 * 2 * 1)**

**hypot()** is used to compute the Euclidean distance from the origin (0, 0) to a point (x, y) in a 2D plane.  
`x = 3`  
`y = 4`  
**result:** 5 (sqrt(32 + 42)

**platform** is a built-in library that provides a portable way to access information about underlying platform (hardware and operating system) on which your Python program is running.  
`import platform`  
`print(platform.processor())`  
**result:** Intel64 Family 6 Model 154 Stepping 4, GenuineIntel


`print(platform.machine())`  
**result:** e.g., ‘x86_64’, ‘AMD64’, etc.

`print(platform.platform())`  
**result:** Windows-10-10.0.26100-SP0

`print(platform.system())`  
**result:** Windows

`print(platform.version())`   This method returns the underlying system’s version.  
**result:** 10.0.19045

`print(platform.python_implementation())`  
**result:** CPython