*** Settings ***
Library  Selenium2Library
Resource  ./varibles.robot

*** Keywords ***
login kuaidi100 with superuser
    [Documentation]  登录快递100
    [Arguments]  ${username}=${superuser_username}      ${password}=${superuser_password}}
    open browser    http://www.kuaidi100.com/       chrome
    click element  xpath=//*[@id="welcome"]/a[2]
    input text  xpath=//*[@id="name"]       ${username}
    input text  xpath=//*[@id="password"]       ${password}
    click element  xpath=//*[@id="submit"]

Get_check_count
    [Documentation]  获取查询次数(set global variable设置成全局变量)
    ${checked_count}    get matching xpath count  //tr[@class='bb']
#    set global variable     ${checked_count}
    [Return]    ${checked_count}

Check_number
    [Documentation]  查询一个快递单号
    click element  xpath=//*[@id="menu-track"]
    input text  xpath=//*[@id="postid"]     ${number}
    click element  xpath=//*[@id="query"]

Get_CompanyName
    [Documentation]  获取查询快递的快递公司名称
    wait until element is visible     xpath=//*[@id="single-name"]
    ${company_name}     get text    xpath=//*[@id="single-name"]
    set global variable     ${company_name}

Goto_check_page
    [Documentation]   进入查询记录页面
    mouse over          xpath=//*[@id="username"]
    click element       xpath=//*[text()="我的查询记录"]
    select window       title=我的查询记录-快递100个人版

Check_count_shouId be plus one
    [Documentation]
    [Arguments]     ${class}
    ${check_count_after}        evaluate    ${class}+1   #${checked_count}+1
    wait until element is visible       //tr[@class="bb"][${check_count_after}]
    set global variable     ${check_count_after}

Check_company_should be right
    [Documentation]
    xpath should match x times      //tr[@class="bb"]       ${check_count_after}
    element text should be      xpath=//tr[${checked_count}+1]/td[2]/a      ${company_name}

send_mail
pass execution