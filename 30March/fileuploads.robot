*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem
*** Variables ***
${url}  https://the-internet.herokuapp.com/
${download}  C:\\Users\\DELL\\Downloads\\file.txt
*** Test Cases ***
Upload
    Open Browser    ${url}  chrome
    Maximize Browser Window
    Click Element    xpath=//a[@href="/upload"]
    Sleep    2s
    
    ${path}  Normalize Path    ${CURDIR}/alerts.robot
    Choose File    id=file-upload  ${path}
    Sleep    2s

    Click Button    id=file-submit

Download
    Open Browser    ${url}  chrome
    Maximize Browser Window
    
    Click Element    xpath=//a[@href="/download"]
    Sleep    2s
    
    Click Element    xpath=//a[@href="download/file.txt"]

    Wait Until Created    ${download}  timeout=10s
    
    File Should Exist    ${download}
    Log To Console    it downloaded successfully
    Close Browser