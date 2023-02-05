import sys
import pyfiglet
banner = pyfiglet.figlet_format("CLI  ZOFixer")
print(banner,end="An unofficial CLI Google Dorker of ZOFixer\n\nhttps://dash.zofixer.com/googlehacking\n\n")

def main():
       target = input('Enter Target: ')
       print(end='\n')
       dict = {
              'SQL Error': f"site:{target} intext:\"sql syntax near\" | intext:\"syntax error has occurred\" | intext:\"incorrect syntax near\" | intext:\"unexpected end of SQL command\" | intext:\"Warning: mysql_connect()\" | intext:\"Warning: mysql_query()\" | intext:\"Warning: pg_connect()\"",
              'Login Pages': f"site:{target} inurl:login | inurl:signin | intitle:Login | intitle:\"sign in\" | inurl:\"auth\"",
              'SignUp Pages': f"site:{target} inurl:signup | inurl:register | intitle:Signup",
              'PHP/Errors/warning': f"site:{target} \"PHP Parse error\" | \"PHP Warning\" | \"PHP Error\"",
              'Backup files': f"site:{target} ext:bkf | ext:bkp | ext:bak | ext:old | ext:backup",
              'Configuration Files EXposed': f"site:{target} ext:xml | ext:conf | ext:cnf | ext:reg | ext:inf | ext:rdp | ext:cfg | ext:txt | ext:ora | ext:ini | ext:env",
              'Document Exposed': f"site:{target} ext:doc | ext:docx | ext:odt | ext:rtf | ext:sxw | ext:psw | ext:ppt | ext:pptx | ext:pps | ext:csv",
              'Directory Listing': f"site:{target} intitle:index of",
              'Find Subdomains': f"site:*.{target}",
              'Error Messages': f"site:{target} \"Lucee" "Error (expression)\" -lucee.org | intext:\"Error Occurred While Processing Request\" | intitle:\"index of\" \"stacktrace.log\" | intitle:\"index of\" \"my-errors.log\" OR \"my-errors.logs\" | intitle:\"index of\" errors.log",
              'Error Messages[L2]': f"site:{target} inurl:\"/WebResource.axd?d=\" AND intext:Error | inurl:\"index.php?id=\" intext:\"Warning: mysql_num_rows()\" | intext:\"sf_app\" + \"frontend sf_app_base_cache_dir:\" | intitle:\"Error log for /LM/\" | inurl:elmah.axd ext:axd",
              'Error Messages[L3]': f'site:{target} inurl:"/errors/report.php" intext:"There has been an error processing your request" | site:*/wp-admin/maint/repair.php intext:"define(WP_ALLOW_REPAIR,true);" | site:*/wp-includes/Requests/php_errorlog | inurl:/php-errors.log filetype:log',
              'File Exposed(password)': f'site:{target} intitle:"Index of" htpasswd | 	intitle:"Index of" pwd.db | site:rentry.co intext:"password" | site:controlc.com intext:"password" | site:pastebin.com "admin password"',
              'File Exposed[L2]': f'site:{target} site:pastebin.com "password" | site:pastebin.com intext:pass.txt | 	intext:"Index of" intext:"password.zip" | site:pastebin.com intext:password.txt | intext:"index of" "uploads" | intext:"password" | "passwd" | "pwd" site:ghostbin.com | intext:"/pfx-password.txt" "[To Parent Directory]"',
              'File Exposed[L3]': f'site:{target} inurl:/wp-content/uploads/ ext:txt "username" | "user name" | "uname" | "user" | "userid" | "user id" AND "password" | "pass word" | "pwd" | "pw" | 	site:pastebin.com intext:username | password | SECRET_KEY | inurl:password site:shodan.io | Inurl: "login" Intitle:index of username and pass',
              'Network or Vulnerability Data': f'site:{target} intitle:"NETSurveillance WEB" | intitle:"jaeger UI" inurl:trace | intitle:"routeros" "sophia" | intitle:"ZAP Scanning Report" + "Alert Detail" | intitle:"Skipfish - scan results browser" | intitle:"Nikto Report" "OSVDB" | intitle:traefik inurl:8080/dashboard',
              'Network or Vulnerability Data[L2]': f'site:{target} intitle:Grapher AND inurl:sensorlist.htm | intitle:"netdata dashboard" AND intext:"Costa Tsaousis" | intitle:"Cacti" AND inurl:"/monitor/monitor.php" | intitle:"Dashboards" AND inurl:"/zabbix/zabbix.php?action=dashboard.list"',
              'Network or Vulnerability Data[L3]': f'site:{target} intitle:"OpenNMS web console" inurl:opennms/index.jsp | inurl:zabbix/zabbix.php | inurl:"/Serviceability?adapter=device.statistics.configuration" | intitle:Host Report inurl:ganglia',
              'Web Server Detection': f'site:{target} inurl:/geoserver/web/ | site:vps-*.vps.ovh.net | inurl *:8080/login.php | site:*/*.asp | Fwd: intitle:"STEP by STIBO Systems" "Launch STEPworkbench" "Web UI Component Report"',
              'Web Server Detection[L2]': f'site:{target} inurl:"/app/kibana#" | "NTRIP Caster Table Contents" "This is a SNIP NTRIP Caster" | intitle:"Shoutcast server" inurl:"/index.html" "SHOUTcast Server" | intitle:"Welfcome to OpenResty!" | intitle:"index of" site:.gov.in',
              'Web Server Detection[L3]': f'site:{target} intitle:"Success!" intext:"Your new web server is ready to use." | intitle:"WATASHI SERVICE" | "Wowza Streaming Engine 4 Developer Edition" | intitle:"index of" "/homedir/etc/" | intitle:"index of" AND inurl:magento AND inurl:/dev'
              }
       v = []
       for keys, value in dict.items():
              v.append(keys)
       for i in v:
              print(v.index(i) + 1, end=' ')
              print(" ", i)
       prompt = input("\nSelect Dorking Query No[1-21]: ")
       if prompt == "1":
              print('\nGoogle this:\n')
              print(dict['SQL Error'])
       elif prompt == "2":
              print('\nGoogle this:\n')
              print(dict['Login Pages'])
       elif prompt == "3":
              print('\nGoogle this:\n')
              print(dict['SignUp Pages'])
       elif prompt == "4":
              print('\nGoogle this:\n')
              print(dict['PHP/Errors/warning'])
       elif prompt == "5":
              print('\nGoogle this:\n')
              print(dict['Backup files'])
       elif prompt == "6":
              print('\nGoogle this:\n')
              print(dict['Configuration Files EXposed'])
       elif prompt == "7":
              print('\nGoogle this:\n')
              print(dict['Document Exposed'])
       elif prompt == "8":
              print('\nGoogle this:\n')
              print(dict['Directory Listing'])
       elif prompt == "9":
              print('\nGoogle this:\n')
              print(dict['Find Subdomains'])
       elif prompt == "10":
              print('\nGoogle this:\n')
              print(dict['Error Messages'])
       elif prompt == "11":
              print('\nGoogle this:\n')
              print(dict['Error Messages[L2]'])
       elif prompt == "12":
              print('\nGoogle this:\n')
              print(dict['Error Messages[L3]'])
       elif prompt == "13":
              print('\nGoogle this:\n')
              print(dict['File Exposed(password)'])
       elif prompt == "14":
              print('\nGoogle this:\n')
              print(dict['File Exposed[L2]'])
       elif prompt == "15":
              print('\nGoogle this:\n')
              print(dict['File Exposed[L3]'])
       elif prompt == "16":
              print('\nGoogle this:\n')
              print(dict['Network or Vulnerability Data'])
       elif prompt == "17":
              print('\nGoogle this:\n')
              print(dict['Network or Vulnerability Data[L2]'])
       elif prompt == "18":
              print('\nGoogle this:\n')
              print(dict['Network or Vulnerability Data[L3]'])
       elif prompt == "19":
              print('\nGoogle this:\n')
              print(dict['Web Server Detection'])
       elif prompt == "20":
              print('\nGoogle this:\n')
              print(dict['Web Server Detection[L2]'])
       elif prompt == "21":
              print('\nGoogle this:\n')
              print(dict['Web Server Detection[L3]'])


if __name__ == '__main__':
    try:
           main()
    except KeyboardInterrupt as e:
           e = '\n\nKeyboard Interrupt Detected Exiting!!'
           print(e)
           sys.exit()