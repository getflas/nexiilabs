*** Settings ***
Library           Selenium2Library    WITH NAME    se

*** Variables ***
@{packages}       robotframework-selenium2library

*** Test Cases ***
verify_edit_roles_without_any_changes
    ${chrome_options} =    Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys, selenium.webdriver
    Call Method    ${chrome_options}    add_argument    headless
    Call Method    ${chrome_options}    add_argument    disable-gpu
    Call Method    ${chrome_options}    add_argument    disable-extension
    Call Method    ${chrome_options}    add_argument    disable-dev-shm-usage
    Call Method    ${chrome_options}    add_argument    no-sandbox
    ${options}=    Call Method    ${chrome_options}    to_capabilities
    Open Browser    http://111.93.7.182    Chrome    desired_capabilities=${options}
    Input Text    xpath=//input[@id='emailid']    veera@gm.com
    Input Password    xpath=//input[@id='pwd']    mypassword
    Click Button    xpath=//button[@class='btn btn-purple btn-block text-uppercase waves-effect waves-light']
    Maximize Browser Window
    Wait Until Page Contains Element    xpath://*[@id="sidebar-menu"]/ul/li[1]/ul/li[2]/a    50
    Click Element    xpath://*[@id="sidebar-menu"]/ul/li[1]/ul/li[2]/a
    Wait Until Page Contains Element    xpath://*[@id="datatable-responsive_filter"]/label/input    50
    Input Text    xpath://*[@id="datatable-responsive_filter"]/label/input    manag1
    Wait Until Page Contains Element    xpath://*[@id="roleList"]/tr[1]/td[3]/a[1]/i    50
    Click Element    xpath://*[@id="roleList"]/tr[1]/td[3]/a[1]/i
    Sleep    2
    Wait Until Page Contains Element    xpath://*[@id="10"]/button[1]    50
    Click Element    xpath://*[@id="10"]/button[1]
    Wait Until Page Contains    No changes found in Role Update.    50
    Close Browser
