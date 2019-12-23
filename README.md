# Web Auto Login
你好，你需要手动修改本程序，来实现自动登陆web认证

num = 你的学号
如果你的运营商为中国移动，那么isp = cmcc；中国联通 = unicom；中国电信 = telecom；校园网 = xyz
password = 你的身份证后6位
请修改dict中的key DDDDD修改为',0,num@isp'
upass key 请改为'password'

如a的学号为201900000000 身份证后6位为000000 且为电信公司办理的宽带
那么他的dict应为这样的：{.....'DDDDD':',0,201900000000@telecom,'upass':'000000', .....}


