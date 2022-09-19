# Data Engineer Assessment

Given information about streaming video plays, find the maximum number of video plays that were playing concurrently.</br>
Write Scala, Java or Python code that accepts a finite collection of video play records and returns the maximum that were playing at once.</br>
Here is the specification of the format of the source data:

```
{
    "VideoPlay1": {
        "startTime": "2022-08-06 02:39:29",
        "endTime": "2022-08-06 02:52:29"
    },
    "VideoPlay2": {
        "startTime": "2022-08-24 11:20:22",
        "endTime": "2022-08-24 12:10:22"
    },
    "VideoPlay3": {
        "startTime": "2022-08-06 04:15:57",
        "endTime": "2022-08-06 05:30:57"
    }
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
