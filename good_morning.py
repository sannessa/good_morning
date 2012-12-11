import random

class GoodMorning:

  def get_name(self):
    person = raw_input("Please enter your name: ")

    list_of_silly_names = ['cockpit lover', 'titty mcboob', 'chesty mctesticle', 'orangey mcboobtoucher'
                           'stoopid head', 'casey stoner', 'dani pedrosa']
    if person.lower() == "jason":
      person = list_of_silly_names[random.randint(0, len(list_of_silly_names) - 1)]

    print "Good morning " + person
    self.name = person

  def display_weather(self):
    weather = raw_input("Would you like to know the weather? ").lower()
    answered_correctly = False
    while not answered_correctly:
      if weather == "y":
        print "Shitty, don't ride"
        answered_correctly = True
      elif weather == "n":
        print "Best of luck with your guessing game"
	answered_correctly = True
      else:
        print "Y/n are the only acceptable answers"
        weather = raw_input("Would you like to know the weather? ").lower()
    self.weather = weather
    return weather

  def determine_state(self):
    print "You should do your best to avoid state"
    no_state = raw_input("Would you like to avoid state? ").lower()
    words = []
    answered_correctly = False
    while not answered_correctly:
      if no_state == "y":
        for num in range(0,10):
          words.append("shit")
        answered_correctly = True
      elif no_state == "n":
        words.append("That's a relief!")
        answered_correctly = True
      else:
        print "Y/n are the only acceptable answers"
        no_state = raw_input("Would you like to avoid state? ").lower()
    self.no_state = no_state
    return words

  def process_user(self):
    self.get_name()
    print "\n"
    self.display_weather()
    print "\n"
    well = self.determine_state()

    for w in well:
      print w
