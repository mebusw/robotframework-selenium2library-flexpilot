from robot.libraries.BuiltIn import BuiltIn
# from selenium.webdriver.common.action_chains import ActionChains

class _FlashControllerKeywords:
    ''' The Locator:
    `name:testText*rea/name:U*TextField*`
    `window.document.getElementById('loginApp').fp_type({name:'password_field', text:'mode'});`
    '''
    def __init__(self):
        self._flex_app = None

    @property
    def s2l(self):
        return BuiltIn().get_library_instance('Selenium2Library')


    def _do_command(self, command, locator, *args):
        self.s2l._debug("Executing command '%s' for application '%s' with options '%s'"
                    % (command, self._flex_app, args))
        params = [self._parse_locator(locator)]
        params.extend(args)
        js = self.js_header + (command % tuple(params))
        return self.s2l.execute_javascript(js) 

    @property
    def js_header(self):
        return "window.document.getElementById('%s')." % self._flex_app

    def _parse_locator(self, locator):
        countOfEqualSign = locator.count('=')
        if countOfEqualSign == 1:
            return ':'.join(["'%s'" % s for s in locator.split('=')])
        elif countOfEqualSign == 0:
            return "'name':'%s'" % locator
        else:
            raise Exception('More than one Equal Sign')

    def select_flex_application(self, locator):
        """Selects Flex application to work with and waits until it is active.

        All further Flex keywords will operate on the selected application and
        thus you *must always* use this keyword before them. You must also use
        this keyword when you want to operate another Flex application.

        Because this keyword waits until the selected application is active,
        it is recommended to use this if the page where the application is
        located is reloaded. The timeout used is the same Selenium timeout that
        can be set in `importing` and with `Set Selenium Timeout` keyword.

        The application is found using `locator` that must be either `id` or
        `name` of the application in HTML. Notice that if you have different
        elements for different browsers (<object> vs. <embed>), you need to
        use different attributes depending on the browser.

        The old locator is returned and can be used to switch back to the
        previous application.

        Example:
        | Select Flex Application                 | exampleFlexApp |
        | Click Flex Element                      | myButton       |
        | ${prev app} | = Select Flex Application | secondFlexApp  |
        | Flex Element Text Should Be             | Hello, Flex!   |
        | Select Flex Application                 | ${prev app}    |
        """

        # TODO to find a default flex_obj_id if none
        # (this.browserbot.locateElementByXPath('//embed', this.browserbot.getDocument())) ? this.browserbot.locateElementByXPath('//embed', this.browserbot.getDocument()) : this.browserbot.locateElementByXPath('//object', this.browserbot.getDocument()).id 
        self._flex_app, old = locator, self._flex_app
        if locator:
            self.s2l.page_should_contain_element(locator)
            # It seems that Selenium timeout is used regardless what's given here
            # TODO self._selenium.do_command("waitForFlexReady", [locator, self._timeout])
        return old

    def click_flex_element(self, locator):
        """ Clicks display object.
        """
        return self._do_command("fp_click({%s});", locator)

    def input_text_into_flex_element(self, locator, text):
        '''Types `text` into the display object found by the locator lookup.
        '''
        return self._do_command("fp_type({%s, text:'%s'});", locator, text)

    def flex_element_should_exist(self, locator):
        '''assert a display object exists, `locator`
        '''
        return self._do_command("fp_assertDisplayObject({%s});", locator)
