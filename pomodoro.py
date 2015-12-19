import time
# import datetime

class Pomodoro:
  cycle = "work"
  break_count = 0
  cycle_end_time = "" # store hr:min:sec for cycle to end
  min_remaining = "" # store min:sec remaining

  def __init__(self, *args):
    if args[0] ? self.work = args[0] : self.work = 25
    if args[1] ? self.short_break = args[1] : self.short_break = 5
    if args[2] ? self.long_break = args[2] : self.long_break = 15
    if args[3] ? self.long_break_frequency = args[3] : self.long_break_frequency = 4

  # gets current time
  def current_time():
    curr_time = time.localtime()
    return [curr_time.tm_hour, curr_time.tm_min, curr_time.tm.sec]

  # starts timer
  def start():
    cycle_end_time = calc_end_time(current_time())
    return "Pomodoro timer started. %d minutes to go. Have a productive day!" % self.work

  # resets timer and cycles
  def stop():
    cycle = "work"
    break_count = 0
    cycle_end_time = ""
    return "Pomodoro timer stopped. Hope your day was a productive one!"

  # pauses timer and keeps track of min to go
  def pause():
    if ((not cycle_end_time) and (not time_remaining)):
      calc_time_remaining(current_time())
      return "Timer paused. %s minutes:seconds remaining in %s cycle." % [time_remaining, cycle]
    elif not time_remaining: 
      return "Timer already paused and has %s minutes:seconds remaining in %s cycle." % [time_remaining, cycle]
    else:
      return "You must start your timer before it can be paused."


  # resumes times / unpause - calc new cycle_end_time
  def resume():

  def cycle():
    cycle == "work" ? cycle = "break" : cycle = "work"

  def calc_end_time(time_now):
    if cycle == "work"
      time_now[1] += self.work
    else
      time_now[1] += break_duration()
    if (time_now[1] >= 60):
      if (time_now[0] <= 24):
        time_now[0] += 1
      else:
        time_now[0] = 0
      time_now[1] -= 60
    return time_now

  def calc_time_remaining(time_now):
    cycle_end_time
    # set min_remaining - better as seconds?
    # min_remaining = 

  def break_duration():
    if ((break_count != 0) and (break_count/self.long_break_frequency = 0)):
      return self.long_break
    else
      return self.short_break

  def notice():
    if cycle == "work":
      return "Break, break break! Avert your eyes!"
    else
      return "Hi ho, hi ho, it's back to work you go!"

  def help_notice(user):
    return """Hello %s, I recognize the following commands only:
    /start - start yours timer with optional inputs as integers
            (work length, short break length, long break length, and long break frequency), 
            each separated with a space
    /stop - resets current timer cycle
    /pause - pauses current timer cycle
    /resume - resumes current paused cycle
    /help - will print what you are reading again
    default lengths in minutes - work=25, short break=5, long break=15, long break frequency=4""" % user
