def run_timing():
    count = 0
    km = 0.0
    stop = False
    while not stop:
      try:
          str = input('Enter 10 km run time: ')
          if not str:
              break
          n = float(str)
          km = km + n
          count = count + 1
      except ValueError as e:
          print("That's not a valid number")
    if count == 0:
        print('No run!')
    else:
        print(f'Average of {km / count}, over {count} runs')


run_timing()