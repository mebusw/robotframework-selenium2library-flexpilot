robotframework-selenium2library-flexpilot
==========================================
Extends the [robotframework-selenium2library](https://github.com/rtomac/robotframework-selenium2library/ "robotframework-selenium2library") to wrap [Flex Pilot](https://github.com/mde/flex-pilot) to support Flex / Flash automation testing. 


Extra keywords
==============

[Flex Pilot API](https://github.com/mde/flex-pilot/wiki/api)
locator/lookup mechanism, eventing



Requirements
============
* Robotframework
* robotframework-selenium2library
* FlashPlayer (debugger version)
* (Optional) FlashFirebug help get the locator of objects

Installation
============

    git clone https://github.com/hmalphettes/robotframework-selenium2library-flexpilot.git

And in your robotframework test, import the library. For example:

    *** Settings
    Library           ${CURDIR}/../../src/Selenium2LibraryFlexPilot    WITH NAME    Selenium2LibraryFlexPilot


Run the tests
=============

    ./test/run_tests.sh

Tips
====

When run `Execute Javascript` keyword of Seleniu2Library, better to add `Set Selenium Speed  1` before it, to wait the Flex completely loaded, otherwise, the js API may not be ready.


Extending robotframework-selenium2library without forking it
============================================================
Use any of the techniques documented to write a python plugin for robotframework.
In your keyword's method here how to access the active selenium's browser:

   selenium2lib = BuiltIn().get_library_instance('Selenium2Library')
   selenium_browser = selenium2lib._current_browser()

Now refer to selenium driver's python API and go wild.

    
License
=======
ASL-2.0 just like robotframework-selenium2library.
