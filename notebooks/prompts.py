from langchain.prompts import PromptTemplate

CREATION_PROMPT_ZS = PromptTemplate(
    input_variables=["summary"],
    template= """Given a summary of a mobile screen, create the corresponding HTML code
    with a bit of styling, that represents the described functionalities: 
    {summary}."""
)
CREATION_PROMPT_FS = PromptTemplate(
    input_variables=["summary"],
    template="""
        Q: 
        Given a summary of a mobile screen, create the corresponding HTML code with a bit of styling, that represents the described functionalities: 

        The Screen displays different workout options to set, alongside the feature to start the workout.

        A: 
        <!DOCTYPE html>
        <html lang="en">
        <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
        body {{
            font-family: 'Arial', sans-serif;
            background: #FFF;
            margin: 0;
            padding: 0;
        }}

        .navbar {{
            background-color: #4CAF50; 
            color: #FFF;
            display: flex;
            justify-content: space-between;
            padding: 10px 20px;
            align-items: center;
        }}

        .navbar h1 {{
            margin: 0;
            font-size: 24px;
        }}

        .navbar button {{
            background: none;
            border: none;
            color: white;
            font-size: 24px;
            cursor: pointer;
            padding: 0;
            margin: 0 5px;
        }}

        .button-start {{
            background: none;
            border: 2px solid #4CAF50;
            border-radius: 50%;
            color: #4CAF50;
            padding: 20px;
            text-align: center;
            margin: 20px auto;
            display: block;
            width: 200px;
            font-size: 18px;
            cursor: pointer;
        }}

        .menu-item {{
            border-bottom: 1px solid #ccc;
            display: flex;
            justify-content: space-between;
            padding: 10px 20px;
            align-items: center;
            color: #4CAF50;
        }}

        .menu-item:last-child {{
            border-bottom: none;
        }}

        .menu-item button {{
            background: none;
            border: none;
            color: inherit;
            padding: 0;
            cursor: pointer;
            text-align: left;
            width: 100%;
            display: flex;
            justify-content: space-between;
        }}

        .footer-nav {{
            background-color: #4CAF50;
            display: flex;
            justify-content: space-around;
            padding: 10px 0;
            text-align: center;
        }}

        .nav-button {{
            background: none;
            border: none;
            color: white;
            padding: 10px;
            font-size: 14px;
            cursor: pointer;
        }}

        </style>
        </head>
        <body>

        <div class="navbar">
        <h1>Workout</h1>
        <div>
            <button class="info-button" aria-label="Information">i</button>
            <button class="more-options-button" aria-label="More options">&#8942;</button>
        </div>
        </div>

        <button class="button-start">
        START WORKOUT
        </button>

        <div class="menu">
        <div class="menu-item">
            <button>
            <span>Workout</span>
            <span id="workout-selection">Full Body</span>
            </button>
        </div>
        <div class="menu-item">
            <button>
            <span>Circuits</span>
            <span id="circuits-selection">1</span>
            </button>
        </div>
        <div class="menu-item">
            <button>
            <span>Instructor</span>
            <span id="instructor-selection">Announcer</span>
            </button>
        </div>
        </div>

        <nav class="footer-nav">
        <button class="nav-button">Workout</button>
        <button class="nav-button">Learn</button>
        <button class="nav-button">Achievements</button>
        <button class="nav-button">Track</button>
        </nav>

        </body>
        </html>

        Q: 
        Given a summary of a mobile screen, create the corresponding HTML code with a bit of styling, that represents the described functionalities: 

        The mobile screen is part of a language learning application that asks the user to translate a given text sentence. 

        A:
        <!DOCTYPE html>
        <html lang="en">
        <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Language Translation Practice</title>
        <style>
        body {{
            font-family: 'Arial', sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }}

        .container {{
            max-width: 400px;
            margin: auto;
            background: #fff;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            padding: 20px;
            margin-top: 20px;
        }}

        .progress-bar {{
            height: 5px;
            background-color: #4CAF50;
            border-radius: 5px;
            margin-bottom: 20px;
        }}

        .title {{
            text-align: center;
            font-size: 1.2em;
            margin-bottom: 20px;
        }}

        .translation-section {{
            display: flex;
            align-items: center;
            margin-bottom: 20px;
        }}

        .audio-button {{
            background-color: #eee;
            border: none;
            padding: 10px;
            margin-right: 10px;
            border-radius: 50%;
            cursor: pointer;
        }}

        .sentence {{
            flex-grow: 1;
        }}

        .input-field {{
            width: calc(100% - 20px);
            padding: 10px;
            margin-bottom: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }}

        .buttons-container {{
            width: 100%;
            padding: 0;
            display: flex;
            justify-content: space-between;
            margin-bottom: 20px; /* If needed */
        }}

        .button {{
            width: 48%;
            padding: 10px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }}

        .skip-button {{
            background-color: #f44336;
            color: white;
        }}

        .check-button {{
            background-color: #4CAF50;
            color: white;
        }}
        </style>
        </head>
        <body>
        <div class="container">
        <div class="progress-bar" style="width: 25%;"></div>
        <div class="title">Translate this sentence</div>
        <div class="translation-section">
            <button class="audio-button">
            &#9658;
            </button>
            <div class="sentence">Mis animales, mi tortuga, mi cangrejo.</div>
        </div>
        <input class="input-field" type="text" placeholder="Type the English translation">
        <div class="buttons-container">
            <button class="button skip-button">Skip</button>
            <button class="button check-button">Check</button>
        </div>
        </div>

        </body>
        </html>

        Q: 
        Given a summary of a mobile screen, create the corresponding HTML code with a bit of styling, that represents the described functionalities: 

        The mobile screen is a display page in a weather forecast app that shows various options.


        A: 
        <!DOCTYPE html>
        <html lang="en">
        <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Weather App</title>
        <style>
            body, button {{
                font-family: 'Arial', sans-serif;
                margin: 0;
                padding: 0;
                background-color: #e9ecef;
                color: #343a40;
            }}

            #app-container {{
                padding: 20px;
            }}

            h2, h3 {{
                margin-bottom: 16px;
            }}

            button {{
                background-color: #f8f9fa;
                border: 1px solid #ced4da;
                color: #343a40;
                padding: 8px;
                margin-bottom: 8px;
                width: calc(100% - 16px);
                border-radius: 4px;
                font-size: 16px;
                cursor: pointer;
            }}

            button:hover {{
                background-color: #e2e6ea;
            }}

            #temperature-toggle {{
                display: flex;
                justify-content: center;
                align-items: center;
                gap: 8px;
                margin-top: 16px;
            }}

            input[type="radio"] {{
                cursor: pointer;
            }}

            label {{
                font-size: 16px;
                cursor: pointer;
            }}

        </style>
        </head>
        <body>
            <div id="app-container">
                <main>
                    <section id="settings">
                        <h2>SETTINGS</h2>
                        <div id="saved-locations">
                            <h3>SAVED LOCATIONS</h3>
                            <button>New Location</button>
                        </div>
                        <div id="forecast-tabs">
                            <h3>FORECAST TABS</h3>
                            <button>7 Day Forecast</button>
                            <button>Hourly Forecast</button>
                            <button>Weather Details</button>
                        </div>
                        <div id="temperature-toggle">
                            <input type="radio" id="fahrenheit" name="temperature" value="fahrenheit" checked>
                            <label for="fahrenheit">F°</label>
                            <input type="radio" id="celsius" name="temperature" value="celsius">
                            <label for="celsius">C°</label>
                        </div>
                    </section>
                </main>
            </div>
        </body>
        </html>

        Q: Given a summary of a mobile screen, create the corresponding HTML code with a bit of styling, that represents the described functionalities: 

        {summary}

        A:"""
)

