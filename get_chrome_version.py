def get_chrome_version():
    # This function attempts to get the installed Chrome version
    try:
        import winreg
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Google\Chrome\BLBeacon")
        version, type = winreg.QueryValueEx(key, "version")
        return version
    except:
        return None