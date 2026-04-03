*** Settings ***
Documentation  Handling elements
Library  SeleniumLibrary

*** Variables ***
${url}  https://the-internet.herokuapp.com/
${prac}  https://testautomationpractice.blogspot.com/

*** Test Cases ***
Handle DropDown
    Open Browser    ${url}  chrome
    Maximize Browser Window
    Click Element    xpath=//a[text()="DropDown"]

    Page Should Contain Link    id=dropdown
    
    ${options}=  Get List Items    id=dropdown
    Log To Console    ${options}
    
    Select From List By Label  id='dropdown'  Option1
    
    ${select_options}=  Get Selected List Label    id=dropdown
    Log To Console    ${select_options}
    
    List Selection Should Be    id=dropdown Option1
    Sleep    2s
    
    Close Browser

