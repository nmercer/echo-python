# echo-python

Amazon Echo Todo/Shopping List API For Python

### Basics
This works off adding things to your todo list or shopping list. It returns None if you have not said anything new. It returns the string of what you said if you did say something new, like "Turn Off Lights".

```py
from amazon_echo import Echo

echo = Echo('username', 'password')

print echo.get_latest_todo()
print echo.get_latest_shopping()
```

The todo list seems to listen to longer strings of commands more accuratly. Like "Turn off the lights and turn the heat down".

The shopping list seems to listen to short command strings better. Like "shuffle" or "turn down".

### Requires
  - beautifulsoup4

  - requests


### Example

``` py
from amazon_echo import Echo
import sched, time

scheduler = sched.scheduler(time.time, time.sleep)
echo = Echo('username', 'password')

# Runs Every 5 Seconds and prints out what you last said
def main(scheduler):
    todo = echo.get_latest_todo()
    if todo:
        pass # Todo - Whatever you want to do based on what you said, Turn on lights, Turn down heat, Etc...

    scheduler.enter(5, 1, main, (scheduler,))

scheduler.enter(0, 1, main, (scheduler,))
scheduler.run()
```
