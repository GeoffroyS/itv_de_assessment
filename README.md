# Data Engineer Assessment

Given information about streaming video plays, find the maximum number of video plays that were playing concurrently.</br>
Write Scala, Java or Python code that accepts a finite collection of video play records and returns the maximum that were playing at once.</br>
Here is the specification of the format of the source data:

```
VideoPlay {
  startTime : an instant in time
  endTime : an instant in time
}
```

### You can assume:
- all end times are after their corresponding start time</br>
- each play lasts at most a few hours
- all of the plays happen within one calendar month

### Please:
- present your solution as you would a production piece of code
- only use the standard library of your chosen language for code you would expect to
run once your program has been deployed (e.g. do not use Pandas/NumPy)
