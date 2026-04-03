*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}  https://demo.automationtesting.in/Frames.html

*** Test Cases ***
Handling single iframe
    Open Browser    ${url}  chrome
    Maximize Browser Window
    Sleep    2s

    Select Frame  id=singleframe

    Input Text  xpath=//input[@type="text"]  iframes
    Sleep    2s
    Unselect Frame
    Sleep    2s

    Close Browser

Handling Nested iframes
    Open Browser    ${url}  chrome
    Maximize Browser Window
    Sleep    2s

    Click Element    xpath=//a[@href="#Multiple"]
    Sleep    2S

    Select Frame    xpath=//iframe[@src="MultipleFrames.html"]
    Select Frame    xpath=//iframe[@src='SingleFrame.html']
    Sleep    2s
    
    Input Text    xpath=//input[@type="text"]  nested iframe

    Sleep    2s

    Close Browser