*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url} https://inc.in/

*** Test Cases ***
handling js
    Open Browser    ${url}  chrome
    Maximize Browser Window
    Sleep    2s

    Execute Javascript    windows.scrollTo(0,document.body.scrollHeight)
    Sleep    2s

    Execute Javascript    window.scrollBy(0,500)
    Sleep    2s

    Execute Javascript    "arguments[0].scrollIntoView();",element

    Close Browser