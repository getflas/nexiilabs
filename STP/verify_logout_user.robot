***Settings***
Library           Selenium2Library    WITH NAME    se
*** Test Cases ***
Verify_Logout_user.robot
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
    Wait Until Page Contains Element    xpath://*[@id="wrapper"]/div[3]/div/div/div[1]/div/div/a    30
    Wait Until Page Contains Element    xpath://*[@id="notification"]/li[7]/a/img    50
    Click Element    xpath://*[@id="notification"]/li[7]/a/img
    Wait Until Page Contains Element    xpath://*[@id="notification"]/li[7]/ul/li[3]/a    50
    Click Element    xpath://*[@id="notification"]/li[7]/ul/li[3]/a
    Wait Until Page Contains    Sign In to STP    50
    Close Browser