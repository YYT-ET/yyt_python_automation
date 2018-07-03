*** Settings ***
Documentation   Suite description
Library  Selenium2Library

*** Test Cases ***
case1
#    login kuaidi100 with superuser
    [Documentation]  登录快递100
#    [Arguments]  ${username}=${superuser_username}      ${password}=${superuser_password}
    open browser    http://www.kuaidi100.com/       chrome
    click element  xpath=//*[@id="welcome"]/a[2]
    input text  xpath=//*[@id="name"]       ${username}
    input text  xpath=//*[@id="password"]       ${password}
    click element  xpath=//*[@id="submit"]

case2
#    Check_number
    [Documentation]  查询一个快递单号
    click element  xpath=//*[@id="menu-track"]
    input text  xpath=//*[@id="postid"]    ${number}
    click element  xpath=//*[@id="query"]

case3
#    Goto_check_page
    [Documentation]   进入查询记录页面
    mouse over          xpath=//*[@id="userName"]
    click element       xpath=//*[@id="userUrl"]/a
    select window       title=我的查件记录 - 快递100个人版

case4
    [Documentation]      获取快递编号
    wait until element is visible       //tr[@class="bb"][1]
    ${check_number}     get text   xpath=//tr[1]/td[3]/a[@title]
    element text should be      //tr[1]/td[3]/a[@title]      ${number}





*** Variables ***
${username}     15902127953
${password}     test123456
${number}        888779603518529476