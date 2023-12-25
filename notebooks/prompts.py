from langchain.prompts import PromptTemplate

CREATION_PROMPT = PromptTemplate(
    input_variables=["summary"],
    template= """create the HTML code for a Mobilepage, 
    with a bit of styling, that represents following functionality: 
    {summary}."""
)

SUMMARY_PROMPT = PromptTemplate(
    input_variables=["summaries"],
    template="""Given a collection of Screensummaries, which descripe the same screen:
        {summaries}.
         
        Extract the provided information of the screen and formulate a new description"""
)

SUMMARY_PROMPT_COT = PromptTemplate(
    input_variables= ["summaries"],
    template="""
    Q: 
    Please provide a short description of the mobile page based on the following five summaries. Functionalities, that are only provided by one of the five summaries should be ignored.

    Summary 1: display image of a recipes app
    Summary 2: list of ingredients for a recipe in a recipe app
    Summary 3: page displaying information about recipes of specific dish
    Summary 4: page displaying list of items required for a dish
    Summary 5: page showing different recipes available.

    Let's think step by step!

    A:
    Certainly, let's break it down step by step:

    Summary 1: "Display image of a recipes app" - This suggests that it's a screen within a recipes app.

    Summary 2: "List of ingredients for a recipe in a recipe app" - This indicates that the screen shows a list of ingredients for a specific recipe within the app.

    Summary 3: "Page displaying information about recipes of specific dish" - This implies that the screen provides information about a particular dish or recipe.

    Summary 4: "Page displaying list of items required for a dish" - Similar to Summary 2, it mentions a list of items (ingredients) required for a dish.

    Summary 5: "Page showing different recipes available" - This suggests that the screen displays a collection of various recipes. This Summary is the only summary, mentioning multiple recipes, so we ignore this information.

    From these summaries, ignoring summary 5, we can formulate a new description:

    The screen is part of a recipe app and serves as a dedicated page displaying information about a specific dish, including a list of ingredients required for that recipe.

    Q: 
    Please provide a short description of the mobile page based on the following five summaries. Functionalities, that are only provided by one of the five summaries should be ignored.

    {summaries}

    A: Let's think step by step!"""
)

SUMMARY_PROMPT_FS = PromptTemplate(
    input_variables= ["summaries"],
    template="""
        Q: Given a collection of Screensummaries, which descripe the same screen:

        Summary 1: page displaying different workout options to set
        Summary 2: page displaying to start exercise
        Summary 3: page displaying to start workout
        Summary 4: pop-up displaying about body work outs
        Summary 5: timer and different features of a fitness app are displaying.
                
        Extract the provided information of the screen and formulate a new description. Exclude information from summaries, that are contradicting to the majority summaries.

        A: The Screen is part of a fitness app and displays different workout options to set, alongside the feature to start the workout.

        Q: Given a collection of Screensummaries, which descripe the same screen:

        Summary 1: app asking to translate the given sentence
        Summary 2: page displaying about translating the sentence
        Summary 3: page displaying the translation
        Summary 4: page to translate the text
        Summary 5: screen page of language translator application.
                
        Extract the provided information of the screen and formulate a new description. Exclude information from summaries, that are contradicting to the majority summaries.

        A: The mobile screen is part of a language translator application that asks the user to translate a given text sentence. 

        Q: Given a collection of Screensummaries, which descripe the same screen:

        Summary 1: display page showing various options in weather forecast app.
        Summary 2: page displaying various settings.
        Summary 3: screen displaying multiple setting options in a weather forecast application.
        Summary 4: setting page displaying various options in weather application.
        Summary 5: settings page displaying various options in weather application.
                
        Extract the provided information of the screen and formulate a new description. Exclude information from summaries, that are contradicting to the majority summaries.

        A: The mobile screen is a display page in a weather forecast app that shows various options. It is a settings page where users can access and adjust different options in the weather application.

        Q: Given a collection of Screensummaries, which descripe the same screen:

        {summaries}
                
        Extract the provided information of the screen and formulate a new description. Exclude information from summaries, that are contradicting to the majority summaries.

        A: 
        """
        )

COT_CREATION_PROMPT = PromptTemplate(
    input_variables=["summary"],
    template= """create the HTML code for a Mobilepage, 
    with a bit of styling, that represents following functionality: 
    {summary}.
    Let's think step by step."""
)

TOT_CREATION_PROMPT = PromptTemplate(
    input_variables=["summary"],
    template="""Imagine three different experts are solving this task.
    All experts will write down 1 step of their thinking,
    then share it with the group.
    Then all experts will go on to the next step, etc.
    If any expert realises they're wrong at any point then they leave.
    The task is: 
    create the HTML code for a Mobilepage, 
    with a bit of styling, that represents following functionality: 
    {summary}. 
    provide me with the html code, all three experts agreed on"""
)


FEW_SHOT_CREATION_PROMPT = PromptTemplate(
    input_variables=["summary"],
    template="""Q: create the HTML code for a Mobilepage, 
    with a bit of styling, that represents following functionality: 
    """
)