desired_cap = {
            'browser': 'Firefox',
            'browser_version': '74.0',
            'os': 'Windows',
            'os_version': '10',
            'resolution': '1024x768',
            'name': 'Bstack-[Python] Frefox Test',
            'acceptSslCerts': True     #c чего запускать
        }
        url = my_url.urls    #это шокрткат для другого файла с адресом
        # desired_cap['acceptSslCerts'] = True
        self.driver = webdriver.Remote(command_executor=url,
                                       desired_capabilities=desired_cap)

        #для работы в browserstack

        #