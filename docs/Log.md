24-03-2025 
    Starting knowledge:
        1. Python: some experience.
        2. Flask: no experience.
        3. SQLite: decent experience.


    AI prompts: 
        1. How do I set up Flask? https://claude.ai/share/f9b5d20a-1d5b-4e39-b979-6ea5b00f9984
            AI gave a detailed guide on how to set up my first simple Flask Application. 
            Since I have no previous experience with Flask, there is no reference point for me 
            to actually do it myself. In this case, AI was used as a source of documentation.

        2. can you in detail explain what this code? each line
            AI explained the initial code required for the flask to output hello world. 
        
        3. can you explain the architecture of a flask application with examples?
            AI explained the main features of a flask framework, such as the way routes and views work.
            I decided to modify the original code to see how it works, such as creating my own views.

       4. how does one connect sqlite to a python flask project? https://chatgpt.com/share/67f4d195-13d8-8012-a890-4297aeb01f92
        4.1 can you explain what is g in this context?
        4.2 why doesn't the get_db get @app?
        4.3 when is @app.teardown_appcontext used?
        4.4 can you explain what does cursor mean here?
        4.5 After getting basic context I decided to focus on implementing the database alone as a part of non-AI baseline
        

       5. hello, i am trying to make a url shortener, can you explain in detail how such software works, its purpose, etc. https://chatgpt.com/share/67f4d17d-04ec-8012-82c4-ba9d72c22537
       5.1 what is a usual approach taken when generating a short code for a url?
       5.2 can you explain a bit more about auto-incrrement id + base62 encoding?
       5.3 are there any libraries in python that convert a number to base 62 or it something that is usually manually implementing following a certain algorithm? 
       At this point ChatGPT decided to provide a full code snippt of encoder to base 62. I avoided using it, instead, i started a new chat asking about the general algorithm logic.

    6. can you explain base 62 encoding algorithm? please avoid providing any full code snippets https://chatgpt.com/share/67f56d0c-21a0-8012-96a1-ab293380234c
    6.1 provide more examples
    6.2 so, each time i take a remainder of the division and use it as an index for a specific character?
            

    7.1 what operator do i need to use in python to see both remainder and the quotient? https://chatgpt.com/share/67f56d20-2cb8-8012-940a-0f8939d2b7be
