class GoodMorning:

  def get_name():
    person = raw_input("Please enter your name: ")
    print "Good morning " + person

  def display_weather():
    weather = raw_input("Would you like to know the weather? ")
    if weather == "y":
      print "Shitty, don't ride"
    elif weather == "n":
      print "Best of luck with your guessing game"
    else:
      print "It must be a yes or a no but I'm too lazy to program" \
             " this correctly so I'm just going to print this statement" \
             " and then force you to have a terrible experience"

  def determine_state():
    print "You should do your best to avoid state"
    no_state = raw_input("Would you like to avoid state? ")
    words = []
    if no_state == "y":
      for num in range(0,10):
        words.append("shit")
    elif no_state == "n":
      words.append("That's a relief!")
    else:
      print "Once again, that edge case that you didn't enter the" \
             " correct thing"
    return words


  get_name()
  display_weather()
  well = determine_state()

  for w in well:
    print w