CREATION_PROMPT_FS_COT = PromptTemplate(
    input_variables=["summaries"],
    template=""
)

CREATION_PROMPT_ZS_COT = PromptTemplate(
    input_variables=["summaries"],
    template=""
)


SUMMARY_PROMPT = PromptTemplate(
    input_variables=["summaries"],
    template="""Given a collection of Screensummaries, which descripe the same screen:
        {summaries}.
         
        Extract the provided information of the screen and formulate a new description"""
)

SUMMARY_PROMPT_FS = PromptTemplate(
    input_variables= ["summaries"],
    template="""
        Q: Given a collection of Screensummaries, which descripe the same screen:

        Summary 1: page displaying different workout options to set
        Summary 2: page displaying to start exercise
        Summary 3: page displaying to start workout
                
        Extract the provided information of the screen and formulate a new description.

        A: The Screen displays different workout options to set, alongside the feature to start the workout.

        Q: Given a collection of Screensummaries, which descripe the same screen:

        Summary 1: app asking to translate the given sentence
        Summary 2: page displaying about translating the sentence
        Summary 4: page to translate the text
        Summary 5: screen page of language translator application.
                
        Extract the provided information of the screen and formulate a new description.

        A: The mobile screen is part of a language translator application that asks the user to translate a given text sentence. 

        Q: Given a collection of Screensummaries, which descripe the same screen:

        Summary 1: display page showing various options in weather forecast app.
        Summary 2: page displaying various settings.
        Summary 3: screen displaying multiple setting options in a weather forecast application.
        Summary 4: setting page displaying various options in weather application.
        Summary 5: settings page displaying various options in weather application.
                
        Extract the provided information of the screen and formulate a new description.

        A: The mobile screen is a display page in a weather forecast app that shows various options.

        Q: Given a collection of Screensummaries, which descripe the same screen:

        {summaries}
                
        Extract the provided information of the screen and formulate a new description.

        A: 
        """
        )

