*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://the-internet-heroukuapp.com/windows

*** Test Cases ***
Handling windows
    Open Browser    ${url}  chrome
    Maximize Browser Window
    Sleep    2s
    Click Element    xpath="//a[@href="/windows/new"]"

    
    @{windows}  Get Window Handles
    
    Switch Window    NEW 
    
    Page Should Contain    New window
    Page Should Contain Element    xpath='//h3[text()='New Window']'
    
    Switch Window    @{windows}[0]
    Close Window
