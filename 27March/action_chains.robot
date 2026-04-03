*** Settings ***
Documentation  Handling elements
Library  SeleniumLibrary

*** Variables ***
${url}  https://the-internet.herokuapp.com/
${prac}  https://testautomationpractice.blogspot.com/

*** Test Cases ***
Handling Drag And Drop
    Open Browser    ${url}  chrome
    Maximize Browser Window
    Click Element    //a[text()="Drag and Drop"]
    Sleep    2s
    Drag And Drop    id=column-a  id=column-b
    Sleep    2s

    Close Browser

Handling mouse hover
    Open Browser    ${url}  chrome
    Maximize Browser Window
    Click Element    //a[text()="Hovers"]
    Sleep    2s
    Mouse Over    xpath=(//div[@class="figure"])[2]
    Sleep    2s
    Close Browser

Scroll To The Element
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    1s

    Scroll Element Into View    xpath=//a[text()="Typos"]
    Sleep    2s

    Close Browser