from robot.libraries.BuiltIn import BuiltIn
# from selenium.webdriver.common.action_chains import ActionChains

class _FlashControllerKeywords:
    ''' The Locator:
    `name:testText*rea/name:U*TextField*`
    `window.document.getElementById('loginApp').fp_type({name:'password_field', text:'mode'});`
    '''
    def __init__(self):
        pass

    @property
    def s2l(self):
        return BuiltIn().get_library_instance('Selenium2Library')

    def _callFlexPilotMethod(self, method, locator, *args):
        params = [self._parse_locator(locator)]
        params.extend(args)
        js = self.js_header + (method % tuple(params))
        return self.s2l.execute_javascript(js) 

    @property
    def js_header(self):
        return "window.document.getElementById('%s')." % self.flashObjectLocator

    def _parse_locator(self, locator):
        countOfEqualSign = locator.count('=')
        if countOfEqualSign == 1:
            return ':'.join(["'%s'" % s for s in locator.split('=')])
        elif countOfEqualSign == 0:
            return "'name':'%s'" % locator
        else:
            raise Exception('More than one Equal Sign')

    def set_flex_object_id(self, flex_obj_id):
        """ TODO to find a default flex_obj_id if none
        (this.browserbot.locateElementByXPath('//embed', this.browserbot.getDocument())) ? this.browserbot.locateElementByXPath('//embed', this.browserbot.getDocument()) : this.browserbot.locateElementByXPath('//object', this.browserbot.getDocument()).id 
        """
        # TODO
        self.flashObjectLocator = flex_obj_id

    def flex_click(self, locator):
        """ Clicks display object.
        """
        return self._callFlexPilotMethod("fp_click({%s});", locator)

    def flex_type(self, locator, text):
        '''Types `text` into the display object found by the locator lookup.
        '''
        return self._callFlexPilotMethod("fp_type({%s, text:'%s'});", locator, text)

    def flex_should_contain_object(self, locator):
        '''assert a display object exists, `locator`
        '''
        return self._callFlexPilotMethod("fp_assertDisplayObject({%s});", locator)
