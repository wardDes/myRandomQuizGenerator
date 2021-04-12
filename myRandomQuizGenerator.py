import random
import pyinputplus as pyip# must download to user's working python version
# The quiz data. Keys are states and value 
# is a list of the cities of the state with
# the first element being the correct capital.
capitals = {
'Alabama': ['Montgomery', 'Mobile', 'Birmingham', 'Huntsville'],
'Alaska': ['Juneau', 'Fairbanks','Anchorage','St. Michael'],
'Arizona': ['Phoenix','Tucson','Flagstaff','Yuma'],
'Arkansas': ['Little Rock', 'Fayetteville','Springdale','Hot Springs'],
'California': ['Sacramento', 'Monterey','San Francisco', 'Los Angeles'],
'Colorado': ['Denver','Boulder','Vail','Monte Vista'],
'Connecticut': ['Hartford', 'Danbury','New Haven','Norwich'],
'Delaware': ['Dover', 'Delaware City', 'Smyrna','Middletown'],
'Florida': ['Tallahassee','Jacksonville','St. Petersburg', 'Tampa Bay'],
'Georgia': ['Atlanta','Macon','Augusta','Savannah'], 
'Hawaii': ['Honolulu', 'Oahu','Hilo','Kailua'],
'Idaho': ['Boise', 'Lewiston','Nampa','Caldwell'],
'Illinois':['Springfield', 'Decatur','Peoria', 'Marion'],
'Indiana': ['Indianapolis', 'Evansville','Terre Haute','Columbus'],
'Iowa': ['Des Moines', 'Iowa City','Cedar Rapids','Davenport'],
'Kansas': ['Topeka', 'Kansas City','Wichita','Winfield'],
'Kentucky': ['Frankfort', 'Lexington','Pikeville','Richmond'],
'Louisiana': ['Baton Rouge', 'Shreveport','New Orleans','Morgan City'],
'Maine': ['Augusta', 'Portland','Lewiston','Bangor'],
'Maryland': ['Annapolis', 'Baltimore','Annapolis','Bethesda'],
'Massachusetts': ['Boston', 'Salem','Worchester','Cambridge'],
'Michigan': ['Lansing', 'Detroit','Saginaw','Dearborn'],
'Minnesota': ['Saint Paul', 'Minneapolis','Duluth','Rochester'],
'Mississippi': ['Jackson', 'Vicksburg','Natchez','Tupelo'],
'Missouri': ['Jefferson City', 'St. Louis', 'Kansas City', 'Springfield'],
'Montana': ['Helena','Billings','Butte','Livingston'],
'Nebraska': ['Lincoln','Omaha','Kearney','Hastings'],
'Nevada': ['Carson City', 'Reno','Las Vegas','Hawthorne'],
'New Hampshire': ['Concord', 'Portsmouth','Franklin','Manchester'],
'New Jersey': ['Trenton', 'Newark','Elizabeth','New Brunswick'],
'New Mexico': ['Santa Fe', 'Albuquerque','Santa Fe','Los Alamos'],
'New York': ['Albany','New York City','Syracuse','Jamestown'],
'North Carolina': ['Raleigh', 'Fayetteville','Winston-Salem','Charolotte'],
'North Dakota': ['Bismarck', 'Fargo','Dickinson','Williston'],
'Ohio': ['Columbus', 'Dayton','Cleveland','Toledo'],
'Oklahoma': ['Oklahoma City','Tulsa','Lawton','Stillwater'],
'Oregon': ['Salem','Portland','Oregon City', 'St. Helena'],
'Pennsylvania': ['Harrisburg', 'Philadelphia','Erie','Pittsburgh'],
'Rhode Island': ['Providence','Warwick','Newport','Cranston'],
'South Carolina': ['Columbia', 'Charleston','Greenwood','Clemson'],
'South Dakota': ['Pierre', 'Sioux Falls', 'Watertown', 'Aberdeen'],
'Tennessee': ['Nashville', 'Memphis','Chattanooga', 'Oak Ridge'],
'Texas': ['Austin', 'Abilene','San Antonio','Houston'],
'Utah': ['Salt Lake City', 'Provo','Brigham City','Richfield'],
'Vermont': ['Montpelier', 'Burlington','Newport','Rutland'],
'Virginia': ['Richmond', 'Arlington','Norfolk','Briston'],
'Washington': ['Olympia', 'Seattle','Spokane','Tacoma'],
'West Virginia': ['Charleston', 'Clarksburg', 'Wheeling', 'Welch'],
'Wisconsin': ['Madison', 'Milwaukee','Green Bay', 'Eau Claire'],
'Wyoming': ['Cheyenne', 'Casper', 'Jackson', 'Rawlins']}

print('Enter number of students to be tested: ')
response=pyip.inputInt()

# Number to Generate quiz files for number of studentss
for quizNum in range(response):
    # Create the quiz and answer key files.
    quizFile = open(f'capitalsquiz{quizNum + 1}.txt', 'w')
    answerKeyFile = open(f'capitalsquiz_answers{quizNum + 1}.txt', 'w')
    
    # Write out the header for the quiz.
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + f'State Capitals Quiz (Form{quizNum + 1})')
    quizFile.write('\n\n')
       
    # Shuffle the order of the states.
    states = list(capitals.keys())
    random.shuffle(states)# reorders list randomly

    # Loop through all 50 states, making a question for each.
    for questionNum in range(50):
        # my changes
        # Get right and wrong answers.
        # use random states list state keys to get capital values
        correctAnswer = capitals[states[questionNum]][0]
        answerOptions = capitals[states[questionNum]]
        random.shuffle(answerOptions)
  

        # Write the question and answer options to the quiz file.
        quizFile.write(f'{questionNum + 1}. What is the capital of {states[questionNum]}?\n')
        for i in range(4):
            # {'ABCD'[i]}} sees 'ABCD' as list that
            # prints elements 0 thru 3 of string
            quizFile.write(f"    {'ABCD'[i]}.{ answerOptions[i]}\n")
        quizFile.write('\n')

        # Write the answer key to a file.
        answerKeyFile.write(f"{questionNum + 1}.{'ABCD'[answerOptions.index(correctAnswer)]}\n")

quizFile.close()
answerKeyFile.close()
